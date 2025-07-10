n=int(input())
li=[]
for i in range(n):
    ele=int(input())
    li.append(ele)
def reverse_list(li):
    s=0
    e=len(li)-1;
    while s<e:
        temp=li[s]
        li[s]=li[e]
        li[e]=temp
        s=s+1
        e=e-1
def print_list(li):
    for i in li:
        print(i,end=" ")
def sum_avg(li):
    s=0
    for i in li:
        s+=i
    print("\nsum: ",s)
    print("Average: ",s/len(li))
print_list(li)
reverse_list(li)
sum_avg(li)