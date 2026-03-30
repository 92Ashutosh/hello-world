def planner_agent(request):
    return {
        "intent": "PR_APPROVAL",
        "steps": ["validate_vendor", "check_budget", "approve_or_reject"]
    }
