class BankAccount:
    def __init__(self, saldo, name):
        self.saldo = saldo
        self.name = name

    def show_saldo(self):
        print(f'masz {self.saldo} zł')

    def print_name(self):
        print(f" nazywam sie {self.name}")

