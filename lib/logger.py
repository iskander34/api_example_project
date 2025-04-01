import datetime
import json
import os

from requests import Response


class Logger:
    file_name = f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"
    time_run_test = ""

    @classmethod
    def _write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url: str, data: str, headers: dict, cookies: dict, method: str):
        testname = os.environ.get('PYTEST_CURRENT_TEST')

        Logger.time_run_test = datetime.datetime.now()

        if data is not None:
            request_data = json.loads(data)
            data = json.dumps(request_data, indent=4)

        data_to_add = f"\n-------\n"
        data_to_add += f"Test: {testname}\n"
        data_to_add += f"\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += f"Request data: {data}\n"
        data_to_add += f"Request headers: {headers}\n"
        data_to_add += f"Request cookies: {cookies}\n"
        data_to_add += f"\n"

        cls._write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, response: Response):
        cookies_as_dict = dict(response.cookies)
        headers_as_dict = dict(response.headers)
        response_data = json.loads(response.text)
        response_data_json = json.dumps(response_data, indent=4)

        data_to_add = f"Response code: {response.status_code}\n"
        data_to_add += f"Response text: {response_data_json}\n"
        data_to_add += f"Response headers: {headers_as_dict}\n"
        data_to_add += f"Response cookies: {cookies_as_dict}\n"
        data_to_add += f"\nTime:\n"
        data_to_add += f"Test START: {str(Logger.time_run_test)}\n"
        time_stop_test = datetime.datetime.now()
        data_to_add += f"Test STOP:  {str(time_stop_test)}\n"
        data_to_add += f"Test RUN:   {str(time_stop_test - Logger.time_run_test)}"
        data_to_add += f"\n-------\n"
        data_to_add += f"\n"

        cls._write_log_to_file(data_to_add)
