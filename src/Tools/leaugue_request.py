import time
import requests
import json

class LeagueRequest:

    def __init__(self, region):
        self.url = f"https://{region}.api.riotgames.com"
        self.session = requests.Session()

    def _check_response_header(self, key):
        """should check the rate limits"""
        print(f'X-Rate-Limit-Type: {key.x_rate_limit_type}')
        print(f'Next retry in : {key.retry_after}')
        time.sleep(int(key.retry_after))

    def _request_handling(self, url, key):
        """Just the request"""
        try:
            response = self.session.get(self.url + url, headers=json.loads(key.header))
        except Exception as e:
            print("request exception: " + str(e))
            return None
        self._update_api_key_headers(key, response)
        return response

    def _update_api_key_headers(self, key, response):
        header = response.headers
        if 'X-Rate-Limit-Type' and 'Retry-After' in header.keys():
            key.retry_after = header['Retry-After']
            key.x_rate_limit_type = header['X-Rate-Limit-Type']

    def send_request(self, url, key):
        """sends the request to RiotsGames"""
        response = self._request_handling(url, key)
        if response is not None:  # with only response: it didnt work by response code like 404 or 403 or 429
            if response.status_code == 403:
                print('Update you API-Key !, message: ' + str(response.json()))
                exit()
                return None
            while response.status_code == 429:
                self._check_response_header(key)
                response = self._request_handling(url, key)
            if response.status_code == 404:
                print(f'Status Code 404: {response.json()}')
                return None
            elif response:
                if response.status_code == 200:
                    response = response.json()
                    response['api_key_id'] = key.id
                    return response
        return None

