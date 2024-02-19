import pytest
from selenium import webdriver
import time
from utilities.read_properties import ReadConfig

from pytest_metadata.plugin import metadata_key

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options

from utilities.custom_logger import LogGen

# global driver and browser
orange_hrm_session = None

@pytest.fixture(scope="function")
def setitup(request):
    '''
        It is a fixture which initializes the driver and opens/closes orange_hrm for every test case.
        :return: driver
    '''

    global orange_hrm_session

    browser = request.config.getoption("--browser")

    # environment = request.config.getoption("--env")

    # user has given browser name in CLI
    if browser:
        if browser.lower() == "chrome":
            opt = Options()
            opt.add_argument("--headless")
            #try:
            chrome_driver_binary_path = ChromeDriverManager().install()
            print(f"\n @@@ chrome_driver_binary_path : {chrome_driver_binary_path}")
            # logger.info(f"\n @@@ chrome_driver_binary_path : {chrome_driver_binary_path}")

            orange_hrm_session = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            #except Exception as e:
            #    print(f"Exception : {e}")

        if browser.lower() == "edge":
            opt = Options()
            # opt.add_argument("--headless")
            # opt.add_argument("--no-sandbox")
            # opt.add_argument("--disable-dev-shm-usage")

            # while mastermind_session == None:
            #try:

            # edge_driver_binary_path = EdgeChromiumDriverManager().install()
            # print(f"\n @@@ edge_driver_binary_path : {edge_driver_binary_path}")
            # logger.info(f"\n @@@ edge_driver_binary_path : {edge_driver_binary_path}")
            # driver_location = "C:\webdrivers\edgedriver\msedgedriver.exe"
            # mastermind_session = webdriver.Edge(service=EdgeService(driver_location),options=opt)

            # selenium 4
            mastermind_session = webdriver.Edge()
            print(f"Edge Driver path : {mastermind_session.service.path}")

            # mastermind_session = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
            #except Exception as e:
            #    print(f"Exception : {e}")

    # no i/p from user for browser name in CLI
    # default browser : chrome
    else:
        opt = Options()
        opt.add_argument("--headless")
        # while mastermind_session == None:
        #try:
        chrome_driver_binary_path = ChromeDriverManager().install()
        print(f"\n @@@ chrome_driver_binary_path : {chrome_driver_binary_path}")
        # logger.info(f"\n @@@ chrome_driver_binary_path : {chrome_driver_binary_path}")
        orange_hrm_session = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        #except Exception as e:
        #    print(f"Exception : {e}")

    request.cls.driver = orange_hrm_session

    # if environment=="ci":
    #     request.cls.environment = "ci"
    # elif environment=="t20":
    #     request.cls.environment = "t20"
    # else:
    #     # t20 by default
    #     request.cls.environment = "t20"


    yield
    # closes orange_hrm
    orange_hrm_session.quit()

########### Pytest HTML Report ################

# 1. Embedding failed TC screenshots to the html report and logs
# test source : tests/orange_hrm

@pytest.mark.hookwrapper
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call" or report.when=='setitup':
        # always add url to report
        # extra.append(pytest_html.extras.url("http://www.example.com/"))

        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            file_name = report.nodeid.replace("::","_") + ".png"
            print(f"\n\n *** File Name : {file_name} \n\n ")
            print(f"\n\n *** Location Before ss : {file_name} \n")
            # call to function
            location = capture_screenshot(file_name)

            print(f"\n\n *** Location After screenshot captured at  : {location} \n")

            # changing location so as its accessible as path of src for reports
            location = location.replace('./reports_screenshots/orange_hrm','../')
            print(f"Final location : {location}")

            if file_name:
                html = '<div><img src="%s" alt="reports" style="width:304px;height:228px;" ' \
                               'onclick="window.open(this.src)" align="right"/></div>' % location
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def capture_screenshot(name):
    '''
        Function to capture screenshot at specified location
    :param name: filename
    :return: screenshot location
    '''
    time.sleep(2)
    global orange_hrm_session

    base_dir = "./reports_screenshots/orange_hrm/screenshots/"
    loc = base_dir + name[17:]
    orange_hrm_session.save_screenshot(loc)
    return loc




# extra information on reports
# 2. Report Title hook
def pytest_html_report_title(report):
    report.title = "Orange HRM - Automation Report"

# 2. It is hook for adding environment info to HTML Report
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "Orange HRM"

    # config._metadata['Project Name'] = 'Infor RPA'
    config.stash[metadata_key]['Module Name'] = 'HR Module'
    #
    # environment = config.getoption("--env")

    # config.stash[metadata_key]['Environment'] = environment
    # config.stash[metadata_key]['Tenant Name'] = ''
    config.stash[metadata_key]['QA Name'] = 'Saish Wadkar'

    browser = config.getoption("--browser")
    browser_version = None

    if browser=="chrome":
        browser="chrome"
        browser_version = ReadConfig.get_chrome_browser_version()
    elif browser=="edge":
        browser="edge"
        browser_version = ReadConfig.get_edge_browser_version()
    else:
        browser = "chrome"
        browser_version = ReadConfig.get_chrome_browser_version()

    config.stash[metadata_key]['Browser'] = browser
    config.stash[metadata_key]['Browser Version'] = browser_version
    config.stash[metadata_key]['Language'] = "English"


# 3. It is hook for delete/modify environment info on html report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("",None)


# multi browser support
# adding addoption for --browser , so that user can give broser name in CLI/terminal
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--env")