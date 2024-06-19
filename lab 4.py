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

# Створення об'єкта класу Car
my_car = Car("Toyota", "Camry", 2020)

# Виконання методу accelerate п’ять разів і виведення поточної швидкості
for _ in range(5):
    my_car.accelerate()
    print(f"Поточна швидкість після прискорення: {my_car.get_speed()} км/год")

# Виконання методу brake п’ять разів і виведення поточної швидкості
for _ in range(5):
    my_car.brake()
    print(f"Поточна швидкість після гальмування: {my_car.get_speed()} км/год")

class Buffer:
    def __init__(self):
        self.buffer = []

    def add(self, *a):
        self.buffer.extend(a)
        while len(self.buffer) >= 5:
            sum_of_five = sum(self.buffer[:5])
            print(f"Сума п'ятірки: {sum_of_five}")
            self.buffer = self.buffer[5:]

    def get_current_part(self):
        return self.buffer

# Приклад використання класу Buffer
buf = Buffer()
buf.add(1, 2, 3)
print("Поточні елементи:", buf.get_current_part())  # [1, 2, 3]
buf.add(4, 5, 6)
print("Поточні елементи:", buf.get_current_part())  # [6]
buf.add(7, 8, 9, 10)
print("Поточні елементи:", buf.get_current_part())  # [6, 7, 8, 9, 10]
buf.add(11)
print("Поточні елементи:", buf.get_current_part())  # [11]
