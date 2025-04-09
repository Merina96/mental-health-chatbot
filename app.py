import streamlit as st
from gpt_suggestion import get_gemini_suggestion  # your Gemini-based suggestion function

st.set_page_config(page_title="Mental Health Bot", page_icon="🧠")
st.title("🧠 Mental Health Support Bot")
st.markdown("Welcome! Answer a few short questions to receive a gentle suggestion for your well-being 🌿")

questions = [
    "Little interest or pleasure in doing things?",
    "Feeling down, depressed, or hopeless?",
    "Trouble falling or staying asleep, or sleeping too much?",
    "Feeling tired or having little energy?",
    "Poor appetite or overeating?",
    "Feeling bad about yourself — or that you are a failure or have let yourself or your family down?",
    "Trouble concentrating on things, such as reading or watching television?",
    "Moving or speaking so slowly that other people could have noticed?"
]

options = ["Not at all", "A little", "Often", "Always"]

# Initialize session variables
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "responses" not in st.session_state:
    st.session_state.responses = []

q_index = st.session_state.current_question

# Show the current question
if q_index < len(questions):
    st.markdown(f"**Q{q_index+1}. {questions[q_index]}**")
    answer = st.radio("Select an option:", options, key=f"q{q_index}")

    if st.button("Next"):
        st.session_state.responses.append(answer)
        st.session_state.current_question += 1
        st.rerun()
else:
    # All questions answered
    st.success("✅ You've completed the assessment!")
    st.markdown("### 💡 Suggestion:")
    suggestion = get_gemini_suggestion(st.session_state.responses)
    st.markdown(f"🫶 *{suggestion}*")

    # Reset after showing suggestion
    if st.button("Start Over"):
        st.session_state.current_question = 0
        st.session_state.responses = []
        st.rerun()

