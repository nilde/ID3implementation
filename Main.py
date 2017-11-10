import Reader


def treeGeneration(data,atributeList,objectiveAtribute,parent=None):

	Tree=Node.Node(parametrosnecesarios) # de momento root,data,childs=[],isLeave=False
	if(TreeFunctions.StoppingCriterion(data)):
		Tree.isLeave=True
		bestLabel=TreeFunctions.assignBestLabel(data)
		Tree.classificationFinal=bestLabel
	else:
		Tree.label,newAttributeList=TreeFunctions.SplitCriterion(data,atributeList,objectiveAtribute)
		for eachPossibleValue in atributeList[Tree.label]:
			subTree=TreeGeneration(TreeFunctions.dataSeparatedByParameter(data,eachPossibleValue),newAttributeList,objectiveAtribute,Tree)
			Tree.child[eachPossibleValue]=subTree.root

	return Tree


def prunningTree(Tree):
	#TODO
	pass

def printTree(Tree):
	#TODO
	pass


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
	print reader.getData()

	#Different methods 
	testSet,trainSet=reader.leaveOneOut()
	#testSet,trainSet=reader.crossValidation(10)
	print testSet
	print trainSet

	if testSet[0] ==[-1]:
		print "Numero de particiones erroneo"
	else:
		fullTree=TreeGeneration(testSet,reader.attributesDomains,reader.attributesDomains[-1])
		print "Generacion del arbol completada"

if __name__=='__main__':
	main()