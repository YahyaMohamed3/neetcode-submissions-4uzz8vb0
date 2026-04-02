class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")" : "(", "}" : "{", "]" : "["}
        stack = []
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack



"""
ok so let me see if i understand so we start by mapping closers to openers
and we create a stack last in first out why a stack because brackets have to close
in reverse order of how they opened. the most recnelty opened bracket must close 
first thats why stack is good last thing pushed first thing chdcked lifo a queue
or an array without LIFO property wouldn't naturally enforce that ordering

then we loop over each char in the string if the char is in c 
that means its a closer.
so then we check is our stack contains the opener if there is nothing 
in our stack we return false

if there is something in our stack we check the top of the stack -1 index 
if its
eqaul to our bracket closer if it is pop it from the stack
if c is not in our closers (keys) we appened it to the stack means its in 
a openner.

once we break out of the loop if there is nothing in the stack return True 
if there is something return flase somehting didnt have a much 

"""



        