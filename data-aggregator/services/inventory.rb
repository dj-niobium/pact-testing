require_relative 'base'

class Inventory < Base
  def initialize(base_url = "http://inventory")
    super(base_url)
  end

  def get_quantity(id)
    get_json("").select{|item| item["id"] == id}.first["quantity"]
  end

  def get_product_name(id)
    get_json("").select{|item| item["id"] == id}.first["name"]
  end
end

