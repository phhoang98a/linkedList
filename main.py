class Node:
    def __init__(self,new_data):
        self.data = new_data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,new_data):
        global n 
        n = n+1
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
    
    def reverse(self):
        # reverse nua sau cua list: 1-2-3-4-5-6 => 1-2-3-6-5-4
        
        l = (n+1)//2+1
        r = n
        pre = self.head
        for i in range(l-2):
            pre = pre.next
        start = pre.next
        then = start.next
        for i in range(r-l):
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next    
            
    def swap(self):
        #vi du 1->2->3->6->5-4. Chia liên kết đơn thành 2 nửa 1->2->3, 6->5->4
        # Đặt 2 con trỏ first = 1, second =2
        # Tiến hành thay đổi vị tri trong liên kết đơn
        # Ở lượt 1, 1 sẽ được thay đổi liên kết với 6, 6 sẽ được thay đổi liên kết với 2. Sau đó chung ta thay đổi first = 2, second là 5
        # Sau lượt 1 liên kết đơn trở thành 1->6->2->3, 5->4. Tiếp tục cho đến khi first hoặc second là None
        
        first = self.head
        temp = self.head
        for i in range((n-1)//2):
            temp = temp.next
        second =temp.next
        temp.next = None   
        
        while (first!=None and second!=None):
            temp1 = first
            temp2 = second
            first = first.next
            second = second.next
            temp2.next = temp1.next
            temp1.next = temp2
 
llist = LinkedList()
n = 0
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.reverse()
llist.swap()
llist.printList()
