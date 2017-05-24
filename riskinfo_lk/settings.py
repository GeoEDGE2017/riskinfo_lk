# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2012 OpenPlans
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

# Django settings for the GeoNode project.
import os
import geonode
from geonode.settings import *
#
# General Django development settings
#
SITEURL = "http://riskinfo.lk/"
# Defines the directory that contains the settings file as the LOCAL_ROOT
# It is used for relative settings elsewhere.
LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))
GEONODE_ROOT = os.path.abspath(os.path.dirname(geonode.__file__))

print GEONODE_ROOT

WSGI_APPLICATION = "riskinfo_lk.wsgi.application"

# Additional directories which hold static files
STATICFILES_DIRS.append(
    os.path.join(LOCAL_ROOT, "static"),
)

# Note that Django automatically includes the "templates" dir in all the
# INSTALLED_APPS, se there is no need to add maps/templates or admin/templates
TEMPLATE_DIRS = (
    os.path.join(LOCAL_ROOT, "templates"),
) + TEMPLATE_DIRS

# Location of url mappings
ROOT_URLCONF = 'riskinfo_lk.urls'

# Load more settings from a file called local_settings.py if it exists

LOCKDOWN_GEONODE = False 

# Initializing BaseLayers 

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
    "source": {"ptype": "gxp_olsource"},
    "type":"OpenLayers.Layer.XYZ",
    "args":["OSM Grayscale", ["http://a.www.toolserver.org/tiles/bw-mapnik/${z}/${x}/${y}.png", "http://b.www.toolserver.org/tiles/bw-mapnik/${z}/${x}/${y}.png", "http://c.www.toolserver.org/tiles/bw-mapnik/${z}/${x}/${y}.png"], {"transitionEffect": "resize","attribution": "osm_attribution"}],
    "visibility": True,
    "fixed": True,
    "group":"background"
}, {
    "source": {"ptype": "gxp_olsource"},
    "type":"OpenLayers.Layer.XYZ",
    "args":["Humanitarian", ["http://a.tile.openstreetmap.fr/hot/${z}/${x}/${y}.png", "http://b.tile.openstreetmap.fr/hot/${z}/${x}/${y}.png", "http://c.tile.openstreetmap.fr/hot/${z}/${x}/${y}.png"], {"transitionEffect": "resize","attribution": "osm_attribution"}],
    "visibility": True,
    "fixed": True,
    "group":"background"
},{
    "source": {"ptype": "gxp_mapquestsource"},
    "name": "osm",
    "group": "background",
    "visibility": True
},{
    "source": {"ptype": "gxp_mapquestsource"},
    "name": "naip",
    "group": "background",
    "visibility": False
}, {
    "source": {"ptype": "gxp_bingsource", "apiKey": "AhHYhMQ6QunWv4ipvSyjabKI9FJC6rs9B0JfwDsyXU4c2tahe1gkzZVIdUazdrmP"},
    "name": "Aerial",
    "fixed": True,
    "group": "background",
    "visibility": False
},
{
    "source": {"ptype": "gxp_googlesource", "apiKey": "AIzaSyBr9pYZ1-db6c2uWMFsizpKoq1ro8qiqrQ"},
    "name": "SATELLITE",
    "fixed": True,
    "group": "background",
    "visibility": False
}
]

# define the urls after the settings are overridden
if 'geonode.geoserver' in INSTALLED_APPS:
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

# Add additional paths (as regular expressions) that don't require authentication.
AUTH_EXEMPT_URLS = ()

if LOCKDOWN_GEONODE:
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('geonode.security.middleware.LoginRequiredMiddleware',)

try:
    from local_settings import *
except ImportError:
    pass
