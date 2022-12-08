# Import functions from funtions.py
from func.functions import NewCustomer, GetCustomer, checkPhone, negationCheck, isOrder, isPizza, getPizzaList, boolConfirm, getReceipt

# Import preprocess functions from preprocess.py
from func.preprocess import preprocess, text_to_vector, get_cosine, checkTypo

# Import Order related functions from orderFunction.py
from func.orderFunction import checkNumber, confirmation, Checkpoint

# Import online libraries
import pandas as pd

# Loading all pizza name into one list
pizza_df= pd.read_csv('pizza.csv', sep=';')
listOfPizza = []
for pizzaKind in pizza_df['pizzaName'].unique():
    listOfPizza.append(pizzaKind)

# Loading customer database
customer = pd.read_csv('database/customer.csv')


# Pizza Class declaration
class Pizza:
    def __init__(self, name, size='small', crust='pan', pizza_df=pizza_df):
        self.name = name
        id = [pizza_df.iloc[i, 0] for i in range(len(pizza_df)) if pizza_df.iloc[i, 1] == name][0]
        self.description = pizza_df.iloc[id-1, 2]
        self.calories = pizza_df.iloc[id-1, 3]
        self.serves = pizza_df.iloc[id-1, 4]
        self.size = size
        self.crust = crust
        self.isVegetarian = pizza_df.iloc[id-1, 7]
        self.isVegan = pizza_df.iloc[id-1, 8]
        self.isSpicy = pizza_df.iloc[id-1, 9]
        self.price = pizza_df.iloc[id-1, 10]
        self.sizeAvailable = pizza_df.iloc[id-1, 5]
        self.crustAvailable = pizza_df.iloc[id-1, 6]

    def __str__(self):
        return self.description
    
    def getPrice(self):
        return self.price
    
    def getSize(self):
        return self.sizeAvailable

    def getCrust(self):
        return self.crustAvailable

    def getName(self):
        return self.name
        
# Reworking on the flow of the chatbot

initialInput = input('Greetings! Before we proceed, may I know your phone number?')

# Check for phone number [CHECK POINT 1]
isCust = GetCustomer(checkPhone(initialInput)[1])

# Final Receipt
receipt = []

firstEntry = True

# List of pizza getting ordered
pizzaOrder = []
while True:
    if firstEntry == True:
        # If isCust returns None, means the person is not in database
        if isCust == None:
            # New Customer [DONE]
            rawInput = input(f'Pizzy: Hi! We havent been friends before. How can I help you today?')
        else:
            # Returning Customer [DONE]
            rawInput = input(f'Pizzy: Welcome back {isCust[0].capitalize()}! How can I help you today?')

    else:
        # Second pizza
        rawInput = input('What will be your next pizza?')

    # Check if any pizza name is in the [DONE]
    for pizzas in listOfPizza:
        if pizzas in rawInput:
            pizzaOrder.append(pizzas)
        else:
            pass

    ## Checking whether pizza name exist in the rawInput
    # 1 Pizza Exist [DONE]
    if len(pizzaOrder) == 1:
        if negationCheck(rawInput) == False:
            tempNegation = [pOrder for pOrder in pizzaOrder][0]
            finalCheck = input(f'are u sure u want to order {tempNegation}?')
            # Final confirmation before proceeding to pizza detail
            CheckpointOutput = []
            CheckpointOutput.append(tempNegation)
        else:
            # There is negation --> Checkpoint 3
            print('what do u want?')
    # More than 1 pizza exists
    elif len(pizzaOrder) > 1:
        print('Sorry! we only serve one pizza at a time! you can place the next one after finishing one pizza.')
    # No Pizza exists
    elif len(pizzaOrder) == 0:
        # No name pizza exist --> Checkpoint 3

        # Order trigger word exist
        if isOrder(rawInput) == True:

            # Word pizza exist
            if isPizza(rawInput) == True:
                
                CheckpointOutput = Checkpoint(listOfPizza, pizza_df)

            # Word pizza not exist
            else:
                print('This chatbot is only taking order for pizza. Would like to have some?')
                
        # Order trigger word is not exist
        else:
            print('General talk huh')

    if len(CheckpointOutput) == 1:
        sizeChoice = []
        crustChoice = []
        currentOrder = Pizza(CheckpointOutput[0])
        sizeAvail = currentOrder.getSize().split(',')
        crustAvail = currentOrder.getCrust().split(',')
        # Taking size
        while True:
            sizePrompt = input(f'The available size are {[sizes for sizes in sizeAvail]}. Which size do you want?')
            if sizePrompt in sizeAvail:
                sizeChoice.append(sizePrompt)
                break
            elif sizePrompt == 'quit':
                break
            else:
                print('Please enter a valid size')

        # Taking crust
        while True:
            crustPrompt = input(f'The available crusts are {[crusts for crusts in crustAvail]}. Which size do you want?')
            if crustPrompt in crustAvail:
                crustChoice.append(crustPrompt)
                break
            elif crustPrompt == 'quit':
                break
            else:
                print('Please enter a valid crust')

        # Append pizza to the receipt
        receipt.append(list([f'{sizeChoice[0].capitalize()} {CheckpointOutput[0].capitalize()} with {crustChoice[0]}.', currentOrder.getPrice()]))
        
        anotherOrder = input('Do you want to have another pizza?')
        if boolConfirm(anotherOrder) == 1:
            firstEntry = False
        else:
            break


print(getReceipt(receipt))