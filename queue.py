class Queue:
    def __init__(self):
        self.qlist=list()
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return(len(self.qlist)-1)
    def enqueue(self,item):
        self.qlist.append(item)
    def dequeue(self):
        assert not self.isEmpty(),"cannot dequeue from an empty queue."
        data=self.data
        return data
    def display(self):
        return len(self.qlist)
q=Queue()
print("Contents of queue")
print("enqueue operation")
q.enqueue(25 -3)
q.enqueue(50 -2)
q.enqueue(75 -1)
q.enqueue(100 -0)
q.display()
print(q.display())
print("dequeue operation")
print("q.dequeue()","is removed from queue")
print("q.dequeue()","is removed from queue")
print("contents of queue")
