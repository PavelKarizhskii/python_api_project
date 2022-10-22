import requests
from termcolor import colored


class Check():

    @staticmethod
    def check_status_code(result_request, correct_status_code):

        print(colored("Correct status code", 'yellow')) if result_request.status_code == correct_status_code else print(colored("incorrect status code", 'red'))
        assert result_request.status_code == correct_status_code

