class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._allocate_seats()

    def _allocate_seats(self):
        self._seats = {f"Seat {i + 1}": [0] * self._cols for i in range(self._rows)}

    def entry_show(self, show_id, movie_name, show_time):
        show_info = (show_id, movie_name, show_time)
        self._show_list.append(show_info)
        self._seats[show_id] = [[0] * self._cols for _ in range(self._rows)]

    def book_seats(self, show_id, seat_list):
        if show_id in self._seats:
            for row, col in seat_list:
                if 1 <= row <= self._rows and 1 <= col <= self._cols:
                    if self._seats[show_id][row - 1][col - 1] == 0:
                        self._seats[show_id][row - 1][col - 1] = 1
                        print(f"Seat booked: Row {row}, Column {col}")
                    else:
                        print(f"Seat already booked: Row {row}, Column {col}")
                else:
                    print(f"Invalid seat: Row {row}, Column {col}")
        else:
            print(f"Show with ID {show_id} not found.")

    def view_show_list(self):
        print(f"Shows Running in Hall {self._hall_no}:")
        for show_id, movie_name, show_time in self._show_list:
            print(f"Show ID: {show_id}, Movie: {movie_name}, Time: {show_time}")

    def view_available_seats(self, show_id):
        if show_id in self._seats:
            available_seats = [
                (row, col)
                for row in range(1, self._rows + 1)
                for col in range(1, self._cols + 1)
                if self._seats[show_id][row - 1][col - 1] == 0
            ]

            print(f"Available Seats for Show {show_id} in Hall {self._hall_no}:")
            for row in range(1, self._rows + 1):
                seat_row = ""
                for col in range(1, self._cols + 1):
                    if (row, col) in available_seats:
                        seat_row += "O "  # Empty seat
                    else:
                        seat_row += "X "  # Booked seat
                print(seat_row)
        else:
            print(f"Show with ID {show_id} not found.")