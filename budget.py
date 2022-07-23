class Category:
    ledger = list()
    name = ''
    
    def __init__(self, name_arg) -> None:
        self.name = name_arg
        print(name_arg, ' was created !')
        
    
    def __str__(self) -> str:
        stars_number = (30 - len(self.name)) // 2
        string = '*' * stars_number + self.name + '*' * stars_number + '\n'
        
        for item in self.ledger :
            (desc, amt) = (item['description'][:23], str(item['amount'])[:7])
            string += desc + ' ' * ( 30 - len(desc) - len(amt)  ) + amt + '\n'
            
        string += 'Total: ' + self.get_balance()
        
        return string
        
        
    def deposit(self, amount, description='') :
        self.ledger.append({ amount: float(amount), description: description })
        return None
    
    def withdraw(self, amount, description='') :
        if self.check_funds(amount) :
            self.ledger.append({ amount: -float(amount), description: description })
            return True
        return False
    
    def get_balance(self) :
        balance = 0
        for ldger in self.ledger :
            balance += ldger['amount']
        return balance
    
    def transfer(self, amount, budget_category) :
        if self.check_funds(amount) :
            self.withdraw(amount, 'Transfer to', budget_category.name)
            budget_category.deposit(amount, 'Transfer from', self.name)
            return True
        return False
    
    def check_funds(self, amount) :
        return self.get_balance() > amount




def create_spend_chart(categories):
    return