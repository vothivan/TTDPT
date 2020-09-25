class TrieNode(object):
        def __init__(self,codeword ='',symbol= None,index = 0):
            self.codeword = codeword
            self.symbol = symbol
            self.index = index
class PrefixCodeTree(object):
    def __init__(self):
        self.codeTree = []
    def insert(self,codeword,symbol):
        indexNode = 0
        for i in range(len(codeword)):
            indexNode = indexNode * 2 + codeword[i] + 1
        self.codeTree.append(TrieNode(codeword,symbol,indexNode))
Tree = PrefixCodeTree()
codebook ={
'x1': [0],
'x2': [1,0,0],
'x3': [1,0,1],
'x4': [1,1]
}
for s in codebook:
    Tree.insert(codebook[s],s)
print(Tree.codeTree)