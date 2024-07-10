def stackReverse(stack : list):
  if not stack :
      return
  top_element = stack.pop()
  stackReverse(stack)
  putAtBottom(stack, top_element)
    
def putAtBottom(stack : list,element):
  if not stack :
    stack.append(element)
    return
  top_element = stack.pop()
  putAtBottom(stack, element)
  stack.append(top_element)
        
stak = [1,2,3,4,5,6,7,8]
stackReverse(stak)
print(stak)

def stackreversed(stack):
  if not stack :
    return
  top_element = stack.pop()
  stackreversed(stack)
  insertAtbottom(stack)

def insertAtbottom(stack,element):
  if not stack:
    stack.append(element)
    return
  top_element = stack.pop()
  insertAtbottom(stack,element)
  stack.append(top_element)