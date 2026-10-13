# average of 3 values 
# def avg(a,b,c):
#     total = a+b+c
#     avg = total/3
#     print(avg)
# avg(2,10,3)


# calculate the lenth of a list by function
# nums =[1,2,3,4,5,6,7]
# def calc_lenth(a):
#     b = len(a)
#     print(b)
# calc_lenth(nums)


# function to print elements of a list in a line
# list =["ramesh","suresh","mahesh","haresh"]
# def printelement(a):
#     b = len(a)
#     i = 0
#     while i<b:
#         print(a[i],end=" ")
#         i+= 1
# printelement(list)


# function to find factorial
# def calc_factorial(n):
#     i=1
#     a =1
#     while i<=n :
#         a *= i
#         i += 1 
#     print(a)
# calc_factorial(11)


#function to convert usd to inr
# def usd_inr(a):
#     inr_value =95*a
#     print( inr_value)
# usd_inr(2)

#function to find odd and even number
# def type_num(a):
#     b = a%2
#     if (b ==0):
#         print("your number is even")
#     else :
#         print("your number is odd")
# type_num(int(input("enter your number :")))

#function to find sum of n numbers with help of recursion
# def sum(n):
#     if(n==0):
#         return 0
#     else:
#         return sum(n-1) + n
# print(sum(5))

# recursive function to print the elements of a list
list = ["raju","ramesh","suresh","mahesh"]
def prt_list(i):
    if(i ==-1):
        return
    else:
        prt_list(i-1)
        return print(list[i])
prt_list(int(len(list))-1)