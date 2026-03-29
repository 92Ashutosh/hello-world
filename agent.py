import requests
from openai import OpenAI
from dotenv import load_dotenv
import os

MCP_URL =  "http://localhost:8000"

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def call_search_tool(query):
    response = requests.post(
        f"{MCP_URL}/tool/search",
        json={"query":query}
        
    )
    return response.json()
memory = []

def agent(query):
    memory.append({"role":"user", "content":query})
    #simple decision logic
    tools = requests.get("http://localhost:8000/tools").json()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages = memory
    )
    output = response.choices[0].message.content
    memory.append({
            "role": "assistant",
            "content":output
        })
    
    return {"response":output}


    



