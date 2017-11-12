class Node:
    def __init__(self,parent,dataNode,actualEntropy,connectionName,isLeave=False,root=None,finalClassification='No'):
        self.parent=parent
        self.childs={}
        self.dataNode=dataNode
        self.actualEntropy=actualEntropy
        self.isLeave=False
        self.connectionName=connectionName
        self.level=0
        self.root=root
        self.label=None
        self.finalClassification=finalClassification
        self.setLevel()

    def setLevel(self):
        if self.parent == None:
            self.level=0
        else:
            self.level = self.parent.level+1

    def setRoot(self):
        self.root=self.parent.root

    def autoParent(self):
        self.parent=self