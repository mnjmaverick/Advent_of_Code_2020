with open('Day_5/input.txt', 'r') as f:
    tickets = [ticket.strip() for ticket in f.readlines()]


def seat_id(ticket):
    row = int(ticket[0:7].replace('F', '0').replace('B', '1'), 2)
    seat = int(ticket[7:].replace('L', '0').replace('R', '1'), 2)
    return row, seat


rows_columns = [seat_id(ticket) for ticket in tickets]

seat_ids = set([row * 8 + seat for row, seat in rows_columns])
all_seat_ids = set(range(min(seat_ids), max(seat_ids)))

# Part 1
print(max(seat_ids))

# Part 2
print(all_seat_ids - seat_ids)
