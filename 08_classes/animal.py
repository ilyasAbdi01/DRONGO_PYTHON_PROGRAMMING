class Animal:
    
    def __init__(self, name, habitat, food):
        self.a_name = name
        self.a_habitat = habitat
        self.a_food = food

    def movement(self):
        pass

    def price(self):
        pass


dog = Animal('Dog', 'Home', 'Meat')

cow = Animal('Cow', 'Home', 'Grass')