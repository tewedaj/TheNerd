from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
path="C:\Program Files (x86)\chromedriver.exe" #path of the driver file for the browser
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
driver =webdriver.Chrome(executable_path=path,options=options)

class Nerd:
	noquestion=0;
	questiones =[]
	def get_homeWork(self,dir):
		homework = open(dir,"r")
		questions =homework.readlines()
		x =0
		for question in questions:
			self.questiones.insert(x,question[2:])
			x+=1
	def do_question(self,question):
		driver.get("https://google.com/")
		se =driver.find_element(By.NAME,"q")
		se.send_keys(question+Keys.ENTER)
		answer	=driver.find_elements(By.CLASS_NAME,"st")
		return answer
	def checkFilet(self,file):
		return file.endswith(".hw")
		
	def writeHomew(self,homeworka,output):
		writed=open(output,"a+",errors="ignore")
		writed.write("question number %d\r\n" %(self.noquestion))
		for x in homeworka:
			print(x.text)
			writed.write(x.text)
	def do_homework(self,dir,output):
		if self.checkFilet(dir):
			self.get_homeWork(dir)
			
			for q in self.questiones:
				self.noquestion+=1;
				self.writeHomew(self.do_question(q),output)
		else:
			print("Wrong file type: i only work with hw")
			

n = Nerd()
arg1 =sys.argv[1]
arg2 =sys.argv[2]
if(arg1!="" and arg2!=""):	
	n.do_homework(arg1,arg2)
