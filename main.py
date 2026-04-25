import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm=ChatGroq(
    api_key= os.environ.get("GROQ_API_KEY"),
    model= "llama-3.1-8b-instant"
    )

response=llm.invoke("Explain what is Retrieval Augmented Generation (RAG) in AI in 3 lines")
print(response.content)

# llama-3.3-70b-versatile