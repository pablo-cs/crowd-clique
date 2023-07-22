import requests

API_KEY = 'oZIHV1MD8gv1hwxxDlhKT3Pqud9pUs3R'
API_SECRET = 'u80uc9VG5Kk0SjFM'
BASE_URL = "https://app.ticketmaster.com/discovery/v2/events"
BASE_SUGGEST_URL = "https://app.ticketmaster.com/discovery/v2/suggest"
def get_event_details(event_id):
    url = f"{BASE_URL}/{event_id}"
    query_params = {
        "apikey": API_KEY
    }
    response = requests.get(url, params=query_params)


    if response.status_code == 200:
        try:
            event_data = response.json()

            event_obj = {}
            event_obj['id'] = event_id
            event_obj['name'] = event_data["name"]
            event_obj['date'] = event_data["dates"]["start"]["localDate"]
            event_obj['time'] = event_data["dates"]["start"]["localTime"]
            if event_data['_embedded']['venues'] is None:
                 event_obj['venue'] = event_data['place']['name']
            else:
                event_obj['venue'] = event_data['_embedded']['venues'][0]['name']
            event_obj['address'] = format_venue_details(event_data['_embedded']['venues'][0])
            print(event_obj)
            # attractions = event_data["_embedded"]["attractions"]
            # event_obj['attractions'] = [attractions[i]['name'] for i in range(len(attractions))]
            event_obj['image'] = event_data['images'][0]['url']
        except:
            event_obj = None
        finally:
            return event_obj
    return None


def search_events(query):
    query_params = {
        "apikey": API_KEY,
        "keyword": query,
        "size": 20  # Number of results to retrieve
    }

    response = requests.get(BASE_URL, params=query_params)
    events  = []
    if response.status_code == 200:
        data = response.json()
        try:
            events_data = data["_embedded"]["events"]
            for event in events_data:
                event_id = event["id"]
                event_details = get_event_details(event_id)
                if event_details:
                    events.append(event_details)
        except:
            return []
    return events

def suggest_events():
    query_params = {
        "apikey": API_KEY
    }

    response = requests.get(BASE_SUGGEST_URL, params=query_params)
    events  = []
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        events_data = data["_embedded"]["events"]
        for event in events_data:
            event_id = event["id"]
            event_details = get_event_details(event_id)
            if event_details:
                events.append(event_details)
    return events

def format_venue_details(venue):
    address = venue.get('address', {})
    city = venue.get('city', {}).get('name', '')
    state = venue.get('state', {}).get('name', '')
    country = venue.get('country', {}).get('name', '')
    
    lines = []
    if address.get('line1'):
        lines.append(address['line1'])
    if address.get('line2'):
        lines.append(address['line2'])
    if address.get('line3'):
        lines.append(address['line3'])
    
    formatted_address = ', '.join(lines)
    formatted_location = ', '.join(filter(None, [city, state, country]))
    
    return f"{formatted_address}<br>{formatted_location}"