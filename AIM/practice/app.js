(() => {
  'use strict';

  const SESSION_KEY = 'aim-quiz-session-v1';
  const state = { bank: [], session: null, index: 0, reviewOnly: false };
  const el = Object.fromEntries([
    'loading-panel','setup-panel','question-panel','result-panel','start-button','resume-button',
    'week-filter','generate-button','question-meta','question-heading','progress-copy','progress-fill',
    'answer-form','choices','check-button','next-button','feedback','question-nav','score-value',
    'score-message','retry-wrong-button','new-set-button','review-list'
  ].map(id => [id, document.getElementById(id)]));

  function shuffle(items) {
    const result = [...items];
    for (let i = result.length - 1; i > 0; i -= 1) {
      const random = new Uint32Array(1);
      crypto.getRandomValues(random);
      const j = random[0] % (i + 1);
      [result[i], result[j]] = [result[j], result[i]];
    }
    return result;
  }

  function saveSession() { localStorage.setItem(SESSION_KEY, JSON.stringify(state.session)); }
  function loadSession() {
    try {
      const saved = JSON.parse(localStorage.getItem(SESSION_KEY));
      if (!saved || !Array.isArray(saved.ids) || !saved.ids.length) return null;
      return saved;
    } catch (_) { return null; }
  }

  function show(panel) {
    ['loading-panel','setup-panel','question-panel','result-panel'].forEach(id => { el[id].hidden = id !== panel; });
  }

  function populateWeeks() {
    const counts = state.bank.reduce((map, q) => map.set(q.week, (map.get(q.week) || 0) + 1), new Map());
    el['week-filter'].innerHTML = '<option value="all">전체 300문항</option>' + [...counts.entries()]
      .sort((a, b) => a[0] - b[0])
      .map(([week, count]) => `<option value="${week}">${week}주차 · ${count}문항</option>`).join('');
  }

  function newSession() {
    const filter = el['week-filter'].value;
    const pool = filter === 'all' ? state.bank : state.bank.filter(q => q.week === Number(filter));
    const selected = shuffle(pool).slice(0, Math.min(30, pool.length));
    state.session = { ids: selected.map(q => q.id), answers: {}, checked: {}, createdAt: Date.now(), filter };
    state.index = 0;
    state.reviewOnly = false;
    saveSession();
    renderQuestion();
  }

  function sessionQuestions() {
    return state.session.ids.map(id => state.bank.find(q => q.id === id)).filter(Boolean);
  }

  function currentQuestion() { return sessionQuestions()[state.index]; }

  function renderQuestion() {
    show('question-panel');
    const questions = sessionQuestions();
    const q = questions[state.index];
    const checked = Boolean(state.session.checked[q.id]);
    const selected = Number(state.session.answers[q.id] || 0);
    el['question-meta'].textContent = `${q.week}주차 · ${q.area} · 난이도 ${q.difficulty}`;
    el['question-heading'].textContent = q.question;
    el['progress-copy'].textContent = `${state.index + 1} / ${questions.length}`;
    el['progress-fill'].style.width = `${((state.index + 1) / questions.length) * 100}%`;
    el['progress-fill'].parentElement.setAttribute('aria-valuemax', questions.length);
    el['progress-fill'].parentElement.setAttribute('aria-valuenow', state.index + 1);
    el.choices.innerHTML = q.choices.map((choice, i) => {
      const number = i + 1;
      const status = checked ? (number === q.answer ? ' is-correct' : number === selected ? ' is-wrong' : '') : '';
      return `<label class="choice${status}"><input type="radio" name="answer" value="${number}" ${selected === number ? 'checked' : ''} ${checked ? 'disabled' : ''}><span class="choice-number">${number}</span><span>${escapeHtml(choice)}</span></label>`;
    }).join('');
    el['check-button'].hidden = checked;
    el['next-button'].hidden = !checked;
    el['next-button'].textContent = state.index === questions.length - 1 ? '결과 보기' : '다음 문제';
    renderFeedback(q, selected, checked);
    renderNav(questions);
  }

  function renderFeedback(q, selected, checked) {
    el.feedback.hidden = !checked;
    if (!checked) return;
    const correct = selected === q.answer;
    el.feedback.className = `feedback${correct ? '' : ' wrong'}`;
    el.feedback.innerHTML = `<strong>${correct ? '정답입니다.' : `정답은 ${q.answer}번입니다.`}</strong><span>${escapeHtml(q.explanation)}</span>`;
  }

  function renderNav(questions) {
    el['question-nav'].innerHTML = questions.map((q, i) => {
      const classes = [i === state.index ? 'current' : '', state.session.checked[q.id] ? 'checked' : ''].filter(Boolean).join(' ');
      return `<button type="button" data-index="${i}" class="${classes}" aria-label="${i + 1}번 문제">${i + 1}</button>`;
    }).join('');
  }

  function submitAnswer(event) {
    event.preventDefault();
    const selected = new FormData(el['answer-form']).get('answer');
    if (!selected) { el.feedback.hidden = false; el.feedback.className = 'feedback wrong'; el.feedback.textContent = '답을 하나 선택하세요.'; return; }
    const q = currentQuestion();
    state.session.answers[q.id] = Number(selected);
    state.session.checked[q.id] = true;
    saveSession();
    renderQuestion();
  }

  function nextQuestion() {
    const questions = sessionQuestions();
    if (state.index < questions.length - 1) { state.index += 1; renderQuestion(); window.scrollTo({ top: el['question-panel'].offsetTop - 20, behavior: 'smooth' }); }
    else renderResults();
  }

  function renderResults() {
    show('result-panel');
    const questions = sessionQuestions();
    const correct = questions.filter(q => state.session.answers[q.id] === q.answer).length;
    const wrong = questions.filter(q => state.session.checked[q.id] && state.session.answers[q.id] !== q.answer);
    el['score-value'].textContent = `${correct} / ${questions.length}`;
    el['score-message'].textContent = `정답률 ${Math.round((correct / questions.length) * 100)}% · 오답 ${wrong.length}문항`;
    el['retry-wrong-button'].hidden = wrong.length === 0;
    el['review-list'].innerHTML = wrong.map(q => `<article class="review-item"><h3>${escapeHtml(q.question)}</h3><p><strong>선택:</strong> ${escapeHtml(q.choices[(state.session.answers[q.id] || 1) - 1])}</p><p><strong>정답:</strong> ${q.answer}번 ${escapeHtml(q.choices[q.answer - 1])}</p><p>${escapeHtml(q.explanation)}</p></article>`).join('');
  }

  function retryWrong() {
    const wrongIds = sessionQuestions().filter(q => state.session.answers[q.id] !== q.answer).map(q => q.id);
    state.session = { ids: wrongIds, answers: {}, checked: {}, createdAt: Date.now(), filter: 'wrong' };
    state.index = 0;
    state.reviewOnly = true;
    saveSession();
    renderQuestion();
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>'"]/g, char => ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', "'":'&#39;', '"':'&quot;' })[char]);
  }

  async function init() {
    try {
      const response = await fetch('./questions.json', { cache: 'no-store' });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const data = await response.json();
      if (!Array.isArray(data.questions) || data.questions.length !== 300) throw new Error('문항 수가 올바르지 않습니다.');
      state.bank = data.questions;
      populateWeeks();
      show('setup-panel');
      const saved = loadSession();
      if (saved && saved.ids.every(id => state.bank.some(q => q.id === id))) {
        state.session = saved;
        el['resume-button'].hidden = false;
      }
    } catch (error) {
      el['loading-panel'].innerHTML = `<p>문제은행을 불러오지 못했습니다. 잠시 후 다시 시도해 주세요.</p><code>${escapeHtml(error.message)}</code>`;
    }
  }

  el['start-button'].addEventListener('click', () => { show('setup-panel'); el['setup-panel'].scrollIntoView({ behavior: 'smooth' }); });
  el['resume-button'].addEventListener('click', () => { state.index = Math.max(0, sessionQuestions().findIndex(q => !state.session.checked[q.id])); if (state.index < 0) state.index = 0; renderQuestion(); });
  el['generate-button'].addEventListener('click', newSession);
  el['answer-form'].addEventListener('submit', submitAnswer);
  el['next-button'].addEventListener('click', nextQuestion);
  el['question-nav'].addEventListener('click', event => { const button = event.target.closest('button[data-index]'); if (button) { state.index = Number(button.dataset.index); renderQuestion(); } });
  el['retry-wrong-button'].addEventListener('click', retryWrong);
  el['new-set-button'].addEventListener('click', () => { localStorage.removeItem(SESSION_KEY); show('setup-panel'); });
  init();
})();
