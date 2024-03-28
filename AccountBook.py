import os

class Account:
    def __init__(self):
        self.money = 0
        self.history = []
        self.filename = '가계부.txt'

    def income(self, amount):
        self.money += amount
        self.history.append(('수입:', amount))
        with open(self.filename, 'a') as file:
                file.write(f"지출: {amount}\n")

    def expense(self, amount):
        if amount <= self.money:
            self.money -= amount
            self.history.append(('지출', amount))
            with open(self.filename, 'a') as file:
                file.write(f"지출: {amount}\n")
        else:
            print("돈이 부족합니다.")

    def display_money(self):
        print(f"현재 가진 돈: {self.money}")

    def display_history(self):
        print("내역")
        for action, amount in self.history:
            print(f"{action}: {amount}")

    def load_history(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                for line in file:
                    action, amount = line.strip().split(': ')
                    self.history.append((action, float(amount)))

def main():
    account = Account()
    account.load_history()
    while True:
        print("\n1. 수입")
        print("2. 지출")
        print("3. 현재 가진 돈")
        print("4. 거래 내역 보기")
        print("5. 나가기")

        choice = input("숫자를 선택하세요: ")

        if choice == '1':
            amount = float(input("입력: "))
            account.income(amount)
        elif choice == '2':
            amount = float(input("입력: "))
            account.expense(amount)
        elif choice == '3':
            account.display_money()
        elif choice == '4':
            account.display_history()
        elif choice == '5':
            print("종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()
