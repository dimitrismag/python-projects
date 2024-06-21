import json

class Transaction:
    def __init__(self, title, amount, type, note =""):
        self.title = title
        self.amount = amount
        self.type = type
        self.note = note

    def display(self):
        return f'Transaction:\n Expense: {self.title}\n Amount: {self.amount}\n Type: {self.type}\n Note:{self.note}\n'
    
class Bank:
    def __init__(self):
        self.wallet = []

    def add_transaction(self, transaction):
        self.wallet.append(transaction)

    def del_trans(self,title):
        for trans in self.wallet:
            if trans.title == title:
                self.wallet.remove(trans)
                return f'{title} has been removed'
        return f'{title} you look was not found'     
        
    def display(self):
        if not self.wallet:
            return f'No transactions in your wallet'
        return f'\n'.join([transaction.display() for transaction in self.wallet])
    
    def search(self,query):
        found = [trans for trans in self.wallet if query.lower() in trans.title or  query.lower() in trans.type]
        if not found:
            return f' No transactions like that found'
        return f'\n' .join([transaction.display() for transaction in found])
    
    def save(self, filename ="wallet.json"):
        data = [{"Expense": transaction.title, "Amount":transaction.amount, "Type":transaction.type, "Note:":transaction.node} for transaction in self.wallet]
        with open(filename, 'w') as file:
            json.dump(data ,file)


def main():
    wallet = Bank()
    while True:
        print("\n YOUR PERSONAL BANKING SYSTEM")
        print("1. add a transaction")
        print("2. remove transaction")
        print("3. display a transaction")
        print("4. search a transaction")
        print("5. save a transaction")
        print("6. exit")
        choise = input("pick an option (1-6): ")

        if choise =="1":
            title = input("Enter the title: ")
            amount: int =input("Enter amount: ")
            type = input("Expense or deposit?: ")
            transaction=Transaction(title,amount,type)
            wallet.add_transaction(transaction)
            print("succesfully added") 

        elif choise =="2":
            title = input("Enter the title")
            print(wallet.del_trans(title))

        elif choise =="3":
            print(wallet.display())

        elif choise =="4":
            query = input("Enter the title or type: ")
            print(wallet.search(query))

        elif choise =="5":
            wallet.save()
            print("succesfully saved as json")

        elif choise == "6":
            break
        else:
            print("Invalid choise")


if __name__ in "__main__":
    main()



            


        


        

