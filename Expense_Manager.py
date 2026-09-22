#Writing a code to track the personal expenses.
import time

date=[]
category=[]
expenses=[]


print("-------Expense Manager---------")
time.sleep(1)
print("\nThe Expense Manager is a simple Python application designed to help users record, manage, and monitor their daily expenses.",
      "\nThe application allows users to add expenses with details such as the date, category, and amount.",
      "\nIt also provides useful summaries, including total expenses, the highest expense, the lowest expense, and average spending.")
print("\nYou will be asked to insert three items.\n1. Date for the expense made","\n2. The category of Expense","\n3. The amount of the expense in US$.")
print("\nFew examples of the categories: \na.Housing\nb.Loans\nc.Insurance\nd.Investment\ne.Public Transportation\nf.Grocery\ng.Leisure\ni.Hospitals")
time.sleep(1)
print("\nWhat do you want to do?")
print("\n1.To add a new expense press 1\n2.To remove an expense press 2\n3.To display the all the expenses press 3\n4.To display summary calculation press 4.")
time.sleep(1)
while True:
    print("\n1. Add | 2. Remove | 3. Display | 4. Summary")
    m=int(input("\nState your choice: "))
    if m==1:       
        dt=input("\nEnter the date on which the expense was incurred in DD/MM/YY format: ")
        catg=input("Enter the category of the expense: ")
        exp=int(input("Enter the expense amount in US$: "))
        date.append(dt)
        category.append(catg)
        expenses.append(exp)
    elif m==2:
        rm=int(input("Insert the Expense ID or Exp_ID of the expense you would like to remove: "))
        dt_rm=date.pop(rm-1)
        catg_rm=category.pop(rm-1)
        exp_rm=expenses.pop(rm-1)
    elif m==3:
        print("\nHere is the summary of the expenses: ")
        print("Exp_ID     Date     Category     Expense")
        print("------------------------------------------")
        for i in range(len(date)):
            print((i+1),"\t",date[i],"\t",category[i],"\t",expenses[i])
    elif m==4:
        Total=(sum(expenses))
        min_exp=min(expenses)
        max_exp=max(expenses)
        Avg_exp=Total/len(date)
        min_idx=expenses.index(min_exp)
        max_idx=expenses.index(max_exp)
        print("\n--------Here is your summary--------")
        print("\nThe total expenses from",date[0],"to",date[(len(date)-1)],"is: $",Total)
        print("\nThe lowest expense of: $",min_exp, "was made on:", date[min_idx], "for:", category[min_idx])
        print("\nThe highest expense of: $",max_exp, "was made on:", date[max_idx], "for:", category[max_idx])
        print("\nThe average of the expenses made during the period is: $",Avg_exp)
    else:
        print("\nInvalid Choice ! Please select a valid choice: ")
    z=int(input("\n\nDo you want to continue?\nPress 0 to Exit. Press 1 to Continue: "))
    if z==0:
        time.sleep(1)
        print("Thank you for using the expense manager.\nClosing the application")
        break