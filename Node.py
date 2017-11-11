#Reescribir la clase para que sea interBD

class Node:
	def __init__(self,parent,atribute,dataNode,actualEntropy,atributeName,isLeave=False):
		self.parent=parent
        self.connectionName=atributeName
        self.childs={}
        self.actualEntropy=actualEntropy
        self.differentCharacteristics=dataCharacteristics
        self.ownData=dataNode
        self.isLeave=False
        self.level=0
        self.classificationFinal=None
        self.root=self.parent.root

    def setLevel(self):
       self.level = self.parent.level+1


    #TODO define some methods























		

