from audioop import avg
from calendar import month


def format_date(pkt):
    months_dict = {1: "January", 2: "Febuary", 3: "March", 4: "April", 5: "May", 6: "June",
                   7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    tokens = pkt.split('-')
    return months_dict.get(int(tokens[1])) + " " + tokens[2]


def get_day_from_date(pkt):
    tokens = pkt.split('-')
    return tokens[2]


def check(value):
    if(value is None):
        return 0
    return value


class Calculations:
    def __init__(self, weather_reading):
        self.weather_reading = weather_reading

    def get_highest_temp(self):
        if(self.weather_reading.head is None):
            print("No weather reading!!!")
            return

        temp_ptr = self.weather_reading.head
        highest_temp = 0
        day = temp_ptr.pkt

        while(temp_ptr is not None):
            if(temp_ptr.max_temperature is not None and temp_ptr.max_temperature > highest_temp):
                highest_temp = temp_ptr.max_temperature
                day = temp_ptr.pkt
            temp_ptr = temp_ptr.next

        return {'day': format_date(day), 'temp': highest_temp}

    def get_lowest_temp(self):
        if(self.weather_reading.head is None):
            print("No weather reading!!!")
            return

        temp_ptr = self.weather_reading.head
        lowest_temp = temp_ptr.min_temperature
        day = temp_ptr.pkt

        while(temp_ptr is not None):
            if(temp_ptr.min_temperature is not None and temp_ptr.min_temperature < lowest_temp):
                lowest_temp = temp_ptr.min_temperature
                day = temp_ptr.pkt
            temp_ptr = temp_ptr.next

        return {'day': format_date(day), 'temp': lowest_temp}

    def get_highest_humidity(self):
        if(self.weather_reading.head is None):
            print("No weather reading!!!")
            return

        temp_ptr = self.weather_reading.head
        highest_humidity = temp_ptr.max_humidity
        day = temp_ptr.pkt

        while(temp_ptr is not None):
            if(temp_ptr.max_humidity is not None and temp_ptr.max_humidity > highest_humidity):
                highest_humidity = temp_ptr.max_humidity
                day = temp_ptr.pkt
            temp_ptr = temp_ptr.next

        return {'day': format_date(day), 'temp': highest_humidity}

    def get_average_highest_temp(self):
        if(self.weather_reading.head is None):
            print("No weather reading!!!")
            return

        temp_ptr = self.weather_reading.head
        sum_max_temp = 0
        count = 0

        while(temp_ptr is not None):
            if(temp_ptr.max_temperature is not None):
                sum_max_temp += temp_ptr.max_temperature
            temp_ptr = temp_ptr.next
            count += 1

        avg_highest_temp = int(sum_max_temp / count)
        return avg_highest_temp

    def get_average_lowest_temp(self):
        if(self.weather_reading.head is None):
            print("No weather reading!!!")
            return

        temp_ptr = self.weather_reading.head
        sum_min_temp = 0
        count = 0

        while(temp_ptr is not None):
            if(temp_ptr.min_temperature is not None):
                sum_min_temp += temp_ptr.min_temperature
            temp_ptr = temp_ptr.next
            count += 1

        avg_lowest_temp = int(sum_min_temp / count)
        return avg_lowest_temp

    def get_average_highest_humidity(self):
        if(self.weather_reading.head is None):
            print("No weather reading!!!")
            return

        temp_ptr = self.weather_reading.head
        sum_max_humidity = 0
        count = 0

        while(temp_ptr is not None):
            if(temp_ptr.max_humidity is not None):
                sum_max_humidity += temp_ptr.max_humidity
            temp_ptr = temp_ptr.next
            count += 1

        avg_highest_humidity = int(sum_max_humidity / count)
        return avg_highest_humidity

    def get_full_month_temp_record(self):
        if(self.weather_reading.head is None):
            print("No weather reading!!!")
            return

        temp_ptr = self.weather_reading.head
        month_record = []

        while(temp_ptr is not None):
            day_temp_dict = {}
            day_temp_dict['day'] = get_day_from_date(temp_ptr.pkt)
            day_temp_dict['high'] = check(temp_ptr.max_temperature)
            day_temp_dict['low'] = check(temp_ptr.min_temperature)
            month_record.append(day_temp_dict)

            temp_ptr = temp_ptr.next

        return month_record
