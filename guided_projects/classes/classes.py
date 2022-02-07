class Car:
    # Create the constructor
    # self = the object
    def __init__(self, make="unknown", model="unknown", color="unknown", year=-1, price=-1):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        # _ = 'hidden'
        self._price = price

    # Property decorator
    @property
    # Getter
    def price(self):
        return self._price
    # Setter
    @price.setter
    def price(self, p):
        if p <= 0:
            raise ValueError("Price is zero or less!")
        print("[log] setter for price called")
        self._price = p
    
    #
    def __str__(self):
        return 'Car(make=' + self.make + ', model=' + self.model +\
            ', color=' + self.color + ', year=' + str(self.year) +\
                ', price=' + str(self.price) + ')'

car = Car()
print("Model =", car.model)
#car.price = -1
car.price = 10000

car =Car("Buick", "lesabre", "red", 2013, 10000)
print("Car:", car)

fh = open("cars.csv", "r")
cars_data = fh.readlines()

cars_data.pop(0)

cars_list = []

for rawstring in cars_data:
    make,model,color,year,price = rawstring.split(',')
    cars_list.append(Car(make,model,color,int(year),float(price)))

cars_list.sort(key=lambda car: car.price)

print(*cars_list, sep='\n')
