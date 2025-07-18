def rerank_score(initial_score, comments):
    rules = {
        "urgent": +10,
        "immediately": +8,
        "call me": +6,
        "not interested": -20,
        "maybe later": -10
    }

    score = initial_score
    for keyword, impact in rules.items():
        if keyword in comments.lower():
            score += impact
    
    return min(max(score, 0), 100)