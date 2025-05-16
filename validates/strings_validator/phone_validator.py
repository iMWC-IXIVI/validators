import re

from base_validator import BaseValidator


class PhoneNumberValidator(BaseValidator):
    regex = re.compile(r'^\+7 \d{3} \d{3} \d{2} \d{2}$')

    def validate(self, phone_number):
        return self.get_data(phone_number) if self.is_valid(phone_number) else ValueError('Validation error')

    def is_valid(self, phone_number):
        return True if self.get_data(phone_number) else False

    def get_data(self, phone_number):
        return self.regex.search(phone_number)
