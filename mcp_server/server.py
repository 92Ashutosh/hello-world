from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="MCP Server - Procurement Tools")

# -----------------------------# Models# -----------------------------
class PRToolInput(BaseModel):
    pr_id: str
    vendor: str
    amount: float

# -----------------------------# Tools# -----------------------------
@app.post("/tools/create_pr")
def create_pr(data: PRToolInput):
    
    return {"status": "PR Created", "pr_id": data.pr_id }

@app.post("/tools/check_vendor")
def check_vendor(data: PRToolInput):
   approved_vendors = ["Dell", "Lenovo", "HP"]
   if data.vendor in approved_vendors:
       return {"vendor_status": "approved"}  
   else: return {"vendor_status": "not approved"}

@app.post("/tools/approve_pr")
def approve_pr(data: PRToolInput):
   if data.amount < 10000: return {"approval": "approved"}
   else:
       return {"approval": "manager_required"}