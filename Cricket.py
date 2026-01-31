import streamlit as st

# 1. INITIALIZATION (Always at the top)
if 'runs' not in st.session_state:
    st.session_state.runs = 0
    st.session_state.wickets = 0
    st.session_state.balls = 0
    st.session_state.history = []

# 2. SIDEBAR SETTINGS
st.sidebar.title("⚙️ Match Settings")
total_players = st.sidebar.number_input("Players per Team", min_value=2, max_value=11, value=5)
max_overs = st.sidebar.slider("Overs per Innings", 1, 20, 6)

if st.sidebar.button("Reset Entire Match"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# 3. SCORING FUNCTIONS
def record_ball(outcome, is_extra=False, is_wicket=False):
    if is_wicket:
        st.session_state.wickets += 1
        st.session_state.balls += 1
        st.session_state.history.append("W")
    elif is_extra:
        st.session_state.runs += 1
        st.session_state.history.append(outcome)
    else:
        st.session_state.runs += int(outcome)
        st.session_state.balls += 1
        st.session_state.history.append(str(outcome))
    st.rerun() # This is the magic line that fixes the "one ball behind" error

# 4. BUTTON INTERFACE (Move buttons UP so user sees them first)
st.title("🏏 Gully Scoreboard")
st.subheader("Record Delivery")

r1, r2, r3, r4 = st.columns(4)
if r1.button("0", use_container_width=True): record_ball("0")
if r2.button("1", use_container_width=True): record_ball("1")
if r3.button("2", use_container_width=True): record_ball("2")
if r4.button("3", use_container_width=True): record_ball("3")

r5, r6, r7, r8 = st.columns(4)
if r5.button("4", use_container_width=True): record_ball("4")
if r6.button("6", use_container_width=True): record_ball("6")
if r7.button("WD", use_container_width=True): record_ball("WD", is_extra=True)
if r8.button("NB", use_container_width=True): record_ball("NB", is_extra=True)

if st.button("🔴 WICKET", type="primary", use_container_width=True):
    if st.session_state.wickets < total_players:
        record_ball("W", is_wicket=True)

# 5. THE SCOREBOARD (Placed AFTER logic to ensure it's up-to-date)
st.divider()
overs_display = f"{st.session_state.balls // 6}.{st.session_state.balls % 6}"

c1, c2 = st.columns(2)
c1.metric("Score", f"{st.session_state.runs} / {st.session_state.wickets}")
c2.metric("Overs", overs_display)

# History and WhatsApp
recent = st.session_state.history[-6:] if st.session_state.history else ["No balls yet"]
st.write(f"**Current Over:** {'-'.join(recent)}")

summary = f"*Gully Match Update*\nScore: {st.session_state.runs}/{st.session_state.wickets}\nOvers: {overs_display}"
st.text_area("WhatsApp Summary:", value=summary)
