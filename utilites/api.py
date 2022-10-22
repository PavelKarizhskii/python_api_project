from utilites.http_metod import Http_metods

"""Методы для тестирования Google maps api"""


base_url = 'https://rahulshettyacademy.com'
key = 'key=qaclick123'   #key

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
        post_url = f"{base_url}{resource_post}?{key}"
        print(post_url)
        result_post = Http_metods.post(post_url, json_create_location)
        print(result_post.text)
        return result_post

    @staticmethod
    def get_place(place_id):

        """Выполнение  Get запроса,получение инфы о новой локации"""

        resource_get = '/maps/api/place/get/json'  # resourse get method
        get_url = f"{base_url}{resource_get}?{key}&place_id={place_id}"
        print(get_url)
        result_get = Http_metods.get(get_url)
        print(result_get.text)
        return resource_get

    @staticmethod
    def update_place(place_id):

        """Выполнение Put запроса, изменение созданной локации"""

        json_update_location = {
            "place_id": f"{place_id}",
            "address": "Ploshchad Revolyutsii, Samara, Samara Oblast, Russia, 443099",
            "key": "qaclick123"
        }

        resource_put = '/maps/api/place/update/json'  #resourse put method
        put_url = f"{base_url}{resource_put}?{key}"
        print(put_url)
        result_put = Http_metods.put(put_url, json_update_location)
        print(result_put.text)
        return result_put


    @staticmethod
    def delete_place(place_id):

        """Выполнение Delete запроса, удаление созданной локации"""

        resource_delete = '/maps/api/place/delete/json'  # resourse post method
        delete_url = f"{base_url}{resource_delete}?{key}"
        json_delete_location = {
            "place_id": place_id
        }

        print(delete_url)
        result_delete = Http_metods.delete(delete_url, json_delete_location)
        print(result_delete.text)
        return result_delete
