from datetime import datetime, timedelta
from date import Date


def __main__():
    today = Date()

    print(today.moment)
    print(today.month())
    print(today.week_day())


if __name__ == "__main__":
    __main__()
