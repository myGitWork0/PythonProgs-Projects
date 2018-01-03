a=[10.6,20.7,30.4,40.7,50.98,60.78]
b=10
big=a[0]
second_big=a[1]
if big < second_big :
    temp=big
    big=second_big
    second_big=temp
a.remove(a[0])
a.remove(a[0])
print(a)
while(len(a)>0):
    if big < a[0] :
            second_big = big
            big=a[0]
    elif second_big < a[0] :
        second_big=a[0]
    a.remove(a[0])
del(a)
print("%1.5f is the biggest number and %.3f is second biggest number"%(big,second_big))







