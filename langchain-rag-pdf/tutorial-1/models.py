import os
from langchain_ollama import OllamaEmbeddings, ChatOllama # type: ignore
# from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI

class Models:
    def __init__(self):
        # ollama pull mxbai-embed-large
        self.embeddings_ollama = OllamaEmbeddings(
            # model="mxbai-embed-large",
            # model="deepseek-r1:14b",
            model="granite3.2:8b-instruct-q8_0",
            # model="llama3.1:8b-instruct-q8_0",
            # model="granite-embedding"
            # model="granite-embedding:278m",
            # model_name="granite-embedding"
            # model_name="bge-m3",
            # model_name="all-minilm:33m",
            # base_url="http://localhost:11434",
            # model="granite3.1-dense:8b-instruct-q8_0",
            # ollama_additional_kwargs={"mirostat": 0}            
        )

        # ollama pull llama3.2
        self.model_ollama = ChatOllama(
            # model="llama3.3",
            # model="deepseek-r1:14b",
            # model="mistral",
            # model="llama3:8b-instruct-q8_0",
            # model="llama3.1:8b-instruct-q8_0",
            # model="llama3.1:70b-instruct-q8_0",
            model="granite3.2:8b-instruct-q8_0",
            # model="granite3.1-dense:8b",
            # model="granite3.1-dense:8b-instruct-q8_0",
            temperature=0,
        )   

        # # Azure OpenAI embeddings
        # self.embeddings_openai = AzureOpenAIEmbeddings(
        #     model="text-embedding-3-large",
        #     dimensions=1536,  # Can specify dimensions with new text-embedding-3 models
        #     azure_endpoint=os.environ.get("AZURE_OPENAI_EMBEDDINGS_ENDPOINT"),
        #     api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
        #     api_version=os.environ.get("AZURE_OPENAI_EMBEDDINGS_API_VERSION"),
        # )

        # # Azure OpenAI chat model
        # self.model_openai = AzureChatOpenAI(
        #     azure_deployment=os.environ.get("AZURE_OPENAI_API_DEPLOYMENT_NAME"),
        #     api_version=os.environ.get("AZURE_OPENAI_API_VERSION"),
        #     temperature=0,
        #     max_tokens=None,
        #     timeout=None,
        #     max_retries=2,
        # )