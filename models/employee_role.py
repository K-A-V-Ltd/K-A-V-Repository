class EmployeeRole:
    NORMAL = "Normal"
    MANAGER = "Manager"
    SUPERVISOR = "Supervisor"

    @classmethod
    def from_string(cls, value: str):
        if value not in [cls.NORMAL, cls.MANAGER, cls.SUPERVISOR]:
            raise ValueError(f"The role {value} is not a valid employee role!")
        return value
