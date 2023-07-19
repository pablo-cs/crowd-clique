import requests

API_KEY = 'oZIHV1MD8gv1hwxxDlhKT3Pqud9pUs3R'
API_SECRET = 'u80uc9VG5Kk0SjFM'
BASE_URL = "https://app.ticketmaster.com/discovery/v2/events"

def get_event_details(event_id):
    url = f"{BASE_URL}/{event_id}"
    query_params = {
        "apikey": API_KEY
    }
    response = requests.get(url, params=query_params)

    if response.status_code == 200:
        event_data = response.json()
        event_obj = {}
        event_obj['name'] = event_data["name"]
        event_obj['date'] = event_data["dates"]["start"]["localDate"]
        event_obj['venue'] = event_data['_embedded']['venues'][0]['name']
        attractions = event_data["_embedded"]["attractions"]
        event_obj['attractions'] = [attractions[i]['name'] for i in range(len(attractions))]
        event_obj['image'] = event_data['images'][0]['url']
        return event_obj



def search_events(query):
    query_params = {
        "apikey": API_KEY,
        "keyword": query,
        "size": 10  # Number of results to retrieve
    }

    response = requests.get(BASE_URL, params=query_params)

    if response.status_code == 200:
        data = response.json()
        events_data = data["_embedded"]["events"]
        events  = []
        for event in events:
            event_id = event["id"]
            event += get_event_details(event_id)
        return events
        
    else:
        return "Error:" + response.status_code
