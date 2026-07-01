#Expense Tracker Project

expensesList = [] #list of expenses in form of dictionary
print("Welcome To Expense Tracker")

while True:
    print("====== MENU ======")
    print("1.Add Expense")
    print("2.View All Expense")
    print("3.View Total Kharcha")
    print("4.Exit")

    choice = int(input("Please Enter Your Choice :"))

#Add Expense
    if(choice == 1):
        date = input("Enter Date :")
        category = input("Enter The Category(Food,Travel,Books,Others) : ")
        description = input("Enter Description :")
        amount = float(input("Enter Amount :"))

        expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount,
        }
        expensesList.append(expense)
        print("\nExpense Is Added Successfully")

#View All Expense
    elif(choice == 2):
        if(len(expensesList) == 0):
            print("No Expenses Added. ")
        else:
            print("===== Ye Hai Apka Kharcha =====")
            count = 1
            for eachKharcha in expensesList:
                print(f"Kharcha Number{count} : {eachKharcha["date"]},{eachKharcha["category"]},{eachKharcha["description"]},{eachKharcha["amount"]}")
                count = count + 1

#View Total Spending
    elif(choice == 3):
        total = 0
        for eachKharcha in expensesList:
            total = total + eachKharcha["amount"]
        print("\nTotal Amount : ",total)

#Exit
    elif(choice == 4):
        print("Thank You For Use My System")
        break
    else:
        print("Invalid Choice, Try Again")
        
