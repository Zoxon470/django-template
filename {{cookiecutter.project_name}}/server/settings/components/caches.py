# Caching
# https://docs.djangoproject.com/en/4.2/topics/cache/
# https://github.com/jazzband/django-redis

import environ

env = environ.Env()

REDIS_URL = env.cache_url("REDIS_URL", default="redis://redis:6379/1")
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL["LOCATION"],
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}
