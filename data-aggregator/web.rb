require 'sinatra'
require_relative 'services/shipping'
require_relative 'services/account'
require_relative 'services/inventory'
require_relative 'controllers/validation'

get '/buy/:account/:id/:quantity' do
  content_type :json
  is_available = Validation.is_available?(params["id"].to_i, params["quantity"].to_i)
  account_details = Account.new.get_account(params["account"].to_i)
  product_name = Inventory.new.get_product_name(params["id"].to_i)
  if is_available
    {
        :status => "Transaction successful",
        :transaction => {
            :account_name => "#{account_details["first_name"]} #{account_details["last_name"]}",
            :product_name => product_name,
            :quantity => params["quantity"]
        }
    }
  else
    {
        :status => "Error. There's not enough product in the warehouse"
    }
  end.to_json
end
