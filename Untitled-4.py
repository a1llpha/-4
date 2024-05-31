class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0  

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed


car = Car("Toyota", "Corolla", 2020)


for _ in range(5):
    car.accelerate()
    print(f"Поточна швидкість після прискорення: {car.get_speed()}")


for _ in range(5):
    car.brake()
    print(f"Поточна швидкість після гальмування: {car.get_speed()}")


    #Завдання 2


    class Buffer:
    def __init__(self):
        self.buffer = []

    def add(self, *a):
        self.buffer.extend(a)
        while len(self.buffer) >= 5:
            sum_five = sum(self.buffer[:5])
            print(f"Сума першої п’ятірки: {sum_five}")
            self.buffer = self.buffer[5:]

    def get_current_part(self):
        return self.buffer


buffer = Buffer()
buffer.add(1, 2, 3)
print(f"Поточна частина: {buffer.get_current_part()}")
buffer.add(4, 5, 6)
print(f"Поточна частина: {buffer.get_current_part()}")
buffer.add(7, 8, 9, 10)
print(f"Поточна частина: {buffer.get_current_part()}")