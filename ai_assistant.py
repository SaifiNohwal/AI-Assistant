import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def get_gemini_response(prompt):
    """Generates a response using Google Gemini API."""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def save_feedback(user_input, ai_response):
    """Logs user feedback for future improvements."""
    feedback = input("\nWas this response helpful? (yes/no): ").strip().lower()
    with open("feedback_log.txt", "a") as f:
        f.write(f"User Query: {user_input}\nAI Response: {ai_response}\nFeedback: {feedback}\n---\n")

def ask_question():
    """Handles factual Q&A with three prompt variations."""
    question = input("\nEnter your question: ")

    prompt_variations = [
        f"Answer this question concisely: {question}",
        f"Provide a detailed explanation for: {question}",
        f"Give a brief yet informative response to: {question}"
    ]

    prompt = prompt_variations[0]  # Default prompt, can be randomized
    response = get_gemini_response(prompt)
    print("\nAI Response:", response)
    save_feedback(question, response)

def summarize_text():
    """Handles text summarization with different prompt styles."""
    text = input("\nEnter text to summarize: ")

    prompt_variations = [
        f"Summarize the following text in a short paragraph:\n{text}",
        f"Provide key points from this text:\n{text}",
        f"Give a bullet-point summary of this text:\n{text}"
    ]

    prompt = prompt_variations[1]  # Default prompt
    response = get_gemini_response(prompt)
    print("\nSummary:", response)
    save_feedback(text, response)

def generate_creative_content():
    """Handles creative content generation with flexible prompts."""
    prompt_type = input("\nWhat do you want? (story/poem/idea): ").strip().lower()
    topic = input("Enter a topic: ")

    prompt_variations = [
        f"Write a {prompt_type} about {topic} in a humorous tone.",
        f"Create a {prompt_type} about {topic} with an inspiring theme.",
        f"Generate a {prompt_type} about {topic} that is suspenseful and engaging."
    ]

    prompt = prompt_variations[2]  # Default prompt
    response = get_gemini_response(prompt)
    print("\nGenerated Content:", response)
    save_feedback(f"{prompt_type} on {topic}", response)

def provide_advice():
    """Handles personalized advice generation."""
    topic = input("\nEnter a topic you need advice on: ")

    prompt_variations = [
        f"Give practical tips on {topic}.",
        f"Provide expert-level advice on {topic} with real-world examples.",
        f"Offer beginner-friendly guidance on {topic} in simple terms."
    ]

    prompt = prompt_variations[0]  # Default prompt
    response = get_gemini_response(prompt)
    print("\nAdvice:", response)
    save_feedback(topic, response)

def main():
    """Main function to run the AI Assistant CLI."""
    while True:
        print("\nWelcome to the AI Assistant!")
        print("1. Answer Questions")
        print("2. Summarize Text")
        print("3. Generate Creative Content")
        print("4. Provide Advice")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            ask_question()
        elif choice == "2":
            summarize_text()
        elif choice == "3":
            generate_creative_content()
        elif choice == "4":
            provide_advice()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
