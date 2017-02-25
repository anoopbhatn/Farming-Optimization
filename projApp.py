from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Label
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

import time
import random

# Find the minimum number in the row of Objective Function co-efficients
def minimumfind(temp):
	m=temp[0]
	for i in temp:
		if i>0 and i<m:
			m=i
	return m

a=int() # Price of Phosphate
b=int() # Price of Nitrate

a=4
b=1

a1=[0 for i in range(3)]
b1=[0 for i in range(3)]
c1=[0 for i in range(3)]

# First co-efficient of all constraints
a1[0]=3
a1[1]=4
a1[2]=1

# Second co-efficient of all constraints
b1[0]=1
b1[1]=3
b1[2]=2

def changeab(na,nb):
	a=na
	b=nb
	print na,nb,'The new values'
	print a,b

# Function to perform two phase simplex
def twophase():
	mat=[[0 for x in range(7)] for y in range(4)]

	a2=-(a1[0])-(a1[1])
	b2=-(b1[0])-(b1[1])
	c2=c1[0]+c1[1]

	mat[0][0]=-a2
	mat[0][1]=-b2
	mat[0][2]=-1
	mat[0][6]=c2

	for i in range(1,4):
		mat[i][0]=a1[i-1]
		for i in range(1,4):
			mat[i][1]=b1[i-1]

	mat[2][2]=-1
	mat[3][3]=1
	mat[1][4]=1
	mat[2][5]=1

	for i in range(1,4):
		mat[i][6]=c1[i-1]

	maxi=mat[0].index(max(mat[0][0:6]))

	indv=dict()

	while mat[0][maxi]>0 and maxi<6:
		temp= [0 for i in range(3)]
		for i in range(3):
			try:
				temp[i]=(mat[i+1][6]/float(mat[i+1][maxi]))
			except:
				print 'Zero Error'
		mini=minimumfind(temp)
		pivot=(temp.index(mini))+1
		div=mat[pivot][maxi]
		indv[maxi]=pivot
		for i in range(7):
			try:
				mat[pivot][i]=mat[pivot][i]/float(div)
			except:
				print 'Zero Error1'
		for i in range(4):
			if i==pivot:
				continue
			num=mat[i][maxi]
			for j in range(7):
				mat[i][j]-=(num*mat[pivot][j])
				mat[i][j]=round(mat[i][j],10)
		maxi=mat[0].index(max(mat[0][0:6]))

	#Second Phase

	second=[[0 for x in range(5)] for y in range(4)]

	x3=-((a*(-mat[indv[0]][2]))+(b*(-mat[indv[1]][2])))
	x4=-((a*(-mat[indv[0]][3]))+(b*(-mat[indv[1]][3])))
	c=(a*mat[indv[0]][6])+(b*mat[indv[1]][6])

	second[0][2]=x3
	second[0][3]=x4
	second[0][4]=c

	for i in range(1,4):
		for j in range(4):
			second[i][j]=mat[i][j]
	for i in range(1,4):
		second[i][4]=mat[i][6]

	maxi=second[0].index(max(second[0][0:4]))

	indv1=dict()
	while second[0][maxi]>0 and maxi<4:
		temp= [0 for i in range(3)]
		for i in range(3):
			try:
				temp[i]=(second[i+1][4]/float(second[i+1][maxi]))
			except:
				print 'Zero Error'
		mini=minimumfind(temp)
		pivot=(temp.index(mini))+1
		div=second[pivot][maxi]
		indv1[maxi]=pivot
		for i in range(5):
			try:
				second[pivot][i]=second[pivot][i]/float(div)
			except:
				print 'Zero Error1'
		for i in range(4):
			if i==pivot:
				continue
			num=second[i][maxi]
			for j in range(5):
				second[i][j]-=(num*second[pivot][j])
				second[i][j]=round(second[i][j],10)
		maxi=second[0].index(max(second[0][0:4]))
	return [str(second[0][4]),str(second[indv[0]][4]),str(second[indv[1]][4])]
	
class FirstScreen(Screen):
	pass

class Farming(ScreenManager):
	pass

class WhiteBox(BoxLayout):
	pass

class LeftLabel(Label):
	pass

class SecondScreen(Screen):
	result = StringProperty()
	result1 = StringProperty()
	result2 = StringProperty()

	def calculate(self,total,phosphate,nitrate):
		c1[0]=int(total)
		c1[1]=int(phosphate)
		c1[2]=int(nitrate)
		try:
			res=twophase()
			self.result= 'The minimum price the farmer can give is :'+res[0]
			self.result1='The amount of Phosphate to be use is : '+res[1]+'kg'
			self.result2= 'The amount of Nitrate to be use is : '+res[2]+'kg'
		except:
			self.result='Sorry!! There is some inconvenience'
			self.result1='Two Phase method failed'
			self.result2='  '
		
class ThirdScreen(Screen):
	pprice= StringProperty()
	nprice=  StringProperty()

	global a
	global b
	def _init_(self):
		global a
		global b
		self.pprice= 'Current price for phosphate is '+str(a)+' per kg'
		self.nprice= 'Current price for nitrate is '+str(b)+' per kg'

	def current(self):
		global a
		global b
		self.pprice= 'Current price for phosphate is '+str(a)+' per kg'
		self.nprice= 'Current price for nitrate is '+str(b)+' per kg'

	def change_price(self,phosprice,nitrateprice,cons1,cons2,cons3,cons4,cons5,cons6):
		global a
		global b
		global a1
		global b1
		
		a=int(phosprice)
		b=int(nitrateprice)

		a1[0]=int(cons1)
		a1[1]=int(cons3)
		a1[2]=int(cons5)

		b1[0]=int(cons2)
		b1[1]=int(cons4)
		b1[2]=int(cons6)

		self.current()

class projApp(App):
    def build(self):
        return root_widget

root_widget=Builder.load_file("proj.kv")

projApp().run()
