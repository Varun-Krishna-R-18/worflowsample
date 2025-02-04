# test_email_validator.py
import unittest
from email_validator import EmailValidator

class TestEmailValidator(unittest.TestCase):
    def test_valid_emails(self):
        """Test valid email addresses"""
        valid_emails = [
            'user@example.com',
            'john.doe@company.co.uk',
            'user123@domain.org',
            'first-last@domain.name',
            'user+tag@example.com'
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(EmailValidator.validate_email(email), 
                                f"Failed to validate valid email: {email}")
    
    def test_invalid_emails(self):
        """Test invalid email addresses"""
        invalid_emails = [
            '',  # Empty string
            'invalid-email',  # Missing @
            'user@.com',  # Invalid domain
            'user@domain',  # Missing top-level domain
            '@domain.com',  # Missing local part
            'user@domain..com',  # Consecutive dots in domain
            'user.@domain.com',  # Trailing dot in local part
            '.user@domain.com',  # Leading dot in local part
            'user@-domain.com',  # Hyphen at start of domain
            'user@domain-.com',  # Hyphen at end of domain
            'user@domain.c',  # Too short top-level domain
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(EmailValidator.validate_email(email), 
                                 f"Failed to reject invalid email: {email}")
    
    def test_email_length_constraints(self):
        """Test email length constraints"""
        # Local part max length is 64 characters
        long_local_part = 'a' * 65 + '@domain.com'
        self.assertFalse(EmailValidator.validate_email(long_local_part))
        
        # Domain max length is 255 characters
        long_domain = 'user@' + 'a' * 256
        self.assertFalse(EmailValidator.validate_email(long_domain))
    
    def test_edge_cases(self):
        """Test edge cases and type handling"""
        # Non-string input
        self.assertFalse(EmailValidator.validate_email(None))
        self.assertFalse(EmailValidator.validate_email(123))
        
        # Whitespace
        self.assertTrue(EmailValidator.validate_email('  user@domain.com  '))

if __name__ == '__main__':
    unittest.main()
