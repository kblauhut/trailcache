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
