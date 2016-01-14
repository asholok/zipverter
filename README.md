# zipveter
## Starting for the first time
1. Create new volume:
    
        docker volume create --name=postgis
    
2. Run 
    
        ./redeploy.sh

3. Go inside postgres:

        docker exec -it zipverter_postgis_1 /bin/bash
        su postgres
        psql -c 'create database djgeo;'
        psql -d djgeo -c "CREATE EXTENSION postgis;"
        psql -d djgeo -c "CREATE EXTENSION postgis_topology;"
        psql -d djgeo -c "CREATE EXTENSION fuzzystrmatch;"
        psql -d djgeo -c "CREATE EXTENSION postgis_tiger_geocoder;"
        psql -c "CREATE USER asholok PASSWORD 'asholok';"
        psql -c "GRANT ALL PRIVILEGES ON DATABASE djgeo TO asholok;"
        exit
        exit

2. Run again:
        
        ./redeploy.sh