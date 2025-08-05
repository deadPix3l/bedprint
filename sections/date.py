from datetime import date

class DateSection(Section):
    def get_data(self):
        return date.today()
