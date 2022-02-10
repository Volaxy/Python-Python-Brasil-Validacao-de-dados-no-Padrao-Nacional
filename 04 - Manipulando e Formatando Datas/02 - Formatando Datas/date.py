from datetime import datetime


class Date:
    def __init__(self):
        # The ".today()" returns the actual date time Ex.: 2022-02-09 21:23:34.044316
        self.moment = datetime.today()

    def month(self):
        months_of_year = [
            "January", "February", "March",
            "April", "May", "June",
            "July", "August", "September",
            "October", "November", "December"
        ]

        # The ".month" returns the month in the integer format
        month = self.moment.month

        return months_of_year[month - 1]

    def week_day(self):
        week_days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
        ]

        return week_days[self.moment.weekday()]

    def __str__(self):
        return self.formatted_date()

    def formatted_date(self):
        return self.moment.strftime("%d/%m/%Y %H:%M")
