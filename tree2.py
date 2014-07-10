import sys

class Tree:

  def __init__(self, val=None):
    self.data = val
    self.left = None
    self.right = None

  def insert(self, val):
    if self.data is None:  # First element.
      self.data = val; self.left = None; self.right = None
      return

    if val < self.data:
      if self.left is None: self.left = Tree(val)
      else: self.left.insert(val)
    else:
      if self.right is None: self.right = Tree(val)
      else: self.right.insert(val)

  def lookUp(self, val, parent=None):
    if val < self.data:
      if self.left is None: return None,None
      return self.left.lookUp(val,self)
    elif val > self.data:
      if self.right is None: return None,None
      return self.right.lookUp(val,self)

    else:
      return self,parent    

  def childrenCount(self):
    ctr = 0
    if self.left:  ctr += 1
    if self.right: ctr += 1
    return ctr 

  def depth(self):
    left_depth = self.left.depth() if self.left else 0
    right_depth = self.right.depth() if self.right else 0
    return max(left_depth, right_depth) + 1

  def ldepth(self):
    left_depth = self.left.ldepth() if self.left else 0
    return left_depth+1

  def rdepth(self):

#    if self.right is None:
#      right_depth = 0
#    else:
#      right_depth = self.right.rdepth()

    right_depth = self.right.rdepth() if self.right else 0
    return right_depth+1
 
#  def isBalanced(self):
#    return ldepth(self)
 


  def delete(self,val):
    n,p = self.lookUp(val)
    if n is None:
      print "That node doesn't exist."
      return

    cc = n.childrenCount()
    if cc == 0:  # no children.
      if p:
        if p.left is n: p.left = None
        else: p.right = None
      del n

    if cc == 1:  # 1 child.
      if p:
        if p.left is n:
          if n.left: p.left = n.left
          else:      p.left = n.right
        else:
          if n.left: p.right = n.left
          else:      p.right = n.right
      del n
 
    else:        # 2 children.
      r = n.right
      if r.left:   # the right sub tree has a left child.
        while r.left: # find the leaf on the left subtree.
          p = r
          r = r.left
        n.data = r.data
        del r
        p.left = None
      else:        # the right sub tree has no left child. Therefore the root is the smallest value. 
        n.data = r.data
        n.right = r.right
        del r

  def printTree(self):
    if self.left:  self.left.printTree()
    print self.data
    if self.right: self.right.printTree()
 

def main():
  myList = [5,3,7,9,10,11]
  myTree = Tree()
  for element in myList: myTree.insert(element)
 
  print myTree.ldepth()
  print myTree.rdepth()
  sys.exit()
 
  myTree.printTree()
  sys.exit()
  n,p = myTree.lookUp(5)
  print n.depth()
  sys.exit()
 
if __name__ == '__main__':
  main()
