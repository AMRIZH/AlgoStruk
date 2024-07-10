stak = [1,2,3,4,5,6,7,8]
def reverseStack(stack):
    if not stack:
        return
    top_element = stack.pop()
    reverseStack(stack)
    insertAtBottom(stack, top_element)
    
def insertAtBottom(stack, element):
    if not stack:
        stack.append(element)
        return
    top_element = stack.pop()
    insertAtBottom(stack, element)
    stack.append(top_element)

reverseStack(stak)
