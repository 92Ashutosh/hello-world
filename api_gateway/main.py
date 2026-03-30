from fastapi import FastAPI
from pydantic import BaseModel
from services.orchestrator import handle_pr_request
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Procurement AI Gateway")

class PRRequest(BaseModel):
    pr_id: str
    vendor: str
    amount: float
    action: str # approve / reject

@app.get("/")
def health():
    return {"status": "API Gateway Running"}

@app.post("/process_pr")
def process_pr(request: PRRequest):
    response = handle_pr_request(request)
    return response