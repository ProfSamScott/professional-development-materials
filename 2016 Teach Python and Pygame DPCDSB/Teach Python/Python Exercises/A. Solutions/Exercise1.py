"""Solution to exercise 1 from the chapter 2 handout
Sam Scott, January 2015"""

print("Product Name?")
pname = input()
print("How much does a",pname,"cost?")
price = float(input())

total = price * 1.13

print("The total cost of a ",pname," including HST will be $",total,sep="")