
from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent

app = FastAPI()

class QueryRequest(BaseModel):
    query: str
class Query(BaseModel):
    query: str    

@app.get("/")
def root():
    return {"message":"MCP Server Running "}

@app.post("/tool/search")
def search_tool(request: QueryRequest):
    #Dummy toool
    return {
        "result": f"search result for: {request.query} "
        }
    
@app.post("/ask")
def ask_agent(request: Query):
    try:
        print("Incoming query : ", request.query)
    #Dummy toool
        result = agent(request.query)
        return result
    except Exception as e:
        print("Error: ", str(e))
        return {"error" :str(e)}
    
    
@app.get("/tools")
def list_tools():
    return [
        {
            "name":"search",
            "description": "Search for information",
            "input_schema":{
                "type":"object",
                "properties":{
                    "query":{"type":"string"}
                }
            }
        }
    ]
    
    