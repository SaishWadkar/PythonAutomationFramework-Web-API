import json
import pytest
import softest
import random
from assertpy import assert_that
from cerberus import Validator
from pprint import pprint
from utilities.csv_utils import CSVUtils
from utilities.excel_utils import ExcelUtils
from utilities.read_properties import ReadConfig
from tests.restful_booker.restful_booker_api_client import RestfulBookerClient
from utilities.custom_logger import LogGen
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from faker import Faker


@pytest.mark.usefixtures('access_token')
class TestRestfulBookerAPI(softest.TestCase):

    # target_file_path = "./test_data/restful_booker/process_names.csv"
    # source_file_path = "./test_data/restful_booker/publishing_details.csv"
    # csv_utils = CSVUtils(source_file_path,target_file_path)

    logger = LogGen.restful_booker_api_logs()
    fake_data = Faker()

    # def instanciate(self):
    #     '''
    #         This method checks for the environment being used (ci/t20) and reads test data accordingly from the test
    #         data excel.
    #         return : RestfulBookerClient object
    #     '''
    #     #print(f" Environment : {self.environment}")
    #     if self.environment == "ci":
    #         self.excel = ExcelUtils(file="./test_data/restful_booker/RestfulBooker_jobs_testdata.xlsx", sheet="ci")
    #         return RestfulBookerClient(base_url=ReadConfig.get_RestfulBooker_api_base_url_ci_pp2())
    #     else:
    #         self.excel = ExcelUtils(file="./test_data/restful_booker/RestfulBooker_jobs_testdata.xlsx", sheet="t20")
    #         return RestfulBookerClient(base_url=ReadConfig.get_RestfulBooker_api_base_url_t20_pp4())

    # POST
    # test 1
    @pytest.mark.skip
    def test_get_access_token(self):
        print(f"\n Token : {self.token}")

    # test 2
    @pytest.mark.regression
    def test_get_booking_ids(self):
        self.logger.info(f" --- Test Case 1 ---")
        self.logger.info(f" --- GET - all booking ids ---")
        # RestfulBooker_client = self.instanciate()
        #print(f"Base Url : {RestfulBooker_client.base_url}")

        restful_booker_client = RestfulBookerClient(ReadConfig().get_restful_booker_base_url())

        response = restful_booker_client.get_booking_ids(self.token) # pass token
        # print(f"\n Response : {response} ") # APIResponse Object
        # print(f"Response as_dict : {response.as_dict} ")
        # print(f"Response as_dict - type : {type(response.as_dict)} ") # python object

        # Assertions
        # 1 .status code
        assert_that(response.status_code).is_equal_to(200)
        self.logger.info(f"Status code : {response.status_code}  ")

        # 2. Count not null and check no of booking ids
        assert_that(len(response.as_dict)).is_greater_than(0)
        self.logger.info(f"Count of booking ids : {len(response.as_dict)}  ")

        # JSON schema validation

        schema = {
    "$schema": "https://json-schema.org/draft/2019-09/schema",
    "$id": "http://example.com/example.json",
    "type": "array",
    "default": [],
    "title": "Root Schema",
    "items": {
        "type": "object",
        "default": {},
        "title": "A Schema",
        "required": [
            "bookingid"
        ],
        "properties": {
            "bookingid": {
                "type": "integer", # integer
                "default": 0,
                "title": "The bookingid Schema",
                "examples": [
                    1234
                ]
            }
        },
        "examples": [{
            "bookingid": 1234
        }]
    },
    "examples": [
        [{
            "bookingid": 1234
        }]
    ]
}

        try:
            validate(instance=response.as_dict ,schema=schema)
            self.logger.info("JSON Schema validated !")
        # except ValidationError as ve:
        #     print(ve)

        except Exception as e:
            print("\n !!!! EXCEPTION !!!!")
            print(e)
            self.logger.info("JSON Schema not matching !")
            assert False


    # test 3
    @pytest.mark.regression
    def test_get_booking(self):
        self.logger.info(f" --- Test Case 2 ---")
        self.logger.info(f" --- GET - booking by id ---")

        restful_booker_client = RestfulBookerClient(ReadConfig().get_restful_booker_base_url())

        resp_1 = restful_booker_client.get_booking_ids(token=self.token)
        id = resp_1.as_dict[0]['bookingid']
        # print(f"booking id : {id} ")

        response = restful_booker_client.get_booking_id(token=self.token,id=id)
        print(f"\n Response : \n {response.as_dict}")

        # Assertions
        # 1. status code
        self.soft_assert(self.assertEqual,response.status_code,200)
        self.logger.info(f"Status code : {response.status_code}  ")

        # # 2. totalprice should be greater than 0
        assert_that(response.as_dict['totalprice']).is_greater_than(0)
        self.logger.info(f"Total Price : {response.as_dict['totalprice']}")

        self.assert_all()

        schema = {
    "$schema": "https://json-schema.org/draft/2019-09/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "default": {},
    "title": "Root Schema",
    "required": [
        "firstname",
        "lastname",
        "totalprice",
        "depositpaid",
        "bookingdates",
        "additionalneeds"
    ],
    "properties": {
        "firstname": {
            "type": "string",
            "default": "",
            "title": "The firstname Schema",
            "examples": [
                "John"
            ]
        },
        "lastname": {
            "type": "string",
            "default": "",
            "title": "The lastname Schema",
            "examples": [
                "Smith"
            ]
        },
        "totalprice": {
            "type": "integer",
            "default": 0,
            "title": "The totalprice Schema",
            "examples": [
                111
            ]
        },
        "depositpaid": {
            "type": "boolean",
            "default": False,
            "title": "The depositpaid Schema",
            "examples": [
                True
            ]
        },
        "bookingdates": {
            "type": "object",
            "default": {},
            "title": "The bookingdates Schema",
            "required": [
                "checkin",
                "checkout"
            ],
            "properties": {
                "checkin": {
                    "type": "string",
                    "default": "",
                    "title": "The checkin Schema",
                    "examples": [
                        "2018-01-01"
                    ]
                },
                "checkout": {
                    "type": "string",
                    "default": "",
                    "title": "The checkout Schema",
                    "examples": [
                        "2019-01-01"
                    ]
                }
            },
            "examples": [{
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            }]
        },
        "additionalneeds": {
            "type": "string",
            "default": "",
            "title": "The additionalneeds Schema",
            "examples": [
                "Breakfast"
            ]
        }
    },
    "examples": [{
        "firstname": "John",
        "lastname": "Smith",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }]
}

        try:
            validate(instance=response.as_dict , schema=schema)
            self.logger.info("JSON Schema validated !")
        except Exception as e:
            print(e)
            self.logger.info("JSON Schema not matching !")
            assert False


    # test 4
    @pytest.mark.regression
    def test_create_booking(self):
        self.logger.info(f" --- Test Case 3 ---")
        self.logger.info(f" --- POST  ---")

        restful_booker_client = RestfulBookerClient(base_url=ReadConfig().get_restful_booker_base_url())

        name = self.fake_data.name()

        payload = {
            "firstname": name,
            "lastname": "Sharma",
            "totalprice": 251,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }

        response = restful_booker_client.create_booking(token=self.token,payload = payload)

        # print(response.as_dict)

        # Assertions
        # 1 status code
        assert_that(response.status_code).is_equal_to(200)
        self.logger.info(f"Status Code : {response.status_code}")

        # 2 booking id greater than 0
        assert_that(response.as_dict['bookingid']).is_greater_than(0)
        self.logger.info(f"Booking ID : {response.as_dict['bookingid']}")

        # schema validation

    @pytest.mark.regression
    def test_update_booking(self):
        self.logger.info(f" --- Test Case 4 ---")
        self.logger.info(f" --- PUT  ---")

        restful_booker_client = RestfulBookerClient(base_url=ReadConfig().get_restful_booker_base_url())

        resp_1 = restful_booker_client.get_booking_ids(token=self.token)
        id = resp_1.as_dict[0]['bookingid']
        # print(f"booking id : {id} ")

        # update all data
        name = self.fake_data.name()

        payload = {
            "firstname": name,
            "lastname": "Sharma",
            "totalprice": 456,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }

        response = restful_booker_client.update_booking(token=self.token, payload=payload, id=id)

        # print(response.as_dict)

        # Assertions
        # 1 status code
        assert_that(response.status_code).is_equal_to(200)
        self.logger.info(f"Status Code : {response.status_code}")

        # 2 booking id greater than 0
        assert_that(response.as_dict['lastname']).is_equal_to("Sharma")
        self.logger.info(f"Lastname : {response.as_dict['lastname']}")

        # schema validation

    @pytest.mark.regression
    def test_partial_update_booking(self):
        self.logger.info(f" --- Test Case 5 ---")
        self.logger.info(f" --- PATCH  ---")

        restful_booker_client = RestfulBookerClient(base_url=ReadConfig().get_restful_booker_base_url())

        resp_1 = restful_booker_client.get_booking_ids(token=self.token)
        id = resp_1.as_dict[0]['bookingid']
        # print(f"booking id : {id} ")

        # update all data
        name = self.fake_data.name()

        payload = {
            "firstname": name,
            "lastname": "Sharma",
            "totalprice": 456,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }

        response = restful_booker_client.update_partial_booking(token=self.token, payload=payload, id=id)

        # print(response.as_dict)

        # Assertions
        # 1 status code
        assert_that(response.status_code).is_equal_to(200)
        self.logger.info(f"Status Code : {response.status_code}")

        # 2 booking id greater than 0
        assert_that(response.as_dict['lastname']).is_equal_to("Sharma")
        self.logger.info(f"Lastname : {response.as_dict['lastname']}")

        # schema validation

    @pytest.mark.tryit
    def test_delete_booking(self):
        self.logger.info(f" --- Test Case 6 ---")
        self.logger.info(f" --- DELETE  ---")

        restful_booker_client = RestfulBookerClient(base_url=ReadConfig().get_restful_booker_base_url())

        resp_1 = restful_booker_client.get_booking_ids(token=self.token)
        id = resp_1.as_dict[0]['bookingid']
        # print(f"booking id : {id} ")

        response = restful_booker_client.delete_booking(token=self.token, id=id)

        print(f"Response Text : {response.text} ")

        # Assertions
        # 1 status code
        assert_that(response.status_code).is_equal_to(201)
        self.logger.info(f"Status Code : {response.status_code}")


        # 2 response text = Created
        assert_that(response.text).is_equal_to("Created")
        self.logger.info(f"Response Text : {response.text}")

        # No schema validation here as nod JSON is returned
