class Node( object ):
 
  def __init__( self, data, next = None ):
    self.data = data
    self.next = next
    

class SinglyLinkedList( object ):
 
    def __init__( self ):
        self.head = None
		self.tail = None 
    
    def addToHead( self, el ):
        self.head = Node( el, self.head )
        if None is self.tail:
            self.tail = self.head
 
    def find( self, el ):
        tmp = self.head
        while None != tmp and tmp.data != el:
            tmp = tmp.next
        return tmp
    
    def reverse( self ) :
        if None == self.head or None == self.head.next:
          return

        a = self.head
        b = a.next
        c = b.next

        # swaps
        a.next = None
        b.next = a;
        a = b;
        while None != c:
          b = c
          c = c.next
          b.next = a
          a = b

        self.head = b
    
    def show(self):
        print("Showing list data:")
        current_node = self.head
        while current_node is not None:
            print(current_node.data.data, " -> ", end='')
            current_node = current_node.next
        print(None)
            
        


n1 = Node('One')
n2 = Node('Two')
n3 = Node('Three')

s1 = SinglyLinkedList()
s1.addToHead(n1)
s1.addToHead(n2)
s1.addToHead(n3)
s1.show()
s1.reverse()
s1.show()