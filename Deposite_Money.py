import pandas as pd
record = pd.read_json("Bank_data.json")

from User_choice import User_Choice

class Deposite(User_Choice):

    def add_amount(self, user_choice):
        print('How much amount you want to deposite \n Enter your amount\n')
        self.amount = int(input())
        record.loc[record.Account_number == user_choice.user_account, 'Balance'] += self.amount
        record.to_json('Bank_data.json')
        print(f"your current balance is {record.loc[record.Account_number == user_choice.user_account, 'Balance']}")

