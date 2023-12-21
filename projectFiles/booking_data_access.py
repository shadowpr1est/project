import os
from datetime import datetime, time


class BookingDataAccess:
    def __init__(self):
        self.file_path = "C:/Users/alish/pyProject/untitled1/projectFiles/bookings.txt"

    def read_from_txt(self):
        with open(self.file_path, 'r') as file:
            places = [line.strip() for line in file]
        for i in range(len(places)):
            lst = places[i].split()
            if len(lst) > 4 and datetime.strptime(lst[-2], "%H:%M").time() < datetime.now().time():
                places[i] = f"{places[0]} available {places[2]} {places[3]}"

        return places

    # if datetime.now().time() > time(20,0) or datetime.now().time() > time(20,0) or start_time > time(20,0):
    #     return "You cannot book this place, because it's too late\nPlease, choose another time"
    # elif datetime.now().time() > start_time or datetime.now().time() > end_time or start_time > end_time:
    #     return "Please, enter the correct time!"
    def write_to_txt_requirements(self, booking_details):
        temp_file_path = "C:/Users/alish/pyProject/untitled1/projectFiles/tempFile.txt"
        id = str(booking_details.get_id())
        start_time = datetime.strptime(booking_details.get_start_time(), '%H:%M').time()
        end_time = datetime.strptime(booking_details.get_end_time(), '%H:%M').time()
        is_socket = str(booking_details.get_socket())
        is_wide = str(booking_details.get_wide())
        written = False
        no_place = False
        with open(temp_file_path, 'w') as temp_file, open(self.file_path, 'r') as file:
            for line in file:
                current_line = line.split()
                if current_line[0] == id and current_line[2] == is_socket and current_line[3] == is_wide and current_line[1] == "available":
                    temp_file.write(
                        f"{id} occupied {current_line[2]} {current_line[3]} {start_time.strftime('%H:%M')} "
                        f"{end_time.strftime('%H:%M')} {booking_details.get_full_name()}")
                    written = True
                elif current_line[0] == id and current_line[2] != is_socket and current_line[3] != is_wide and current_line[1] == "available":
                    no_place = True
                else:
                    temp_file.write(line.strip())
                temp_file.write("\n")
        os.remove(self.file_path)
        os.rename(temp_file_path, self.file_path)

        if no_place:
            return "There is no such place ❌"
        elif written:
            return "Booking successful ✅"
        else:
            return "This place is occupied by someone 🚫"

    def write_to_txt_number(self, booking_details):
        temp_file_path = "C:/Users/alish/pyProject/untitled1/projectFiles/tempFile.txt"
        id = str(booking_details.get_id())
        start_time = datetime.strptime(booking_details.get_start_time(), '%H:%M').time()
        end_time = datetime.strptime(booking_details.get_end_time(), '%H:%M').time()
        written = False
        with open(temp_file_path, 'w') as temp_file, open(self.file_path, 'r') as file:
            for line in file:
                current_line = line.split()
                if current_line[0] == id and current_line[1] == "available":
                    temp_file.write(f"{id} occupied {current_line[2]} {current_line[3]} {start_time.strftime('%H:%M')} "
                                    f"{end_time.strftime('%H:%M')} {booking_details.get_full_name()}")
                    written = True
                else:
                    temp_file.write(line.strip())
                temp_file.write("\n")
        os.remove(self.file_path)
        os.rename(temp_file_path, self.file_path)
        if written:
            return "Booking successful ✅"
        else:
            return "This place is occupied by someone 🚫"

    def cancel_to_txt(self, booking_details):
        temp_file_path = "C:/Users/alish/pyProject/untitled1/projectFiles/tempFile.txt"
        id = str(booking_details.get_id())
        removed = False
        with open(temp_file_path, 'w') as temp_file, open(self.file_path, 'r') as file:
            for line in file:
                current_line = line.split()
                if current_line[0] == id and current_line[-1].strip() == booking_details.get_full_name():
                    temp_file.write(f"{id} available {current_line[2]} {current_line[3]}")
                    removed = True
                else:
                    temp_file.write(line.strip())

                temp_file.write("\n")

        os.remove(self.file_path)
        os.rename(temp_file_path, self.file_path)
        if removed:
            return "Deleted successfully ✅"
        else:
            return "Failed to delete ❌"

    def find_from_txt(self, username):
        matching_places = []
        with open(self.file_path, 'r') as file:
            for line in file:
                if username in line:
                    matching_places.append(line.strip())
        return matching_places
