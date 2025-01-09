from langchain_openai import ChatOpenAI

# Load .env
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI()
print(llm.invoke("Hello, world!"))