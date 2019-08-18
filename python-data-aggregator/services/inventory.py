from services.base import Base


class Inventory(Base):
    def get_data(self):
        return self.get("/")

    def get_quantity(self, prod_id):
        return [el for el in self.get_data() if el["id"] == prod_id][0]["quantity"]

    def get_product_name(self, prod_id):
        return [el for el in self.get_data() if el["id"] == prod_id][0]["name"]

