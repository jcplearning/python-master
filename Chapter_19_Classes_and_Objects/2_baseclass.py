class Car:
	def __init__(self, brand, model, year):
		self.brand = brand
		self.model = model
		self.year = year

	def car_info(self): 
		info = f'Car is {self.year} {self.brand} {self.model}'
		return info

car1 = Car('Hyundai','Elantra','2018')
print(car1.car_info())