class Car():
    def __init__(self, model, color, fuel, window, year, price):
        self.model = model
        self.color = color
        self.fuel =  fuel
        self.balon = True
        self.door = True
        self.window = window
        self.year = year
        self.price = price
        
        
        
        
        
    def acceleration(self):
        if self.fuel in ['electricity', 'hibrid']:
            print(f"{self.model} - This model reaches 100 km/h in 1.2 seconds")
        elif self.fuel in ['Gaz', 'Benzin']:
            print(f"{self.model} - This model reaches 100 km/h in 13 seconds")
            
            
            
            
            
    def fuller(self):
        if self.fuel in ['electricity', 'hibrid']:
            print(f"{self.model} - Ushbu model 8 soat da to'liq toladi")
        elif self.fuel in [ 'Benzin']:
            print(f"{self.model} - Ushbu model tez to'ladi 80 l")
        elif self.fuel in ['Gaz']:
            print(f"{self.model} - Ushbu model sekin to'ladi, 150 l")
            
            
            
            
            
    def prices(self):
        if 2010 <= self.year < 2020:
            self.price = self.price * 0.10
        elif 2000 <= self.year <= 2009:
            self.price = self.price * 0.20
        elif 1990 <= self.year < 2000:
            self.price = self.price * 0.30
        elif 1980 <= self.year < 1990:
            self.price = self.price * 0.40
        elif 2020 <= self.year <= 2026:
            print('')
        else:
            print('Bunday Mashina Bizda Sotilmaydi')
        
        
        
       
       
            
        
chevrolet = Car(model='Malibu', color='black', fuel='Benzin', window='black', year=2010, price=30000)
BMW = Car(model='BMW', color='white', fuel='Gaz', window='white', year=2020, price=400000)
byd = Car(model='Chempion', color='green', fuel='electricity', window='green', year=2015, price=300000)
Toyota = Car(model='Corolla', color='Black', fuel='Benzin', window='Black', year=2024, price=24000)
Honda = Car(model='Civic', color='White', fuel='Benzin', window='White', year=2025, price=29000)
Ford = Car(model='Mustang', color='White', fuel='Benzin', window='White', year=2009, price=30000)


BMW.acceleration()
BMW.fuller()
BMW.prices()
byd.acceleration()
byd.fuller()
byd.prices()
chevrolet.acceleration()
chevrolet.fuller()
chevrolet.prices()
Toyota.acceleration()
Toyota.fuller()
Toyota.prices()
Honda.acceleration()
Honda.fuller()
Honda.prices()
Ford.acceleration()
Ford.fuller()
Ford.prices()
# BMW.acceleration()
# BMW.acceleration()

print(f"{int(chevrolet.price)}")
print(f"{int(BMW.price)}")
print(f"{int(byd.price)}")
print(f"{int(Toyota.price)}")
print(f"{int(Honda.price)}")
print(f"{int(Ford.price)}")
# 
# 
# print(f"{chevrolet.model}, {chevrolet.color}, {chevrolet.fuel}")
# print(f"{BMW.model}, {BMW.color}, {BMW.fuel}, {BMW.window}")
# print(byd.fuel)




# 10%

# narx




