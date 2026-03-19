class vehicle:
    def __init__(self,registration_number,capacity):
        self.registration_number=registration_number
        self.capacity=capacity
        
    def vehicle_info(self):
        print(f"registration_number:{self.registration_number}")
        print(f"capacity:{self.capacity}")
        
    def is_overloaded(self,amount):
        if self.amount>self.capacity:
            return True
        else:
            return False
            
class Car(vehicle):
    def __init__(self,registration_number,capacity,trunk_size):
        super().__init__(self,registration_number,capacity)
        self.trunk_size=trunk_size
        
    def vehicle_info(self):
        print(f"registration_number:{self.registration_number}")
        print(f"capacity:{self.capacity}")
        print(f"trunk_size:{self.trunk_size}")
        
class Truck(vehicle):
    def __init__(self,registration_number,capacity,max_load):
        super().__init__(self,registration_number,capacity)
        self.max_load=max_load
        
    def is_overloaded(self,amount):
        if self.amount>self.max_load:
            return True
        else:
            return False
            
class Bus(vehicle):
    def __init__(self,registration_number,capacity,standing_capacity):
        super().__init__(self,registration_number,capacity)
        self.standing_capacity=standing_capacity
        
    def vehicle_info(self):
        print(f"registration_number:{self.registration_number}")
        print(f"capacity:",{self.capacity})  
        print(f"standing_capacity:{self.standing_capacity}")
        
    fleet=["Car","Truck","Bus"]
    for vehicle in fleet:
        for vehicle_info in vehicle:
            print(vehicle_info)
    if is_overloaded=="True":
        print(vehicle)
    else:
        print("is not over loaded") 
     

            
        
        