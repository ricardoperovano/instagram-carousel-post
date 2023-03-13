import requests

class Facebook():
    def __init__(self) -> None:
        self.__base_url = 'https://graph.facebook.com/v16.0'
        self.__instagram_page_id = '<your_instgram_page_id>'
        self.__access_token = '<your_user_access_token>'

    # uploads image to instagram
    def post_image(self, media_url):
        resp = requests.post(
            '{0}/{1}/media'.format(self.__base_url, self.__instagram_page_id),
            params={
                'access_token': self.__access_token,
                'image_url': media_url # this media should be stored online in a public server
            }
        )
    
        return resp.json()
    
    # creates a carousel container
    def create_carousel(self, ids=[], caption=''):
        resp = requests.post(
            '{0}/{1}/media'.format(self.__base_url, self.__instagram_page_id),
            params={
                'access_token': self.__access_token,
                'children': ','.join(ids), # ids is a list of media, media could be IMAGE OR VIDEO
                'media_type': 'CAROUSEL',
                'caption': caption
            }
        )

        return resp.json()
    
    def publish_media(self, container_id):
        resp = requests.post(
            '{0}/{1}/media_publish'.format(self.__base_url, self.__instagram_page_id),
            params={
                'access_token': self.__access_token,
                'creation_id': container_id # carousel id
            }
        )

        return resp.json()
    
