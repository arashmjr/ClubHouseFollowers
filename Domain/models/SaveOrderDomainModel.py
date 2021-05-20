import datetime

class SaveOrderDomainModel:

    user_id: str
    order_id: str
    size: int
    creation_date: datetime
    isActive: bool

    def __init__(self, user_id: str, order_id: str, size: int, creation_date: datetime, isActive: bool ):
        self.user_id = user_id
        self.order_id = order_id
        self.size = size
        self.creation_date = creation_date
        self.isActive = isActive

    def to_dict(self):
        return {"user_id": self.user_id,
                "order_id": self.order_id,
                "size": self.size,
                "creation_date": self.creation_date,
                "isActive": self.isActive
                }