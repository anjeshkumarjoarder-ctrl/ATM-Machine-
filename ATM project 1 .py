Money = 0

def Display_Balance():
    while True :
        if Money == 0 :
            print("Balance Nil")
        else :
            print("Balance :",Money)
        break


#^ Display Balance 1

def Withdraw_Money() :
    global Money
    while True :
        Amount = int(input("enter the amount :"))
        if Amount > Money :
            print("Paise Kaam hai Dost")
            
        else :
            Money = Money - Amount 
            print("Money Withdrawn",Money)
            print("Available Balance :",Money)
            break
        

#^ Withdraw Money 2

def Deposit_Money() :
    global Money
    while True :
       Amount = int(input("enter the money :"))
       if Amount > 0 :
           Money = Money + Amount 
           print("Money Deposited :",Amount)
           print("Available Balance :",Money)
           break
       else :
           print("Money Cannot Deposited")


#^ deposit money 3


def Statement() :
    print("\n-----Statement-----")
    print("Money Withdrawn :",Money)
    print("Money Deposited :",Money)
    print("Available Balance :",Money)

#^ statement 4

def Atm () :
    while True :
        print("\n1.Display Balance")
        print("2.Withdraw Money")
        print("3.Deposit Money")
        print("4.Statement")
        print("5.exit")

        choice = int(input("enter the choice :"))
        if choice == 1 :
            Display_Balance()
        elif choice == 2 :
            Withdraw_Money()
        elif choice == 3 :
            Deposit_Money()
        elif choice == 4 :
            Statement()
        elif choice == 5 :
            print("Thank you")
            break
        else :
            print("Invalid choice")
            break
        
Atm()

