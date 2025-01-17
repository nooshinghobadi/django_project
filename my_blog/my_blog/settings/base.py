from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_i4$++la1in_f4*ng97-%7rf+%0_)t=bm-u-2m2h799ozg3a*5'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'myblog.com']

SITE_ID = 1

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'firstblog',
    'taggit',
    'bootstrap5',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.postgres',
    'images.apps.ImagesConfig',
    'django_extensions',
    'easy_thumbnails',
    'shop',
    'cart',
    'orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    #'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'my_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
#man ezafeh kardam va khata dad:
#STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
#print([os.path.join(BASE_DIR, "static")])
#STORAGE={
    #'staticfiles':{
        #'BACKEND':'whitenoise.storage.CompressedManifestStaticFilesStorage',
    #},
#}
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'nooshinghobadi0@gmail.com'
EMAIL_HOST_PASSWORD = 'qizlcczhhdwbwbfm'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'

LOGIN_REDIRECT_URL = 'account:dashboard'
LOGIN_URL = 'account:login'
LOGOUT_URL = 'account:logout'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend' ,
    'account.authentication.EmailAuthBackend' ,
]

CART_SESSION_ID = 'cart'