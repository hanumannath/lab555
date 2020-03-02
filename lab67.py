list=[9,5,3,9,2,7,5,8,9,1]
for i in range(0,8):
    for j in range(i+1,7):
        if(list[i]==list[j]):
            list.remove(list[j])
print(list)