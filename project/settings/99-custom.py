SESSION_COOKIE_NAME = 'sessionid_ciec_auf_org'

ROOT_URLCONF = 'project.urls'

INSTALLED_APPS += (
    'project.ciec',
    'auf.django.references',
)

ALLOWED_HOSTS = ['ciec-caraibe.auf.org']
THUMBNAIL_PROGRESSIVE = False


