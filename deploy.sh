sudo git pull istenitk:#includeistenitk.h@https://github.com/m0bi5/ISTE-NITK_Website
sudo pkill -9 -f manage.py
sudo screen python3 manage.py runserver 0.0.0.0:80