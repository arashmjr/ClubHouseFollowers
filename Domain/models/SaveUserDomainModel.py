import datetime


class SaveUserDomainModel:

    user_id: str
    name: str
    photo_url: str
    username: str
    token: str
    phone_number: str
    bio: str
    coin: int

    def __init__(self, user_id: str, name: str, photo_url: str, username: str, token: str, phone_number: str, bio:str, coin: int):
        self.user_id = user_id
        self.name = name
        self.photo_url = photo_url
        self.username = username
        self.token = token
        self.phone_number = phone_number
        self.bio = bio
        self.coin = coin

    def to_dict(self):
        return {"user_id": self.user_id,
                "name": self.name,
                "photo_url": self.photo_url,
                "username": self.username,
                "token": self.token,
                "phone_number": self.phone_number,
                "bio":self.bio,
                "coin": self.coin
                }