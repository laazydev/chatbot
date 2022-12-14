from importance.funcs import getPizzaList, boolConfirm
from func.preprocess import checkTypo
from func.preprocess import getReco

def checkNumber(text):
    oneTrigger = ['one', '1']
    for i in text:
        if i[1] == 'NUM':
            # Only allow one order at a time
            if i[0] in oneTrigger:
                return True
            else: 
                return False

def confirmation(pizzaName):
    positive_bool = ['yes', 'yesh', 'yeah', 'yup', 'yea', 'yuh']
    negative_bool= ['no', 'noh', 'nope', 'nah', 'naur', 'naw']

    confirm = input(f'Are you ordering {pizzaName}?')

    if confirm in positive_bool:
        return True
    elif confirm in negative_bool:
        return False
    else:
        confirmationFlag = 0
        for i in range(2):
            secondConfirm = input('Please enter a confirmation')
            if [pos in positive_bool for pos in secondConfirm.split()][0]:
                confirmationFlag = 1
                break
            elif [neg in negative_bool for neg in secondConfirm.split()][0]:
                confirmationFlag = -1
                break
        
        if confirmationFlag == 1:
            return True
        elif confirmationFlag == -1:
            return False

def Checkpoint(listOfPizza, pizza_df):
    trialsFlag = 0
    order = []
    while True:
        trials = 0
        if trials == 2:
            rePrintPizza = input('Pizzy: Do you want to see the list of pizza first?\nYou: ')
            # Positive: Want to see pizza list [DONE]
            if boolConfirm(rePrintPizza) == 1:
                print('\n')
                print(getPizzaList(pizza_df))
                break

            # Negative: Dont want [DONE]
            elif boolConfirm(rePrintPizza) == -1:
                print('Pizzy: Alright, sure sure')
                break

        pizzaOrderInput = input('Pizzy: What pizza do you want?\nYou: ')
        flagOrder = False

        # Typo checking is here
        for typoCheck in listOfPizza:
            # Accurate 100%
            if checkTypo(typoCheck.lower(), pizzaOrderInput.lower()) == 100:
                print(f'Pizzy: You are ordering {typoCheck.capitalize()}')
                trialsFlag = 1
                order.append(typoCheck)
                flagOrder = True
                break
            
            # Above 80% Confidence
            elif checkTypo(typoCheck.lower(), pizzaOrderInput.lower()) > 80:
                typoPrompt = input(f'Pizzy: Do you mean by {typoCheck.capitalize()}?\n You: ')
                # Positive confirmation
                if boolConfirm(typoPrompt) == 1:
                    print(f'Pizzy: You are orderring {typoCheck.capitalize()}')
                    trialsFlag = 1
                    order.append(typoCheck)
                    flagOrder = True
                    break

                # Negative Confirmation
                elif boolConfirm(typoPrompt) == -1:
                    break
                
                # Not understandable response
                else:
                    print('Pizzy: I am not sure I understand :.')
            
            # Under 80% Confidence
            else:
                pass
        
        if flagOrder == True:
            break
        else:
            rePrintPizza = input('Pizzy: Do you want to see the list of pizza first?\nYou: ')
            # Positive: Want to see pizza list [DONE]
            if boolConfirm(rePrintPizza) == 1:
                print('\n')
                print(getPizzaList(pizza_df))

            # Negative: Dont want [DONE]
            elif boolConfirm(rePrintPizza) == -1:
                recoPromtpt = input('\nPizzy: Do you want to get a recommendation in picking your food?\nYou: ')
                # True
                if boolConfirm(recoPromtpt) == 1:
                    keywordPrompt = input('\nPizzy: How do you like your pizza?\nYou: ')
                    print(getReco(keywordPrompt))
                break


        # Checkpoint [DONE]
        if trialsFlag == 0:
            pass
        else:
            break
    return order