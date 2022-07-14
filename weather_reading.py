from hashlib import new


class Node:
    def __init__(self, weather_reading):
        self.next = None

        self.pkt = weather_reading[0]

        self.max_temperature = weather_reading[1]
        self.mean_temperature = weather_reading[2]
        self.min_temperature = weather_reading[3]

        self.max_dew_point = weather_reading[4]
        self.mean_dew_point = weather_reading[5]
        self.min_dew_point = weather_reading[6]

        self.max_humidity = weather_reading[7]
        self.mean_humidity = weather_reading[8]
        self.min_humidity = weather_reading[9]

        self.max_sea_level_pressure = weather_reading[10]
        self.mean_sea_level_pressure = weather_reading[11]
        self.min_sea_level_pressure = weather_reading[12]

        self.max_visibility = weather_reading[13]
        self.mean_visibility = weather_reading[14]
        self.min_visibility = weather_reading[15]

        self.max_wind_speed = weather_reading[16]
        self.mean_wind_speed = weather_reading[17]

        self.max_gust_speed = weather_reading[18]

        self.precipitation = weather_reading[19]
        self.cloud_cover = weather_reading[20]
        self.events = weather_reading[21]
        self.wind_direction = weather_reading[22]


class WeatherReading:
    def __init__(self):
        self.head = None

    def add(self, weather_reading):
        new_node = Node(weather_reading)
        if(self.head is None):
            self.head = new_node
            return

        temp_ptr = self.head
        while(temp_ptr.next is not None):
            temp_ptr = temp_ptr.next

        temp_ptr.next = new_node

    def display(self):
        if(self.head is None):
            print("NOTHING TO DISPLAY !!!!!")
            return

        temp_ptr = self.head

        while(temp_ptr is not None):
            print("Date: ", temp_ptr.pkt)
            print("Temperature: ", temp_ptr.max_temperature)
            temp_ptr = temp_ptr.next
