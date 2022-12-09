import pandas as pd

pizza_df = pd.read_csv('pizza.csv', sep=';')

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