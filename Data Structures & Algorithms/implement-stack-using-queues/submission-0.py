class MyStack:
   
    def __init__(self):
        self.lst = [] 
        

    def push(self, x: int) -> None:
        self.lst.append(x)
        

    def pop(self) -> int:
        if not self.empty():
            return self.lst.pop()  
        else:
            raise IndexError("Pop from empty stack")

        

    def top(self) -> int:
        if not self.empty():
            return self.lst[-1]  # return top element without removing
        else:
            raise IndexError("Top from empty stack")
        

    def empty(self) -> bool:
         return len(self.lst) == 0     
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()