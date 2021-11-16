import pyperclip

def get_row_number(boarding_pass):
    row_binary = boarding_pass[:-3].replace("F", "0").replace("B", "1")
    return int(row_binary, 2)


def get_seat_number(boarding_pass):
    seat_binary = boarding_pass[-3:].replace("L", "0").replace("R", "1")
    return int(seat_binary, 2)


with open("inputs/day_5_input.txt", "r") as input:
    boarding_passes = [line.strip() for line in input.readlines()]

# seat_ids = []
# for boarding_pass in boarding_passes:
#     row_number = get_row_number(boarding_pass)
#     seat_number = get_seat_number(boarding_pass)
#     id_number = 8 * row_number + seat_number
#     seat_ids.append(id_number)

# print(max(seat_ids))

print(
    max(
        [
            8 * get_row_number(boarding_pass) + get_seat_number(boarding_pass)
            for boarding_pass in boarding_passes
        ]
    )
)

with open("inputs/day_5_input.txt", 'r') as input:
    boarding_passes = [line.strip("\n") for line in input.readlines()] 

seat_ids = []
for boarding_pass in boarding_passes:
    row_number = get_row_number(boarding_pass)
    seat_number = get_seat_number(boarding_pass)
    id_number = 8 * row_number + seat_number
    seat_ids.append(id_number)



for seat in range(min(seat_ids), max(seat_ids)):
    if seat not in seat_ids:
        print(seat)
        pyperclip.copy(seat)


# Matt Harrison uses sets instead of creating lists. This allows for set operations.
# First create a set of seat ids, then create a set of all possible seats ranging from the seat_ids min to max.
# Then take the difference.

# seat_ids = {8 * get_row_number(boarding_pass) + get_seat_number(boarding_pass) for boarding_pass in boarding_passes}
# all_seats = set(range(min(seat_ids), max(seat_ids)+1))
# print(all_seats - seat_ids)
