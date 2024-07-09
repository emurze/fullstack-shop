import os

import sentry_sdk
from dotenv import load_dotenv
from sentry_sdk.integrations.django import DjangoIntegration

load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVEL")

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
)

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "stream": {
#             "level": LOG_LEVEL,
#             "class": "logging.StreamHandler",
#         },
#     },
#     "loggers": {
#         "django": {
#             "level": LOG_LEVEL,
#             "handlers": [
#                 "stream",
#             ],
#             "propagate": False,
#         },
#     },
# }