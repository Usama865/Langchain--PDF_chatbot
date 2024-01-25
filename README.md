# Langchain-PDF_chatbot

This code provides a Python script for creating a simple yet powerful PDF text search and question-answering system. The system is designed to extract text from the provided PDF documents, split the text into manageable chunks, convert the chunks into vectors, and then utilize a language model for question-answering based on user queries.

## How it Works

1. **Text Extraction from PDFs:**
   - The `get_pdf_text` function uses the `PdfReader` class from the `pypdf` library to extract text from a given PDF file. It iterates through the pages, extracting and concatenating the text.

2. **Text Chunking:**
   - The `RecursiveCharacterTextSplitter` class is employed to split the extracted text into smaller, manageable chunks. It utilizes specified separators like double line breaks, single line breaks, and periods to define chunk boundaries. The `get_chunks` function calls this splitter to obtain a list of text chunks.

3. **Vectorization of Text:**
   - The script uses the `HuggingFaceEmbeddings` class from the `langchain.embeddings` module to convert each text chunk into numerical vectors. The chosen model for embeddings is "all-MiniLM-L6-v2."

4. **FAISS Indexing:**
   - The `FAISS` class from the `langchain.vectorstores` module is employed to create a vector database from the text chunks. This database enables efficient similarity search and retrieval based on vector representations.

5. **Question-Answering Chain:**
   - The system utilizes a language model for question-answering. Specifically, the `GooglePalm` class from `langchain.llms` is used, configured with a [Google API](https://makersuite.google.com/app/apikey) key and parameters like temperature and maximum output tokens.

6. **Memory for Conversations:**
   - The script implements a conversation buffer memory using the `ConversationBufferMemory` class from `langchain.memory`. This memory helps maintain context during interactions with the question-answering system.

7. **Retrieval and Question-Answering Chain:**
   - The vector database, language model, and conversation memory are combined into a `RetrievalQA` chain using the `RetrievalQA.from_chain_type` method. This chain facilitates seamless interaction with the system, allowing users to ask questions based on the processed PDF text.

## Setup Instructions

1. Install the required dependencies from the requiremnt.text file provided in the repository.
2. Ensure you have a Google API key for the GooglePalm language model.
3. Load your API key from a `.env` file using 
```python
from dotenv import load_dotenv()
```
or use your API key directly [(click here for Google API documentation)](https://ai.google.dev/docs)

The script will process the PDF, create a searchable database, and allow users to interact with the question-answering system
 
 **NOTE:** It is crucial to comply with ethical considerations and API usage policies when utilizing external services, such as Google's language model API.
  
