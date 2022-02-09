import re


class Phone:
    def __init__(self, phone):
        if self.validate_phone(phone):
            self.phone = phone
        else:
            raise ValueError("Incorrect Phone Number!")

    def validate_phone(self, phone):
        # Mold: (55)993869486
        pattern = "([0-9]{2,3})([0-9]{2})([0-9]{4,5})([0-9]{4})"

        return True if re.findall(pattern, phone) else False

    def __str__(self):
        return self.format_phone()

    def format_phone(self):
        pattern = "([0-9]{2,3})([0-9]{2})([0-9]{4,5})([0-9]{4})"
        response = re.search(pattern, self.phone)

        formatted_number = "+{}({}){}-{}".format(
            response.group(1),
            response.group(2),
            response.group(3),
            response.group(4)
        )

        return formatted_number
