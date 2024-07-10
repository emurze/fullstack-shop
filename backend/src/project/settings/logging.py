import os

from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVEL")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "stream": {
            "level": LOG_LEVEL,
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "level": LOG_LEVEL,
            "handlers": [
                "stream",
            ],
            "propagate": False,
        },
    },
}