"""
Django settings for stride project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Did not fix css not loading:
# http://stackoverflow.com/questions/39670443/django-1-9-7-admin-pages-css-loaded-but-not-rendering
# import mimetypes
# mimetypes.add_type("text/css", ".css", True)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..'))
FILES_DIR = os.path.abspath(os.path.join(BASE_DIR, '../data'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=nqdei0*$&k&n^qgiqkk8djxvpe=b#n$6xz8o7&0)cg_94h4-k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# TODO: Allow eventual web host
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'maystride.com', 'www.maystride.com', '45.55.74.52']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_cron',
    'home',
    'stride_recommender',
    'stride_stats',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CRON_CLASSES = [
    'home.crons.RunCronJob',
    'home.crons.TaskReadMALShowsAggregated',
    # python manage.py runcrons "home.crons.TaskReadMALShowsAggregated"
    'home.crons.TaskReadMALShowsIndividual',
    # python manage.py runcrons "home.crons.TaskReadMALShowsIndividual"
    'home.crons.TaskReadMALShowsMaster',
    # python manage.py runcrons "home.crons.TaskReadMALShowsMaster"
    'home.crons.TaskUpdateUserData',
    # python manage.py runcrons "home.crons.TaskUpdateUserData"
    'home.crons.TaskWriteBasicStats',
    # python manage.py runcrons "home.crons.TaskWriteBasicStats"
    'home.crons.TaskWriteExtendedStats',
    # python manage.py runcrons "home.crons.TaskWriteExtendedStats"
    # ...
]

ROOT_URLCONF = 'stride.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # App directories currently contain no templates
        'DIRS': [os.path.join(BASE_DIR, 'templates'), 'stride_recommender/templates', 'stride_stats/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'stride.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# DATABASE_ROUTERS = ['manager.router.DatabaseAppsRouter']
# DATABASE_APPS_MAPPING = {'show_data_extended_model': 'show_data_extended'}

DATABASES = {
    # Database in external filepath
    # http://stackoverflow.com/questions/39228449/how-to-access-directory-file-outside-django-project
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(FILES_DIR, 'show_data_aggregated.db'),
    },
    # 'show_data_extended': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(FILES_DIR, 'show_data_aggregated.db'),
    # },
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
    'PAGE_SIZE': 10
}

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'static/'),
    'templates/static/',
    'stride_recommender/templates/static',
    'stride_stats/templates/static',
    'home/templates/static',
]

