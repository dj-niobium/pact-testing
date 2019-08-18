class Validator(object):
    def __init__(self, inventory_service, shipping_service):
        self.inventory = inventory_service
        self.shipping = shipping_service

    def is_available(self, product_id, required_quantity):
        shipping_quantity = self.shipping.get_quantity_on_hold(product_id)
        inventory_quantity = self.inventory.get_quantity(product_id)
        return required_quantity <= inventory_quantity - shipping_quantity
