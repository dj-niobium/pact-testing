require_relative 'base'

class Account < Base
  def initialize(base_url = "http://account")
    super(base_url)
  end

  def get_account(id)
    get_json("/").select{|account| account["id"] == id}.first
  end
end
