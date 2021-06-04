

class UserFollowDomainModel:

    user_id: str
    follow_id: str
    order_id: str

    def __init__(self, user_id: str, follow_id: str, order_id: str):
        self.user_id = user_id
        self.follow_id = follow_id
        self.order_id = order_id

    def to_dict(self):
        return {"user_id": self.user_id,
                "follow_id": self.follow_id,
                "order_id": self.order_id
                }

