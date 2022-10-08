from person import Person


class Client(Person):

    def __init__(self, id, full_name, age, id_no, phone_number):
        super().__init__(id, full_name, age, id_no)
        self.phone_number = phone_number


    clientList = []


    def ClientsMenu():

        flag:bool = False
        while (not flag):

            choice = input("\n\tClients Menu\n"
                           "\t ----------------------\n"
                           "1. Add new client\n"
                           "2. Delete client\n"
                           "3. View client\n"
                           "4. List all clients\n"
                           "5.  Main menu\n"
                           "Enter no. of your choice: ")

            if choice == "1":
                Client.AddClient()

            elif choice == "2":
                Client.DeleteClient()

            elif choice == "3":
                Client.ViewClient()

            elif choice == "4":
                Client.ListClients()

            elif choice == "5":
                flag = True

            else:
                print("Enter valid no.")


    def SearchClient(id):

        for client in Client.clientList:
            if client.id == id:
                return Client.clientList.index(client)
        return -1


    def AddClient():

        id = input("\nEnter client id: ")
        if id.strip() != '' and id.isdigit() and Client.SearchClient(id) == -1:
            full_name = input("Enter client full name: ")
            if full_name.strip() != '' and full_name.replace(' ', '').isalpha():
                age = input("Enter client age: ")
                if age.strip() != '' and age.isdigit():
                    id_no = input("Enter client id number: ")
                    if id_no.strip()!= '' and id_no.isdigit():
                        phone_number = input("Enter client phone number: ")
                        if phone_number.strip() != '' and phone_number.isdigit():

                            newClient = Client(id, full_name, age, id_no, phone_number)
                            Client.clientList.append(newClient)
                            print("\nClient added successfully\n")

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



    def DeleteClient():

        clientId = input("\nEnter the client id you want to delete.\n"
                         "id: ")
        index = Client.SearchClient(clientId)
        if index != -1:
            Client.clientList.pop(index)
            print("\nClient deleted successfully\n")
        else:
            print("\nNot found\n")

        flag = True



    def ViewClient():

        id = input("\nEnter a client id to view its data\n"
                   "id: ")
        index = Client.SearchClient(id)
        if index != -1:
            print("\nClient id || Client name || Client age || Client ID || Client phone number")
            print(Client.clientList[index].id, "||", Client.clientList[index].full_name, "||",
                  Client.clientList[index].age, "||", Client.clientList[index].id_no, "||",
                  Client.clientList[index].phone_number)

        else:
            print("\nInvalid input!")

        flag = True


    def ListClients():

        if len(Client.clientList) > 0:
            print("\nClient id\t Client name\t Client age\t Client ID\t Client phone")
            for client in Client.clientList:
                print (client.id, "\t", client.full_name, "\t", client.age, "\t", client.id_no, "\t", client.phone_number)
        else:
            print("\nThere are no registered clients yet")