from .base_settings import *
import dj_database_url

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())


DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}