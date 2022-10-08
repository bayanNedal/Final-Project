from book import Book
from client import Client
from librarian import Librarian
from borrowing_order import BorrowingOrder



def MainMenu():

        choice = input("\t-----------------"
                       "\n\tMain Menu\n"
                       "\t-----------------\n"
                       "1. Clients Menu\n"
                       "2. Librarian Menu\n"
                       "3. Books Menu\n"
                       "4. Borrowing Orders Menu\n"
                       "5. Exit \n"
                       "Enter no. of your choice: ")

        if choice == "1":
            Client.ClientsMenu()
            MainMenu()

        if choice == "2":
            Librarian.LibrariansMenu()
            MainMenu()

        elif choice == "3":
            Book.BooksMenu()
            MainMenu()

        elif choice == "4":
            BorrowingOrder.OrdersMenu()
            MainMenu()

        elif choice == "5":
            exit("** See you again :) **")

        else:
            print("Enter valid no.")
            MainMenu()

MainMenu()