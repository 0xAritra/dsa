from collections import deque

class Stack:
  def __init__(self):
    self.container = deque()

  def push(self, val):
    self.container.append(val)

  def pop(self):
    return self.container.pop()
  
  def peek(self):
    return self.container[-1]

  def is_empty(self):
    return len(self.container) == 0

  def size(self):
    return len(self.container)

def is_balanced(s):
  st = Stack()
  for c in s:
    if c == "(" or c == "[" or c == "{":
      st.push(c)

    elif c == ")" or c == "]" or c == "}":
      if st.is_empty():
        return False
      else:
        chk = st.peek() + c
        if  chk == "()" or chk == "{}" or chk == "[]":
          st.pop()

  return st.is_empty()

if __name__ == "__main__":
  print(is_balanced("({a+b})"))
  print(is_balanced("))((a+b}{"))
  print(is_balanced("((a+b))"))
  print(is_balanced("))"))
  print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))