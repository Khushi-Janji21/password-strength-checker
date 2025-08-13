# 🔐 Password Strength Checker

A comprehensive Python tool that analyzes password strength and provides detailed feedback to help users create secure passwords.

## Features

- **Real-time password analysis** - Instant feedback on password strength
- **Comprehensive scoring system** - 0-100 point scoring algorithm
- **Multiple security checks**:
  - Length requirements (minimum 8 characters)
  - Character complexity (uppercase, lowercase, numbers, special chars)
  - Common password detection
  - Pattern recognition (sequential chars, keyboard patterns)
  - Repeated character detection
- **Detailed suggestions** - Actionable advice to improve password security
- **User-friendly interface** - Clean command-line interface

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Khushi Janji/password-strength-checker.git
   cd password-strength-checker
   ```

2. **Ensure you have Python 3.6+ installed:**
   ```bash
   python --version
   ```

## Usage

1. **Run the password checker:**
   ```bash
   python password_checker.py
   ```

2. **Follow the interactive prompts:**
   - Choose option 1 to check password strength
   - Enter your password when prompted
   - Review the detailed analysis and suggestions

## How It Works

### Scoring Algorithm

The password strength is calculated based on multiple factors:

- **Length Points**: 
  - 8+ characters: 20 points
  - 12+ characters: +10 bonus points
  - 16+ characters: +10 additional bonus points

- **Complexity Points**: 10 points each for:
  - Lowercase letters (a-z)
  - Uppercase letters (A-Z) 
  - Numbers (0-9)
  - Special characters (!@#$%^&*(),.?":{}|<>)

- **Variety Bonus**:
  - 3+ character types: +10 points
  - All 4 character types: +10 additional points

- **Security Deductions**: -15 points each for:
  - Common passwords
  - Sequential patterns (123, abc)
  - Repeated characters (aaa)
  - Keyboard patterns (qwerty, asdf)

### Strength Levels

| Score Range | Strength Level |
|-------------|---------------|
| 0-29        | Very Weak     |
| 30-49       | Weak          |
| 50-69       | Moderate      |
| 70-84       | Strong        |
| 85-100      | Very Strong   |

## File Structure

```
password-strength-checker/
├── pass.py      # Main application script
├── common_passwords.txt     # Database of common passwords
└── README.md               # Project documentation
```

## Example Output

```
🔐 Password Strength Checker
========================================

Enter password to check: MySecureP@ssw0rd123

📊 Analysis Results:
Score: 85/100
Strength: Very Strong
Length: Excellent length (12+ characters)

✅ Complexity Checks:
  Lowercase letters: ✓
  Uppercase letters: ✓
  Numbers: ✓
  Special characters: ✓

💡 Suggestions:
  - Your password looks good!
```

## Security Features

- **No password storage** - Passwords are analyzed in memory only
- **Common password database** - Checks against 70+ common passwords
- **Pattern recognition** - Detects weak patterns and sequences
- **Comprehensive analysis** - Multiple security criteria evaluation

## Customization

You can customize the tool by:

1. **Adding more common passwords** to `common_passwords.txt`
2. **Modifying scoring criteria** in the `calculate_score()` method
3. **Adding new pattern checks** in the `check_common_patterns()` method
4. **Adjusting strength thresholds** in the `get_strength_level()` method

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only built-in libraries)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Future Enhancements

- [ ] GUI interface using Tkinter or PyQt
- [ ] Password generation with customizable criteria
- [ ] Entropy calculation
- [ ] Dictionary attack simulation
- [ ] Multi-language support
- [ ] Password history tracking
- [ ] Breach database integration

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for educational and security awareness purposes. Always use strong, unique passwords for your accounts and consider using a reputable password manager.

## Contact

Khushi Janji - khushijanji@gmail.com
Project Link: https://github.com/Khushi Janji/password-strength-checker