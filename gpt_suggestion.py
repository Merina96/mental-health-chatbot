import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_suggestion(responses):
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

    answer_texts = responses

    summary = "; ".join([
        f"Q{i+1}: {questions[i]} - {answer_texts[i]}" for i in range(len(responses))
    ])

    prompt = (
        "You are a compassionate mental health assistant. Based on the following questionnaire, "
        "give a short, kind, and personalized suggestion to improve well-being.\n\n"
        f"{summary}\n\nSuggestion:"
    )

    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-pro")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error generating suggestion: {e}"
