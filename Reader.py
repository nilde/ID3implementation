from random import choice,randint
from collections import OrderedDict
import numpy as np

class Reader:
	def __init__(self,filenameBD,filenameBDInfo,modeOfSubstitution=0):
		self.__readedData=[]
		self.__dataPossibilities=OrderedDict()
		self.__attributes=[]
		self.__attributesDomains=[]
		self.__totalExamples=0
		self.__canUse=[]
		self.__cantUse=[]
		self.__cleanedData=[]

		self.__dataDB=open(filenameBD, 'r')
		self.__dataDBInfo=open(filenameBDInfo,'r')

		self.__chargeData()
		self.__chargeDataInfo()
		self.__cleanData(modeOfSubstitution)
		self.__definitiveCleaning()
		self.__dataDBInfo.close()
		self.__dataDB.close()

	def getData(self):
		return self.__readedData


	def __chargeData(self):
		for eachData in self.__dataDB:
			eachReadedData=self.__cleanReadedData(eachData)
			self.__readedData.append(eachReadedData)
		self.__totalExamples=len(self.__readedData)

	def __cleanReadedData(self,eachData):
		eachData.replace(' ', '')
		cleanedData=eachData.split(',')
		cleanedData[-1]=cleanedData[-1][0]
		return cleanedData

	def __chargeDataInfo(self):
		self.eachcharacteristicInfo=[]
		for eachData in self.__dataDBInfo:
			eachReadedData=self.__cleanReadedData(eachData)
			self.eachcharacteristicInfo.append(eachReadedData)


		self.__attributes=self.eachcharacteristicInfo[0]
		self.__attributes[-1]=self.__attributes[-1][0:-1]
		self.__attributesDomains=self.eachcharacteristicInfo[1]
		self.__attributesDomains[-1]=self.__attributesDomains[-1][0:-1]
		self.__generateTypeOfData()

	def __generateTypeOfData(self):
		for attribute,domain in zip(self.__attributes,self.__attributesDomains):
			if domain == 'continuous':
				self.__cantUse.append(attribute)
			else:
				self.__canUse.append(attribute)

	def __cleanData(self,modeOfSubstitution=0):
		#At this moment just work with deleting attributes with not acceptable values
		if modeOfSubstitution!=0:
			return False

		if modeOfSubstitution==0:
			self.__deleteNoneValues()


		elif modeOfSubstitution==1:
			self.__substituteNonesForMean()

		else:
			self.__substituteNonesForMode()

		return True

	def __deleteNoneValues(self):
		self.__readedData=[x for x in self.__readedData if '?' not in x]
				
	def __substituteNonesForMean(self):

		dataForIter = list(zip(*self.__adultsData))
		QuantityOfValues=self.__totalExamples

		for indexCharacteristic,eachCaracteristic in enumerate(dataForIter):
			mean=self.__calculateMean(eachCharacteristic,QuantityOfValues)
			self.__substituteForMean(eachAdultCharacteristic,mean)
		self.__adultsData = list(zip(*dataForIter))

	def __calculateMean(self,QuantityOfValues):
		totalSum=0
		for eachAdultCharacteristic in self.__readedData:
			if eachAdultCharacteristic != '?':
				totalSum+=eachAdultCharacteristic
				QuantityOfValues-=1

			mean=totalSum/QuantityOfValues

		return mean

	def __substituteForMean(self,mean):
		#Mirar si retorna bien los valores
		for eachValue in self.__adultsData:
			if eachValue == '?':
				eachValue=mean

	def __substituteNonesForMode(self):
	
		dataForIter=list(zip(*self.__adultsData))
		for indexCharacteristic,eachCharacteristic in enumerate(dataForIter):
			mode=self.__calculateMode(eachCharacteristic)
			self.__substituteForMode(eachCharacteristic,mode)
		self.__adultsData = list(zip(*dataForIter))

	def __calculateMode(self,eachCharacteristic):
		common_values={}
		for eachAdultCharacteristic in eachCharacteristic:
			if eachAdultCharacteristic != '?':
				if eachCharacteristic in common_values:
					common_values[eachCharacteristic] += 1
				else:
					common_values[eachCharacteristic] = 1
		return max(common_values, key=common_values.get) 

	def __substituteForMode(self,eachCharacteristic,mode):
		for eachData in eachCharacteristic:
			if eachData=='?':
				eachCharacteristic[eachData] = mode


	def crossValidation(self,numPartitions=10):
		if type(numParts) != int:
			return [-1],[-1]

		totalSize=len(self.readedData)-1
		partitionSize=len(self.readedData)/numPartitions
		actualIndex=0
		partitions=[]

		for i in range(numPartitions-1):
			partitions.append(self.readedData[actualIndex:actualIndex+partitionSize][:])
		partitions.append(self.readedData[actualIndex:][:])

		return trainSet,testSet

	def leaveOneOut(self):
		trainSet=self.__readedData[:]
		testValue=randint(0, self.__totalExamples-1)
		testSet=trainSet[testValue][:]

		del trainSet[testValue]

		return trainSet,testSet

	def __definitiveCleaning(self):
		for attribute in self.__canUse:
			self.__attributes.index(attribute)






	


