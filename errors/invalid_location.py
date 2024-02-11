class InvalidLocation(Exception):
    def __init__(self, location: str):
        super().__init__(f"'{location}' is not a valid location.")
