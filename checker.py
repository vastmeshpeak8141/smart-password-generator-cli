import re

def check_strength(password):
    """Evaluate password strength and return score + label."""
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters")
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters")
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add digits")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add special characters")

    # Check for common patterns
    if not re.search(r'(.)\1{2,}', password):
        score += 1
    else:
        feedback.append("Avoid repeated characters")

    levels = {
        0: "Very Weak",
        1: "Very Weak",
        2: "Weak",
        3: "Weak",
        4: "Fair",
        5: "Good",
        6: "Strong",
        7: "Very Strong",
        8: "Excellent",
    }
    label = levels.get(min(score, 8), "Excellent")
    return {"score": score, "max_score": 8, "label": label, "feedback": feedback}

def print_strength(password):
    """Print a formatted strength report."""
    result = check_strength(password)
    bar_len = 20
    filled = int(bar_len * result["score"] / result["max_score"])
    bar = "#" * filled + "-" * (bar_len - filled)
    print(f"Strength: [{bar}] {result['label']} ({result['score']}/{result['max_score']})")
    if result["feedback"]:
        print("Suggestions:")
        for tip in result["feedback"]:
            print(f"  - {tip}")
