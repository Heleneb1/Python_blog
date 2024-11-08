from django.core.exceptions import ValidationError
from django.core import validators
from django import forms

class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):  # Correction : utilisation de isalpha()
            raise ValidationError(
                'The password must contain at least one letter.',
                code='password_no_letter'
            )

    def get_help_text(self):
        return 'Your password must contain at least one letter.'
    
class ContainsNumberValidator:
    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):  # Correction : utilisation de isdigit()
            raise ValidationError(
                'The password must contain at least one number.',
                code='password_no_number'
            )

    def get_help_text(self):
        return 'Your password must contain at least one number.'
    
class PostalCodeValidator:
    def __init__(self, code_length=5):
        self.code_length = code_length

    def validate(self, postal_code, user=None):
        if not postal_code.isdigit() or len(postal_code) != self.code_length:
            raise ValidationError(
                'The postal code must be a {0}-digit number.'.format(self.code_length),
                code='postal_code_invalid'
            )

    def get_help_text(self):
        return 'Your postal code must be a {0}-digit number.'.format(self.code_length)