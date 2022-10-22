from requests import Response

from utilites.api import Google_maps_api
from utilites.checking import Check


"""Создание, изменение и удаление новой локации"""


class Test_create_place():

    def test_create_new_place(self):

        print("\nMethod Post")
        result_post = Google_maps_api.create_new_place()
        Check.check_status_code(result_post, 200)
        place_id = result_post.json().get("place_id")

        print("\nMethod Get after Post")
        result_get = Google_maps_api.get_place(place_id)
        # Check.check_status_code(result_get, 200)

        print("\nMethod Put")
        result_put = Google_maps_api.update_place(place_id)
        Check.check_status_code(result_put, 200)

        print("\nMethod Get after Put")
        result_get = Google_maps_api.get_place(place_id)
        Check.check_status_code(result_get, 200)

        print("\nMethod Delete")
        result_delete = Google_maps_api.delete_place(place_id)
        Check.check_status_code(result_delete, 200)

        print("\nMethod Get after Delete")
        result_get = Google_maps_api.get_place(place_id)
        Check.check_status_code(result_get, 200)