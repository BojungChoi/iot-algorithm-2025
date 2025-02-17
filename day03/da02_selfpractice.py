
memory = []
head, current, pre = None, None, None
dataArray = [['최씨'],['김씨'],['황씨'],['이씨'],['박씨']]

class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    if current == None: return
    
    print(current.data, end=' -> ')

    while current.link != None:
        current = current.link
        
        # if current.link() == None:
        #     print(current.data(), end = '')
        # else:
        #     print(current.data(), end=' -> ')

        print(current.data, end=' -> ')

    print()


def makeSimpleLinkedList(namePhone):
    global memory, head, current, pre
    printNodes(head)
    node = Node()
    node.data = namePhone
    memory.append(node)
    
    if head == None : 
        head = node
        return
    
    if head.data[0] :
        node.link = head
        head = node
        return
    
    current = head
    while current.link != None :
        pre = current
        current = current.link()
        if current.data[0] > namePhone[0]:
            pre.link = node
            node.link = current
            return
        
    current.link = node


    
if __name__ == "__main__" :

    for data in dataArray : 
         makeSimpleLinkedList(data)
        
    printNodes(head)




