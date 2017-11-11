import Reader
import Node


def treeGenerationID3(data,attributeList,objectiveAttribute,parent=None):

	Tree=Node.Node(parametrosnecesarios) # de momento root,data,childs=[],isLeave=False
	if(TreeFunctions.StoppingCriterion(data)):
		Tree.isLeave=True
		bestLabel=TreeFunctions.assignBestLabel(data)
		Tree.classificationFinal=bestLabel
	else:
		Tree.label,newAttributeList=TreeFunctions.SplitCriterionID3(data,attributeList,objectiveAttribute)
		for eachPossibleValue in attributeList[Tree.label]:
			subTree=TreeGeneration(TreeFunctions.dataSeparatedByParameter(data,eachPossibleValue),newAttributeList,objectiveAttribute,Tree)
			Tree.child[eachPossibleValue]=subTree.root

	return Tree

def treeGenerationID45(data,attributeList,objectiveAttribute,parent=None):

	Tree=Node.Node(parametrosnecesarios) # de momento root,data,childs=[],isLeave=False
	if(TreeFunctions.StoppingCriterion(data)):
		Tree.isLeave=True
		bestLabel=TreeFunctions.assignBestLabel(data)
		Tree.classificationFinal=bestLabel
	else:
		Tree.label,newAttributeList=TreeFunctions.SplitCriterionID45(data,attributeList,objectiveAttribute)
		for eachPossibleValue in attributeList[Tree.label]:
			subTree=TreeGeneration(TreeFunctions.dataSeparatedByParameter(data,eachPossibleValue),newAttributeList,objectiveAttribute,Tree)
			Tree.child[eachPossibleValue]=subTree.root

	return Tree

	'''
	StoppingCriterion STATUS: DONE
	assignBestLabel STATUS: DONE
	SplitCriterion STATUS: DONE
	dataSeparatedByParameter STATUS: TODO

	'''


def prunningTree(Tree):
	#TODO
	pass

def genTree(node,listNodes):
	if node.level==0:
        if node.level == levelmax:
            return None
        else:
        	for eachNode in node.childs:
        		listNodes.append([eachNode.level,eachNode])
            	self.genTree(eachNode,listNodes)

def printTree(Tree):
	listNodes=[]
	genTree(Tree,listNodes)
	#Some treatement to clean the list generated
	cleanGeneratedList(listNodes)

def cleanGeneratedList(listNodes):



def lastNode(Tree):
	actualNode=Tree.root

	#keep choosing the last child for each level, this automatically gives the last leave of the tree
	while(not actualNode.isLeave):
		actualNode=actualNode.childs[-1]
	return actualNode

def main():
	#modeOfSubstitution=0->delete none values, modeOfSubstitution=1 -> substitute for mean,modeOfSubstitution=2 -> substitute for mode
	modeOfSubstition=0

	reader=Reader.Reader('mushroom.data','mushroomInfo.data',modeOfSubstition)

	#Different methods 
	trainSet,testSet=reader.leaveOneOut()
	#testSet,trainSet=reader.crossValidation(10)
	print testSet

	if testSet[0] ==[-1]:
		print "Numero de particiones erroneo"
	else:
		print reader.canUse
		fullTree=treeGenerationID3(testSet,reader.canUse,reader.canUse[-1])
		print "Generacion del arbol completada"

if __name__=='__main__':
	main()