import os
from re import split
import time
# from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from uuid import uuid4
from models import Models

# load_dotenv()

# Initialize the models
models = Models()
embeddings = models.embeddings_ollama
llm = models.model_ollama

# Define constants
data_folder ="all_pdfs_m"
chunk_size = 500
chunk_overlap = 100
check_interval = 10 
batch_size = 41666
# Chroma vector store
# for i in range(0, len(split), batch_size):
#     batch = split[i:i + batch_size]
vector_store = Chroma(
    collection_name="IntelliMagic",
    embedding_function=embeddings,
    persist_directory="./db/chroma_langchain_db_text_deepseek",  # Where to save data locally
    # show_progress=True,
)

# Ingest a file
def ingest_file(file_path):
    # Skip non-PDF files
    if not file_path.lower().endswith('.txt'):
        print(f"Skipping non-PDF file: {file_path}")
        return
    
    print(f"Starting to ingest file: {file_path}")
    loader = TextLoader(file_path)
    loaded_documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap,     separators=[
        # "\n\n",
        # "\n\n",
        # "\n",
        # " ",
        # ".",
        # ",",
        "-------------------------------------------------------------------------------------------------",
        # "\u200b",  # Zero-width space
        # "\uff0c",  # Fullwidth comma
        # "\u3001",  # Ideographic comma
        # "\uff0e",  # Fullwidth full stop
        # "\u3002",  # Ideographic full stop
        "",
    ]
    )
    documents = text_splitter.split_documents(loaded_documents)
    uuids = [str(uuid4()) for _ in range(len(documents))]
    print(f"Adding {len(documents)} documents to the vector store")
    vector_store.add_documents(documents=documents, ids=uuids,show_progress=True,)
    print(f"Finished ingesting file: {file_path}")


# Main loop
def main_loop():
    while True:
        for filename in os.listdir(data_folder):
            if not filename.startswith("_"):
                file_path = os.path.join(data_folder, filename)
                ingest_file(file_path)
                new_filename = "_" + filename
                new_file_path = os.path.join(data_folder, new_filename)
                os.rename(file_path, new_file_path)
        time.sleep(check_interval)  # Check the folder every 10 seconds

# Run the main loop
if __name__ == "__main__":
    main_loop()