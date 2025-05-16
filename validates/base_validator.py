from abc import ABC, abstractmethod


class BaseValidator(ABC):
    @abstractmethod
    def validate(self, phone_number):
        pass

    @abstractmethod
    def is_valid(self, phone_number):
        pass

    @abstractmethod
    def get_data(self, phone_number):
        pass
