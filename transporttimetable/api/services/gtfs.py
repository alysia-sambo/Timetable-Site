import requests
from django.conf import settings
from google.transit import gtfs_realtime_pb2

def get_real_time_feed():
    url = settings.REALTIME_URL
    try:
        feed = gtfs_realtime_pb2.FeedMessage()
        response = requests.get(url)
        response.raise_for_status()
        feed.ParseFromString(response.content)
    except Exception as e:
        print(f"Could not connect to real time feed: {e}")
        raise 
    return feed