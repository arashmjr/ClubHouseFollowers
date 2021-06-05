
class GetPackagesDomainModel:

    package_id: str
    package_name: str
    price: int

    def __init__(self, package_id: str, package_name: str, price: int):
        self.package_id = package_id
        self.package_name = package_name
        self.price = price

    def to_dict(self):
        return {"package_id": self.package_id,
                "package_name": self.package_name,
                "price": self.price,
                }

