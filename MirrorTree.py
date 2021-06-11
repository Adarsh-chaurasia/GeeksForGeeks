class Solution:
    def MirrorTree(self, root: TreeNode):
        if root is None:
            return 
        else:
            temp=root
            self.MirrorTree(root.left)
            self.MirrorTree(root.right)
            temp=root.left
            root.left=root.right
            root.right=temp
            
            
        return root
