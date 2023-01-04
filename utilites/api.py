from utilites.http_metod import Http_metods

"""Методы для тестирования Google maps api"""


base_url_google = 'https://rahulshettyacademy.com'
key = 'key=qaclick123'   #key
base_url_petstore= 'https://petstore.swagger.io/v2'
user_name = 'Pavel_AutoQA'

class Google_maps_api():

    @staticmethod
    def create_new_place():

        """Выполнение Post запроса, создание новой локации"""

        json_create_location = {
            "location": {
                "lat": 53.155501,
                "lng": 48.474795
            }, "accuracy": 50,
            "name": "Lenin monument",
            "phone_number": "",
            "address": "Sovetskaya Ulitsa, 96, Syzran, Samara Oblast, Russia, 446026",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        resource_post = '/maps/api/place/add/json'  #resourse post method
        post_url = f"{base_url_google}{resource_post}?{key}"
        print(post_url)
        result_post = Http_metods.post(post_url, json_create_location)
        print(result_post.text)
        return result_post

    @staticmethod
    def get_place(place_id):

        """Выполнение  Get запроса,получение инфы о новой локации"""

        resource_get = '/maps/api/place/get/json'  # resourse get method
        get_url = f"{base_url_google}{resource_get}?{key}&place_id={place_id}"
        print(get_url)
        result_get = Http_metods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def update_place(place_id):

        """Выполнение Put запроса, изменение созданной локации"""

        json_update_location = {
            "place_id": f"{place_id}",
            "address": "Ploshchad Revolyutsii, Samara, Samara Oblast, Russia, 443099",
            "key": "qaclick123"
        }

        resource_put = '/maps/api/place/update/json'  #resourse put method
        put_url = f"{base_url_google}{resource_put}?{key}"
        print(put_url)
        result_put = Http_metods.put(put_url, json_update_location)
        print(result_put.text)
        return result_put


    @staticmethod
    def delete_place(place_id):

        """Выполнение Delete запроса, удаление созданной локации"""

        resource_delete = '/maps/api/place/delete/json'  # resourse post method
        delete_url = f"{base_url_google}{resource_delete}?{key}"
        json_delete_location = {
            "place_id": place_id
        }

        print(delete_url)
        result_delete = Http_metods.delete(delete_url, json_delete_location)
        print(result_delete.text)
        return result_delete


class Petstore_swagger():

    @staticmethod
    def create_new_pet(pet_name):

        """Выполнение Post запроса, создание нового питомца"""

        json = {
          "id": 0,
          "category": {
            "id": 0,
            "name": "Dogs"
          },
          "name": f"{pet_name}",
          "photoUrls": [
            "Null"
          ],
          "tags": [
            {
              "id": 0,
              "name": "Dogs"
            }
          ],
          "status": "available"
        }

        resource_post = '/pet'  #resourse post method
        post_url = f"{base_url_petstore}{resource_post}"
        print(json)
        print(post_url)
        result_post = Http_metods.post(post_url, json)
        print(result_post.text)
        return result_post

    @staticmethod
    def get_pet_information(pet_id):

        """Выполнение  Get запроса,получение инфы о новом питомце"""

        resource_get = '/pet/'  # resourse get method
        get_url = f"{base_url_petstore}{resource_get}{pet_id}"
        print(get_url)
        result_get = Http_metods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def update_pet_information(pet_id, new_name_pet):

        """Выполнение Put запроса, изменение информации о юзере"""

        json_put = {
          "id": pet_id,
          "name": new_name_pet
        }

        resource_put = '/pet'  #resourse put method
        put_url = f"{base_url_petstore}{resource_put}"
        print(put_url)
        result_put = Http_metods.put(put_url, json_put)
        print(result_put.text)
        return result_put

    @staticmethod
    def delete_pet(pet_id):

        """Выполнение  Delete запроса, удаление питомца из базы"""

        resource_delete = '/pet/'  # resourse get method
        delete_url = f"{base_url_petstore}{resource_delete}{pet_id}"
        print(delete_url)
        result_delete = Http_metods.delete(delete_url, body="")
        print(result_delete.text)
        return result_delete


    @staticmethod
    def negative_create_new_pet():

        """Выполнение Post запроса, создание нового питомца"""

        json = {
            "id": "98hjd923424343"
        }

        resource_post = '/pet'  #resourse post method
        post_url = f"{base_url_petstore}{resource_post}"
        print(post_url)
        result_post = Http_metods.post(post_url, json)
        print(result_post.text)
        return result_post