#if sum == 15 to 20 it will show 20
try:
    _1st=int(input("Enter first Number:>>>"))
    _2nd=int(input("Enter second Number:>>>"))
    sum=_1st+_2nd
    if(sum <=15 & sum>= 20):
        print(20)
    else:
        print(sum)
except:
    print("Enter number not Alphabet or String")
#good