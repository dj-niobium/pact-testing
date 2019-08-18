require 'sinatra'

get '/' do
  content_type :json
  File.read('db_response.json')
end
