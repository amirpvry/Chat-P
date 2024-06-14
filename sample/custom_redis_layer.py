from channels_redis.core import RedisChannelLayer
import redis
import json

class CustomRedisChannelLayer(RedisChannelLayer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

    async def send(self, channel, message):
        # Ensure the message is a dict before passing it to the parent class's send method
        if isinstance(message, str):
            message = json.loads(message)
        await super().send(channel, message)

    async def receive(self, channel):
        while True:
            message = self.redis_client.blpop(channel)
            if message:
                _, data = message
                return json.loads(data)
