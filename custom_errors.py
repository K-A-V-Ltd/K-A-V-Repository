class OwnedVehicles(Exception):
    def __init__(self, value):
        super().__init__(f"You don't own more {value} vehicles!")
