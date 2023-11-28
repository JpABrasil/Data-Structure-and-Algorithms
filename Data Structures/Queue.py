#Creating node class
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

#Creating queue class
class Queue:
    def __init__(self):
        self.front = self.rear = None #Initiates the front and the rear of the queue

    #Check if is empty
    def isEmpty(self):
        return self.front == None
            

    #Adding
    def add(self,data):
        new_node = node(data)
        if self.rear == None:                   #If the last node of the queue its equal to none so there arent any nodes in queue
            self.front = self.rear = new_node   #The front and the rear of the queue become the new node
            return                              #Breaks the code 
        else:
            self.rear.next = new_node           #Turns the new node the next node of the last added
            self.rear = new_node                #Turns the new node the last added node

    #Removing
    def remove(self):
        if self.isEmpty():
            return 'Empty Queue its not possible to remove'
        removed_node = self.front               #The removed node its the first added node
        self.front = removed_node.next          #The new front node becomes the node next to the removed one
        if(self.front == None):                 #If we dont have any nodes next to the removed one
            self.rear == None                   #We dont have any nodes

    #Seeing the queue
    def see(self):
        if self.isEmpty():
            return 'Empty Queue you have not to see'
        current_node = self.front
        print('Front')
        while current_node is not None:
            print(current_node.data,)
            current_node = current_node.next
        print('Rear')

#Just Checking
queue = Queue()         
queue.add(30)
queue.add(20)
queue.add(10)
queue.see()
queue.remove()
queue.see()