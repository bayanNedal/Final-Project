from person import Person


class Librarian(Person):

    def __init__(self, id, full_name, age, id_no, employment_type):
        super().__init__(id, full_name, age, id_no)
        self.employment_type = employment_type

    librarianList = []

    def LibrariansMenu():

        flag: bool = False

        while (not flag):

            choice = input("\n\tLibrarians Menu\n"
                           "1. Add new librarian\n"
                           "2. Delete librarian\n"
                           "3. View librarian\n"
                           "4. List all librarians\n"
                           "5. Return to main menu\n"
                           "Your choice: ")

            if choice == "1":
                Librarian.AddLibrarian()

            elif choice == "2":
                Librarian.DeleteLibrarian()

            elif choice == "3":
                Librarian.ViewLibrarian()

            elif choice == "4":
                Librarian.ListLibrarians()

            elif choice == "5":
                flag = True

            else:
                print("Enter valid no.")

    def SearchLibrarian(id):

        for librarian in Librarian.librarianList:
            if librarian.id == id:
                return librarian.librarianList.index(librarian)
        return -1

    def AddLibrarian():

        id = input("\nEnter librarian id: ")
        if id.strip() != '' and id.isdigit() and Librarian.SearchLibrarian(id) == -1:
            full_name = input("Enter librarian full name: ")
            if full_name.strip() != '' and full_name.replace(' ', '').isalpha():
                age = input("Enter librarian age: ")
                if age.strip() != '' and age.isdigit():
                    id_no = input("Enter librarian id number: ")
                    if id_no.strip() != '' and id_no.isdigit():
                        emplyment_type = input("Enter librarian emplyment type (Enter 1 or 2):\n"
                                               "1. Full time\n"
                                               "2. Part time\n"
                                               "Emplyment type: ")
                        if emplyment_type == "1":
                            emplyment_type = "Full"

                            newlibrarian = Librarian(id, full_name, age, id_no, emplyment_type)
                            Librarian.librarianList.append(newlibrarian)
                            print("\nLibrarian added successfully\n")

                        elif emplyment_type == "2":
                            emplyment_type = "Part"

                            newlibrarian = Librarian(id, full_name, age, id_no, emplyment_type)
                            Librarian.librarianList.append(newlibrarian)
                            print("\nLibrarian added successfully\n")

                        else:
                            print("\nInvalid input!\n")
                    else:
                        print("\nInvalid input!\n")
                else:
                    print("\nInvalid input!\n")
            else:
                print("\nInvalid input!\n")
        else:
            print("\nInvalid input!\n")

        flag = True


    def DeleteLibrarian():

        librarianId = input("\nEnter the librarian id you want to delete.\n"
                            "id: ")
        index = Librarian.SearchLibrarian(librarianId)
        if index != -1:
            Librarian.librarianList.pop(index)
            print("\nLibrarian deleted successfully\n")
        else:
            print("\n Not found\n")

        flag = True


    def ViewLibrarian():

        id = input("\nEnter a librarian id to view its data\n"
                   "id: ")
        index = Librarian.SearchLibrarian(id)

        if index != -1:
            print("Librarian id\t Librarian name\t Librarian age\t Librarian ID\t Librarian employment type")
            print(Librarian.librarianList[index].id, "\t", Librarian.librarianList[index].full_name, "\t",
                  Librarian.librarianList[index].age, "\t", Librarian.librarianList[index].id_no, "\t",
                  Librarian.librarianList[index].emplyment_type)

        else:
            print("\nInvalid input!")

        flag = True



    def ListLibrarians():

        if len(Librarian.librarianList) > 0:
            print("\nLibrarian id\t Librarian name\t Librarian age\t Librarian ID\t Librarian employment type")
            for librarian in Librarian.librarianList:
                print(librarian.id, "\t", librarian.full_name, "\t", librarian.age, "\t", librarian.id_no, "\t",
                      librarian.emplyment_type)
        else:
            print("\nThere are no registered librarians yet")