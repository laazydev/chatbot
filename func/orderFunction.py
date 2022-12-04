
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
