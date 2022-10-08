from book import Book
from client import Client
from librarian import Librarian
from datetime import date


class BorrowingOrder:

    def __init__(self, id, date, client_id, book_id, librarian_id, status):
        self.id = id
        self.date = date
        self.client_id = client_id
        self.book_id = book_id
        self.librarian_id = librarian_id
        self.status = status


    ordersList = []

    counter = 0

    def OrdersMenu():

        flag :bool= False
        while (not flag):

            choice = input("\n\t Borrowing Orders Menu:\n"
                           "\t --------------------------------------\n"
                           "1. Borrow a book\n"
                           "2. Return a book\n"
                           "3. Cancel order\n"
                           "4. View order\n"
                           "5. List client orders\n"
                           "6. List all orders\n"
                           "7. Total borrowed orders\n"
                           "8. Main menu\n"
                           "Enter no. of your choice: ")

            if choice == "1":
                BorrowingOrder.BorrowBook()

            elif choice == "2":
                BorrowingOrder.ReturnBook()

            elif choice == "3":
                BorrowingOrder.CancelOrder()

            elif choice == "4":
                BorrowingOrder.ViewOrder()

            elif choice == "5":
                BorrowingOrder.ClientOrders()

            elif choice == "6":
                BorrowingOrder.ListOrders()

            elif choice == "7":
                BorrowingOrder.TotalOrders()

            elif choice == "8":
                flag = True

            else:
                print("Enter valid no.")


    def SearchOrder(id):

        for order in BorrowingOrder.ordersList:
            if order.id == id:
                return BorrowingOrder.ordersList.index(order)
        return -1


    def ActiveOrders():

        print("\nActive orders: ")
        print("\nBorrowing id\t  Order date\t Client id\t Book id\t Librarian id\t Status")
        for order in BorrowingOrder.ordersList:
            if order.status == "Active":
                print(order.id, "\t", order.date, "\t", order.client_id, "\t", order.book_id,
                      "\t", order.librarian_id, "\t", order.status)

    def BorrowBook():

        librarian_id = input("\nEnter your librarian id: ")
        librarianIndex =Librarian.SearchLibrarian(librarian_id)
        if librarianIndex != -1:
            Book.ActiveBooks()
            book_id = input("\nEnter book id you want to borrow: ")
            bookIndex = Book.SearchBook(book_id)
            if bookIndex != -1:
                if Book.bookList[bookIndex].status == "Active":
                    client_id = input("\nEnter client id: ")
                    if Client.SearchClient(client_id) != -1:
                        id = str(BorrowingOrder.counter + 1)
                        BorrowingOrder.counter = BorrowingOrder.counter + 1
                        orderDate = date.today()
                        status = "Active"

                        newOrder = BorrowingOrder(id, orderDate, client_id, book_id, librarian_id, status)
                        BorrowingOrder.ordersList.append(newOrder)
                        print("\nSuccess\n")

                        Book.bookList[bookIndex].status = "Inactive"


                    else:
                        print("\nNot found")
                else:
                    print("\nInactive book")
            else:
                print("\nNot found")
        else:
            print("\nNot found")

        flag = True


    def ReturnBook():

        BorrowingOrder.ActiveOrders()
        borrowing_id = input("\nEnter borrowing id you want to return:\n"
                             "Borrowing id: ")
        index = BorrowingOrder.SearchOrder(borrowing_id)
        if index != -1:
            BorrowingOrder.ordersList[index].status = "Expired"
            book_index = Book.SearchBook(BorrowingOrder.ordersList[index].book_id)
            Book.bookList[book_index].status = "Active"
            print("\nSuccess\n")
        else:
            print("\nNot found\n")

        flag = True

    def CancelOrder():

        BorrowingOrder.ActiveOrders()
        borrowing_id = input("\nEnter borrowing id you want to cancel:\n"
                             "Borrowing id: ")
        index = BorrowingOrder.SearchOrder(borrowing_id)
        if index != -1:
            BorrowingOrder.ordersList[index].status = "Canceled"
            book_index = Book.SearchBook(BorrowingOrder.ordersList[index].book_id)
            Book.bookList[book_index].status = "Active"
            print("\nSuccess\n")
        else:
            print("\nNot found\n")

        flag = True


    def ViewOrder():

        borrowing_id = input("\nEnter a borrowing id to view its data\n"
                   "Borrowing id: ")
        index = BorrowingOrder.SearchOrder(borrowing_id)

        if index != -1:
            print("\nBorrowing id\t  Order date\t Client id\t Book id\t Librarian id\t Status")
            print(BorrowingOrder.ordersList[index].id, "\t", BorrowingOrder.ordersList[index].date, "\t",
                  BorrowingOrder.ordersList[index].client_id, "\t", BorrowingOrder.ordersList[index].book_id, "\t",
                  BorrowingOrder.ordersList[index].librarian_id, "\t", BorrowingOrder.ordersList[index].status)

        else:
            print("\nInvalid input!")

        flag = True

    def ListOrders():

        if len(BorrowingOrder.ordersList) > 0:
            print("\nBorrowing id\t  Order date\t Client id\t Book id\t Librarian id\t Status")
            for order in BorrowingOrder.ordersList:
                print(order.id, "\t", order.date, "\t", order.client_id, "\t", order.book_id,
                      "\t", order.librarian_id, "\t", order.status)
        else:
            print("\nNo registered orders yet")


    def TotalOrders():

        active, expired, canceled = 0, 0, 0
        for order in BorrowingOrder.ordersList:
            if order.status == "Active":
                active = active + 1
            elif order.status == "Expired":
                expired = expired + 1
            else:
                canceled = canceled + 1

        print("\nTotal active orders = ", active,
              "\nTotal expired orders = ", expired,
              "\nTotal canceled orders = ", canceled)


    def ClientOrders():

        id = input("\nEnter client id: ")
        index = Client.SearchClient(id)
        if index != -1:
            print("\nBorrowing id ||  Order date || Client id ||Book id || Librarian id ||  Status")
            for order in BorrowingOrder.ordersList:
                if order.client_id == id:
                    print(order.id, "||", order.date, "||", order.client_id, "||", order.book_id,
                          "||", order.librarian_id, "||", order.status)