import os,csv
import xlrd
import xml.dom.minidom

class DataHelper(object):
	def __init__(self):
		pass
	def getList(self):
		list=[['老诚一锅','羊蝎子']]#,['电影票','电影院']
		return list

	def data_dirs(self,folder_name):
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		DATA_DIRS = (
			os.path.join(BASE_DIR,folder_name),)
		d='/'.join(DATA_DIRS)
		return d
		
	'''  读取 txt 文件数据  '''
	def readFile(self,index):
		f=open(self.data_dirs('Data')+'/system.txt','r')
		d=f.readlines()
		f.close()
		return d[index]

	def readFile_all(self,filename):
		f=open(self.data_dirs('Data')+'/'+filename)
		rows=[]
		for eachLine in f:
			item_tmp = []
			item_list = eachLine.strip().split(",")
			rows.append(item_list)
		f.close()
		# print rows
		return rows

	'''  读取 csv 文件数据  '''
	def readCsv(self,value1,value2):
		rows=[]
		data_file=open(self.data_dirs('Data')+'/system.csv')
		reader=csv.reader(data_file)
		next(reader,None)
		for row in reader:
			rows.append(row)
		return ''.join(rows[value1][value2]).decode('gb2312')


	def readCsvs(self):
		rows=[]
		with open(self.data_dirs('Data')+'/system.csv', 'rb') as f:
			readers=csv.reader(f)
			#next(readers,None)
			for line in readers:
				rows.append(line)
		return rows

	'''  读取 excel 文件数据  '''
	def readExcel(self,rowValue,colValue):
		book=xlrd.open_workbook(self.data_dirs('Data')+'/login.xlsx')
		sheet=book.sheet_by_index(0)
		return sheet.cell_value(rowValue,colValue)

	def readExcels(self,):
		rows=[]
		book=xlrd.open_workbook(self.data_dirs('Data')+'/login.xlsx')
		sheet=book.sheet_by_index(0)
		for row in range(1,sheet.nrows):
			rows.append(list(sheet.row_values(row,0,sheet.ncols)))

		return rows

	def readExcel_ddt(self,rowValue,colValue):
		book=xlrd.open_workbook(self.data_dirs('Data')+'/system_ddt.xlsx')
		sheet=book.sheet_by_index(0)
		# print sheet.cell_value(rowValue,colValue)
		return sheet.cell_value(rowValue,colValue)

	def readExcels_ddt(self):
		rows=[]
		book=xlrd.open_workbook(self.data_dirs('Data')+'/system_ddt.xlsx')
		sheet=book.sheet_by_index(0)
		for row in range(1,sheet.nrows):
			rows.append(list(sheet.row_values(row,0,sheet.ncols)))
		return rows


	'''  读取 xml 文件数据  '''
	def getXmlData(self,value):
		dom=xml.dom.minidom.parse(self.data_dirs('Data')+"/system.xml")
		db=dom.documentElement
		name=db.getElementsByTagName(value)
		nameValue=name[0]
		return nameValue.firstChild.data

	def getXmlUser(self,parent,child):
		dom=xml.dom.minidom.parse(self.data_dirs('Data')+"/system.xml")
		db=dom.documentElement
		itemlist=db.getElementsByTagName(parent)
		item=itemlist[0]
		return item.getAttribute(child)


	def getXmlUser_ddt(self,parent,child1,child2):
		dom=xml.dom.minidom.parse(self.data_dirs('Data')+"/system.xml")
		db=dom.documentElement
		itemlist=db.getElementsByTagName(parent)
		parent_list = []
		for i in range(0,len(itemlist)):
			item=itemlist[i]
			child_list = []
			child_list.append(item.getAttribute(child1))
			child_list.append(item.getAttribute(child2))
			parent_list.append(list(child_list))

		return parent_list


		

