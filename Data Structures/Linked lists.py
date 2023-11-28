#Creating node class
class node:
    def __init__(self,data):
        self.data = data #value for the node
        self.next = None #apoints for the next node

#Creating LinkedList class:
class LinkedList: #Will contain nodes
    def __init__(self):
        self.head = None
        self.tail = None
    
    #Creating insert at the beggining function
    def insert_at_beginning(self,data):
        new_node = node(data)               #Armazenate the value in the new node object
        if self.head:                       #If the list already have a value
            new_node.next = self.head       #new_node.next will be the value that already been in the list
            self.head = new_node            #The new head of the linked list is the new node
        else:                               #If the list dont have any value
            self.tail = new_node            #The new node is the tail and the head of the list
            self.head = new_node
    
    #Creating insert at the end function
    def insert_at_end(self,data):
        new_node = node(data)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node

    #Creating a search method
    def search(self,data):
        current_node = self.head                #indicates the current node as the head
        while current_node:                     #While exists current_node       
            if current_node.data == data:       #If the data in the current node equals to the data there we are searching
                return True                     #return true
            else:                               #If not the new current node is the next node
                current_node = current_node.next 
        return False                            #If we dont match the data while a current node exists return false
        
    #remove at the beginning:
    def remove_at_beginning(self):
        # The "next" node of the head becomes the new head node
        self.head = self.head.next #the next
#Example
sushi_preparation = LinkedList()                    #Initiates sushi preparation as a new empty Linked List
sushi_preparation.insert_at_end("prepare")          #Adds 'prepare' in the end of the list 
sushi_preparation.insert_at_end("roll")             #Adds 'roll' in the end of the list
sushi_preparation.insert_at_beginning("assemble")   #Adds 'assemble' in the beggining of the list
#searching = sushi_preparation.search("roll")        #Search for roll
#print(searching)

searching = sushi_preparation.search("roll")
print(searching)