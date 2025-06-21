def mock_agent_response(prompt):
    if "palindrome" in prompt:
        return "def is_palindrome(s): return s == s[::-1]"
    return "I don't know."