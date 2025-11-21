import sys

# sys.argv[0] is the program name, so actual inputs start from index 1
if len(sys.argv) != 5:
    print("Usage: python movie_details.py <movie_name> <duration> <language> <ticket_price>")
    sys.exit()

movie_name = sys.argv[1]
duration = sys.argv[2]
language = sys.argv[3]
ticket_price = sys.argv[4]

print("\n--- Movie Details ---")
print(f"Movie Name   : {movie_name}")
print(f"Duration     : {duration}")
print(f"Language     : {language}")
print(f"Ticket Price : {ticket_price}")
