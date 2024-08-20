import pytest
import requests
import json
import base64
from pytest_metadata.plugin import metadata_key
from utilities.read_properties import ReadConfig

# def base64_encoding(original_value):
#     '''
#         Base 64 encoding of a string
#     :param original_value: it is the string to be encoded
#     :return: encoded string
#     '''
#
#     string_bytes = original_value.encode("ascii")
#     base64_bytes = base64.b64encode(string_bytes)
#     base64_string = base64_bytes.decode("ascii")
#
#     return base64_string


# @pytest.fixture(scope='class')
# def access_token(request):
#     '''
#         It is a fixture which gets the access token for each test case.
#         :return: token
#     '''
#     token = ""
#     file = None
#     environment = None
#     environment = request.config.getoption("--env")
#
#     try:
#         if environment=="dev":
#             file = open("configurations/dev.json")
#         elif environment == "trial":
#             file = open("configurations/trial.json")
#         else:
#             file = open("configurations/dev.json")
#
#         data = json.load(file)
#
#         # for i, j in data.items():
#         #     print(f"Key : {i} --- Value : {j}")
#
#         url = ""
#         payload = f"grant_type=password&username={data['username']}&password={data['password']}"
#         encoded_username_password = base64_encoding(data['ci']+":"+data['cs'])
#         headers = {
#             'Content-Type': 'application/x-www-form-urlencoded',
#             'Authorization': 'Basic '+encoded_username_password
#         }
#         response = requests.request("POST", url, headers=headers, data=payload)
#         #print()
#         #print(response.json())
#
#         token = response.json()['access_token']
#
#     except Exception as e:
#         print(f" ----- Exception : {e}")
#
#     finally:
#         request.cls.token = "Bearer " + token
#         request.cls.only_token = token
#         request.cls.environment = environment
#         file.close()

    # yield
    # post test actions

@pytest.fixture(scope="class")
def access_token(request):
    base_url = ReadConfig().get_restful_booker_base_url()

    # url = base_url + "/auth"
    # print(f"URL : {url}")

    credentials = {"username" : "admin","password" : "password123"}

    response = requests.post(url=base_url+'/auth',json=credentials)

    # print(f"\n Response : {response}")
    # print(type(response))   # <class 'requests.models.Response'>
    # print(f"Status Code : {response.status_code}")
    # print(f"Text : {response.text}")
    # print(f"JSON : {response.json()}")
    # print(f"Token only : {response.json()['token']}")

    request.cls.token = response.json()['token']

# extra information on reports
# 1. Report Title hook
def pytest_html_report_title(report):
    report.title = "Restful Booker - Automation Report"

# 2. It is hook for adding environment info to HTML Report
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Restful Booker'
    config.stash[metadata_key]['Module Name'] = 'Bookings'

    environment = config.getoption("--env")
    if environment:
        if environment == "t20":
            config.stash[metadata_key]['Environment'] = 't20'
            config.stash[metadata_key]['Tenant Name'] = 'DEV_PP4'
        elif environment == "ci":
            config.stash[metadata_key]['Environment'] = 'ci'
            config.stash[metadata_key]['Tenant Name'] = 'DEV_PP2'
    else:
        config.stash[metadata_key]['Environment'] = 't20'
        config.stash[metadata_key]['Tenant Name'] = 'DEV_PP4'

    config.stash[metadata_key]['QA Name'] = 'Saish Wadkar'

# adding addoption for --env , so that user can give environment name in CLI/terminal
def pytest_addoption(parser):
    parser.addoption("--env")


# 3. It is hook for delete/modify environment info on html report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("",None)
