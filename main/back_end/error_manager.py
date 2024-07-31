from django.utils import timezone


class SearchValidation:
    def __init__(self, date_array):  # object requires a list/array of dates.
        self.date = date_array
        self.current_date = timezone.now()

    def is_date_valid(self):  # returns a boolean - takes a list of dates and works out if date A is before date B
        # otherwise throws an error
        valid_date = []
        for date in self.date:
            if date > self.current_date:
                valid_date.append(True)
            else:
                valid_date.append(False)

        if not valid_date[0] or not valid_date[1]:
            raise ValueError("Dates are void")

    def is_country_valid(self):  # return a boolean - Check if a country is valid otherwise throws an error
        pass
