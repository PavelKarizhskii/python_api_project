import requests
from termcolor import colored
import json


class Check():


    """"Метод проверки статус кода"""
    @staticmethod
    def check_status_code(result_request, correct_status_code):

        print(f"Status code: {result_request.status_code}")
        print(colored("Correct status code", 'yellow')) if result_request.status_code == correct_status_code else print(colored("Incorrect status code", 'red'))
        assert result_request.status_code == correct_status_code

    """Метод проверки наличия обязаетльных полей"""
    @staticmethod
    def check_response_field(result_request, correct_value):

        response_json = json.loads(result_request.text)
        print(colored("Correct list response fields", 'yellow')) if list(response_json) == correct_value else print(colored("Incorrect list response fields", 'red'))
        assert list(response_json) == correct_value
        # print(list(response_json))

