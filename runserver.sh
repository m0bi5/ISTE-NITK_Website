uwsgi --http :8000 --ini conf/iste_uwsgi.ini
cp conf/iste_nginx_conf /etc/nginx/sites-available
rm /etc/nginx/sites-enabled/iste_nginx_conf
ln -s /etc/nginx/sites-available/iste_nginx_conf /etc/nginx/sites-enabled
 
