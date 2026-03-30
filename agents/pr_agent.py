def pr_agent(request):

    if request.amount > 10000:
        return "High Value PR"
    return "Normal PR"