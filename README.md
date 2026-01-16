import re

def audit_password(password):
    """
    Audits a password against standard complexity rules.
    Returns a score and a list of missing requirements.
    """
    score = 0
    feedback = []
    
    # Rule 1: Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (min 8 chars).")

    # Rule 2: Upper and Lowercase
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Missing mix of uppercase and lowercase letters.")

    # Rule 3: Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Missing a number.")

    # Rule 4: Special Characters
    if re.search(r"[ !#$%&'()*+,-./:;<=>?@[\]^_`{|}~]", password):
        score += 1
    else:
        feedback.append("Missing a special character.")

    return score, feedback

if __name__ == "__main__":
    print("--- Password Policy Auditor ---")
    user_pass = input("Enter password to test: ")
    
    score, issues = audit_password(user_pass)
    
    print(f"\nPassword Score: {score}/4")
    if score == 4:
        print("[+] Status: STRONG")
    else:
        print("[-] Status: WEAK")
        for issue in issues:
            print(f"    - {issue}")
