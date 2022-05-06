from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    a=nums
    length=len(a)
    l=[0]*length
    r=[0]*length

    l[0]=1             #since there is no element to the left of the first element we keep it's left product as 1

    for i in range(1,length):
        l[i]=l[i-1]*a[i-1]

    '''Ex: take i=1 the left product at i=1 is product of all elements
    to the left of it. Since we have the left product of the
    previous element already stored in the list l we multiply
    it with the element at i-1.'''

    r[length-1]=1       #since there is no element to the right of the last element.

    for i in reversed(range(length-1)):
        r[i]=r[i+1]*l[i+1]
        #same logic as above but in reverrse order

    #calculating the individual product
    for i in range(length):
        r[i]*=l[i]
    print(r)



print(productExceptSelf([1, 2, 3, 4]))
