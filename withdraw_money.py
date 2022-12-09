from User_choice import User_Choice
import pandas as pd
record = pd.read_json("Bank_data.json")

class Withdraw(User_Choice):
    def take_with_draw_amount(self):
        self.with_draw_amount = int(input('how much amount you want to withdraw'))

    def check_balance(self, user_choice):
        self.b = 0
        self.money_in_account = record.loc[record.Account_number == user_choice.user_account, 'Balance'][0]
        if self.money_in_account >= self.with_draw_amount:
            print('your money is withdraw ')
            print('please collect your money')
            record.loc[record.Account_number == user_choice.user_account, 'Balance'] -= self.with_draw_amount
            record.to_json('Bank_data.json')
            print(f"Now your balance is {record.loc[record.Account_number == user_choice.user_account, 'Balance'][0]}")
        else:
            self.b = 1
            print(f"There is not enough money your current bank balance is {record.loc[record.Account_number == user_choice.user_account, 'Balance'][0]}")

