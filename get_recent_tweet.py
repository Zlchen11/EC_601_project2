Python 3.10.7 (v3.10.7:6cc6b13308, Sep  5 2022, 14:02:52) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... import requests
... import os
... import json
... import pandas as pd
... 
... 
... bearer_token = 'Enter your own token'
... 
... search_url = "https://api.twitter.com/2/tweets/search/recent"
... 
... 
... query_params = {'query': '(from:'twitters name' )'  ,'tweet.fields': 'author_id', 'max_results': '100'}
... 
... 
... 
... 
... def bearer_oauth(r):
...     """
...     Method required by bearer token authentication.
...     """
... 
...     r.headers["Authorization"] = f"Bearer {bearer_token}"
...     r.headers["User-Agent"] = "v2RecentSearchPython"
...     return r
... 
... def connect_to_endpoint(url, params):
...     response = requests.get(url, auth=bearer_oauth, params=params)
...     print(response.status_code)
...     if response.status_code != 200:
...         raise Exception(response.status_code, response.text)
...     return response.json()
... 
... 
... def main():
...     json_response = connect_to_endpoint(search_url, query_params)
    #print(json_response['text'])
    #print(json_response)
    #print(json_response['data'])
    data = json_response['data']
    print(len(data),type(data))
    str = []
    for i in range(len(data)) :
        #print(data[i]['text'])
        str.append(data[i]['text'])
    return str



    #print(json.dumps(json_response, indent=4, sort_keys=True))
    #print(json_response('text'))


if __name__ == "__main__":
    main()

