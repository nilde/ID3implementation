import math
def chooseBestAttribute(allAtributes,allData,listOfValidsAttributes):
    attributeWithMaxGain=-1
    maxGain=0
    #Last column is equivalent to the result
    result=extractDataByAttribute(-1)

    quantityOfAttributes=len(allAtributes[:-1])
    for indexAttribute in range(quantityOfAttributes):
        if attributeIsValid(indexAttribute,listOfValidsAttributes):
            attributeValues=extractDataByAttribute(indexAttribute)
            attributeGain=calcGain(attributeValues,result)
            if attributeGain > maxGain:
                maxGain=attributeGain
                attributeWithMaxGain=attribute

    return attributeWithMaxGain


def attributeIsValid(index,listOfValidsAttributes):
    return index in listOfValidsAttributes


#Extracts all values from a choosen characteristic
def extractDataByAttribute(attributeIndex):
    extractedData=[]
    for eachData in allData:
        extractedData.append(eachData[attributeIndex])
    return extractedData


def generateAttributesDictionary(diffCharacteristics):
    attributeDictionary={}
    for characteristic in diffCharacteristics:
        attributeDictionary[characteristic]=[]
    return attributeDictionary

def calcGain(data,attributeIndex):
    #TODO
    #Re-write that function because we use other structures
    diffValues={}
    diffValues=genDiffValues(data,diffValues)

    for val in diffValues.keys():
        valProb        = 1.0*diffValues[val] / sum(diffValues.values())
        dataSubset     = [entry for entry in data if entry[attributeIndex] == val]
        subsetEntropy += valProb * entropy(attributes, dataSubset, targetAttr)
    
    return (entropy(attributes, data, targetAttr) - subsetEntropy)


def calcEntropy(data,attributeIndex):
    diffValues={}
    diffValues=genDiffValues(data,diffValues)

    for freq in diffValues.values():
        attributeEntropy += (-1.0*freq/len(data)) * math.log(1.0*freq/len(data), 2) 

    return attributeEntropy

def genDiffValues(data,diffValues):
    for entry in data:
        if (diffValues.has_key(entry[attributeIndex])):
            diffValues[entry[attributeIndex]] += 1
        else:
            diffValues[entry[attributeIndex]]  = 1
    return diffValues

def StoppingCriterion(data):
    #All values to classify gives the same result 

    numValues=len(data[0])
    valueAll=data[0][-1]
    for eachData in data:
        if eachData[-1] != valueAll:
            return False
    return True

def assignBestLabel(data):
    #Some doubts about that works how i think that it will
    return data[0][-1]


def dataSeparatedByParameter():
    pass

def splitCriterion():
    pass


