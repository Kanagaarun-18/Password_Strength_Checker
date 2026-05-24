import math
import re
from zxcvbn import zxcvbn

with open("common_passwords.txt", "r", encoding="utf-8") as file:
    COMMON_PASSWORDS = set(file.read().splitlines())

def analyze_password(password):

    feedback = []
    score = 0

    lower = bool(re.search(r"[a-z]", password))
    upper = bool(re.search(r"[A-Z]", password))
    digit = bool(re.search(r"\d", password))
    symbol = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # -----------------------------
    # Basic Rule-Based Checks
    # -----------------------------
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if lower:
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if upper:
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if digit:
        score += 1
    else:
        feedback.append("Add numbers.")

    if symbol:
        score += 1
    else:
        feedback.append("Add special symbols.")

    # -----------------------------
    # Sequential Patterns
    # -----------------------------
    sequences = ["123", "abc", "qwerty", "password", "admin"]

    for seq in sequences:
        if seq in password.lower():
            score -= 2
            feedback.append("Avoid common or sequential patterns.")
            break

    # -----------------------------
    # Repeated Characters
    # -----------------------------
    if re.search(r"(.)\1\1", password):
        score -= 1
        feedback.append("Avoid repeated characters.")

    # -----------------------------
    # Common Password Detection
    # -----------------------------
    if password.lower() in COMMON_PASSWORDS:
        score -= 5
        feedback.append("This password is extremely common and unsafe.")

    # -----------------------------
    # Entropy Calculation
    # -----------------------------
    charset = 0

    if lower:
        charset += 26

    if upper:
        charset += 26

    if digit:
        charset += 10

    if symbol:
        charset += 32

    if charset > 0:
        entropy = round(len(password) * math.log2(charset), 2)
    else:
        entropy = 0

    # -----------------------------
    # zxcvbn Analysis
    # -----------------------------
    zx = zxcvbn(password)

    zxcvbn_score = zx["score"]

    crack_time = zx["crack_times_display"][
        "offline_fast_hashing_1e10_per_second"
    ]

    guesses = zx["guesses"]

    # Add zxcvbn suggestions
    for item in zx["feedback"]["suggestions"]:
        if item not in feedback:
            feedback.append(item)

    if zx["feedback"]["warning"]:
        feedback.append(zx["feedback"]["warning"])

    # -----------------------------
    # Hybrid Final Score
    # -----------------------------
    final_score = zxcvbn_score * 2

    # Small bonus for entropy
    final_score += min(entropy / 50, 1.5)

    # Small bonus for rule-based checks
    final_score += max(score, 0) * 0.3

    final_score = round(min(final_score, 10), 1)
    
    # -----------------------------
    # Strength Classification
    # -----------------------------
    if zxcvbn_score == 0:
        strength = "Extremely Weak"

    elif zxcvbn_score == 1:
        strength = "Weak"

    elif zxcvbn_score == 2:
        strength = "Moderate"

    elif zxcvbn_score == 3:
        strength = "Strong"

    else:
        strength = "Very Strong"
            
    
    if "second" in crack_time:
        strength = "Weak"
        final_score = min(final_score, 3.5)

    if feedback == []:
        feedback.append("Great password! No immediate weaknesses detected.")
        
    # -----------------------------
    # Final Result
    # -----------------------------
    result = {
        "strength": strength,
        "score": final_score,
        "entropy": entropy,
        "crack_time": crack_time,
        "guesses": f"{guesses:,}",
        "feedback": feedback
    }

    return result