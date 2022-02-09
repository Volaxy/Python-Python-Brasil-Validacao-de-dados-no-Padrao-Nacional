import re


class Phone:
    def __init__(self, phone):
        if self.validate_phone(phone):
            self.phone = phone
        else:
            raise ValueError("Incorrect Phone Number!")

    def validate_phone(self, phone):
        # Mold: (55)993869486
        pattern = "[0-9]{2,3}[0-9]{2}[0-9]{4,5}[0-9]{4}"

        # The "re.findall()" returns a list containing the matches in the string
        return True if re.findall(pattern, phone) else False
