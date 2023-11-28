#Creating node class
class node:
    def __init__(self,data):
        self.data = data #value for the node
        self.next = None #apoints for the next node

#Creating a class for the stack
class Stack:
    def __init__(self):
        self.top = None #Initiates the top of the stack that will be the last node added

    #Push method
    def push(self,data):
        new_node = node(data)
        if self.top:                    #If the stack its not empty
            new_node.next = self.top    #The next node of the new node  its the top node
        self.top = new_node             #The new node  becomes the top node

    #Pop/Remove
    def pop(self):
        if self.top is None:           #If dont have nodes return none
            return None
        if self.top :                  #If have
            popped_node = self.top     #The popped node must be the top node
            self.top = self.top.next   #The node next to the top node becomes the new top node
            popped_node.next = None    #The popped node will not have next node
            return popped_node.data    #Return the value of the popped node
    
    #Peek method
    def peek(self):
        if self.top is None:           #If dont have data return none
            return None
        if self.top:
            return self.top.data       #If has data return the value of the top node
        
    #Check if it is empty
    def empty(self):
        if self.top is None:
            return "Empty"
        else:
            return "Have Data"
        

 #Just checking       
stack_test = Stack()
stack_test.push("test")
empty_test = stack_test.empty()
print(empty_test)
stack_test.pop()
empty_test = stack_test.empty()
print(empty_test)
    
    #OBS: We cant create LIFOQueue (Structures similiar to stack) with the native librarie 'queue'
    #queue = queue.LifoQueue(maxsize=0) Creates a queue without max size
    #queue.put('...') will add this to the queue