﻿import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

SITEURL = "http://riskinfo.lk/"

#Email configurations
REGISTRATION_OPEN = True

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = 'riskinfo2016@gmail.com'
#EMAIL_HOST_PASSWORD = 'riskinfo123'
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.dmc.gov.lk'
EMAIL_HOST_USER = 'riskinfo@dmc.gov.lk'
EMAIL_HOST_PASSWORD = 'riskinfo@dmc'
DEFAULT_FROM_EMAIL = 'riskinfo@dmc.gov.lk'
SERVER_EMAIL = 'riskinfo@dmc.gov.lk'
EMAIL_PORT = 25
EMAIL_USE_TLS = True


DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'riskinfo_lk_app',
         'USER': 'riskinfo_lk',
         'PASSWORD': 'riskinfo_lk',
     },
    # vector datastore for uploads
    'riskinfo_lk' : {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'riskinfo_lk',
        'USER' : 'riskinfo_lk',
        'PASSWORD' : 'riskinfo_lk',
        'HOST' : 'localhost',
        'PORT' : '5432'
    }
}

# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default' : {
        'BACKEND' : 'geonode.geoserver',
        'LOCATION' : 'http://localhost:8080/geoserver/',
        'PUBLIC_LOCATION' : 'http://riskinfo.lk/geoserver/',
        'USER' : 'admin',
        'PASSWORD' : 'DMC@admin321',
        'MAPFISH_PRINT_ENABLED' : True,
        'PRINT_NG_ENABLED' : True,
        'GEONODE_SECURITY_ENABLED' : True,
        'GEOGIG_ENABLED' : False,
        'WMST_ENABLED' : False,
        'BACKEND_WRITE_ENABLED': True,
        'WPS_ENABLED' : False,
        'LOG_FILE': '%s/geoserver/data/logs/geoserver.log' % os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir)),
        # Set to name of database in DATABASES dictionary to enable
        'DATASTORE': 'riskinfo_lk', #'datastore',
    }
}

MAP_BASELAYERS = [{
    "source": {"ptype": "gxp_olsource"},
    "type": "OpenLayers.Layer",
    "args": ["No background"],
    "visibility": False,
    "fixed": True,
    "group":"background"
}, {
    "source": {"ptype": "gxp_osmsource"},
    "type": "OpenLayers.Layer.OSM",
    "name": "mapnik",
    "visibility": True,
    "fixed": True,
    "group": "background"
},
# {    
#     "source": {"ptype": "gxp_bingsource"},
#     "name": "AerialWithLabels",
#     "fixed": True,
#     "visibility": False,
#     "group": "background"
# }, 
{
    "source": {"ptype": "gxp_mapboxsource"},
},
{
    "source": {"ptype": "gxp_bingsource", "apiKey": "AhHYhMQ6QunWv4ipvSyjabKI9FJC6rs9B0JfwDsyXU4c2tahe1gkzZVIdUazdrmP"},
    "name": "Aerial",
    "fixed": True,
    "group": "background",
    "visibility": False
},
 {
    "source": {"ptype": "gxp_olsource"},
    "type":"OpenLayers.Layer.XYZ",
    "args":["OSM Grayscale", ["http://a.www.toolserver.org/tiles/bw-mapnik/${z}/${x}/${y}.png", "http://b.www.toolserver.org/tiles/bw-mapnik/${z}/${x}/${y}.png", "http://c.www.toolserver.org/tiles/bw-mapnik/${z}/${x}/${y}.png"], {"transitionEffect": "resize","attribution": "osm_attribution"}],
    "visibility": False,
    "fixed": True,
    "group":"background"
}, {
    "source": {"ptype": "gxp_olsource"},
    "type":"OpenLayers.Layer.XYZ",
    "args":["Humanitarian", ["http://a.tile.openstreetmap.fr/hot/${z}/${x}/${y}.png", "http://b.tile.openstreetmap.fr/hot/${z}/${x}/${y}.png", "http://c.tile.openstreetmap.fr/hot/${z}/${x}/${y}.png"], {"transitionEffect": "resize","attribution": "osm_attribution"}],
    "visibility": False,
    "fixed": True,
    "group":"background"
}
]

LOCAL_GEOSERVER = {
    "source": {
        "ptype": "gxp_wmscsource",
        "url": OGC_SERVER['default']['PUBLIC_LOCATION'] + "wms",
        "restUrl": "/gs/rest"
    }
}
baselayers = MAP_BASELAYERS
MAP_BASELAYERS = [LOCAL_GEOSERVER]
MAP_BASELAYERS.extend(baselayers)

CATALOGUE = {
    'default': {
        'ENGINE': 'geonode.catalogue.backends.pycsw_local',
        'URL': '%scatalogue/csw' % SITEURL,
    }
}

LANGUAGES = (
    ('en', 'English'),
    ('si', 'සිංහල'),
    ('ta', 'தமிழ்'),
)
EXTRA_LANG_INFO = {
    'ta': {
        'bidi': False,
        'code': 'ta',
        'name': 'தமிழ்',
        'name_local':'தமிழ்',
        },
    'si': {
        'bidi': False,
        'code': 'si',
        'name': 'සිංහල',
        'name_local': 'සිංහල',
        },
}

MEDIA_ROOT = "/opt/webapps/www/riskinfo_lk/uploaded"
STATIC_ROOT = "/opt/webapps/www/riskinfo_lk/static"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level': 'ERROR',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR', 'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/geonode/geonode.log',
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console","file"], "level": "INFO", },
        "geonode": {
            "handlers": ["console","file"], "level": "INFO", },
        "gsconfig.catalog": {
            "handlers": ["console","file"], "level": "INFO", },
        "owslib": {
            "handlers": ["console","file"], "level": "INFO", },
        "pycsw": {
            "handlers": ["console","file"], "level": "INFO", },
        },
    }

CLIENT_RESULTS_LIMIT = 10

