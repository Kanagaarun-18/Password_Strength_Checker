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
- HTML5, CSS3, Vanilla JavaScript

## Project Structure

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

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

git clone https://github.com/yourusername/Password_Strength_Analyzer.git
cd Password_Strength_Analyzer

### Step 2: Create Virtual Environment

Windows:
python -m venv venv
venv\Scripts\activate

Mac/Linux:
python3 -m venv venv
source venv/bin/activate

### Step 3: Install Dependencies

pip install -r requirements.txt

### Step 4: Run the Application

python app.py

### Step 5: Access the Tool

Open your browser and navigate to:
http://localhost:5000

## requirements.txt

Flask==2.3.3
zxcvbn-python==4.4.28

## Usage Examples

| Password | Strength | Crack Time |
|----------|----------|-------------|
| password123 | Weak | Instant |
| P@ssw0rd | Fair | Minutes |
| BlueSky$42 | Good | Months |
| Tr0ub4dor&3 | Strong | Centuries |
| C0rrect-Horse-Battery-Staple | Very Strong | Millennia |

## How It Works

1. Entropy Calculation: Measures password randomness in bits
2. Pattern Analysis: Detects sequences, repeats, and common structures
3. Dictionary Check: Compares against 10,000+ common passwords
4. Attack Simulation: Estimates time to crack using modern hardware
5. Real-time Feedback: Updates strength meter as you type

## Security Note

🔒 Your passwords are NEVER stored or transmitted - all analysis happens locally in your browser via JavaScript.

## Deployment Options

### Deploy to Render (Free)
1. Push code to GitHub
2. Create new Web Service on Render
3. Connect repository
4. Set build command: pip install -r requirements.txt
5. Set start command: gunicorn app:app

### Deploy to Railway

railway login
railway init
railway up

### Deploy to Heroku

heroku create your-app-name
git push heroku main
heroku open

## Local Development

To modify the analyzer:
1. Edit analyzer.py - change strength calculation logic
2. Edit templates/index.html - modify UI structure
3. Edit static/style.css - update styling
4. Refresh browser to see changes

## Troubleshooting

Issue: Port 5000 already in use
python app.py --port 5001

Issue: zxcvbn not found
pip install --upgrade zxcvbn-python

Issue: Common passwords not loading
- Ensure common_passwords.txt is in the root directory
- File should contain one password per line

## License

MIT License - free for personal and commercial use.

## Acknowledgments

- zxcvbn by Dropbox
- Inspired by Bitwarden's password strength meter

## Support

For issues or feature requests, please open an issue on GitHub.
