from models.employee_role import EmployeeRole


class Employee:
    def __init__(self, username: str, password: str, role: EmployeeRole):
        self.username = username
        self.password = password
        self.role = role
        self.is_manager = True if self.role == "Manager" else False
        self.is_supervisor = True if self.role == "Supervisor" else False

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value: str):
        if 2 <= len(value) <= 20:
            for symbol in value:
                if not symbol.isalpha() and not symbol.isdigit():
                    raise ValueError('Username contains invalid symbols!')
            self._username = value
        else:
            raise ValueError('Username must be between 2 and 20 characters long!')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if 5 <= len(value) <= 30:
            for symbol in value:
                if not symbol.isalpha() and not symbol.isdigit() and symbol not in ["@", "*", "-", "_"]:
                    raise ValueError('Password contains invalid symbols!')
            self._password = value
        else:
            raise ValueError('Password must be between 5 and 30 characters long!')
