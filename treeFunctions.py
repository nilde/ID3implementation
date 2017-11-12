import math
def splitCriterionID3(allData,validAttributes,actualEntropy):
    maxGain=0
    maxGainPossiblitities=[]
    attributeWithMaxGain=''
    newEntropy=0
    bestEntropy=0

    listIndexValidAttributes=genValidAttributeListIndexes(validAttributes)
    for indexAttribute in listIndexValidAttributes[:-1]:
        attributeGain,possibilities,newEntropy=calcGain(allData,indexAttribute)

        if attributeGain > maxGain:
            maxGain=attributeGain
            attributeWithMaxGain=extractValidAttributeName(indexAttribute,validAttributes)
            maxGainPossiblitities=possibilities
            bestEntropy=newEntropy
    if attributeWithMaxGain !='':
        validAttributes[attributeWithMaxGain]=0
    return attributeWithMaxGain,validAttributes,maxGainPossiblitities,bestEntropy

def splitCriterionID45(allData,validAttributes,actualEntropy):
    attributeWithMaxGainRatio=0
    maxGainRatio=0

    listIndexValidAttributes=genValidAttributeListIndexes(validAttributes)
    for indexAttribute in listIndexValidAttributes:
        extractedData=extractDataByAttribute(allData,indexAttribute)
        attributeGain=calcGain(extractedData,indexAttribute) 

        diffValues=genDiffValues(allData,attributeGain)
        totalValues=len(allData)
        attributeSplitInfo=calcSplitinfo(diffValues,totalValues)
        attributeGainRatio=attributeGain/attributeSplitInfo

        if attributeGainRatio > maxGainRatio:
            maxGainRatio=attributeGainRatio
            attributeWithMaxGainRatio=attribute


    listOfValidsAttributes[attributeWithMaxGain]=0
    return attributeWithMaxGain,listOfValidsAttributes

def extractValidAttributeName(indexAttribute,validAttributes):
    listOfAttributes=validAttributes.keys()
    return listOfAttributes[indexAttribute]

def genValidAttributeListIndexes(validAttributes):
    return [index for index,attribute in enumerate(validAttributes.keys()) if validAttributes[attribute] == 1]

def calcSplitInfo(diffValues,totalValues):
    totalSum=0
    for sv in diffValues.keys():
        totalSum+=(1.0*sv/totalValues)* math.log(1.0*sv/totalValues,2)
    totalSum*= -1.0

    return totalSum

#Extracts all values from a choosen characteristic
def extractDataByAttribute(allData,attributeIndex):
    extractedData=[]
    for eachData in allData:
        extractedData.append(eachData[attributeIndex])
    return extractedData


def calcGain(data,attributeIndex):
    #Re-write that function because we use other structures
    diffValues={}
    diffValues=genDiffValues(data,diffValues,attributeIndex)
    subsetEntropy=0

    for val in diffValues.keys():

        valProb        = 1.0*diffValues[val] / sum(diffValues.values())
        dataSubset     = [entry for entry in data if entry[attributeIndex] == val]
        subsetEntropy += valProb * calcEntropy(dataSubset,attributeIndex)

    return (calcEntropy(data,attributeIndex) - subsetEntropy),diffValues.keys(),subsetEntropy


def calcEntropy(data,attributeIndex):
    diffValues={}
    diffValues=genDiffValues(data,diffValues,-1) #-1 is equal to the column of the result
    attributeEntropy=0
    for freq in diffValues.values():
        attributeEntropy += (-1.0*freq/len(data)) * math.log(1.0*freq/len(data), 2) 

    return attributeEntropy

def genDiffValues(data,diffValues,attributeIndex):
    for entry in data:
        if (diffValues.has_key(entry[attributeIndex])):
            diffValues[entry[attributeIndex]] += 1
        else:
            diffValues[entry[attributeIndex]]  = 1
    return diffValues

def StoppingCriterion(data):

    valueAll=data[0][-1]
    for eachData in data:
        if eachData[-1] != valueAll:
            return False

    return True

def assignBestLabel(data):
    return data[0][-1]


def dataSeparatedByParameter(data,specificValueOfAttribute,attributeName,attributeList):
    attributes=attributeList.keys()
    indexOfAttribute=attributes.index(attributeName)

    dataExtractedFromAttribute=[]
    for eachData in data:
        if eachData[indexOfAttribute]==specificValueOfAttribute:
            dataExtractedFromAttribute.append(eachData)

    return dataExtractedFromAttribute




