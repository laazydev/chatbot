def checkNumber(text):
    oneTrigger = ['one', '1']
    for i in text:
        if i[1] == 'NUM':
            # Only allow one order at a time
            if i[0] in oneTrigger:
                return True
            else: 
                return False