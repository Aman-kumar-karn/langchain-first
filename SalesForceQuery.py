import os
from langchain_community.document_loaders import TextLoader as TL
from langchain_text_splitters import RecursiveCharacterTextSplitter as RCTS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

loader=TL("imformation.txt")
doc=loader.load()

splitter=RCTS(
    chunk_size=90,
    chunk_overlap=10,
    separators = [""]
)

chunk = splitter.split_documents(doc)


# print(chunk[1].page_content)
# splitDoc=[page.page_content for page in chunk ]
# # print(os.environ.get("GOOGLE_API_KEY"))

embeddings = HuggingFaceEmbeddings(
model_name="all-MiniLM-L6-v2"
)
# vector = embeddings.embed_documents(splitDoc)
if os.path.exists("./chroma_langchain_db"):
    print("Loading existing DB...")
    db = Chroma(
    collection_name="chunk",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db"
    )
else:
    print("Creating new DB...")
    db = Chroma.from_documents(
    documents=chunk,
    embedding=embeddings,
    collection_name="chunk",
    persist_directory="./chroma_langchain_db"
    )

query = "what is a governer limit"
results = db.similarity_search(query, k=1)
print(results[0].page_content)




