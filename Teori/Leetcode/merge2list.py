list1 = [2,4,5]
list2 = [1,2,4,5]
def mergeTwoLists(list1, list2):
    for i in list2 :
        list1.append(i)
    print(sorted(list1))