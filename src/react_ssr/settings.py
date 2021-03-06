from django.conf import settings as django_settings

SETTINGS = getattr(django_settings, "REACT_SSR")

RENDER_URL = SETTINGS.get(
    "RENDER_URL",
    "http://127.0.0.1:3000/render"
)

RENDER_TIMEOUT = SETTINGS.get(
    "RENDER_TIMEOUT",
    5.0
)

TEMPLATE_NAME = SETTINGS.get(
    "TEMPLATE_NAME",
    None
)

SECRET_KEY = SETTINGS.get(
    "SECRET_KEY",
    None
)

USER_SERIALIZER = SETTINGS.get(
    "USER_SERIALIZER",
    None
)

USER_AGENT_HEADER_NAME = SETTINGS.get(
    "USER_AGENT_HEADER_NAME",
    "HTTP_USER_AGENT"
)

AUTH_STATE_NAME = SETTINGS.get(
    "AUTH_STATE_NAME",
    "auth"
)

AUTH_TOKENS_NAME = SETTINGS.get(
    "AUTH_TOKENS_NAME",
    "tokens"
)

AUTH_USER_NAME = SETTINGS.get(
    "AUTH_USER_NAME",
    "user"
)

DEFAULT_STATE_URL = SETTINGS.get(
    "DEFAULT_STATE_URL",
    "http://127.0.0.1:3000/state"
)

DEFAULT_STATE_TIMEOUT = SETTINGS.get(
    "DEFAULT_STATE_TIMEOUT",
    5.0
)
