import time
from datetime import UTC, datetime
import pytz

def extract_departures(feed, stop_ids):
    next_trips = {stop_id: [] for stop_id in stop_ids}
    for entity in feed.entity:
        if entity.HasField('trip_update'):
            trip_update = entity.trip_update
            if trip_update.HasField('trip') and trip_update.trip.HasField('route_id'):
                route_id = trip_update.trip.route_id
                for stop_time_update in trip_update.stop_time_update:
                    if stop_time_update.HasField('stop_id') and stop_time_update.stop_id in stop_ids:
                        stop_id = stop_time_update.stop_id
                        departure_time = stop_time_update.departure.time

                        if departure_time >=  time.time():
                            departure_time_dt = datetime.fromtimestamp(departure_time, UTC)
                            departure_time_brisbane = departure_time_dt.astimezone(pytz.timezone("Australia/Brisbane"))

                            next_trips[stop_id].append((departure_time_brisbane, route_id))

    return next_trips