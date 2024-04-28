def change(amount):
    """Prints the number of coins of each type required to make the given amount of change
    amount: The amount to return, in cents. Must be an integer multiple of 5."""
    print("$",format(amount/100,".2f"),sep="")
    toonies = amount // 200
    amount = amount % 200
    loonies = amount // 100
    amount = amount % 100
    quarters = amount // 25
    amount = amount % 25    
    dimes = amount // 10
    amount = amount % 10  
    nickels = amount // 5
    print("Toonies:",toonies)
    print("Loonies:",loonies)
    print("Quarters:",quarters)
    print("Dimes:",dimes)
    print("Nickels:",nickels)
    
