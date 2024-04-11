list1=[1,2,5,6,7,8,9]
item_to_find=3
def find_element(mylist, item):
    low=0
    high=len(mylist)-1
    while low<=high:
        mid=(low+high)//2
        if mylist[mid] == item:
            return mid
        elif item < mylist[mid]:
            high=mid-1
        else:
            low=mid+1
    return False
print(find_element(list1,item_to_find))
