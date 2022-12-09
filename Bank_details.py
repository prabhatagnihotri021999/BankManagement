import pandas as pd
record = pd.read_json("Bank_data.json")

class Bank_details:

    def take_password(self):
        print("are you employee of bank if yes enter your pin")
        self.n = int(input())

    def check_pin(self):
        self.b = 0
        if self.n == 67890:
            print('Bank details are')
            print(f"There are total {len(record)} account holder in a bank.")
            print(f"Total money currently hold by bank is {record['Balance'].sum()} ")
        else:
            print('you are in danger')
            self.b = 1

    def check_details(self):
        print('Do you want to check details of any account holder if yes enter y else n')
        self.c = input()
        if self.c.lower() == 'y':
            print('by what you want to search the account holder by name or account_number\n Type Account_number  or Name')
            self.d = input()
            if self.d.lower() == 'account_number':
                print('enter account number')
                self.e = int(input())
                if self.e in record['Account_number']:
                    print(record.loc[record.Account_number == self.e])
                else:
                    print('Such account number does not exit')
                    exit()

            else:
                print('enter account holder name \n It is case sensitive')
                self.f = input()
                if self.f in list(record['Name']):
                    print(record[record['Name'] == self.f])
                else:
                    print(f"Any account holder does not have name {self.f}")
                    exit()

        elif self.c.lower() == 'n':
            exit()
        else:
            print('wrong choice')


