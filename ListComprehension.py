# 1.	Flatten the nested list [[1, 2], [3, 4], [5, 6]] into a single list.

l=[[1,2],[3,4],[5,6]]
res=[j for i in l for j in i]
print(res)

#output: [1, 2, 3, 4, 5, 6]

# 2.	From a nested list [[2, 5], [7, 9], [12, 15]], extract all even numbers.

l=[[2, 5], [7, 9], [12, 15]]
res=[j for i in l for j in i if j%2==0]
print(res)

#output:[2, 12]

# 3.	Create a list of squares for numbers from 1 to 20.

res=[i**2 for i in range(1,21)]
print(res)

#output:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]

# 4.	Print prime numbers between 10 to 20 using list comprehension?

res= [ i for i in range(10,21) if all(i%j!=0 for j in range(2,i))]
print(res)

#output: [11, 13, 17, 19]

# 5.	Convert a=10 int data type to 10 string data type  with out using str()?

a=10
res=""
b = "0123456789"
while a>0:
    digit= a%10
    a//=10
    for i in range(len(b)):
        if digit==i:
            res= b[i]+res
print(f"Converting int to str without using str() {type(res)}")

#output: Converting int to str without using str() <class 'str'>

# 6.	Write a Python program to swap the case of each character in a given string without using the built-in swapcase() method

s="MounIKA"
swap_case=""
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
for i in s:
    if i in upper:
        pos=upper.index(i)
        swap_case+=lower[pos]
    elif i in lower:
        pos1=lower.index(i)
        swap_case+=upper[pos1]
print(swap_case)

#output: mOUNika

# 7.	Write a list comprehension to print only the word 'python' from the list. S=["python" ,"java", "c++","developer"]

s=[ "python","java", "c++","developer" ]
res=[i for i in s if i=="python"]
print(res)

#output: ['python']






