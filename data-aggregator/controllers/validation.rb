require_relative '../services/shipping'
require_relative '../services/inventory'

class Validation
  def self.is_available?(id, required_quantity)
    shipping_quantity = Shipping.new.get_quantity_on_hold(id)
    inventory_quantity = Inventory.new.get_quantity(id)
    required_quantity <= inventory_quantity - shipping_quantity
  end
end
