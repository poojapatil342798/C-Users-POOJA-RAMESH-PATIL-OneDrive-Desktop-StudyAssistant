
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load API key
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

# Check API key
if not api_key:
    print("Error: Google API key not found. Check your .env file.")
    exit()

# Connect Gemini AI
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        google_api_key=api_key,
        temperature=0.3
    )

    # Create prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a helpful Study Assistant.
        Explain academic topics in simple language.
        Give clear examples and help students prepare for exams.
        Keep answers organized and easy to understand."""),
        ("human", "{question}")
    ])

    # Create LangChain chain
    chain = prompt | llm

    print("\n================================")
    print("       AI STUDY ASSISTANT")
    print("================================")
    print("Ask any academic question!")
    print("Type 'exit' to close the chatbot.")

    while True:
        question = input("\nEnter your question: ")

        if question.lower().strip() == "exit":
            print("Thank you for using Study Assistant!")
            break

        if not question.strip():
            print("Please enter a question.")
            continue

        try:
            response = chain.invoke({"question": question})
            print("\nAI Answer:")
            print(response.content)

        except Exception as e:
            print("\nSorry! Something went wrong.")
            print("Please check your internet connection and API key.")

except Exception as e:
    print("Unable to connect to Gemini AI.")
    print("Error:", e)

print("STUDY ASSISTANT FILE IS RUNNING!")