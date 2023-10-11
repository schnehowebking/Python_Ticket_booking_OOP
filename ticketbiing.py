from star_cinema import Star_Cinema
from hall import Hall
from counter import Counter



while True:
    print()
    print("Welcome to Star Cinema Management System")
    print("1. Add a new hall")
    print("2. Add a new show")
    print("3. View all shows")
    print("4. View available seats for a show")
    print("5. Book tickets")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        hall_no = input("Enter the hall number: ")
        hall = Hall(rows, cols, hall_no)
        Star_Cinema.entry_hall(hall)
        print(f"Hall {hall_no} added.")
    elif choice == "2":
        hall_no = input("Enter the hall number: ")
        show_id = input("Enter the show ID: ")
        movie_name = input("Enter the movie name: ")
        show_time = input("Enter the show time: ")
        for hall in Star_Cinema._hall_list:
            if hall._hall_no == hall_no:
                hall.entry_show(show_id, movie_name, show_time)
                print(f"Show {show_id} added to Hall {hall_no}.")
                break
        else:
            print(f"Hall {hall_no} not found.")
    elif choice == "3":
        counter = Counter(Star_Cinema._hall_list)
        counter.view_all_shows()
    elif choice == "4":
        show_id = input("Enter the Show ID: ")
        hall_no = input("Enter the Hall Number: ")
        counter = Counter(Star_Cinema._hall_list)
        counter.view_available_seats_in_show(show_id, hall_no)
    elif choice == "5":
        show_id = input("Enter the Show ID: ")
        hall_no = input("Enter the Hall Number: ")
        seat_list_str = input("Enter the seats to book (e.g., '1,2 2,3 3,4'): ")
        seat_list = [tuple(map(int, seat.split(',')) for seat in seat_list_str.split())]
        counter = Counter(Star_Cinema._hall_list)
        counter.book_tickets(show_id, hall_no, seat_list)
    elif choice == "6":
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
