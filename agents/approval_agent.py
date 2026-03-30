def approval_agent(request):

    if request.amount < 10000:
        return "Approved"
    else:
        return "Needs Manager Approval"
