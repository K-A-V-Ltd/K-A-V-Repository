from datetime import datetime

my_current_time = None


def my_time():
    if not my_current_time:
        return datetime.now()
    else:
        return my_current_time
