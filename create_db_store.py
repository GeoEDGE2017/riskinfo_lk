from geoserver.catalog import Catalog

cat = Catalog('http://localhost:8080/geoserver/rest')
ds = cat.create_datastore('riskinfo_lk','geonode')
ds.connection_parameters.update(host='localhost', port='5432', database='riskinfo_lk', user='riskinfo_lk', passwd='riskinfo_lk', dbtype='postgis', schema='public')
cat.save(ds)
