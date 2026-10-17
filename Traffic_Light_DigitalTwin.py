class trafficlight:
    def __init__(self, location):
        self.location = location
        self.color = "RED"
        self.status = "ON"
        self.cars_waiting = 0
        self.cycles_completed = 0

    def turn_green(self):
        if self.status == "ON" and self.color == "RED":
            self.color = "GREEN"
            print(f"{self.location} light is now GREEN.")
        else:
            print("Cannot turn green right now.")

    def turn_yellow(self):
        if self.status == "ON" and self.color == "GREEN":
            self.color = "YELLOW"
            print(f"{self.location} light is now YELLOW.")
        else:
            print("Cannot turn yellow right now.")

    def turn_red(self):
        if self.status == "ON" and self.color == "YELLOW":
            self.color = "RED"
            self.cycles_completed += 1
            print(f"{self.location} light is now RED.")
        else: 
            print("Cannot turn red right now.")

    def add_car(self):
        if self.status == "ON" and self.color == "RED":
            self.cars_waiting += 1
            print(f"A car is waiting. Cars waiting: {self.cars_waiting}")
        else: 
            print("Cars cannot join the waiting line right now.")

    def let_cars_go(self):
        if self.status == "ON" and self.color == "GREEN":
            print(f"{self.cars_waiting} cars are moving through.")
            self.cars_waiting = 0
        else: 
            print("Cars must wait for a green light.")

    def turn_off(self):
        self.status = "OFF"
        self.color = "OFF"
        print(f"{self.location} traffic light is OFF.")

    def turn_on(self):
        self.status = "ON"
        self.color = "RED"
        print(f"{self.location} traffic light is ON and RED.")

    def display_status(self):
        print(f"\n--- Traffic Light Status ---")
        print (f"Location: {self.location}")
        print(f"Color: {self.color}")
        print(f"Status: {self.status}")
        print(f"Cars Waiting: {self.cars_waiting}")
        print(f"Cycles Completed: {self.cycles_completed}")

#Create a traffic light object
traffic_light = trafficlight("Main Street")

#Demonstrate the traffic light
traffic_light.display_status()

traffic_light.add_car()
traffic_light.add_car()

traffic_light.turn_green()
traffic_light.let_cars_go()

traffic_light.turn_yellow()
traffic_light.turn_red()

traffic_light.display_status()

traffic_light.turn_off()
traffic_light.display_status()

traffic_light.turn_on()
traffic_light.display_status()
