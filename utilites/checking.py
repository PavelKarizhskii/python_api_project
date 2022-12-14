import requests
from termcolor import colored
import json


class Check():



    @staticmethod
    def check_status_code(result_request, correct_status_code):
        """"Метод проверки статус кода"""
        print(f"Status code: {result_request.status_code}")
        print(colored("Correct status code", 'yellow')) if result_request.status_code == correct_status_code else print(colored("Incorrect status code", 'red'))
        assert result_request.status_code == correct_status_code


    @staticmethod
    def check_response_field(result_request, correct_value):
        """Метод проверки наличия обязательных полей"""
        response_json = json.loads(result_request.text)
        print(colored("Correct list response fields", 'yellow')) if list(response_json) == correct_value else print(colored("Incorrect list response fields", 'red'))
        assert list(response_json) == correct_value
        # print(list(response_json))



    @staticmethod
    def check_value_field_response(result_request, field_name, correct_value):
        """Метод проверки содержания указанного поля"""
        value_field = result_request.json().get(field_name)
        print(colored(f"Correct value field {field_name}", 'yellow')) if str(value_field) == str(correct_value) else print(colored(f"Incorrect value field {field_name}", 'red'))
        assert str(value_field) == str(correct_value)