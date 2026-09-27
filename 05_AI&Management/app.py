from __future__ import annotations

import json
from datetime import datetime

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from sklearn.datasets import make_moons
from sklearn.neural_network import MLPClassifier

from lab_logic import (
    MODEL_CANDIDATES,
    TOY_EMBEDDINGS,
    activate,
    activation_array,
    activation_derivative,
    l2_penalty,
    nearest_words,
    weighted_sum,
)


st.set_page_config(
    page_title="4주차 신경망·정규화·임베딩 실습",
    page_icon="🧠",
    layout="wide",
)

st.markdown(
    """
    <style>
    html, body, [class*="css"] { font-family: "Paperlogy 5 Medium", "Pretendard", sans-serif; }
    .block-container { max-width: 1180px; padding-top: 2rem; }
    .small-note { color: #68706B; font-size: 0.92rem; }
    </style>
    """,
    unsafe_allow_html=True,
)


def init_state() -> None:
    defaults = {
        "student_id": "",
        "student_name": "",
        "team": "",
        "answers": {},
        "completed": set(),
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def record(key: str, value) -> None:
    st.session_state.answers[key] = value


def mark_complete(section: str) -> None:
    st.session_state.completed.add(section)


def report_payload() -> dict:
    return {
        "course": "인공지능과 경영",
        "week": 4,
        "topic": "딥러닝·신경망·정규화·임베딩",
        "submitted_at": datetime.now().isoformat(timespec="seconds"),
        "student": {
            "student_id": st.session_state.student_id,
            "name": st.session_state.student_name,
            "team": st.session_state.team,
        },
        "completed_sections": sorted(st.session_state.completed),
        "answers": st.session_state.answers,
    }


@st.cache_data(show_spinner=False, max_entries=64)
def run_network_experiment(hidden_layers: tuple[int, ...], learning_rate: float, noise: float, alpha: float):
    """Train once per parameter combination and reuse the result across sessions."""
    X, y = make_moons(n_samples=320, noise=noise, random_state=42)
    rng = np.random.default_rng(42)
    order = rng.permutation(len(X))
    train_idx, test_idx = order[:224], order[224:]
    model = MLPClassifier(
        hidden_layer_sizes=hidden_layers,
        learning_rate_init=learning_rate,
        alpha=alpha,
        max_iter=450,
        early_stopping=True,
        n_iter_no_change=20,
        random_state=42,
    )
    model.fit(X[train_idx], y[train_idx])
    train_acc = model.score(X[train_idx], y[train_idx])
    test_acc = model.score(X[test_idx], y[test_idx])
    gx, gy = np.meshgrid(
        np.linspace(X[:, 0].min() - 0.4, X[:, 0].max() + 0.4, 85),
        np.linspace(X[:, 1].min() - 0.4, X[:, 1].max() + 0.4, 85),
    )
    prob = model.predict_proba(np.c_[gx.ravel(), gy.ravel()])[:, 1].reshape(gx.shape)
    return X, y, train_idx, test_idx, gx, gy, prob, train_acc, test_acc


init_state()

st.title("🧠 딥러닝·신경망·임베딩 실습")
st.caption("인공지능과 경영 · 04주차 · 실습 및 예제풀이 1시간")

with st.sidebar:
    st.header("학습자 정보")
    st.session_state.student_id = st.text_input("학번", value=st.session_state.student_id)
    st.session_state.student_name = st.text_input("이름", value=st.session_state.student_name)
    st.session_state.team = st.text_input("팀", value=st.session_state.team)
    progress = len(st.session_state.completed) / 5
    st.progress(progress, text=f"완료 {len(st.session_state.completed)}/5")
    st.markdown("---")
    st.markdown("**권장 흐름**")
    st.write("1. 뉴런 계산\n2. 신경망 실험\n3. 정규화\n4. 임베딩\n5. 팀 결정")
    st.markdown("---")
    st.link_button("Google MLCC 신경망", "https://developers.google.com/machine-learning/crash-course/neural-networks?hl=ko")
    st.link_button("Google MLCC 임베딩", "https://developers.google.com/machine-learning/crash-course/embeddings?hl=ko")

tabs = st.tabs(["① 뉴런 계산", "② 신경망 실험", "③ 과적합·정규화", "④ 임베딩", "⑤ 팀 결정·제출"])

with tabs[0]:
    st.header("뉴런과 활성화 함수 손계산")
    st.write("슬라이더로 입력과 가중치를 바꾸고 가중합과 활성값이 어떻게 변하는지 확인합니다.")
    c1, c2, c3 = st.columns(3)
    with c1:
        x1 = st.slider("입력 x₁", -5.0, 5.0, 3.0, 0.1)
        x2 = st.slider("입력 x₂", -5.0, 5.0, 2.0, 0.1)
    with c2:
        w1 = st.slider("가중치 w₁", -2.0, 2.0, -0.4, 0.1)
        w2 = st.slider("가중치 w₂", -2.0, 2.0, 0.8, 0.1)
    with c3:
        bias = st.slider("편향 b", -2.0, 2.0, -0.1, 0.1)
        function = st.selectbox("활성화 함수", ["ReLU", "Sigmoid", "tanh"])

    z = weighted_sum(x1, x2, w1, w2, bias)
    output = activate(z, function)
    m1, m2, m3 = st.columns(3)
    m1.metric("가중합 z", f"{z:.3f}")
    m2.metric(f"{function}(z)", f"{output:.3f}")
    m3.metric("w₁x₁ + w₂x₂ + b", f"{w1*x1:.2f} + {w2*x2:.2f} + {bias:.2f}")

    answer = st.text_area("이 출력값을 바로 고객 이탈 확률이라고 말할 수 없는 이유를 쓰세요.", key="neuron_interpretation")
    record("neuron", {"inputs":[x1,x2], "weights":[w1,w2], "bias":bias, "activation":function, "z":z, "output":output, "interpretation":answer})
    if st.button("뉴런 계산 완료", type="primary"):
        mark_complete("1_neuron")
        st.success("뉴런 계산 결과를 기록했습니다.")

    st.divider()
    st.subheader("활성화 함수 시뮬레이터")
    st.write("입력 범위와 현재 입력값을 조절하며 함수의 출력과 기울기를 비교합니다.")
    left, right = st.columns([1, 2])
    with left:
        selected_functions = st.multiselect(
            "비교할 함수",
            ["ReLU", "Leaky ReLU", "Sigmoid", "tanh"],
            default=["ReLU", "Sigmoid", "tanh"],
        )
        input_range = st.slider("그래프 입력 범위", 2.0, 15.0, 6.0, 0.5)
        current_z = st.slider("현재 입력 z", -15.0, 15.0, -2.0, 0.1)
        view = st.radio("그래프", ["출력값", "기울기"], horizontal=True)

        if selected_functions:
            values_now = {}
            for name in selected_functions:
                out = float(activation_array(np.array([current_z]), name)[0])
                grad = float(activation_derivative(np.array([current_z]), name)[0])
                values_now[name] = {"output": out, "gradient": grad}
                st.metric(name, f"출력 {out:.3f}", delta=f"기울기 {grad:.3f}", delta_color="off")
        else:
            values_now = {}
            st.warning("비교할 함수를 하나 이상 선택하세요.")

    with right:
        xs = np.linspace(-input_range, input_range, 500)
        curve = go.Figure()
        palette = {"ReLU":"#0E7A49", "Leaky ReLU":"#31A16E", "Sigmoid":"#B8493B", "tanh":"#246B8E"}
        for name in selected_functions:
            ys = activation_array(xs, name) if view == "출력값" else activation_derivative(xs, name)
            curve.add_trace(go.Scatter(x=xs, y=ys, mode="lines", name=name, line=dict(width=3, color=palette[name])))
        curve.add_vline(x=current_z, line_dash="dash", line_color="#BE8A2F", annotation_text="현재 z")
        curve.add_hline(y=0, line_width=1, line_color="#68706B")
        curve.update_layout(height=470, margin=dict(l=10,r=10,t=20,b=10), xaxis_title="입력 z", yaxis_title=view, legend_title="활성화 함수")
        st.plotly_chart(curve, use_container_width=True)

    st.subheader("입력 분포와 Dead ReLU 실험")
    d1, d2, d3 = st.columns(3)
    mean = d1.slider("입력 평균", -5.0, 5.0, -1.0, 0.1)
    std = d2.slider("입력 표준편차", 0.1, 3.0, 1.0, 0.1)
    sample_size = d3.slider("가상 뉴런 수", 100, 3000, 1000, 100)
    rng_activation = np.random.default_rng(42)
    simulated_inputs = rng_activation.normal(mean, std, sample_size)
    relu_outputs = activation_array(simulated_inputs, "ReLU")
    leaky_outputs = activation_array(simulated_inputs, "Leaky ReLU")
    zero_ratio = float(np.mean(relu_outputs == 0))
    a1, a2 = st.columns(2)
    a1.metric("ReLU 출력이 0인 비율", f"{zero_ratio:.1%}")
    a2.metric("Leaky ReLU 출력 평균", f"{np.mean(leaky_outputs):.3f}")
    hist_df = pd.DataFrame({"입력 z":simulated_inputs, "ReLU 출력":relu_outputs, "Leaky ReLU 출력":leaky_outputs})
    histogram = px.histogram(hist_df, x=["ReLU 출력", "Leaky ReLU 출력"], nbins=45, barmode="overlay", opacity=0.62, color_discrete_sequence=["#0E7A49", "#246B8E"])
    histogram.update_layout(height=380, margin=dict(l=10,r=10,t=20,b=10), xaxis_title="활성값", yaxis_title="뉴런 수", legend_title="함수")
    st.plotly_chart(histogram, use_container_width=True)
    if zero_ratio >= 0.8:
        st.error("ReLU 뉴런의 80% 이상이 0을 출력합니다. 입력 분포, 편향, 학습률 또는 Leaky ReLU 사용을 검토하세요.")
    elif zero_ratio >= 0.5:
        st.warning("절반 이상의 ReLU 뉴런이 0을 출력합니다. 기울기가 흐르지 않는 뉴런이 많아질 수 있습니다.")
    else:
        st.success("현재 입력 분포에서는 활성화되는 ReLU 뉴런이 절반 이상입니다.")
    saturation = st.text_area("현재 설정에서 ReLU의 0 출력 또는 Sigmoid·tanh의 포화가 학습에 미칠 영향을 설명하세요.", key="activation_simulation_note")
    record("activation_simulator", {"functions":selected_functions, "current_z":current_z, "view":view, "values":values_now, "input_mean":mean, "input_std":std, "sample_size":sample_size, "relu_zero_ratio":zero_ratio, "interpretation":saturation})

with tabs[1]:
    st.header("신경망의 복잡도와 결정경계")
    st.write("같은 데이터에서 은닉층 구조와 학습률을 바꿔 훈련·테스트 성능을 비교합니다.")
    with st.form("network_settings"):
        c1, c2, c3 = st.columns(3)
        hidden_layers = c1.selectbox("은닉층 구조", [(2,), (4,), (8,), (8, 4)], format_func=lambda x: " × ".join(map(str, x)))
        learning_rate = c2.select_slider("학습률", options=[0.001, 0.003, 0.01, 0.03, 0.1], value=0.01)
        noise = c3.slider("데이터 잡음", 0.05, 0.45, 0.25, 0.05)
        regularization_alpha = st.slider("L2 강도 α", 0.0001, 1.0, 0.01, format="%.4f")
        st.form_submit_button("설정으로 신경망 학습", type="primary", use_container_width=True)

    with st.spinner("신경망을 학습하고 결정경계를 계산하는 중입니다..."):
        X, y, train_idx, test_idx, gx, gy, prob, train_acc, test_acc = run_network_experiment(
            tuple(hidden_layers), float(learning_rate), float(noise), float(regularization_alpha)
        )
    fig = go.Figure()
    fig.add_trace(go.Contour(x=gx[0], y=gy[:,0], z=prob, colorscale=[[0,"#EAF5EF"],[0.5,"#FFFFFF"],[1,"#31D88A"]], opacity=0.65, showscale=False, contours=dict(start=0,end=1,size=0.1)))
    fig.add_trace(go.Scatter(x=X[test_idx,0], y=X[test_idx,1], mode="markers", marker=dict(color=y[test_idx], colorscale=[[0,"#246B8E"],[1,"#B8493B"]], line=dict(color="white",width=0.5)), name="테스트 데이터"))
    fig.update_layout(height=480, margin=dict(l=10,r=10,t=20,b=10), xaxis_title="특징 1", yaxis_title="특징 2")
    st.plotly_chart(fig, use_container_width=True)
    m1, m2, m3 = st.columns(3)
    m1.metric("훈련 정확도", f"{train_acc:.1%}")
    m2.metric("테스트 정확도", f"{test_acc:.1%}")
    m3.metric("일반화 격차", f"{(train_acc-test_acc)*100:.1f}%p")
    observation = st.text_area("복잡도나 L2 강도를 바꿨을 때 경계와 일반화 격차가 어떻게 달라졌나요?", key="boundary_observation")
    record("network_experiment", {"hidden_layers":hidden_layers, "learning_rate":learning_rate, "noise":noise, "alpha":regularization_alpha, "train_accuracy":train_acc, "test_accuracy":test_acc, "gap":train_acc-test_acc, "observation":observation})
    if st.button("신경망 실험 완료", type="primary"):
        mark_complete("2_network")
        st.success("실험 조건과 관찰 내용을 기록했습니다.")

with tabs[2]:
    st.header("과적합과 정규화")
    st.write("L2가 큰 가중치에 어떤 비용을 부과하는지 계산하고 세 모델 중 하나를 선택합니다.")
    lambda_ = st.slider("λ", 0.0, 1.0, 0.1, 0.05)
    a = [4.0, 0.0]
    b = [2.0, 2.0]
    df_penalty = pd.DataFrame({
        "모델": ["가중치 [4, 0]", "가중치 [2, 2]"],
        "가중치 제곱합": [16.0, 8.0],
        "L2 비용": [l2_penalty(a, lambda_), l2_penalty(b, lambda_)],
    })
    st.dataframe(df_penalty, use_container_width=True, hide_index=True)
    st.info("데이터 손실이 같다면 L2는 제곱합이 작은 가중치 조합을 더 선호합니다.")

    df_models = pd.DataFrame([
        {"모델":m.name, "훈련 정확도":m.train_accuracy, "검증 정확도":m.validation_accuracy, "일반화 격차":m.generalization_gap, "월 비용 지수":m.monthly_cost}
        for m in MODEL_CANDIDATES
    ])
    styled_models = df_models.style.format({
        "훈련 정확도":"{:.0%}",
        "검증 정확도":"{:.0%}",
        "일반화 격차":lambda value: f"{value*100:.0f}%p",
    })
    st.dataframe(styled_models, use_container_width=True, hide_index=True)
    choice = st.radio("현재 정보만으로 선택할 모델", [m.name for m in MODEL_CANDIDATES], horizontal=True)
    reason = st.text_area("검증 성능, 일반화 격차, 비용을 사용해 선택 이유를 쓰세요.", key="regularization_reason")
    strategy = st.multiselect("과적합 완화 전략", ["L2", "Dropout", "조기 종료", "데이터 추가", "모델 단순화"])
    record("regularization", {"lambda":lambda_, "model_choice":choice, "reason":reason, "strategy":strategy})
    if st.button("정규화 문제 완료", type="primary"):
        mark_complete("3_regularization")
        st.success("모델 선택과 정규화 계획을 기록했습니다.")

with tabs[3]:
    st.header("임베딩 공간 탐색")
    st.warning("이 앱의 벡터는 수업용으로 만든 작은 2차원 예시입니다. 실제 Google 실습은 아래 링크에서 10,000개 Word2Vec 벡터를 탐색합니다.")
    st.link_button("Google Embedding Projector 실습 열기", "https://developers.google.com/machine-learning/crash-course/embeddings/interactive-exercises?hl=ko")
    selected = st.selectbox("탐색할 단어", sorted(TOY_EMBEDDINGS))
    neighbors = nearest_words(selected, 5)
    df_emb = pd.DataFrame([{"단어":word,"x":vec[0],"y":vec[1],"선택":word==selected} for word,vec in TOY_EMBEDDINGS.items()])
    fig = px.scatter(df_emb, x="x", y="y", text="단어", color="선택", color_discrete_map={True:"#B8493B",False:"#0E7A49"})
    fig.update_traces(textposition="top center", marker=dict(size=11))
    fig.update_layout(height=500, showlegend=False, margin=dict(l=10,r=10,t=20,b=10))
    st.plotly_chart(fig, use_container_width=True)
    st.subheader(f"'{selected}'와 코사인 유사도가 높은 단어")
    st.dataframe(pd.DataFrame(neighbors, columns=["단어","코사인 유사도"]).style.format({"코사인 유사도":"{:.3f}"}), use_container_width=True, hide_index=True)
    unexpected = st.text_area("예상과 달랐던 관계와 가능한 이유를 쓰세요.", key="embedding_unexpected")
    risk = st.text_area("추천이나 검색에 사용할 때 확인해야 할 편향을 한 가지 쓰세요.", key="embedding_risk")
    record("embedding", {"selected_word":selected, "nearest":neighbors, "unexpected":unexpected, "risk":risk})
    if st.button("임베딩 탐색 완료", type="primary"):
        mark_complete("4_embedding")
        st.success("임베딩 탐색 결과를 기록했습니다.")

with tabs[4]:
    st.header("팀 결정과 제출")
    final_choice = st.radio("팀의 최종 모델 선택", [m.name for m in MODEL_CANDIDATES], horizontal=True, key="final_choice")
    evidence = st.text_area("선택을 지지하는 근거 두 가지", key="final_evidence")
    additional_test = st.text_area("배포 전에 추가할 검증 한 가지", key="additional_test")
    reversal = st.text_area("이 조건이 나타나면 선택을 바꾼다", key="reversal_condition")
    reflection = st.text_area("오늘 처음 생각과 달라진 점", key="reflection")
    record("team_decision", {"final_choice":final_choice, "evidence":evidence, "additional_test":additional_test, "reversal_condition":reversal, "reflection":reflection})
    if st.button("팀 결정 완료", type="primary"):
        mark_complete("5_decision")
        st.success("팀 결정을 기록했습니다. 아래에서 결과 파일을 내려받으세요.")

    payload = report_payload()
    st.download_button(
        "결과 JSON 내려받기",
        data=json.dumps(payload, ensure_ascii=False, indent=2),
        file_name=f"week04_{st.session_state.student_id or 'student'}_result.json",
        mime="application/json",
        use_container_width=True,
    )
    rows = []
    for section, content in payload["answers"].items():
        rows.append({"section":section, "response":json.dumps(content, ensure_ascii=False)})
    st.download_button(
        "결과 CSV 내려받기",
        data=pd.DataFrame(rows).to_csv(index=False).encode("utf-8-sig"),
        file_name=f"week04_{st.session_state.student_id or 'student'}_result.csv",
        mime="text/csv",
        use_container_width=True,
    )

st.markdown("---")
st.caption("© 2026 강송희 · 한국공학대학교. 수업용 실습 도구")
