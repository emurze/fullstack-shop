import os

from dotenv import load_dotenv

load_dotenv()

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': os.getenv("REDIS_DSN"),
        'OPTIONS': {
            'db': 1,
        },
    }
}
