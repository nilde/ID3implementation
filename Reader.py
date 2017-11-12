from random import choice,randint
from collections import OrderedDict
import numpy as np

class Reader:
	def __init__(self,filenameBD,filenameBDInfo,modeOfSubstitution=0,containID=0):
		self.__readedData=[]
		self.__dataPossibilities=OrderedDict()
		self.__attributes=[]
		self.__attributesDomains=[]
		self.__totalExamples=0
		self.canUse=[]
		self.cantUse=[]
		self.__cleanedData=[]
		self.__containID=containID

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

		

	def __cleanReadedData(self,eachData):
		eachData.replace(' ', '')
		cleanedData=eachData.split(',')

		#Delete \n char
		cleanedData[-1]=cleanedData[-1][0:-1]
		if self.__containID:
			cleanedData=cleanedData[1:]
		return cleanedData

	def __chargeDataInfo(self):
		self.eachcharacteristicInfo=[]
		for eachData in self.__dataDBInfo:
			eachReadedData=self.__cleanReadedData(eachData)
			self.eachcharacteristicInfo.append(eachReadedData)


		self.__attributes=self.eachcharacteristicInfo[0]
		self.__attributes[0]=self.__attributes[0][1:]
		self.__attributesDomains=self.eachcharacteristicInfo[1]
		self.__generateTypeOfData()

	def __generateTypeOfData(self):
		for attribute,domain in zip(self.__attributes,self.__attributesDomains):
			if domain == 'continuous':
				self.cantUse.append(attribute)
			else:
				self.canUse.append(attribute)

	def __cleanData(self,modeOfSubstitution=0):
		#At this moment just work with deleting attributes with not acceptable values
		if modeOfSubstitution==0:
			self.__deleteNoneValues()

		elif modeOfSubstitution==1:
			self.__substituteNonesForMean()

		else:
			self.__substituteNonesForMode()

		#Save the number of total examples
		self.__totalExamples=len(self.__readedData)
		return True

	def __deleteNoneValues(self):
		self.__readedData=[x for x in self.__readedData if '?' not in x]
				
	def __substituteNonesForMean(self):

		dataForIter = list(zip(*self.__readedData))
		QuantityOfValues=self.__totalExamples

		for indexCharacteristic,eachCaracteristic in enumerate(dataForIter):
			mean=self.__calculateMean(eachCharacteristic,QuantityOfValues)
			self.__substituteForMean(eachCharacteristic,mean)
		self.__readedData = list(zip(*dataForIter))

	def __calculateMean(self,QuantityOfValues):
		totalSum=0
		for eachParticularCharacteristic in self.__readedData:
			if eachParticularCharacteristic != '?':
				totalSum+=eachParticularCharacteristic
				QuantityOfValues-=1

			mean=totalSum/QuantityOfValues

		return mean

	def __substituteForMean(self,mean):
		#Mirar si retorna bien los valores
		for eachValue in self.__adultsData:
			if eachValue == '?':
				eachValue=mean

	def __substituteNonesForMode(self):
	
		dataForIter=list(zip(*self.__readedData))[:]
		for indexCharacteristic,eachCharacteristic in enumerate(dataForIter):
			mode=self.__calculateMode(eachCharacteristic)
			eachCharacteristic=list(eachCharacteristic)
			self.__substituteForMode(eachCharacteristic,mode)
		self.__readedData = zip(*dataForIter)[:]

	def __calculateMode(self,eachCharacteristic):
		common_values={}
		for entry in eachCharacteristic:
			if common_values.has_key(entry):
				common_values[entry] += 1
			else:
				common_values[entry]  = 1
		return max(common_values, key=common_values.get) 

	def __substituteForMode(self,eachCharacteristic,mode):
		for eachData in eachCharacteristic:
			if eachData=='?':
				eachCharacteristic[eachCharacteristic.index(eachData)] = mode


	def crossValidation(self,numPartitions=10):
		if type(numPartitions) != int:
			return [-1],[-1]

		partitionSize=len(self.__readedData)/numPartitions
		actualIndex=0
		partitions=[]

		for i in range(numPartitions-1):
			partitions.append(self.__readedData[actualIndex:actualIndex+partitionSize])
			actualIndex+=partitionSize
		partitions.append(self.__readedData[actualIndex:])
		return partitions

	def leaveOneOut(self):
		
		trainSet=self.__readedData[:]
		testValue=randint(0, self.__totalExamples-2)
		testSet=trainSet[testValue][:]

		del trainSet[testValue]
		return trainSet,testSet

	def __definitiveCleaning(self):
		for attribute in self.canUse:
			self.__attributes.index(attribute)






	


