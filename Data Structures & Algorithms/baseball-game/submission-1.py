class Solution:
    def calPoints(self, ops: List[str]) -> int:
        new_lst = []
        for i in ops:
            if i == "+":
                new_lst.append(new_lst[-1]+new_lst[-2])
            elif i == "C":
                new_lst.pop()   
            elif i == "D":
                new_lst.append(2*new_lst[-1]) 
            else:
                new_lst.append(int(i))    
        return sum(new_lst)   


        