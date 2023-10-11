class Counter:
    def __init__(self, hall_list):
        self._hall_list = hall_list

    def view_all_shows(self):
        for hall in self._hall_list:
            hall.view_show_list()

    def view_available_seats_in_show(self, show_id, hall_no):
        for hall in self._hall_list:
            if hall._hall_no == hall_no:
                hall.view_available_seats(show_id)

    def book_tickets(self, show_id, hall_no, seat_list):
        for hall in self._hall_list:
            if hall._hall_no == hall_no:
                hall.book_seats(show_id, seat_list)
                return
        print(f"Show with ID {show_id} not found in Hall {hall_no}")