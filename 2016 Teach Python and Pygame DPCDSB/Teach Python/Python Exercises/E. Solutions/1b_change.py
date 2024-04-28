def change(amount):
    """Prints the number of coins of each type required to make the given amount of change
    amount: The amount to return, in cents. Must be an integer multiple of 5."""
    print("$",format(amount/100,".2f")," can be made with: ",sep="",end="")
    toonies = amount // 200
    amount = amount % 200
    loonies = amount // 100
    amount = amount % 100
    quarters = amount // 25
    amount = amount % 25    
    dimes = amount // 10
    amount = amount % 10  
    nickels = amount // 5
    if toonies > 0:
        if toonies == 1:
            print("1 toonie ",end="")
        else:
            print(toonies,"toonies ",end="")
    if loonies > 0:
        if loonies == 1:
            print("1 loonie ",end="")
        else:
            print(loonies,"loonies ",end="")
    if quarters > 0:
        if quarters == 1:
            print("1 quarter ",end="")
        else:
            print(toonies,"quarters ",end="")
    if dimes > 0:
        if dimes == 1:
            print("1 dime ",end="")
        else:
            print(dimes,"dimes ",end="")
    if nickels > 0:
        if nickels == 1:
            print("1 nickel ",end="")
        else:
            print(nickels,"nickels ",end="")


    
