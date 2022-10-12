# Program to sort array of 0,1,2
# sorting array of 0,1,2
def sort_arr(a):
    l = len(a)
    low = 0
    mid = 0
    high = l-1
    while mid <= high:
        if a[mid] == 0:
            a[mid],a[low] = a[low],a[mid]
            mid+=1
            low+=1
        elif a[mid] == 1:
            mid+=1

        elif a[mid] == 2:
            a[mid],a[high] = a[high],a[mid]
            high-=1


    return a






a = [2,0,1,2,1,1]
# a = [0,1,1,0,1,2,1,2,0,0,0,1]
res = sort_arr(a)
print(res)
