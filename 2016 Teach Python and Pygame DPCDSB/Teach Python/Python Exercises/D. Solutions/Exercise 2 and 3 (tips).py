def tip(amount, percent):
    """Displays the tip for the given amount using the given percentage"""
    tip_amount = amount * percent / 100
    print("A ",percent,"% tip on $",format(amount,'.2f')," would be $",format(tip_amount,'.2f'), sep="")
    
def tip_calculator():
    amount = float(input("Enter the amount of the check: "))
    tip_percent = float(input("Enter the tip percentage: "))
    tip(amount, tip_percent)
    
# main program
tip_calculator()