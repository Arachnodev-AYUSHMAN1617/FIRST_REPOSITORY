importmysql.connector as sqltor

con = sqltor.connect(host = "localhost", user = "root", passwd = "0000", database = "library")
cursor = con.cursor()
ifcon.is_connected():
print('')
else :
print("Sorry \n the problem is being currently resolved")

def __main__():
	print('='*176)
	print("Select from the choices given below(1-3):-\n\t1)DISPLAY BOOKS INFORMATION \n\t2)TO ISSUE A BOOK \n\t3)TO RETURN A BOOK \n\t4)EXIT")
	a = int(input("What do you want to do?"))
	if a==1:
		display_books()
	elif a==2:
		issue_book()
	elif a==3:
		return_book()
	elif a==4:
	exit()
	else:
	print('Please choose from 1,2,3 or 4\n\n')
	__main__()


defdisplay_books():
	total_books=0
	print('\n'+'='*14+' List of Books '+'='*14+'\n')
	print("Showing the information")
	cursor.execute("select * from books ")
	all_books = cursor.fetchall()
	print('BkIDNameofbooks',' '*33,'Author',' '*22, 'Qty',' Category',' '*3,'Publication',' '*17,' Price')
	for book in all_books:
bookID,book_name,author,qty=str(book[0]),str(book[1]),str(book[2]),str(book[3])
	category,publication,price=str(book[4]),str(book[5]),str(book[6])
	print(bookID,' '*(3-len(bookID)),book_name,' '*(44-len(book_name)),author,' '*(29-len(author)),end='')
	print(qty,' '*(3-len(qty)),category,' '*(11-len(category)),publication,' '*(29-len(publication)),price,' '*(9-len(price)))



defissue_book():
	book_genre={1:'educational',2:'adventure',3:'fantasy',4:'horror',5:'comic'}
	total_books=0

	print('\n'+'='*14+' Book Issuing '+'='*14+'\n')
	print("Which type of book do you want to issue ?\n\t1)educational books\n\t2)adventure books\n\t3)fantasy books\n\t4)horror books\n\t5)comic books")
	user_choice = int(input("Enter your choice(1-5):"))
	book_type=book_genre[user_choice]
	ifuser_choice<0 or user_choice>5:
	print('Please choose from 1,2,3 or 5')
	__main__()
	else:
	print("Showing books")
	book_category ="SELECT*from books WHERE Category = '{}'".format(book_type) 
	cursor.execute(book_category)
	all_books_in_category = cursor.fetchall()

	all_books_inlist="SELECT * FROM books;"
	cursor.execute(all_books_inlist)
	all_books = cursor.fetchall()
	for books in all_books:
		total_books+=1

for book in all_books_in_category:
bookID,book_name,author,qty=str(book[0]),str(book[1]),str(book[2]),str(book[3])
			category,publication,price=str(book[4]),str(book[5]),str(book[6])
		print(bookID,' '*(3-len(bookID)),book_name,' '*(44-len(book_name)),author,' '*(29-len(author)),end='')
		print(qty,' '*(3-len(qty)),category,' '*(11-len(category)),publication,' '*(29-len(publication)),price,' '*(9-len(price)))

book_id = int(input("Enter Book Number you want:"))
book_quntity="SELECT Quantity FROM books WHERE BookID={}".format(book_id)
cursor.execute(book_quntity)
x=cursor.fetchone()
quntity_of_book=x[0]

ifbook_id<0 or book_id>total_books:
		print('choose between the book id\'s given')
		__main__()

	elifquntity_of_book==0:
		print('book is not in stock')
		issue_book()

	else:    
		print("Book is available.You can issue it")
		student_name = input("Enter your name:")
		class_section = input("Enter your class and section(eg:12F):")
		roll_no = int(input("Enter your roll number:"))
		date_of_issue = int(input("Enter date of issue(YYYYMMDD):"))

query = "INSERT INTO bookissue(Studentname,BookID,Booktype,DateofISSUE,Rollno)VALUES('{}',{},'{}',{},{})".format(student_name,book_id,book_type,date_of_issue,roll_no)
		cursor.execute(query)
		con.commit()

		update_book_quntity = "UPDATE books SET Quantity = Quantity-1 WHERE BookID = {}".format(book_id)
		cursor.execute(update_book_quntity)
		con.commit()

		print("Successfully issued!!")
		print("Enjoy READING") 


defreturn_book():
book_genre={1:'educational',2:'adventure',3:'fantasy',4:'horror',5:'comic'}
	total_books=0

	print('\n'+'='*14+' Book Returning '+'='*14+'\n')
	print("Which type of book do you want to return ?\n\t1)educational books\n\t2)adventure books\n\t3)fantasy books\n\t4)horror books\n\t5)comic books")
	user_choice = int(input("Enter your choice(1-5):"))
	book_type=book_genre[user_choice]
	ifuser_choice<0 or user_choice>5:
		print('Please choose from 1,2,3 or 5')
		__main__()
	else:
		print("Showing books")
		book_category ="SELECT*from books WHERE Category = '{}'".format(book_type) 
		cursor.execute(book_category)
		all_books_in_category = cursor.fetchall()

		all_books_inlist="SELECT * FROM books;"
		cursor.execute(all_books_inlist)
		all_books = cursor.fetchall()
		for books in all_books:
		total_books+=1


for book in all_books_in_category:
		bookID,book_name,author,qty=str(book[0]),str(book[1]),str(book[2]),str(book[3])
	category,publication,price=str(book[4]),str(book[5]),str(book[6])
	print(bookID,' '*(3-len(bookID)),book_name,' '*(44-len(book_name)),author,' '*(29-len(author)),end='')
	print(qty,' '*(3-len(qty)),category,' '*(11-len(category)),publication,' '*(29-len(publication)),price,' '*(9-len(price)))
	total_books+=1

		book_id = int(input("Enter Book Number you want to return:"))
		quntity_of_book="SELECT Quantity FROM books WHERE BookID={}".format(book_id)
ifbook_id<0 or book_id>total_books:
	print('choose between the book id\'s given')
	 __main__()

	else:    
		student_name = input("Enter your name:")
	class_section = input("Enter your class and section(eg:12F):")
	roll_no = int(input("Enter your roll number:"))
	date_of_return = int(input("Enter date of issue(YYYYMMDD):"))

	query = "INSERT INTO bookreturn(Studentname,BookID,Booktype,DateofRETURN,Rollno)VALUES('{}',{},'{}',{},{})".format(student_name,book_id,book_type,date_of_return,roll_no)
	cursor.execute(query)
	con.commit()

	update_book_quntity = "UPDATE books SET Quantity = Quantity+1 WHERE BookID = {}".format(book_id)
	cursor.execute(update_book_quntity)
	con.commit()

	print("Successfully returned!!")
	print("Try READING a New Book") 

#LIBRARY MANAGMENT USER INTERFACE STARTS 

print('='*176+"\n\t\t\t\t\t\t\t\tWELCOME TO LIBRARY MANAGEMENT\n"+'='*176)
while True:
__main__()
