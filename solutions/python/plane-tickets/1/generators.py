"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    seats = ['A', 'B', 'C', 'D']
    seat_count = 0
    count = 0
    while count < number:
        yield seats[seat_count]
        count += 1
        seat_count += 1
        if seat_count == 4:
            seat_count = 0



def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """
    seats = ['A', 'B', 'C', 'D']
    count = 0
    seat_count = 0
    row_count = 1
    # if row_count == 13:
    #     yield None
    while count < number:
        # if count == 12:
        #     continue
        if row_count != 13:
            yield f"{row_count}{seats[seat_count]}"
            count+=1
        seat_count += 1
        if seat_count == 4:
            row_count += 1
            seat_count = 0


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seat_map = dict()
    seats = generate_seats(len(passengers))
    for passenger in passengers:
        seat_map[passenger] = next(seats)
    return seat_map


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """
    for seat_number in seat_numbers:
        seat_id = f"{seat_number}{flight_id}"
        remaining = 12 - len(seat_id)
        zeros = '0' * remaining
        seat_id +=zeros
        yield seat_id