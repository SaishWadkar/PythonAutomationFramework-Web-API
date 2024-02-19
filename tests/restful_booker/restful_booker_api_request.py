import json
import base64
import requests
from dataclasses import dataclass
from utilities.read_properties import ReadConfig

@dataclass
class APIResponse():
    status_code : int
    text : str
    as_dict : object
    headers : dict
    time : int

class APIRequest:
    '''
        GET , POST , PUT , DELETE and collect all resp
    '''

    # GET
    def get_booking_ids(self,base_url,token):
        # header = {"Authorization": token}
        try:
            response = requests.get(url=f"{base_url}/booking")
            # print(f"3-Response JSON : {response.json()}")
            # print(f"3-Response JSON Type : {type(response.json())}")

            return self.__get_responses(response)

        # except requests.exceptions.Timeout as e:
        #     print(f"Time out exception : {e}")
        #     return e

        except Exception as e:
            print(f"General Exception : {e}")
            return e

        finally:
            pass


    def get_booking_id(self,url,token,id):
        response = requests.get(url=f"{url}/booking/{id}")
        return self.__get_responses(response)

    def create_booking(self,base_url,token,payload):
        data = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        # print(data)
        response = requests.post(url=f"{base_url}/booking",data=data,headers=headers)
        # print(response)
        return self.__get_responses(response)

    def update_booking(self, base_url, token, payload,id):
        data = json.dumps(payload)
        complete_token = 'token='+token
        headers = {
            'Cookie': complete_token ,
            'Content-Type': 'application/json'
        }

        response = requests.put(url=f"{base_url}/booking/{id}", data=data, headers=headers)
        print(response)
        return self.__get_responses(response)

    def update_partial_booking(self, base_url, token, payload, id):
        data = json.dumps(payload)
        complete_token = 'token=' + token
        headers = {
            'Cookie': complete_token,
            'Content-Type': 'application/json'
        }

        response = requests.patch(url=f"{base_url}/booking/{id}", data=data, headers=headers)
        print(response)
        return self.__get_responses(response)

    def delete_booking(self,url,token,id):
        complete_token = 'token=' + token
        headers = {
            'Cookie': complete_token,
            'Content-Type': 'application/json'
        }
        response = requests.delete(url=f"{url}/booking/{id}",headers=headers)
        return self.__get_responses(response)


    def __get_responses(self,response):
        status_code = response.status_code
        text = response.text

        time = response.elapsed.total_seconds()

        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}

        headers = response.headers

        return APIResponse(status_code,text,as_dict,headers,time)