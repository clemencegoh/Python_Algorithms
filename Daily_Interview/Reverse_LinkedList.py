# Reverse Linked list
# Node class  
class Node: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # Function to reverse the linked list
    # Note: iterative method 
    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 

    # recursive reverse method
    def reverseUtil(self, curr, prev): 
        # If last node mark it head 
        if curr.next is None : 
            self.head = curr  
              
            # Update next to prev node 
            curr.next = prev 
            return 
          
        # Save curr.next node for recursive call 
        next = curr.next
  
        # And update next  
        curr.next = prev 
        self.reverseUtil(next, curr)  
  
  
    # This function mainly calls reverseUtil() 
    # with random as None 
    def reverse_recur(self): 
        if self.head is None: 
            return 
        self.reverseUtil(self.head, None) 


    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data) 
            temp = temp.next


# Driver program to test above functions 
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(85) 
  
print("Given Linked List")
llist.printList() 
llist.reverse() 
print("\nReversed Linked List")
llist.printList() 