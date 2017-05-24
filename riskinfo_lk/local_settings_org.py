import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

SITEURL = "http://riskinfo.lk/"

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
        'PORT' : 5432
    }
}

# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default' : {
        'BACKEND' : 'geonode.geoserver',
        'LOCATION' : 'http://localhost:8080/geoserver/',
        'PUBLIC_LOCATION' : '%sgeoserver/' % SITEURL,
        'USER' : 'admin',
        'PASSWORD' : 'geoserver',
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
    "visibility": False,
    "fixed": True,
    "group": "background"
}, {
    "source": {"ptype": "gxp_mapquestsource"},
    "name": "osm",
    "group": "background",
    "visibility": True
}, {
    "source": {"ptype": "gxp_mapquestsource"},
    "name": "naip",
    "group": "background",
    "visibility": False
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
}]

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

MEDIA_ROOT = "/var/www/riskinfo_lk/uploaded"
STATIC_ROOT = "/var/www/riskinfo_lk/static"

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

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

SITEURL = "riskinfo_lk"

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
        'PORT' : 5432
    }
}

# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default' : {
        'BACKEND' : 'geonode.geoserver',
        'LOCATION' : 'http://localhost:8080/geoserver/',
        'PUBLIC_LOCATION' : 'http://192.168.10.50/geoserver/',
        'USER' : 'admin',
        'PASSWORD' : 'geoserver',
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

CATALOGUE = {
    'default': {
        'ENGINE': 'geonode.catalogue.backends.pycsw_local',
        'URL': '%scatalogue/csw' % SITEURL,
    }
}

MEDIA_ROOT = "/var/www/riskinfo_lk/uploaded"
STATIC_ROOT = "/var/www/riskinfo_lk/static"
