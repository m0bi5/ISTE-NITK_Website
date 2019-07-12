import importlib,os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'
django.setup()
from account import models
from django.contrib.auth.models import Group

def install_pip(log=None):
   # log("Installing pip, the standard Python Package Manager, first")
    from os     import remove
    from urllib import urlretrieve
    urlretrieve("https://bootstrap.pypa.io/get-pip.py", "get-pip.py")
    subprocess.call(["python", "get-pip.py"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    remove("get-pip.py")

def get_pip(log=None):
    from os.path import isfile, join
    from sys     import prefix
    pipPath = join(prefix, 'Scripts', 'pip.exe')
    if not isfile(pipPath):
        install_pip(log)
        if not isfile(pipPath):
            raise("Failed to find or install pip!")
    return pipPath

def install_package(name, pip_name=None, notes="", log=None):
    from pkgutil import iter_modules
    from sys import prefix
    try:
    	pip=get_pip(log)
    except:
    	if getos()=='mac':
    		pip=str(Path(prefix).parent.parent.joinpath('shims','pip3'))
    	else:
    		pip=str(os.system('which pip3'))
    if name not in [tuple_[1] for tuple_ in iter_modules()]:
        #log("Installing " + name + notes + " Library for Python")
        subprocess.call([pip, "install", pip_name if pip_name else name], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

class SpreadsheetHandler():
	def __init__(self):
		install_package('xlrd')
		self.xlrd=importlib.import_module('xlrd')
		install_package('xlsxwriter')
		self.xlsxwriter=importlib.import_module('xlsxwriter')
		install_package('openpyxl')
		self.openpyxl=importlib.import_module('openpyxl')

	def excel_read(self,file,sheet_name='Sheet1'):	
		book = self.xlrd.open_workbook(file)
		sheet = book.sheet_by_name(sheet_name)
		data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
		return data

	def excel_write(self,dataset,file):
		workbook = self.xlsxwriter.Workbook(file)
		worksheet = workbook.add_worksheet()
		n=1
		for data in dataset:
			c='A'
			for x in data:
				cell=c+str(n)
				worksheet.write(cell, x)
				c=chr(ord(c)+1)
			n+=1
		workbook.close()

	def excel_append(self,dataset,file,sheet_name='Sheet1'):
		wb = self.openpyxl.load_workbook(filename=file)
		ws = wb.get_sheet_by_name(sheet_name)
		for new_row in dataset:
			row = ws.max_row+ 1
			for col, entry in enumerate(new_row, start=1):
				ws.cell(row=row, column=col, value=entry)
		wb.save(file)

sheet=SpreadsheetHandler()
sigs=['Crypt','Charge','Chronicle','Clutch','Concrete','Create','Credit','Catalyst']
l=sheet.excel_read('list.xlsx','4th Years')[1:]
accounts=[]
for members in l:
    name=members[0]
    email=members[-1]
    username="".join(name.split(' '))
    username=username.lower()
    first_name=name.split(' ')[0]
    last_name=name.replace(first_name,"")
    sig_models=list(models.SIG.objects.all())
    sig_responses=members[1:-1]
    my_sigs=[]
    for i in range(len(sig_responses)):
        if 'Y' in sig_responses[i] or 'y' in sig_responses[i]:
            for sig_model in sig_models:
                if sig_model.name.lower()==sigs[i].lower():
                    my_sigs.append(sig_model)
    try:
        if len(my_sigs)!=0:
            u=models.User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email,batch_of=2020)
            u.is_staff=True
            u.sigs.set(my_sigs)
            u.groups.add(Group.objects.get(name='Member'))
            u.set_password('istenitk')
            u.save()
    except Exception as e:
        print(e)
        print(username," already exists")