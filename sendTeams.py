from .emailer import EmailHandler as em


try:
    em_obj=em()
    em_obj.send_email(member[2],"You have registered for ISTE NITK's Obscura!","Hello "+member[0]+"!\n\nYour password to login is:"+member[1]+"\nGet started ASAP!!\n\nWith love,\nISTE NITK",'istenitkchapter@gmail.com','#includeistenitk.h')
except:
    print("No Email Required for registration")
