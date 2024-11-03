<a href="https://veritai-chat-with-docs.streamlit.app">
<img src="https://raw.githubusercontent.com/MuriloKrominski/VeritAI-Chat-with-Docs/refs/heads/main/VeritAI-Chat-with-Docs.png" alt="VeritAI - Chat with Docs" style="max-width: 1280px; max-height: 640px; width: au
to; height: auto;">
</a>

# VeritAI - Chat with Docs
<br>
By <a href="https://murilokrominski.github.io/autor.htm">Murilo Krominski</a>.

## Description

**VeritAI - Chat with Docs** is an AI-powered chatbot application that enables users to interact with content extracted from uploaded PDF documents. Leveraging advanced language models, VeritAI responds to questions and provides information based on the document content. This solution is ideal for developers and users needing a quick, user-friendly interface to query documents.

## Features

- **PDF Upload and Parsing**: Allows users to upload PDF documents, reading and extracting content for query-based responses.
- **Interactive Chat**: A dynamic and user-friendly chat interface for document queries.
- **Customizable Language Model**: Integrates Groq's `llama-3.1-70b-versatile` model, which can be adjusted as needed.
- **Real-Time Processing**: Provides quick and accurate responses based on document content.

## Requirements

Make sure you have the following prerequisites installed:

- **Python** 3.8 or higher
- **Groq Account** with a valid API key
- Libraries listed in the `requirements.txt` file

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/VeritAI-Chat-with-Docs.git
    cd VeritAI-Chat-with-Docs
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure the API key:

   Create a `.env` file in the project root directory and add your Groq API key:

    ```plaintext
    GROQ_API_KEY=your_groq_api_key_here
    ```

## Usage

1. Start the Streamlit application:

    ```bash
    streamlit run app.py
    ```

2. The app will open in your browser at `http://localhost:8501`.

3. Upload a PDF file by clicking on "Send PDF file" and selecting the document. The file name will appear on the screen once uploaded.

4. Type a question related to the PDF content in the input box and press Enter. The VeritAI chatbot will respond based on the document content.

## Code Structure

### Key Files and Directories

- `app.py`: Main file containing the chatbot interface code and PDF upload functionality.
- `requirements.txt`: List of dependencies needed for the project.
- `.env`: File to store environment variables, including the API key.

### Key Dependencies

- `streamlit`: Framework for building interactive web applications in Python.
- `langchain` and `langchain-community`: Frameworks for language model integration and additional plugins.
- `pypdf2`: Library for PDF file handling.
- `python-dotenv`: Loads environment variables from `.env` files.

### Code Workflow

1. **PDF Loading**: Utilizes `PyPDFLoader` to read content from PDF files uploaded by the user.
2. **Language Model Interaction**: Uses `ChatGroq` to process questions and generate responses based on the PDF content.
3. **Chat Interface**: Streamlit renders a chat interface, allowing the user to query the PDF content.

## Example Use Case

Here’s an example of how to use VeritAI:

1. **Upload a PDF**: Load a PDF containing a manual, academic paper, or other document you want to query.
2. **Ask a Question**: Type a specific question about the PDF content, such as "What are the main topics covered in the document?"
3. **Receive an Answer**: VeritAI will analyze the content of the PDF and provide a response based on the information in the document.

## Common Issues

- **API Key Error**: Ensure that the API key in the `.env` file is correct and active.
- **PDF File Not Loaded**: Make sure the PDF file is valid and in a supported format.
- **Missing Dependencies**: Run `pip install -r requirements.txt` to ensure all required libraries are installed.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b my-feature`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to your fork: `git push origin my-feature`
5. Open a Pull Request to the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

Developed by [Murilo Krominski](https://murilokrominski.github.io). This project is a practical AI application for interacting with documents, designed to provide an intuitive interface for PDF queries.
