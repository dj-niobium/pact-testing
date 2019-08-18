require_relative 'base'

class Shipping < Base
  def initialize(base_url = "http://shipping")
    super(base_url)
  end

  def get_status_for_item(id)
    get_json("/").select{|item| item["id"] == id}.first["status"]
  end

  def get_quantity_on_hold(id)
    get_json("/").select{|item| item["id"] == id && item["status"] == "awaiting_shipping"}.first["quantity"]
  end
end