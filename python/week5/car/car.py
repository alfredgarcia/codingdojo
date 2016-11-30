class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def display_all(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel", self.fuel
        print "Mileage", self.mileage
        print "Tax", self.tax
        return self

car1 = Car(2000, "35mph", "Full", "15mpg")
car1.display_all()

car2 = Car(5000, "50mph", "Kind of Full", "10mpg")
car2.display_all()

car3 = Car(20000, "100mph", "Empty", "10mpg")
car3.display_all()

car4 = Car(15000, "100mph", "Not Full", "10mpg")
car4.display_all()

car5 = Car(7000, "50mph", "Kind of Full", "10mpg")
car5.display_all()

car6 = Car(9000, "50mph", "Full", "10mpg")
car6.display_all()
