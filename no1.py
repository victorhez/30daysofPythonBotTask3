#Python Program that finds numbers which are divisible by 7  and mutiple of 5, between 1500 to 2700


small=1500
big=2700

for i in range(1500,2700):
    if(i %7 ==0 & i %5==0):
        print(i)


