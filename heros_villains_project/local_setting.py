# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b!0f)n)h39up!yg%#p!h20nv-@-ka$ou(yb7j!h9m_-0ov%ovt'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heros_and_villains_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD':'Password10'

    }
}
