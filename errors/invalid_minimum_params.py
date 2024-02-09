class InvalidMinimumParams(Exception):  # used in the CreateRoute
    def __init__(self, cmd_name: str, count: int):
        super().__init__(f"{cmd_name} command expects a minimum of {count} parameters.")
