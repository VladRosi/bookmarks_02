"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-_anbrxu1d00-uanohrvt4jm=d)h@o^i)w3k9gv@o7w7c_5k=78"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mysite.com', '127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS = [
  "account.apps.AccountConfig",
  "django.contrib.admin",
  "django.contrib.auth",
  "django.contrib.contenttypes",
  "django.contrib.sessions",
  "django.contrib.messages",
  "django.contrib.staticfiles",
  'tailwind',
  'theme',
  'django_browser_reload',
  "crispy_forms",
  "crispy_tailwind",
  "social_django",
  "django_extensions",
  "images.apps.ImagesConfig",
]

MIDDLEWARE = [
  "django.middleware.security.SecurityMiddleware",
  "django.contrib.sessions.middleware.SessionMiddleware",
  "django.middleware.common.CommonMiddleware",
  "django.middleware.csrf.CsrfViewMiddleware",
  "django.contrib.auth.middleware.AuthenticationMiddleware",
  "django.contrib.messages.middleware.MessageMiddleware",
  "django.middleware.clickjacking.XFrameOptionsMiddleware",
  "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
  {
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": ['templates/'],
    "APP_DIRS": True,
    "OPTIONS": {
      "context_processors": [
        "django.template.context_processors.debug",
        "django.template.context_processors.request",
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
      ],
    },
  },
]

WSGI_APPLICATION = "project.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": BASE_DIR / "db.sqlite3",
  }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
  {
    "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
  },
  {
    "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
  },
  {
    "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
  },
  {
    "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
  },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
"""=========================================================================="""
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = [
  '127.0.0.1',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

STATICFILES_DIRS = [
  BASE_DIR / "static",
]

STATIC_URL = "static/"

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

AUTHENTICATION_BACKENDS = [
  'django.contrib.auth.backends.ModelBackend',
  'account.authentication.EmailAuthBackend',
  # 'social_core.backends.facebook.FacebookOAuth2',
  'social_core.backends.twitter.TwitterOAuth',
  'social_core.backends.google.GoogleOAuth2',
]

SOCIAL_AUTH_TWITTER_KEY = 'tWAt8VaPZuv0cI4DL0iqbMWoO'
SOCIAL_AUTH_TWITTER_SECRET = 'n7KGQLCXg4kIvD82aLRYWD8KLAOnf3AVzx9QNgoDF0qIOaNoaY'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1022798439259-lf4nkkdgrkslhfpjfmc8cttjbk26ln53.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_PIPELINE = [
  'social_core.pipeline.social_auth.social_details',
  'social_core.pipeline.social_auth.social_uid',
  'social_core.pipeline.social_auth.auth_allowed',
  'social_core.pipeline.social_auth.social_user',
  'social_core.pipeline.user.get_username',
  'social_core.pipeline.user.create_user',
  'account.authentication.create_profile',
  'social_core.pipeline.social_auth.associate_user',
  'social_core.pipeline.social_auth.load_extra_data',
  'social_core.pipeline.user.user_details',
]

# PASSWORD_HASHERS = [
#  'django.contrib.auth.hashers.PBKDF2PasswordHasher',
#  'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
#  'django.contrib.auth.hashers.Argon2PasswordHasher',
#  'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
#  'django.contrib.auth.hashers.ScryptPasswordHasher',
# ]
