class Category:
    ledger = None
    name = ''

    def __init__(self, name_arg) -> None:
        self.name = name_arg
        self.ledger = list()

    def __str__(self) -> str:
        stars_number = (30 - len(self.name)) // 2
        string = '*' * stars_number + self.name + '*' * stars_number + '\n'

        for item in self.ledger:
        
            (desc, amt) = (item['description'][:23], str( round(item['amount'], 2) )[:7])
            while amt[-3:][0] != '.' : amt += '0'
            
            string += desc + ' ' * (30 - len(desc) - len(amt)) + amt + '\n'

        string += 'Total: ' + str(self.get_balance())

        return string

    def deposit(self, amount, description=''):
        self.ledger.append(
            {'amount': round(float(amount), 2), 'description': description})
        return None

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append(
                {'amount': -round(float(amount), 2), 'description': description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for ldger in self.ledger:
            balance += ldger['amount']
        return balance

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, ('Transfer to ' + budget_category.name))
            budget_category.deposit(amount, 'Transfer from ' + self.name)
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

def create_spend_chart(categories):
    def helper(categorie_name):
        return len(categorie_name)

    perc = dict()
    string = 'Percentage spent by category\n'
    label = [((3 - len(str(x))) * " " + str(x) + '|')
             for x in range(100, -1, -10)]

    for categorie in categories:
        total_withdraws = 0
        for entry in categorie.ledger:
            if entry['amount'] < 0:
                total_withdraws += entry['amount']

        perc[categorie.name] = abs(total_withdraws)
    total = sum(perc.values())

    for key in perc:
        key_percentage = int(perc[key] / total * 100)
        key_arr = []
        for i in range(100, -1, -10):
            if key_percentage >= i:
                key_arr.append('o')
            else:
                key_arr.append(' ')

        perc[key] = key_arr

    for i in range(11):
        string += label[i] + ' '
        for key in perc:
            string += perc[key][i] + '  '
        string += '\n'

    string += '    ' + '-' * (len(categories) * 3 + 1) + '\n'

    for i in range(len(max(perc, key=helper))) :
        string += '     '
        for cat in perc :
            try :
                string += cat[i:i+1][0] + '  '
            except :
                string += '   '
        string += '\n'
        
    return string[:len(string) - 1]


Food = Category('Food')
Food.deposit(25000, 'Salary of the week')
Food.withdraw(650, 'Sugar')
Food.withdraw(2000, 'Credit telephonique')
# print(Food)

Trans = Category('Transport')
Trans.deposit(2000, 'this is it !')
Trans.withdraw(1500, 'One way , to work')
# print(Trans)

Auto = Category('Auto')
Auto.deposit(125630, 'First deposit')
Auto.withdraw(3410)

# Food.transfer(25000, Trans)

# print(Food, Trans, sep='\n')

print(create_spend_chart([Food, Trans, Auto]))
