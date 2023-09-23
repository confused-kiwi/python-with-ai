class Car:
    def __init__(self, maker, model,year,colour,VIN):
        self.maker = maker
        self.model = model
        self.year = year
        self.colour = colour
        self.VIN = VIN
    def display(self):
        print(f"{self.maker} {self.model} {self.colour} {self.VIN}")


def main():
    cars = []
    cars.append( Car("Tesla","Model Y", 2019, "White","WMWSU3C54DT677253") )
    cars.append( Car("Ford", "EcoSport", 2001, "Black", "1HGEM21242L044172"))
    cars.append( Car("Nissan", "Sentra", 1492, "Blue", "WBAVD13526KV48437"))
    cars.append( Car("Jeep", "Grand Cherokee", 1677, "Green", "JNKCV51E94M664932"))

    maker = input("Search by maker: ")
    
    for car in cars:
        if car.maker == maker:
            car.display()


main()
    
    