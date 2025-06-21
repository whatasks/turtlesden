CERT_QUESTIONS = {
    "code_generation": [
        {"question": "Write a Python function to check for palindrome.", "keywords": ["def", "[::-1]", "=="]}
    ]
}

def simulate_certification(agent_callback):
    import random
    results = {}
    for cert_area, questions in CERT_QUESTIONS.items():
        q = random.choice(questions)
        answer = agent_callback(q["question"])
        passed = all(keyword in answer for keyword in q["keywords"])
        results[cert_area] = {
            "question": q["question"],
            "answer": answer,
            "evaluation": "pass" if passed else "fail"
        }
    return results