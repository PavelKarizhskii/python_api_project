from utilites.api import Google_maps_api
from utilites.checking import Check


"""Создание, изменение и удаление новой локации"""


class Test_create_place_class():

    def test_create_new_place(self):

        print("\nMethod Post")
        result_post = Google_maps_api.create_new_place()
        Check.check_status_code(result_post, 200)
        place_id = result_post.json().get("place_id")
        Check.check_response_field(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Check.check_value_field_response(result_post, "status", "OK")


        print("\nMethod Get after Post")
        result_get = Google_maps_api.get_place(place_id)
        Check.check_status_code(result_get, 200)
        Check.check_response_field(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Check.check_value_field_response(result_get, "name", "Lenin monument")

        print("\nMethod Put")
        result_put = Google_maps_api.update_place(place_id)
        Check.check_status_code(result_put, 200)
        Check.check_response_field(result_put, ['msg'])
        Check.check_value_field_response(result_put, "msg", "Address successfully updated")

        print("\nMethod Get after Put")
        result_get = Google_maps_api.get_place(place_id)
        Check.check_status_code(result_get, 200)
        Check.check_response_field(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Check.check_value_field_response(result_get, "address", "Ploshchad Revolyutsii, Samara, Samara Oblast, Russia, 443099")

        print("\nMethod Delete")
        result_delete = Google_maps_api.delete_place(place_id)
        Check.check_status_code(result_delete, 200)
        Check.check_response_field(result_delete, ['status'])
        Check.check_value_field_response(result_delete, "status", "OK")


        print("\nMethod Get after Delete")
        result_get = Google_maps_api.get_place(place_id)
        Check.check_status_code(result_get, 404)
        Check.check_response_field(result_get, ['msg'])
        Check.check_value_field_response(result_get, "msg", "Get operation failed, looks like place_id  doesn't exists")



    def test_negative_requests_google_place(self):

        incorrect_place_id = 555

        print("\nMethod Get")
        result_get = Google_maps_api.get_place(incorrect_place_id)
        Check.check_status_code(result_get, 404)
        Check.check_response_field(result_get, ['msg'])
        Check.check_value_field_response(result_get, "msg", "Get operation failed, looks like place_id  doesn't exists")

        print("\nMethod Put")
        result_put = Google_maps_api.update_place(incorrect_place_id)
        Check.check_status_code(result_put, 404)
        Check.check_response_field(result_put, ['msg'])
        Check.check_value_field_response(result_put, "msg", "Update address operation failed, looks like the data doesn't exists")


        print("\nMethod Delete")
        result_delete = Google_maps_api.delete_place(incorrect_place_id)
        Check.check_status_code(result_delete, 404)
        Check.check_response_field(result_delete, ['msg'])
        Check.check_value_field_response(result_delete, "msg", "Delete operation failed, looks like the data doesn't exists")

