import pandas
import pandas as pd
import numpy as np
import random
import os
import datetime
import sys
import os.path
def getDFFromCSV(filename):
    if os.path.isfile(filename):
        return pandas.read_csv(filename)
    else:
        raise IOError
def GetDateFrame(date1,date2):
	start = datetime.datetime.strptime(date1, '%Y-%m-%d')
	end = datetime.datetime.strptime(date2, '%Y-%m-%d')
	step = datetime.timedelta(days=1)
	dateslist=[]
	while start <= end:
		dateslist.append(start.date())
		start += step
	return dateslist
def GenerateRandomNumbers(length,Minvalue,Maxvalue):
	randsample=[]
	for i in range(length):
		a=random.randint(Minvalue,Maxvalue)
		randsample.append(a)
	return randsample
filename=sys.argv[1]
date1=sys.argv[2]
date2=sys.argv[3]
a=sys.argv[4]
b=sys.argv[5]
Minvalue=int(a)
Maxvalue=int(b)
def GenerateFile():
	# filename=input("Please Enter Input FIle Name:")
	if os.path.isfile(filename):
		FileContent=getDFFromCSV(filename)
		#filepath=input("Please Enter Target File Path:")
		start=0
		end=filename.find('.')
		OutputFileName1=filename[start:end]
		OutputFileName2='_TestDataGenerator.csv'
		OutputFileName=OutputFileName1+OutputFileName2
		FileDataFrame=pd.DataFrame(FileContent,columns=['Account Names'])
		# date1=input("Please Enter From Date Value:")
		# date2=input("Please Enter To Date Value:")
		dateslist=GetDateFrame(date1,date2)
		datesframe=pd.DataFrame(dateslist,columns=['Date'])
		# Minvalue=input("Please Enter Range From Value:")
		# Maxvalue=input("Please Enter Range To Value:")
		for i in range(len(datesframe)):
			randsample=GenerateRandomNumbers(len(FileContent),Minvalue,Maxvalue)
			NumberDataFrame=pd.DataFrame(randsample,columns=['Int Value'])
			onedayarray=[]
			for j in range(len(FileDataFrame)):
				x=datesframe.ix[i]
				y=x.item()
				onedayarray.append(y)
			daydataframe=pd.DataFrame(onedayarray,columns=['Date'])
			Framelist=[FileContent,daydataframe,NumberDataFrame]
			ResultFrame=pd.concat(Framelist,axis=1)
			ResultFrame.to_csv(OutputFileName,index=False,mode='a',header=False)
		print "Successfully Generated output file"
	else:
		print "Input file does not exist Please enter Correct Input File"
GenerateFile()