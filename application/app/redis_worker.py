import redis

class RedisWorker:
    def __init__(self):
        pool = redis.ConnectionPool(
            host='localhost',
            port=6379,
            db=0
        )
        self.redis = redis.Redis(
            connection_pool=pool
        )

    def set_key_value(self, key, value):
        self.redis.set(key, value)

    def get_by_key(self, key):
        return self.redis.get(key)

    def write_temp_record(self, temperature, time_moment):
        self.redis.get()

    def disconnect(self):
        self.redis.close()