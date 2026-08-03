class MinStack:

    def __init__(self):
        self.st=[]
        self.mini=float('inf')

    def push(self, value: int) -> None:
        self.mini=min(self.mini,value)
        self.st.append([value,self.mini])
        

    def pop(self) -> None:
        self.st.pop()
        if self.st:
            self.mini=self.st[-1][1]
        else:
            self.mini=float('inf')

    def top(self) -> int:
        return self.st[-1][0]
        

    def getMin(self) -> int:
        return self.st[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()