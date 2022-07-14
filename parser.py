import re
import os


class Parser:
    def get_files(self, path_to_file, year, month=None):
        self.path_to_file = path_to_file
        if month is None:
            regex_str = '.*{year}.*txt$'.format(year=year)
        else:
            months_dict = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
                           7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}
            month_str = months_dict[month]
            regex_str = '.*{year}_{month}.*txt$'.format(
                year=year, month=month_str)

        regex = re.compile(regex_str)

        file_list = []

        for file in os.listdir(path_to_file):
            if type(file) is str and regex.match(file):
                file_list.append(file)
        return file_list

    def populate(self, file_list, weather_reading):
        for file in file_list:
            with open("/{path}/{file}".format(path=self.path_to_file, file=file)) as f:
                f.readline()
                c = 0
                for line in f:
                    tokens = []

                    for token in line.split(","):
                        token = token.strip()
                        if(token == ""):
                            tokens.append(None)
                        elif(token.isdecimal()):
                            tokens.append(eval(token))
                        else:
                            tokens.append(token)
                        
                    weather_reading.add(tokens)
                    c+=1