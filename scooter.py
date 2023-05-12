class Scooter:
    def __init__(self, rental_company, starting_fee, price_per_100m, available_dist_km):
        self.rental_company = rental_company
        self.starting_fee = starting_fee
        self.price_per_100m = price_per_100m
        self.available_dist_km = available_dist_km
    
    def price(self, ride_length_in_km):
        if ride_length_in_km > self.available_dist_km:
            return 1000
        else:
            ride_length_in_m = ride_length_in_km * 1000
            final_price = self. price_per_100m * (ride_length_in_m / 100)
            return self.starting_fee + final_price
    
    def ride(self, ride_length_in_km):
        self.available_dist_km -= ride_length_in_km
        if self.available_dist_km < 0:
            self.available_dist_km = 0
        
    def charge(self, no_of_km):
        self.available_dist_km += no_of_km

class Rentals:
    def __init__(self, scooters) -> None:
        self.scooters = scooters
    
    def display_choices(self, ride_length_in_km) -> None:
        price_l = []
        for i, sc in enumerate(self.scooters):
            price_l.append(sc.price(ride_length_in_km))
        sorted_prices = sorted(price_l)
        for p in sorted_prices:
            print(f'Rental - {self.scooters[price_l.index(p)].rental_company}.........price = {p}')
    
    def rent(self, scooter_name, ride_length_in_km) -> None:
        for scooter in self.scooters:
            if scooter.rental_company == scooter_name:
                if ride_length_in_km <= scooter.available_dist_km:
                    print("Price of Ride -", scooter.price(ride_length_in_km))
                    scooter.ride(ride_length_in_km)
                else:
                    print("Length to ride more than available distance for scooter")
    
    def charge_scooter(self, scooter_name, ride_length_in_km) -> None:
        for scooter in self.scooters:
            if scooter.rental_company == scooter_name:
                scooter.charge(ride_length_in_km)

scooter_list = []
while len(scooter_list) < 3:
    scooter_details = input("Enter Scooter deatils (all in one line separated by a space) \n")
    inner_details = scooter_details.split(" ")
    scooter_list.append(Scooter(inner_details[0], float(inner_details[1]), float(inner_details[2]), float(inner_details[3])))


rentals = Rentals(scooter_list)
rentals.display_choices(2)
rentals.rent("Bolt", 3)
rentals.rent("Tuul", 18)
rentals.rent("Tuul", 5)
rentals.charge_scooter("Tuul", 5)
rentals.rent("Tuul", 2)