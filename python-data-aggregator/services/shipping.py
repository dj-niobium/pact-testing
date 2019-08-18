from services.base import Base


class Shipping(Base):
    def get_data(self):
        return self.get("/")

    def get_quantity_on_hold(self, product_id):
        first_resp = [el for el in self.get_data() if el["id"] == product_id and el["status"] == "awaiting_shipping"][0]
        return first_resp['quantity']
