import streamlit as st

# Setup
if 'runs' not in st.session_state:
    st.session_state.runs = 0
    st.session_state.wickets = 0
    st.session_state.balls = 0
    st.session_state.total_players = 5 
    st.session_state.history = []

st.title("🏏 Jodhpur Gully Scoreboard")

# Score Display
col1, col2 = st.columns(2)
with col1:
    st.metric("Score", f"{st.session_state.runs} / {st.session_state.wickets}")
with col2:
    overs = f"{st.session_state.balls // 6}.{st.session_state.balls % 6}"
    st.metric("Overs", overs)

# Last Man Standing Logic
if st.session_state.wickets == st.session_state.total_players - 1:
    st.warning("🔥 Last Man Standing!")

# Scoring Buttons
st.subheader("Tap to Score")
r1, r2, r3, r4 = st.columns(4)
if r1.button("0"): st.session_state.balls += 1; st.session_state.history.append("0")
if r2.button("1"): st.session_state.runs += 1; st.session_state.balls += 1; st.session_state.history.append("1")
if r3.button("2"): st.session_state.runs += 2; st.session_state.balls += 1; st.session_state.history.append("2")
if r4.button("3"): st.session_state.runs += 3; st.session_state.balls += 1; st.session_state.history.append("3")

r5, r6, r7, r8 = st.columns(4)
if r5.button("4"): st.session_state.runs += 4; st.session_state.balls += 1; st.session_state.history.append("4")
if r6.button("6"): st.session_state.runs += 6; st.session_state.balls += 1; st.session_state.history.append("6")
if r7.button("WD"): st.session_state.runs += 1; st.session_state.history.append("WD")
if r8.button("NB"): st.session_state.runs += 1; st.session_state.history.append("NB")

if st.button("🔴 WICKET", use_container_width=True):
    if st.session_state.wickets < st.session_state.total_players:
        st.session_state.wickets += 1
        st.session_state.balls += 1
        st.session_state.history.append("W")

# WhatsApp Summary
summary = f"Match Score: {st.session_state.runs}/{st.session_state.wickets} ({overs} overs)"
st.text_area("WhatsApp Summary:", summary)

if st.button("Reset"):
    for key in st.session_state.keys(): del st.session_state[key]
    st.rerun()
