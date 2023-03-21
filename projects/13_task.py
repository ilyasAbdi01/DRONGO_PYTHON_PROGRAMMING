class vehicle:

    color = 'white'

    def __init__(self,name,mileage,capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fair(self):
        return self.capacity  * 100    

    # def max_speed(self):
    #     pass
    
    # def mileage(self):
    #     pass
        

class bus(vehicle):
    def fair(self):
        amount = super().fair()
        amount += amount * 0.1
        return amount
   
bus1 = bus('school_bus',100,50)
print(f"Total bus fair is {bus1.fair()}")

        

   

 



      
       
