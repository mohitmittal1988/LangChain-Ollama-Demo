import os
from dotenv import load_dotenv  # To load environment variables from a .env file
from langchain_community.llms import Ollama  # Import Ollama LLM interface
import streamlit as st  # Streamlit for building the UI
from langchain_core.prompts import ChatPromptTemplate  # To structure prompt templates
from langchain_core.output_parsers import StrOutputParser  # To parse the LLM output as string

# Load environment variables from the .env file
load_dotenv()

# Set LangChain-specific environment variables
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"  # Enable tracing for debugging or monitoring
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# -------------------------------
# Prompt Template
# -------------------------------

# Define a chat prompt with system and user messages
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked."),
        ("user", "Question: {question}")
    ]
)

# -------------------------------
# Streamlit UI
# -------------------------------

# Set the title for the Streamlit app
st.title("LangChain Demo with LLaMA 3.2")

# Input field for user to enter a question
input_text = st.text_input("What question do you have in mind?")

# -------------------------------
# LLM Initialization
# -------------------------------

# Initialize the Ollama LLM with the LLaMA 3.2 model
llm = Ollama(model="llama3.2")

# Create an output parser to convert the response to a string
output_parser = StrOutputParser()

# Create a processing chain: prompt -> LLM -> output parser
chain = prompt | llm | output_parser

# -------------------------------
# Execute Chain on User Input
# -------------------------------

# If the user has entered a question, run it through the chain and display the result
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
