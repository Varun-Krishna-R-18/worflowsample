# email_validator.py
import re

class EmailValidator:
    """
    A comprehensive email validation class that checks multiple aspects of email addresses.
    """
    
    @staticmethod
    def validate_email(email):
        """
        Validate an email address based on multiple criteria.
        
        Args:
            email (str): Email address to validate
        
        Returns:
            bool: True if email is valid, False otherwise
        """
        # Check if email is a string and not empty
        if not isinstance(email, str) or not email:
            return False
        
        # Remove leading/trailing whitespace
        email = email.strip()
        
        # Basic regex pattern for email validation
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        # Check if email matches the basic pattern
        if not re.match(email_pattern, email):
            return False
        
        # Additional checks
        return (
            EmailValidator._check_local_part(email.split('@')[0]) and
            EmailValidator._check_domain(email.split('@')[1])
        )
    
    @staticmethod
    def _check_local_part(local_part):
        """
        Validate the local part of the email (before @).
        
        Args:
            local_part (str): Local part of the email address
        
        Returns:
            bool: True if local part is valid, False otherwise
        """
        # Check length constraints
        if len(local_part) < 1 or len(local_part) > 64:
            return False
        
        # Check for consecutive dots
        if '..' in local_part:
            return False
        
        # Check for leading or trailing dot
        if local_part.startswith('.') or local_part.endswith('.'):
            return False
        
        return True
    
    @staticmethod
    def _check_domain(domain):
        """
        Validate the domain part of the email (after @).
        
        Args:
            domain (str): Domain part of the email address
        
        Returns:
            bool: True if domain is valid, False otherwise
        """
        # Check length constraints
        if len(domain) < 3 or len(domain) > 255:
            return False
        
        # Check for consecutive dots
        if '..' in domain:
            return False
        
        # Check domain parts
        parts = domain.split('.')
        
        # Ensure at least one dot and valid top-level domain
        if len(parts) < 2 or len(parts[-1]) < 2:
            return False
        
        # Check each part of the domain
        for part in parts:
            if not re.match(r'^[a-zA-Z0-9-]+$', part):
                return False
            if part.startswith('-') or part.endswith('-'):
                return False
        
        return True
