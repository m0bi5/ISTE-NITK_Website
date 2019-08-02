cp conf/iste_website.service /etc/systemd/system/iste_website.service
cp conf/iste_nginx_conf /etc/nginx/sites-available
rm /etc/nginx/sites-enabled/iste_nginx_conf
ln -s /etc/nginx/sites-available/iste_nginx_conf /etc/nginx/sites-enabled
 
