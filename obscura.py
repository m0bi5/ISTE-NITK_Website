import importlib,os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'
django.setup()
from obscura import models
from django.contrib.auth.models import Group
from django.core.files.images import ImageFile
import xlrd,xlsxwriter

def excel_read(file,sheet_name='Sheet1'):
        book = xlrd.open_workbook(file)
        sheet = book.sheet_by_name(sheet_name)
        data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
        return data

l=excel_read('obscura.xlsx','Teams')[1:]
accounts=['Name','Username']
for members in l:
    name=members[0]
    pwd = str(members[1])[:10]
    try:
        u=models.Team.objects.create(name=name,pwd=pwd)
        u.save()
    except Exception as e:
        print(e)
        print(username," already exists")
print("Done")
