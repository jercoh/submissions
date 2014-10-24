import requests
from requests_oauthlib import OAuth1
import twitter_credentials as credentials
import urllib


oauth = OAuth1(credentials.consumer_key,
               client_secret = credentials.consumer_secret,
               resource_owner_key = credentials.access_token,
               resource_owner_secret = credentials.access_secret)

base_url = "https://api.twitter.com/1.1"

def get(endpoint, params):
    url = base_url+endpoint+params
    response = requests.get(url, auth = oauth)
    response = response.json()
    return response

def search(query):
    query = urllib.urlencode({'q': query})
    url = base_url+"/search/tweets.json?"+query+"&src=typd"
    print url
    response = requests.get(url, auth = oauth)
    response = response.json()
    return response

def search_all(query):
    results = []
    current_page = search(query)
    results.extend(current_page['statuses'])
    for i in range(200):
        try:
            next_results = current_page['search_metadata']['next_results']
            current_page = get('/search/tweets.json', next_results)
            results.extend(current_page['statuses'])
        except:
            return results
