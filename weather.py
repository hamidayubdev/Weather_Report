import sys
import parser as p
import weather_reading as wr
import calculations as calc


colors = {'BLUE': '\033[94m', 'RED': '\033[31m', 'BLACK': '\033[30m'}


def perform_calculation_based_on_option(option, weather_reading):
    # data structure for storing calculation results
    results = {}
    weather_calculation = calc.Calculations(weather_reading)

    if(option == 'e'):
        results['highest_temp'] = weather_calculation.get_highest_temp()
        results['lowest_temp'] = weather_calculation.get_lowest_temp()
        results['highest_humidity'] = weather_calculation.get_highest_humidity()

        # if there exists a record for the specified month/year
        if(results['highest_temp'] is not None):
            print("Highest: {}C on {}".format(results.get('highest_temp').get(
                'temp'), results.get('highest_temp').get('day')))
            print("Lowest: {}C on {}".format(results.get('lowest_temp').get(
                'temp'), results.get('lowest_temp').get('day')))
            print("Humidity: {}% on {}".format(results.get('highest_humidity').get(
                'temp'), results.get('highest_humidity').get('day')))

    elif(option == 'a'):
        results['avg_highest_temp'] = weather_calculation.get_average_highest_temp()
        results['avg_lowest_temp'] = weather_calculation.get_average_lowest_temp()
        results['avg_highest_humidity'] = weather_calculation.get_average_highest_humidity()

        # if there exists a record for the specified month/year
        if(results['avg_highest_temp'] is not None):
            print(f"Highest Average: {results.get('avg_highest_temp')}C")
            print(f"Lowest Average: {results.get('avg_lowest_temp')}C")
            print(
                f"Average Mean Humidity: {results.get('avg_highest_humidity')}%")

    elif(option == 'c'):
        results['month_temp_record'] = weather_calculation.get_full_month_temp_record()

        # if there exists a record for the specified month/year
        if(results['month_temp_record'] is not None):
            for day_record in results.get("month_temp_record"):
                print("{}{:02} {} {:02}C".format(colors.get('RED'), int(day_record.get('day')),
                                                 '+'*day_record.get('high'), int(day_record.get('high'))))
                print("{}{:02} {} {:02}C".format(colors.get('BLUE'), int(day_record.get('day')),
                                                 '+'*day_record.get('low'), int(day_record.get('low'))))

            print("\n\nBONUS TASK\n")

            for day_record in results.get("month_temp_record"):
                print("{}{:02} {}{}{}{} {}{:02}C - {}{:02}C".format(colors.get('BLACK'), int(day_record.get('day')), colors.get('BLUE'),
                                                                    '+'*day_record.get('low'), colors.get('RED'), '+'*day_record.get('high'), colors.get('BLUE'), int(day_record.get('low')), colors.get('RED'), int(day_record.get('high'))))


def perform_calculations(options_dict, path_to_file):
    parser = p.Parser()

    for option in options_dict.keys():
        year_month = options_dict.get(option)

        if(len(year_month) == 2):
            files = parser.get_files(
                path_to_file, year_month[0], year_month[1])
        else:
            files = parser.get_files(path_to_file, year_month[0])

        weather_reading = wr.WeatherReading()
        parser.populate(files, weather_reading)

        perform_calculation_based_on_option(option, weather_reading)
        print()


def main():
    cmd_args = sys.argv
    path_to_file = cmd_args[1]
    options_dict = {}

    for i in range(2, len(cmd_args), 2):
        tokens = cmd_args[i+1].split("/")
        years = []

        if(len(tokens) > 1):
            years.append(int(tokens[0]))
            years.append(int(tokens[1]))
        else:
            years.append(int(tokens[0]))

        option = cmd_args[i].lstrip('-')
        if((option == 'a' or option == 'c') and len(years) <= 1):
            print("Month not specified for ", years[0])
            exit(1)

        options_dict[option] = years

        # if(len(options_dict['e']) != 2 or len(options_dict['e']) != 2)

    perform_calculations(options_dict, path_to_file)


if __name__ == "__main__":
    main()
