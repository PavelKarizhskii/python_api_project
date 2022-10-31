from utilites.api import Petstore_swagger
from utilites.checking import Check





class Test_petstore():

    """Тестирование APi https://petstore.swagger.io/#/pet"""

    def test_create_pet_in_petstore(self):


        """Создание, измение и удаление записи о питомце"""

        print("\nMethod Post")
        result_post = Petstore_swagger.create_new_pet("Bobick")
        pet_id = result_post.json().get("id")
        print(f"pet_id = {pet_id}")
        Check.check_status_code(result_post, 200)
        Check.check_value_field_response(result_post, "name", "Bobick")

        print("\nMethod Get")
        result_get = Petstore_swagger.get_pet_information(pet_id)
        Check.check_status_code(result_get, 200)
        Check.check_value_field_response(result_get, "name", "Bobick")

        print("\nMethod Put")
        result_put = Petstore_swagger.update_pet_information(pet_id, new_name_pet="Great Bobster III")
        Check.check_status_code(result_put, 200)
        Check.check_value_field_response(result_put, "name", "Great Bobster III")

        print("\nMethod Get after Put")
        result_get = Petstore_swagger.get_pet_information(pet_id)
        Check.check_status_code(result_get, 200)
        Check.check_value_field_response(result_get, "name", "Great Bobster III")

        print("\nMethod Delete")
        result_delete = Petstore_swagger.delete_pet(pet_id)
        Check.check_status_code(result_delete, 200)
        Check.check_value_field_response(result_delete, "message", pet_id)

        print("\nMethod Get after Delete")
        result_get = Petstore_swagger.get_pet_information(pet_id)
        Check.check_status_code(result_get, 404)
        Check.check_value_field_response(result_get, "message", "Pet not found")



    def test_negative_pet_petstore(self):

        """"Проверка негативных сценариев в API по работе с записями о питомцах"""

        print("\nMethod Post")
        result_post = Petstore_swagger.negative_create_new_pet()
        Check.check_status_code(result_post, 500)
        Check.check_value_field_response(result_post, "message", "something bad happened")


        print("\nMethod Get")
        result_get = Petstore_swagger.get_pet_information(0)
        Check.check_status_code(result_get, 404)
        Check.check_value_field_response(result_get, "message", "Pet not found")

        print("\nMethod Put")
        result_put = Petstore_swagger.update_pet_information(pet_id=9999333434343434344343, new_name_pet="Great Bobster III")
        Check.check_status_code(result_put, 500)
        Check.check_value_field_response(result_put, "message", "something bad happened")

        print("\nMethod Delete")
        result_delete = Petstore_swagger.delete_pet(32)
        Check.check_status_code(result_delete, 404)


