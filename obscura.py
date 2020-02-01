import importlib,os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'
django.setup()
from obscura import models
from django.contrib.auth.models import Group
from django.core.files.images import ImageFile
import xlrd,xlsxwriter
from emailer import EmailHandler as em


def excel_read(file,sheet_name='Sheet1'):
        book = xlrd.open_workbook(file)
        sheet = book.sheet_by_name(sheet_name)
        data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
        return data

l=excel_read('obscura.xlsx','Teams')[1:]
accounts=['Name','Username']
for member in l:
    name=member[0]
    pwd = str(member[1])[:10]
    try:
        em_obj=em()
        em_obj.send_email(member[2],"You have registered for ISTE NITK's Obscura!","Hello "+member[0]+"!\n\nIf you have any issues with the previous link, try this one: https://iste.nitk.ac.in/obscura/\n"+pwd+"\nGet started ASAP!!\n\nWith love,\nISTE NITK",'istenitkchapter@gmail.com','#includeistenitk.h')
        print('Done with',name)
    except:
        print("No Email Required for registration for",name)
print("Done")
