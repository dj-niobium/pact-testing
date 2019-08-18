require "http"
require "json"

class Base
  def initialize(base_url)
    @base_url = base_url
  end

  def get_json(url)
    JSON.parse(HTTP.get("#{@base_url}").body)
  end
end