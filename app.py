import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader  # Import PDF loader
from dotenv import load_dotenv
import tempfile  # Library to handle temporary files

# Load environment variables from the .env file
load_dotenv()

# API key and model configuration
api_key = os.getenv('GROQ_API_KEY')
os.environ['GROQ_API_KEY'] = api_key

# Initializes the AI model for chat with the model "llama-3.1-70b-versatile"
chat = ChatGroq(model='llama-3.1-70b-versatile')

# Function to generate chatbot response
def generate_response(messages, document):
    system_message = '''You are an assistant named VeritAI, developed by Murilo Krominski.
    Use the following information to formulate your responses: {information}'''
    message_model = [('system', system_message)] + messages
    template = ChatPromptTemplate.from_messages(message_model)
    chain = template | chat
    return chain.invoke({'information': document}).content

# Function to load content from a PDF file
def load_content(pdf_file):
    # Create a temporary file to save the PDF content
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(pdf_file.read())
        temp_pdf_path = temp_pdf.name  # Store the path of the temporary file

    # Load content from the temporary PDF file
    loader = PyPDFLoader(temp_pdf_path)
    documents = loader.load()
    
    # Delete the temporary file after loading
    os.remove(temp_pdf_path)

    return ''.join(doc.page_content for doc in documents)

# User interface with Streamlit
st.title('📃VeritAI - Chat with Docs')

# Upload PDF file
uploaded_file = st.file_uploader("Send PDF file", type=["pdf"])
if uploaded_file:
    st.write("Name of PDF: ", uploaded_file.name)  # Display the file name
    document = load_content(uploaded_file)  # Loads the content from the PDF
    st.write("Content loaded successfully!")  # Success message

# Session initialization to store chat messages
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# User question input and response generation
question = st.text_input('Your question:')
if question and uploaded_file:
    st.session_state["messages"].append(('user', question))  # Adds the question to the session
    response = generate_response(st.session_state["messages"], document)  # Generates the response
    st.session_state["messages"].append(('assistant', response))  # Stores the response
    st.write(f"VeritAI: {response}")  # Displays the chatbot response
    st.markdown("---")  # Divider line

# Thank-you message and credits
st.markdown("---")
st.write("Thank you for using VeritAI - Chat with Docs.")
st.write("This open-source AI chatbot was developed by me to interact with the user based on information extracted from user-provided PDF documents.")
st.write("Developed by Murilo Krominski. [Author's Repository](https://murilokrominski.github.io)")
