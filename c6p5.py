class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def get_hour(self):
        return self.__hour

    def get_minute(self):
        return self.__minute

    def get_second(self):
        return self.__second

    def set_hour(self, hour):
        self.__hour = hour

    def set_minute(self, minute):
        self.__minute = minute

    def set_second(self, second):
        self.__second = second

    def __add__(self, other):
        if isinstance(other, Time):
            total_seconds = self.__to_seconds() + other.__to_seconds()
            return self.__from_seconds(total_seconds)
        else:
            raise TypeError("Operand must be of type 'Time'")

    def __to_seconds(self):
        return self.__hour * 3600 + self.__minute * 60 + self.__second

    def __from_seconds(self, total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return Time(hours, minutes, seconds)

    def display(self):
        return f"{self.__hour:02}:{self.__minute:02}:{self.__second:02}"

def get_time_input():
    while True:
        try:
            hour = int(input("Enter hours (0-23): "))
            minute = int(input("Enter minutes (0-59): "))
            second = int(input("Enter seconds (0-59): "))

            if 0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59:
                return Time(hour, minute, second)
            else:
                print("Invalid input. Please enter valid time values.")
        except ValueError:
            print("Invalid input. Please enter integers for hours, minutes, and seconds.")

print("Enter the first time:")
time1 = get_time_input()

print("Enter the second time:")
time2 = get_time_input()

time3 = time1 + time2

print(f"\nTime 1: {time1.display()}")
print(f"Time 2: {time2.display()}")
print(f"Sum of Time 1 and Time 2: {time3.display()}")
