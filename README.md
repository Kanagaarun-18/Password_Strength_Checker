# Password Strength Analyzer

A modern real-time password strength analyzer built with Python, Flask, JavaScript, and zxcvbn.

This tool evaluates password security through entropy calculations, pattern detection, common password databases, and attack simulations.

## Features

- Real-time password analysis as you type
- Visual strength meter with animated feedback
- Entropy calculation (bits of randomness)
- Estimated crack time analysis (instant to centuries)
- Guess number approximation
- Common password detection (10,000+ passwords)
- Pattern detection (sequential, repeated characters)
- Password visibility toggle
- Interactive FAQ section
- Modern glassmorphism UI
- Zero-knowledge - passwords never leave your browser

## Technologies Used

### Backend
- Python 3.8+
- Flask 2.3+
- zxcvbn-python 4.4+

### Frontend
- HTML5
- CSS3
- JavaScript

## Project Structure

```text
Password_Strength_Analyzer/
├── app.py
├── analyzer.py
├── common_passwords.txt
├── requirements.txt
├── Procfile
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/Password_Strength_Analyzer.git
cd Password_Strength_Analyzer
```

### Step 2: Create Virtual Environment

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Access the Tool

Open your browser and navigate to:
http://localhost:5000

## Security Note

🔒 Your passwords are NEVER stored or transmitted - all analysis happens locally in your browser via JavaScript.


## License

MIT License - free for personal and commercial use.

## Acknowledgments

- zxcvbn by Dropbox
- Inspired by Bitwarden's password strength meter

## Support

For issues or feature requests, please open an issue on GitHub.
