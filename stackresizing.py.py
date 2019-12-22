class stack:
    def __init__(self,length=3):
        self.stk=[]
        self.length=length

    def isempty(self):
        return len(self.stk)<=0
    def push(self,data):
        if(len(self.stk)>self.length):
            self.resize()
        self.stk.append(data)
        print("stack after push is :",self.stk)

    def pop(self):
        if(len(self.stk))<=0:
            print("stack underflow")
        else:
            self.stk.pop()
            print("stack after pop is:",self.stk)

    def peek(self):
        if(len(self.stk))<=0:
            print("stack underflow")
            return 0
        else:
            return self.stk[-1]

    def size(self):
        return len(self.stk)

    def resize(self):
        newstk=self.stk
        self.length=2*self.length
        self.stk=newstk

    def search(self,value):
        if value in self.stk:
            print("value found in position:",self.stk.index(value))
        else:
            print("value not in stack")
                

            
my=stack()
my.push("2")
my.push("3")
my.push("1")
my.push("4")
my.push("5")
print(my.peek())
print(my.pop())
print(my.size())
my.search("9")
my.search("4")

        
