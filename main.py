from datetime import datetime, timedelta #Imports datetime module https://www.tutorialgateway.org/python-datetime/

class TramTime:
    def parse_time(time_str):
        return datetime.strptime(time_str, "%H:%M")
        # Source: https://www.w3schools.com/python/ref_datetime_strptime.asp

    def format_time_24(time_obj):
        return time_obj.strftime("%H:%M")
        # Converts into 24-hour string 

    def format_time_12(time_obj):
        return time_obj.strftime("%I:%M %p")
        # Converts to 12-hour format 

    def Display(time_obj):
        return TramTime.format_time_24(time_obj)

class TramDirection:
    def __init__(self):
        self.TramDirection = "Tram"
        self.CarlingfordLane = 1
        self.WestmeadLane = 1
        # Source: https://www.w3schools.com/python/python_classes.asp

    def Tram(self, direction):
        return f"Tram heading {direction}"
        # Shows tram's current direction

    def Direction(self):
        return "Carlingford to Westmead"
        # Shows the route

class TramCapicity:
    def __init__(self):
        self.TramCapicity = 400
        self.Tram_sPeople = 0
        # Setting up  tram capacity, cars and number of people

    def Capacity(self, people):
        return min(people, self.TramCapicity)
        # Limits the number of people to the tram's maximum
        # Source: https://www.w3schools.com/python/ref_func_min.asp


        
class LightRailSystem:
    def __init__(self):
        self.TramSystem = "Parramatta Light Rail"
        self.TramInterface = "Console"
        self.TramName = "PLR Tram"
        self.TramSevice = "Regular"
        self.TramCapicity = TramCapicity()
        self.direction = TramDirection()
        self.start_time = TramTime.parse_time("05:00")
        self.end_time = TramTime.parse_time("01:00") + timedelta(days=1)
        self.TimeIntervals = TramTime
        self.tram_stops = [
            "Carlingford", "Robin Thomas", "Parramatta Square",
            "Church Street", "Prince Alfred Square", "Westmead"
        ]
  
    def Operator(self, tram):
        return f"Operating {tram}"

    def Tram(self, name):
        return name

    def Service(self):
        return self.TramSevice

    def get_interval(self, current_time):
        if (TramTime.parse_time("06:30") <= current_time <= TramTime.parse_time("08:30")) or \
           (TramTime.parse_time("15:00") <= current_time <= TramTime.parse_time("18:00")):
            return 7.5
        elif TramTime.parse_time("07:00") <= current_time <= TramTime.parse_time("19:00"):
            return 15
        else:
            return None

    def calculate_trams_per_hour(self, interval):
        if interval:
            return int(60 / interval)
        return 0


    def get_status(self, interval):
        if interval == 7.5:
            return "Peak"
        elif interval == 15:
            return "Off-Peak"
        else:
            return "No Service"

    def DisplayTime(self):
        current_time = self.start_time
        print("Tram Service Schedule from 05:00 to 01:00 (next day)\n")
        print("Time     Interval (min)     Trams per hour     Service Status")
        print("--------------------------------------------------------------")

        while current_time <= self.end_time:
            interval = self.get_interval(current_time)
            trams_per_hour = self.calculate_trams_per_hour(interval)
            status = self.get_status(interval)
            time_string = TramTime.format_time_24(current_time)
            interval_string = str(interval) + " mins" if interval else "N/A"
            print(f"{time_string}   {interval_string:<17} {trams_per_hour:<18} {status}")
            current_time += timedelta(minutes=15)

    def Display(self, time):
        return TramTime.Display(time)

    def Time(self, next_time):
        return TramTime.format_time_24(next_time)

    def check_user_time(self, user_time_str):
        try:
            user_time = TramTime.parse_time(user_time_str)
        except ValueError:
            print("Invalid time format. Please use HH:MM (e.g., 07:30).")
            return None

        if not (self.start_time.time() <= user_time.time() or user_time.time() <= self.end_time.time()):
            print("Trams do not run at this time.")
            return None

        interval = self.get_interval(user_time)
        if interval:
            trams_per_hour = self.calculate_trams_per_hour(interval)
            status = self.get_status(interval)
            print(f"\nTram details for {user_time_str}:")
            print(f"Service Status: {status}")
            print(f"Interval between trams: {interval} minutes")
            print(f"Number of trams per hour: {trams_per_hour}")
        else:
            print("No tram service at this time.")
        return user_time

class TramApp:
    def __init__(self):
        self.system = LightRailSystem()
 

    def run(self):
        self.system.DisplayTime()
        user_time_str = input("Enter your departure time (HH:MM, 24‑hour format): ")
        user_time = self.system.check_user_time(user_time_str)

        if user_time:
            convert = input("Convert time to 12-hour format? (yes/no): ").strip().lower()
            if convert == "yes":
                time_12 = TramTime.format_time_12(user_time)
                print(f"Your departure time in 12-hour format is: {time_12}")
            else:
                print("No conversion performed.")
        print("Thank you for using the tram service schedule program!")

if __name__ == "__main__":
    TramApp().run()
