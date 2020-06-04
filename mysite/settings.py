#^i#      # adds a '#' to start of line
#^x        # removes '#' from start of line

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "CHANGE_ME!!!! (P.S. the SECRET_KEY environment variable will be used, if set, instead)."

DEBUG = True
#DEBUG = False

ALLOWED_HOSTS = [
        '127.0.0.1', 
        'localhost', 
        'sluffpg.pythonanywhere.com', 
        'sluffpg.herokuapp.com', 
        'imagesdev.pythonanywhere.com',
        'imagesdev.herokuapp.com',
        'imagesdevs3.herokuapp.com',
        'diarys3.pythonanywhere.com',
        'diarys3.herokuapp.com',
        'diarymy.pythonanywhere.com',
        'diarypg.herokuapp.com',
]

#TITLE = "Sluffpg on Sqlite3 (local)"
#TITLE = "Sluffpg on Sqlite3 (Pythonanywhere)"
#TITLE = "Imagesdev on Sqlite3 (Pythonanywhere)"
#TITLE = "Sluffpg3 on Sqlite3 (Heroku)"
#TITLE = "Imagesdevs3 on Sqlite3 (Heroku)"
#TITLE = "Sluffpg on Postgres (local)"
#TITLE = "Sluffpg on Postgres (Heroku)"
#TITLE = "Diary on Sqlite3 (local)"
#TITLE = "Diary on sqlite3 (Pythonanywhere)"
TITLE = "Diary on Sqlite3 (Heroku)"                                          # heroku sqlite3
#TITLE = "Diary on Postgres (local)"
#TITLE = "Diary on Postgres (Pythonanywhere)"
#TITLE = "Diary on Postgres (Heroku)"                                          # heroku postgres

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "mysite",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",                                  #  heroku
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mysite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "mysite.wsgi.application"

DATABASES = {
    'default': {
        #"ENGINE" : "django.db.backends.sqlite3",
        #"NAME": os.path.join(BASE_DIR, "db.sqlite3")
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_sluffpg',
        #'NAME': 'db_postgresql',
        'USER': 'user4',
        'PASSWORD': 'Septembers%^&*()',                          # local postgres
        'HOST': 'localhost', 
} }
import dj_database_url                                            # heroku postgres          ? local postgres
db_from_env = dj_database_url.config(conn_max_age=500)             # heroku postgres          ? local postgres
DATABASES['default'].update(db_from_env)                          # heroku postgres          ? local postgres

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-gb"
TIME_ZONE = "Europe/London"
USE_I18N = True
USE_L10N = True
USE_TZ = True
DATE_INPUT_FORMATS = ('%Y-%m-%d',)
DATE_FORMAT = ('%Y-%m-%d',)

LOGOUT_REDIRECT_URL = '/'

STATIC_URL = "/static/"
MEDIA_URL = '/media/'

## long time
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

## from github/heroku/pythongettingstartes
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

## from github coding-for-entrepreneurs
#STATIC_ROOT = "/home/cfedeploy/webapps/cfehome_static_root/"
#STATICFILES_DIRS = ( os.path.join(BASE_DIR, "static"),)
#STATIC_ROOT = os.path.join(BASE_DIR, "live-static-files", "static-root")
###STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
#MEDIA_ROOT = os.path.join(BASE_DIR, "live-static-files", "media-root")
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'     # heroku
#static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
# https://docs.djangoproject.com/en/2.0/topics/i18n/
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#https://docs.djangoproject.com/en/2.0/topics/settings/
#https://docs.djangoproject.com/en/2.0/ref/settings/
