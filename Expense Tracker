# #####################################################################
# PROJECT 5: EXPENSE TRACKER
# #####################################################################

expenses =[ { "item": "burger", "price": 180, "category": "food"} , { "item": "movie", "price": 200, "category": "entertainment"} , { "item": "book", "price": 100, "category": "studies"} ] 

def add_expense():
	item = input(" Enter item Name: ")
	while True:
		try:
			price = int(input(" Enter Price of item: "))
			print("item Price = ", price)
			break
		except:
			print(" Invalid Price! ")
	category = input(" Enter Category: ")
	new_expense = { "item": item , "price": price , "category": category } 
	expenses.append(new_expense)
	print(expenses)
	
def view_expenses():
	print(expenses)
	if expenses == []:
		print(" No expenses found")
	
def search_expense():
	while True:
		search = input(" Enter item name: ").lower()
		for expense in expenses:
			if expense["item"].lower() == search:
				print("Expense Found! ")
				print(expense)
				return 
		else:
				print(" Expense Not found! ")
				

def delete_expense():
	while True:
				search = input(" Enter item name : ")
				for expense in expenses:
					if expense["item"] == search:
						print(" Expense found! ")
						expenses.remove(expense)
						print(" Deleted successfully")
						print(expenses)
						return
				else:
						print(" Expense Not found!")
						
def total_spending():
		total = 0
		for expense in expenses:
			price = expense["price"]
			total += price
			
		print(" Total Expenses is: ", total)
		return
		
def expensive():
		highest = 0
		for expense in expenses:
			if expense["price"] > highest:
				highest = expense["price"]
		print(" Expensive expense is: ", highest)
		
def category():
		while True:
			category = input(" Enter Category of item: ")
			for expense in expenses:
				if category == expense["category"]:
					print(" Expense found! ")
					print(expense)
					return
			
		
		
def save_data():
		with open("expenses.txt" , "w") as file:
			
			for expense in expenses:
				file.write( expense["item"] + "," +  str(expense["price"]) + "," + expense["category"] + "\n" ) 
			print("Data saved successfully! ")
			
def load_data():
		expenses.clear()
		
		with open("expenses.txt" , "r" ) as file:
				for line in file:
					data = line.strip().split(",")
					new_expenses = { "item":  data[0], "price":  int(data[1]),  "category":  data[2] }
					expenses.append(new_expenses)
				print(" Data loaded successfully! ")
				
		

print("#" * 60)
print("                Expense Tracker            ")
print("#" * 60)
while True:
	choice = input(" Enter 1. Add Expense or 2. View Expenses or 3. Search Expense or 4. Delete Expense or 5. Total Spending or 6. Expensive or 7. Show by Category or 8. Save Data or 9. Load Data or 10. Exit: ").lower()
	
	if choice == "1":
		add_expense()
	
	elif choice == "2":
		view_expenses()
		
	elif choice == "3":
		search_expense()
		
	elif choice == "4":
		delete_expense()
		
	elif choice == "5":
		total_spending()
		
	elif choice == "6":
		expensive()
		
	elif choice == "7":
		category()
		
	elif choice == "8":
		save_data()
		
	elif choice == "9":
		load_data()
		
	elif choice == "10":
		print(" Exit Successful! ")
		break
		
	else:
		print(" Invalid choice! ")


