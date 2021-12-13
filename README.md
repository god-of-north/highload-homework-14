# Homework #14 for Highload:Projector

**Load Balancer**

Set up load balancer on nginx that will have:

- 1 server for UK
- 2 servers for US
- 1 server for the rest
- In case of failure, it should send all traffic to backup server. Health check should happen every 5 seconds


## Instllation

```
git clone https://github.com/god-of-north/highload-homework-14.git
cd highload-homework-14
docker-compose build
```

## GeoIP2 Module Settings

Getting counrty code from GeoLite2 DB by ```$remote_addr``` and store it to the ```$geoip2_data_country_code```
```
geoip2 /usr/share/geoip/GeoLite2-Country.mmdb {
    $geoip2_data_country_code default=default source=$remote_addr country iso_code;
}
```

Setting upsreams by countries
```
upstream backend_default {
    server web_general:5000 fail_timeout=5;
    server web_backup:5000 backup;
}
upstream backend_UK {
    server web_uk:5000 fail_timeout=5;
    server web_backup:5000 backup;
}
upstream backend_US {
    server web_us1:5000 fail_timeout=5;
    server web_us2:5000 fail_timeout=5;
    server web_backup:5000 backup;
}
```

Setting redirect by the ```$geoip2_data_country_code``` variable
```
location / {
    set $addr_backend "http://backend_${geoip2_data_country_code}";
    proxy_pass $addr_backend;
}
```

## Backup Server Test

- Run container ```docker-compose up```
- Test that system works and **web_general** responses by the link http://localhost:1337/
- Down the **web_general** container ```docker-compose stop web_general```
- Update page for next 5 seconds http://localhost:1337/

NGINX config for backup server:
```
upstream backend_US {
    server web_us1:5000 fail_timeout=5;
    server web_us2:5000 fail_timeout=5;
    server web_backup:5000 backup;
}
```

