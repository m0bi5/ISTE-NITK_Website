cp conf/iste_website.service /etc/systemd/system/iste_website.service
cp conf/iste_nginx_conf /etc/nginx/sites-available
rm /etc/nginx/sites-enabled/iste_nginx_conf
ln -s /etc/nginx/sites-available/iste_nginx_conf /etc/nginx/sites-enabled
 
uid = iste
base = /home/iste

chdir = %(base)/ISTE-NITK_Website
#home = %(base)/projects/p1
module = website.wsgi:application

master = true
processes = 5

socket = /run/uwsgi/iste_website.sock
chown-socket = %(uid):www-data
chmod-socket = 660
vacuum = true
