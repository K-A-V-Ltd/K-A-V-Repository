class InvalidTime(Exception):
    def __init__(self, time):
        super().__init__(f"'{time}' is in the past.")
