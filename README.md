# Password Strength Analyzer

A modern real-time password strength analyzer built using Python, Flask, JavaScript, and zxcvbn.

This project analyzes password security using entropy calculations, pattern detection, common password databases, and intelligent attack simulations inspired by professional password managers like Bitwarden and 1Password.

---

# Features

- Real-time password analysis
- Live strength meter
- Animated security bar
- Entropy calculation
- Estimated crack time analysis
- Approximate guess estimation
- Common password detection
- Sequential pattern detection
- Repeated character detection
- Eye toggle for password visibility
- Interactive FAQ section
- Modern glassmorphism + SaaS UI
- Zero-knowledge analysis (passwords are never stored)

---

# Technologies Used

## Backend
- Python
- Flask
- zxcvbn

## Frontend
- HTML5
- CSS3
- JavaScript

---

# Project Structure

```text
Password_Strength_Analyzer/
│
├── app.py
├── analyzer.py
├── common_passwords.txt
├── requirements.txt
├── Procfile
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
