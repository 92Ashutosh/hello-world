from agents.planner_agent import planner_agent
from agents.pr_agent import pr_agent
from agents.vendor_agent import vendor_agent
from agents.approval_agent import approval_agent


def handle_pr_request(request):

    trace = []

    # Step 1: Planner
    plan = planner_agent(request)
    trace.append("Planner Agent → Plan created")

    # Step 2: Vendor Check
    vendor_result = vendor_agent(request.vendor)
    trace.append("Vendor Agent → Vendor validated")

    # Step 3: PR Processing
    pr_result = pr_agent(request)
    trace.append("PR Agent → PR processed")

    # Step 4: Approval Decision
    approval = approval_agent(request)
    trace.append(f"Approval Agent → {approval}")

    return {
        "status": approval,
        "trace": trace,
        "pr_id": request.pr_id
    }

