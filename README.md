# 🔐 Password Strength Checker

A comprehensive Python tool that analyzes password strength and provides detailed feedback to help users create secure passwords.

## ✨ Key Features

- **Real-time Analysis**: Instant password strength evaluation (0-100 scoring)
- **Multi-layer Security Checks**: Length, complexity, patterns, and common passwords  
- **Educational Feedback**: Detailed suggestions for password improvement
- **User-friendly Interface**: Clean command-line experience
- **Secure Processing**: No password storage - analysis in memory only

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher

### Installation & Usage
```bash
# Clone the repository
git clone https://github.com/Khushi-Janji21/password-strength-checker.git

# Navigate to project directory
cd password-strength-checker

# Run the application
python password_checker.py

🔬 How It Works
Scoring System

Length: 20 points (8+ chars) + bonuses for 12+ and 16+
Complexity: 10 points each for uppercase, lowercase, numbers, special chars
Variety Bonus: Extra points for using multiple character types
Security Deductions: -15 points for common passwords/patterns

Strength Categories

0-29: Very Weak 🔴
30-49: Weak 🟠
50-69: Moderate 🟡
70-84: Strong 🟢
85-100: Very Strong 🟢

🛡️ Security Features

Common password detection (70+ passwords)
Sequential pattern recognition (123, abc)
Keyboard pattern detection (qwerty, asdf)
Repeated character analysis
No data storage or logging

🔮 Future Enhancements

 GUI interface
 Password generation
 Breach database integration
 Export reports

👨‍💻 Author
Khushi Janji

Email: khushijanji@gmail.com
GitHub: @Khushi-Janji21

📄 License
This project is licensed under the MIT License.
