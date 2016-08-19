class SinglyLinkedList( object ):
 
    def __init__( self ):
        self.head , self.tail = None, None
    
    def addToHead( self, el ):
        self.head = Node( el, self.head )
        if None is self.tail:
            self.tail = self.head
 
    def find( self, el ):
        tmp = self.head
        while None != tmp and tmp.data != el:
            tmp = tmp.next
        return tmp
    
    def reverseRecursive(self):
        self._reverseRecursive(self.head)
 
    def _reverseRecursive(self, n):
        right = None
        if None != n:
            right = n.next
            if self.head != n:
                n.next = self.head
                self.head = n
            else:
                n.next = None

            self._reverseRecursive( right )
    
    def show(self):
        print("Showing list data:")
        current_node = self.head
        while current_node is not None:
            print(current_node.data.data, " -> ", end='')
            current_node = current_node.next
        print(None)
            
        

class Node( object ):
 
  def __init__( self, data, next = None ):
    self.data = data
    self.next = next
    
n1 = Node('One')
n2 = Node('Two')
n3 = Node('Three')

s1 = SinglyLinkedList()
s1.addToHead(n1)
s1.addToHead(n2)
s1.addToHead(n3)
s1.show()
s1.reverseRecursive()
s1.show()