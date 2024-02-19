from utilities.read_properties import ReadConfig
from tests.restful_booker.restful_booker_api_request import APIRequest

class RestfulBookerClient:

    def __init__(self,base_url):
        self.base_url = base_url
        self.request = APIRequest()

    # GET
    def get_booking_ids(self,token):
        return self.request.get_booking_ids(self.base_url,token)

    def get_booking_id(self, token,id):
        return self.request.get_booking_id(self.base_url, token,id)

    def create_booking(self,token,payload):
        return self.request.create_booking(self.base_url,token,payload)

    def update_booking(self,token,payload,id):
        return self.request.update_booking(self.base_url,token,payload,id)

    def update_partial_booking(self,token,payload,id):
        return self.request.update_booking(self.base_url,token,payload,id)

    def delete_booking(self, token,id):
        return self.request.delete_booking(self.base_url, token,id)
