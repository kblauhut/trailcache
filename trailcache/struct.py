class Cache:
    def __init__(self, gc_code, latitude, longitude, cache_type, container_id, difficulty, terrain):
        self.gc_code = gc_code
        self.latitude = latitude
        self.longitude = longitude
        self.cache_type = cache_type
        self.container_id = container_id
        self.difficulty = difficulty
        self.terrain = terrain

    def get_gc_code(self):
        return self.gc_code

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude

    def get_cache_type(self):
        return self.cache_type

    def get_container_id(self):
        return self.container_id

    def get_difficultye(self):
        return self.difficulty

    def get_terrain(self):
        return self.terrain


class Filters:
    def __init__(self, distance, cache_types, container_ids, difficulty_range, terrain_range):
        self.distance = distance
        self.cache_types = cache_types
        self.container_ids = container_ids
        self.difficulty_range = difficulty_range
        self.terrain_range = terrain_range

    def get_distance(self):
        return self.distance

    def get_cache_types(self):
        return self.cache_types

    def get_container_ids(self):
        return self.container_ids

    def get_difficulty_range(self):
        return self.difficulty_range

    def get_terrain_range(self):
        return self.terrain_range


class Settings:
    def __init__(self, token, request_limit, filters):
        self.token = token
        self.request_limit = request_limit
        self.filters = filters

    def get_token(self):
        return self.token

    def get_request_limit(self):
        return self.request_limit

    def get_filters(self):
        return self.filters
