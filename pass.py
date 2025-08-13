import re
import os
from typing import Dict, List, Tuple

class PasswordStrengthChecker:
    def __init__(self):
        """Initialize the password strength checker."""
        self.common_passwords = self.load_common_passwords()
    
    def load_common_passwords(self) -> set:
        """Load common passwords from file."""
        common_passwords = set()
        try:
            # Check if common_passwords.txt exists
            if os.path.exists('common_passwords.txt'):
                with open('common_passwords.txt', 'r', encoding='utf-8') as file:
                    for line in file:
                        common_passwords.add(line.strip().lower())
            else:
                # Default common passwords if file doesn't exist
                common_passwords = {
                    'password', '123456', 'password123', 'admin', 'qwerty',
                    'letmein', 'welcome', 'monkey', '1234567890', 'abc123',
                    'password1', 'qwerty123', 'welcome123', 'admin123'
                }
        except Exception as e:
            print(f"Error loading common passwords: {e}")
            # Fallback to default set
            common_passwords = {
                'password', '123456', 'password123', 'admin', 'qwerty',
                'letmein', 'welcome', 'monkey', '1234567890', 'abc123'
            }
        
        return common_passwords
    
    def check_length(self, password: str) -> Tuple[bool, str]:
        """Check if password meets length requirements."""
        if len(password) < 8:
            return False, "Password should be at least 8 characters long"
        elif len(password) >= 12:
            return True, "Excellent length (12+ characters)"
        else:
            return True, "Good length (8-11 characters)"
    
    def check_complexity(self, password: str) -> Dict[str, bool]:
        """Check password complexity requirements."""
        checks = {
            'has_lowercase': bool(re.search(r'[a-z]', password)),
            'has_uppercase': bool(re.search(r'[A-Z]', password)),
            'has_numbers': bool(re.search(r'\d', password)),
            'has_special_chars': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
        }
        return checks
    
    def check_common_patterns(self, password: str) -> List[str]:
        """Check for common weak patterns."""
        warnings = []
        
        # Check for common passwords
        if password.lower() in self.common_passwords:
            warnings.append("This is a commonly used password")
        
        # Check for sequential patterns
        if re.search(r'123|abc|qwe', password.lower()):
            warnings.append("Contains sequential characters")
        
        # Check for repeated characters
        if re.search(r'(.)\1{2,}', password):
            warnings.append("Contains repeated characters")
        
        # Check for keyboard patterns
        keyboard_patterns = ['qwerty', 'asdf', 'zxcv', '1234', '4567']
        for pattern in keyboard_patterns:
            if pattern in password.lower():
                warnings.append("Contains keyboard patterns")
                break
        
        return warnings
    
    def calculate_score(self, password: str) -> int:
        """Calculate password strength score (0-100)."""
        score = 0
        
        # Length scoring
        length = len(password)
        if length >= 8:
            score += 20
        if length >= 12:
            score += 10
        if length >= 16:
            score += 10
        
        # Complexity scoring
        complexity = self.check_complexity(password)
        score += sum(complexity.values()) * 10  # 10 points each for complexity
        
        # Bonus for variety
        if sum(complexity.values()) >= 3:
            score += 10
        if sum(complexity.values()) == 4:
            score += 10
        
        # Deduct points for common patterns
        warnings = self.check_common_patterns(password)
        score -= len(warnings) * 15
        
        # Ensure score is between 0 and 100
        return max(0, min(100, score))
    
    def get_strength_level(self, score: int) -> str:
        """Get strength level based on score."""
        if score < 30:
            return "Very Weak"
        elif score < 50:
            return "Weak"
        elif score < 70:
            return "Moderate"
        elif score < 85:
            return "Strong"
        else:
            return "Very Strong"
    
    def analyze_password(self, password: str) -> Dict:
        """Analyze password and return comprehensive results."""
        if not password:
            return {
                'score': 0,
                'strength': 'Very Weak',
                'length_check': (False, 'Password cannot be empty'),
                'complexity': {},
                'warnings': ['Password is empty'],
                'suggestions': ['Enter a password to analyze']
            }
        
        score = self.calculate_score(password)
        strength = self.get_strength_level(score)
        length_check = self.check_length(password)
        complexity = self.check_complexity(password)
        warnings = self.check_common_patterns(password)
        
        # Generate suggestions
        suggestions = []
        if not length_check[0]:
            suggestions.append("Make password at least 8 characters long")
        
        if not complexity['has_lowercase']:
            suggestions.append("Add lowercase letters")
        if not complexity['has_uppercase']:
            suggestions.append("Add uppercase letters")
        if not complexity['has_numbers']:
            suggestions.append("Add numbers")
        if not complexity['has_special_chars']:
            suggestions.append("Add special characters (!@#$%^&*)")
        
        if warnings:
            suggestions.append("Avoid common passwords and patterns")
        
        if not suggestions:
            suggestions.append("Your password looks good!")
        
        return {
            'score': score,
            'strength': strength,
            'length_check': length_check,
            'complexity': complexity,
            'warnings': warnings,
            'suggestions': suggestions
        }

def main():
    """Main function to run the password strength checker."""
    print("🔐 Password Strength Checker")
    print("=" * 40)
    
    checker = PasswordStrengthChecker()
    
    while True:
        print("\nOptions:")
        print("1. Check password strength")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ").strip()
        
        if choice == '1':
            password = input("\nEnter password to check: ")
            result = checker.analyze_password(password)
            
            print(f"\n📊 Analysis Results:")
            print(f"Score: {result['score']}/100")
            print(f"Strength: {result['strength']}")
            print(f"Length: {result['length_check'][1]}")
            
            print(f"\n✅ Complexity Checks:")
            complexity = result['complexity']
            print(f"  Lowercase letters: {'✓' if complexity.get('has_lowercase') else '✗'}")
            print(f"  Uppercase letters: {'✓' if complexity.get('has_uppercase') else '✗'}")
            print(f"  Numbers: {'✓' if complexity.get('has_numbers') else '✗'}")
            print(f"  Special characters: {'✓' if complexity.get('has_special_chars') else '✗'}")
            
            if result['warnings']:
                print(f"\n⚠️  Warnings:")
                for warning in result['warnings']:
                    print(f"  - {warning}")
            
            print(f"\n💡 Suggestions:")
            for suggestion in result['suggestions']:
                print(f"  - {suggestion}")
        
        elif choice == '2':
            print("Thank you for using Password Strength Checker!")
            break
        
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()