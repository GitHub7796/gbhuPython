class tree:
    data=""
    child_tree={}
    def __init__(self,data):
        self.data=data
    def addChild(self,cTree):
        print(cTree.data)
        self.child_tree[cTree.data]=cTree
        print(self.child_tree)
    def to_dict(self):

        return {
            'data': self.data,
            'child_tree': {
                }
        }
    def __repr__(self, level=0):
        indent = "  " * level
        result = f"{indent}{self.data}\n"
        print(self.child_tree)
        if self.child_tree=={}:
            return
        for child in self.child_tree.values():
            result += child.__repr__(level + 1)
        return result
child_tree1=tree('child1')
child_tree2=tree('child2')
parent_tree=tree('parent')
parent_tree.addChild(child_tree1)
parent_tree.addChild(child_tree2)