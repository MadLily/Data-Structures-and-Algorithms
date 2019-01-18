# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False



if __name__ == "__main__":
    text = sys.stdin.read()

#    opening_brackets_stack = []
#    opening_brackets_stack2 = [0]
#    pos = 0
#    for i, next in enumerate(text):
##        print(opening_brackets_stack)
#
#        if next == '(' or next == '[' or next == '{':
#            # Process opening bracket, write your code here
#            opening_brackets_stack.append(next)
#            opening_brackets_stack2.append(i)
#            pos += 1
#
#        if next == ')' or next == ']' or next == '}':
#            # Process closing bracket, write your code here
#            if len(opening_brackets_stack)>0:
#                b = Bracket(opening_brackets_stack[-1],opening_brackets_stack2[-1])
#                if b.Match(next):
#                    opening_brackets_stack.pop()
#                    opening_brackets_stack2.pop()
#                    pos -= 1
#                else:
#                    print (i+1)
#                    sys.exit()
#            else:
#                print (i+1)
#                sys.exit()
#    if pos==0:
#        print("Success")
#    else:
#       print(opening_brackets_stack2[-1]+1)
    opening_brackets_stack = []
    pos = 0
    for i, next in enumerate(text):
        #        print(opening_brackets_stack)
        
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            pos += 1
        
        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if len(opening_brackets_stack)>0:
                b = Bracket(opening_brackets_stack[-1],opening_brackets_stack2[-1])
                if b.Match(next):
                    opening_brackets_stack.pop()
                    opening_brackets_stack2.pop()
                    pos -= 1
                else:
                    print (i+1)
                    sys.exit()
            else:
                print (i+1)
                sys.exit()
    if pos==0:
        print("Success")
        else:
            print(opening_brackets_stack2[-1]+1)

