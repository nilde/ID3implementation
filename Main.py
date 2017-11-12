import Reader
import Node
import Test
import TreeFunctions
import copy


def treeGenerationID3(data,attributeList,parent=None,entropy=1,connectionName=None,prof=0,root=None):
	Tree=Node.Node(parent,data,entropy,connectionName,False,root,'No')
	if prof==0:
		Tree.autoParent()
		Tree.setRoot()

	if(TreeFunctions.StoppingCriterion(Tree.dataNode)):
		Tree.isLeave=True
		bestLabel=TreeFunctions.assignBestLabel(data)
		Tree.finalClassification=bestLabel
		Tree.label=bestLabel
	else:
		Tree.label,newAttributeList,listOfCharacteristics,newEntropy=TreeFunctions.splitCriterionID3(Tree.dataNode,attributeList,entropy)

		for eachPossibleValue in listOfCharacteristics:
			Tree.dataNode=TreeFunctions.dataSeparatedByParameter(data,eachPossibleValue,Tree.label,attributeList)
			subTree=treeGenerationID3(Tree.dataNode,newAttributeList,Tree,newEntropy,eachPossibleValue,prof+1,Tree.root)

			Tree.childs[eachPossibleValue]=subTree
	return Tree

def treeGenerationID45(data,attributeList,parent=None,entropy=1,connectionName=None,prof=0,root=None):	
	Tree=Node.Node(parent,data,entropy,connectionName,False,root,'No')
	if prof==0:
		Tree.autoParent()
		Tree.setRoot()

	if(TreeFunctions.StoppingCriterion(data)):
		Tree.isLeave=True
		bestLabel=TreeFunctions.assignBestLabel(data)
		Tree.classificationFinal=bestLabel
		Tree.label=bestLabel
	else:
		Tree.label,newAttributeList,listOfCharacteristics,stateOfEntropy=TreeFunctions.splitCriterionID45(Tree.dataNode,attributeList,entropy)
		for eachPossibleValue in listOfCharacteristics:
			Tree.dataNode=TreeFunctions.dataSeparatedByParameter(data,eachPossibleValue,Tree.label,attributeList)
			subTree,prof=treeGenerationID45(Tree.dataNode,newAttributeList,Tree,stateOfEntropy,eachPossibleValue,prof+1,Tree.root)
			Tree.childs[eachPossibleValue]=subTree

	return Tree


def prunningTree(Tree):
	#TODO
	pass

def genTree(node,listNodes,maxProf):
    if node.level == maxProf:
        return None
    else:
    	for eachNode in node.childs:
        	listNodes.append([eachNode.level,eachNode])
        	genTree(eachNode,listNodes)

def printTree(Tree):
	listNodes=[]
	maxProf=lastNode(Tree).level
	print genTree(Tree,listNodes,maxProf)


	#Some treatement to clean the list generated because we made an postorder exploratio and we need to apply some changes to visualize correctly the tree 
	cleanGeneratedList(listNodes)

	print listNodes

def cleanGeneratedList(listNodes):
	#TODO
	pass

def lastNode(Tree):
	actualNode=Tree.root

	#keep choosing the last child for each level, this automatically gives the last leave of the tree
	while(not actualNode.isLeave):
		differentNodesList=actualNode.childs.values()
		actualNode=differentNodesList[-1]
	return actualNode

def solveForCrossValidation(Tree,testSet,attributesUsed):
	for eachTest in testSet:
		comprobation=copy.deepcopy(Tree)
		while(not comprobation.isLeave):

			label=comprobation.label
			correspondentIndex=attributesUsed.keys().index(label)
			value=eachTest[correspondentIndex]
			comprobation=comprobation.childs[value]

		if comprobation.finalClassification == eachTest[-1]:
			print 'Correct'
		else:
			print 'Mistake'
def solveForLeave1Out(Tree,testSet,attributesUsed):
	comprobation=copy.deepcopy(Tree)
	while(not comprobation.isLeave):
		printChilds(comprobation)
		label=comprobation.label
		correspondentIndex=attributesUsed.keys().index(label)
		value=testSet[correspondentIndex]
		comprobation=comprobation.childs[value]
	if comprobation.finalClassification == testSet[-1]:
		print 'Correct'
	else:
		print 'Mistake'

def printChilds(Node):
	print Node.childs
	for ep in Node.childs.values():
		print ep.label


def generateSets(partitions):
	testSet=[]
	trainSet=[]

	for eachPartition in partitions[:-1]:
		trainSet.extend(eachPartition)

	testSet=partitions[-1]
	return testSet,trainSet

	

def main():
	#modeOfSubstitution=0-> delete none values
	#modeOfSubstitution=1 -> substitute for mean
	#modeOfSubstitution=2 -> substitute for mode
	modeOfSubstition=2
	numPartitions=6
	containID=1

	reader=Reader.Reader('breastCancer.data','breastCancerInfo.data',modeOfSubstition,containID)

	#Different methods for generating the set
	trainSet,testSet=reader.leaveOneOut()

	#partitions=reader.crossValidation(numPartitions)
	#testSet,trainSet=generateSets(partitions)
	
	if testSet[0] ==[-1]:
		print "Numero de particiones erroneo"
	else:
		attributesUsed=initListOfAttributes(reader.canUse)
		#fullTreeID3=treeGenerationID3(trainSet,attributesUsed)
		fullTreeID45=treeGenerationID45(trainSet,attributesUsed)
		print fullTreeID45.childs['9'].connectionName
		solveForLeave1Out(fullTreeID45,testSet,attributesUsed)
		#solveForCrossValidation(fullTreeID3,testSet,attributesUsed)			
		#printTree(fullTreeID3)
		print "Generacion del arbol completada"

#Change structure to a new one that will be more handly
def initListOfAttributes(listOfAttributes):
	return {attribute: 1 for attribute in listOfAttributes}

if __name__=='__main__':
	main()