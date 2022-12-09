

# from func.functions2 import NewCustomer, GetCustomer, checkPhone, negationCheck, isOrder, isPizza, getPizzaList, boolConfirm, getReceipt

from importance.funcs import GetCustomer, checkPhone, negationCheck, isOrder, isPizza, getPizzaList, boolConfirm, getReceipt

# Import preprocess functions from preprocess.py
from func.preprocess import preprocess, text_to_vector, get_cosine, checkTypo, getReco, getBill

# Import Order related functions from orderFunction.py
from func.orderFunction import checkNumber, confirmation, Checkpoint

from func.additionals import clear, opening

from importance.pizza import Pizza

# Import online libraries
import pandas as pd

# Loading all pizza name into one list
pizza_df= pd.read_csv('pizza.csv', sep=';')
listOfPizza = []
for pizzaKind in pizza_df['pizzaName'].unique():
    listOfPizza.append(pizzaKind)

# Loading customer database
customer = pd.read_csv('database/customer.csv')

### Main Chatbot code starts here ###
### Reworking on the flow of the chatbot ###
clear()
pflag = False

opening()
# Check for phone number [CHECK POINT 1]
while True:
    if pflag == False:
        initialInput = input('\nPizzy: Greetings! Before we proceed, please enter your phone number. \nYou: ')
    else:
        initialInput = input('\nPizzy: Please enter a correct UK phone number.\nYou: ')

    if checkPhone(initialInput)[0] == 0:
        pflag = True
    else:
        break

isCust = GetCustomer(checkPhone(initialInput)[1])

# Final Receipt
receipt = []

firstEntry = True

# List of pizza getting ordered
pizzaOrder = []
while True:
    rawInput = ''
    if firstEntry == True:
        # If isCust returns None, means the person is not in database
        if isCust == None:
            # New Customer [DONE]
            rawInput = input(f'\nPizzy: Hi! We havent been friends before. How can I help you today?\nYou: ')
        else:
            # Returning Customer [DONE]
            rawInput = input(f'\nPizzy: Welcome back {isCust[0].capitalize()}! How can I help you today?\nYou: ')

    elif firstEntry == False:
        # Second pizza
        rawInput = input('\nPizzy: What will be your next pizza?\nYou:')

    # Check if any pizza name is in the [DONE]
    for pizzas in listOfPizza:
        if pizzas in rawInput:
            pizzaOrder.append(pizzas)
            CheckpointOutput = []
            CheckpointOutput.append(pizzas)
        else:
            pass

    ## Checking whether pizza name exist in the rawInput
    # 1 Pizza Exist [DONE]
    if len(pizzaOrder) == 1:
        if negationCheck(rawInput) == False:
            tempNegation = [pOrder for pOrder in pizzaOrder][0]
            finalCheck = input(f'\nPizzy: To confirm, do you want to order {tempNegation.capitalize()}?\nYou: ')
            # Final confirmation before proceeding to pizza detail
            if boolConfirm(finalCheck) == 1:
                CheckpointOutput = []
                CheckpointOutput.append(tempNegation)
                pizzaOrder.append(tempNegation)
        else:
            # There is negation
            print('what do u want?')
    # More than 1 pizza exists
    elif len(pizzaOrder) > 1:
        print('Pizzy: Sorry! we only serve one pizza at a time! You can place the next one after finishing one pizza.')
    # No Pizza exists
    elif len(pizzaOrder) == 0:
        # No name pizza exist
        # Order trigger word exist
        if isOrder(rawInput) == True:

            # Word pizza exist
            if isPizza(rawInput) == True:
                
                CheckpointOutput = Checkpoint(listOfPizza, pizza_df)
                pizzaOrder.append(CheckpointOutput[0])

            # Word pizza not exist
            else:
                boolOptions = input('\nPizzy: For now, I will only be taking orders for Pizzas. Would like to have some?\nYou: ')
                if boolConfirm(boolOptions) == 1:
                    keywordPrompt = input('\nPizzy: How do you like your pizza?\n You:')
                    print(getReco(keywordPrompt))
                    CheckpointOutput = Checkpoint(listOfPizza, pizza_df)
                
        # Order trigger word is not exist
        else:
            recoPromtpt = input('\nPizzy: Do you want to get a recommendation in picking your food?\nYou: ')
            # True
            if boolConfirm(recoPromtpt) == 1:
                keywordPrompt = input('\nPizzy: How do you like your pizza?\nYou: ')
                print(getReco(keywordPrompt))
                CheckpointOutput = Checkpoint(listOfPizza, pizza_df)
                # Return back to how can i help you

    if len(CheckpointOutput) == 1:
        sizeChoice = []
        crustChoice = []
        currentOrder = Pizza(CheckpointOutput[0])
        sizeAvail = currentOrder.getSize().split(',')
        crustAvail = currentOrder.getCrust().split(',')
        # Taking size
        while True:
            sizePrompt = input(f'\nPizzy: The available size are {[sizes for sizes in sizeAvail]}. Which size do you want?\nYou: ')
            if sizePrompt in sizeAvail:
                sizeChoice.append(sizePrompt)
                break
            elif sizePrompt == 'quit':
                break
            else:
                print('Pizzy: Please enter a valid size')

        # Taking crust
        while True:
            crustPrompt = input(f'\nPizzy: The available crusts are {[crusts for crusts in crustAvail]}. Which size do you want?\nYou:')
            if crustPrompt in crustAvail:
                crustChoice.append(crustPrompt)
                break
            elif crustPrompt == 'quit':
                break
            else:
                print('Pizzy: Please enter a valid crust')

        # Append pizza to the receipt
        receipt.append(list([f'Pizzy: {sizeChoice[0].capitalize()} {CheckpointOutput[0].capitalize()} with {crustChoice[0]}.', currentOrder.getPrice()]))
        
        anotherOrder = input('\nPizzy: Do you want to have another pizza?\nYou: ')
        if boolConfirm(anotherOrder) == 1:
            firstEntry = False
        else:
            break

print(getReceipt(receipt))
if isCust != None:
    print(getReceipt(receipt))
    print(f'\nThankyou {isCust[0].capitalize()} for orderring! The total is {getBill(pizzaOrder)}')
    print(f'Your pizza will be delivered to {isCust[1]}. See you next time!')
else:
    while True:
        addPrompt = input('\nPizzy: Please input your address here.\nYou: ')
        addConf = input(f'\nPizzy: Is it true that {addPrompt} is your address?\nYou: ')
        if boolConfirm(addConf) == 1:
            break
        else:
            pass
    while True:
        namePrompt = input('\nPizzy: What should we call you?\nYou: ')
        nameConf = input(f'\nDo you want me to call you {namePrompt}?\nYou: ')
        if boolConfirm(nameConf) == 1:
            break
        else:
            pass
    print(getReceipt(receipt))
    print(f'\nThankyou {namePrompt.capitalize()} for orderring! The total is {getBill(pizzaOrder)}')
    print(f'Your pizza will be delivered to {addPrompt}. See you next time!')