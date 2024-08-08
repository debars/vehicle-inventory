
class Vehicle:
    def __init__(self, vehicle_data):
        self.vin = vehicle_data['vin']
        self.manufacturer = vehicle_data['manufacturer']
        self.model = vehicle_data['model']
        self.color = vehicle_data['color']
        self.year = vehicle_data['year']

    def __repr__(self):
        return f'VIN: {self.vin}, Manufacturer: {self.manufacturer}, Model: {self.model}, Year: {self.year}, Color: {self.color}'