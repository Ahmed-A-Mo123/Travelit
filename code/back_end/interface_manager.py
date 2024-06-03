from .api_interface import SkyscannerApi, Chatgpt
from datetime import datetime, date
import json
import os

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

    def get_number_days(self):  # Make sure this doesn't return a negative number otherwise the return date is before
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

    def get_flight_list(self):
        return self.returned_flight_data['data']['itineraries'][:5]

    def get_flight_results_summary(self):
        return self.returned_flight_data['data']['context']

    def get_hotel_list(self):
        return self.returned_hotel_data['data']['hotels']

    def get_hotel_results_summary(self):
        return self.returned_hotel_data['data']['resultsSummary']

    def get_hotel_search_status(self):
        return self.returned_hotel_data['data']['searchStatus']

#
# search = Search('london', 'New york', '2', '2024-05-15', '2024-05-20')
#
#
# search.flights()
# search.hotels()
#
# print(s)
# print(search.get_hotel_search_status())

