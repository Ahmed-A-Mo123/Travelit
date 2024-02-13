from api_manager import SkyscannerApi, Chatgpt
from datetime import datetime, date


# this is where we check the input from the user and make api calls
class Search(SkyscannerApi):  # Inherits from the sky scanner API class/ allows me not to repeat code

    def check_if_date_valid(self):
        split_date = self.departure_date.split('-')
        year = int(split_date[0])
        month = int(split_date[1])
        day = int(split_date[2])
        present = datetime.now()
        if not datetime(year, month, day) > present:  # the entered date should be greater than the present
            raise ValueError()
        return True

    def get_passengers(self):
        return int(self.passengers)

    def get_destination(self):
        return self.destination

    def get_origin(self):
        return self.origin

    def get_dates(self):
        return [self.departure_date, self.return_date]

    def get_number_days(self):  # Make sure this doesnt return a negative number otherwise the return date is before
        # the departure
        dates = self.get_dates()
        dates_list = []
        for each_date in dates:
            split_date = each_date.split('-')
            year = int(split_date[0])
            month = int(split_date[1])
            day = int(split_date[2])
            dates_list.append(date(year, month, day))
        return (dates_list[1] - dates_list[0]).days  # finds the difference between the two dates entered and
        # returns the number of days


search = Search('london', 'New york', '2', '2024-02-13', '2024-02-20')

print(search.get_number_days())
