uwsgi --http :8000 --ini conf/iste_uwsgi.ini
sudo cp conf/iste_nginx_conf /etc/nginx/sites-available
sudo rm /etc/nginx/sites-enabled/iste_nginx_conf
sudo ln -s /etc/nginx/sites-available/iste_nginx_conf /etc/nginx/sites-enabled
 
