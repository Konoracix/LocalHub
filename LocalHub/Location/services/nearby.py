import math

class NearbyService():

    def filter_nearby_events(self, queryset, lat, lon, distance_km):

        distance_in_degrees_lat = distance_km/111
        distance_in_degrees_lon = distance_km / (111 * math.cos(math.radians(lat)))

        max_lat = lat + distance_in_degrees_lat
        min_lat = lat - distance_in_degrees_lat
        max_lon = lon + distance_in_degrees_lon
        min_lon = lon - distance_in_degrees_lon

        return queryset.filter(latitude__gte=min_lat, latitude__lte=max_lat,
                                longitude__gte=min_lon, longitude__lte=max_lon)

    def get_distance(self, lat1, lon1, lat2, lon2):
        dlat = math.radians(lat1) - math.radians(lat2)
        dlon = math.radians(lon1) - math.radians(lon2)
        a = (math.sin(dlat/2) ** 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * (math.sin(dlon/2) ** 2)
        c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
        return round(c * 6371, 3)

    def sort_events_by_distance(self, queryset, lat, lon, limit = None):
        sorted_events = []
        for event in queryset:
            sorted_events.append((self.get_distance(event.latitude, event.longitude, lat, lon), event))

        sorted_events.sort(key= lambda x : x[0])

        if limit:
            return [event for distance, event in sorted_events[:limit]]
            
        return [event for distance, event in sorted_events]
