import sys

# sys.argv[0] is the program name, so actual inputs start from index 1
if len(sys.argv) == 5:
    movie_name = sys.argv[1]
    duration = sys.argv[2]
    ticket_price = sys.argv[3]
    language = sys.argv[4]
    print("User input provided")
else:
    print("No input given, using default values")
    movie_name = "Kantara"
    duration = "3"
    ticket_price = "300"
    language = "Kannada"

print("\n--- Movie Details ---")
print(f"Movie Name   : {movie_name}")
print(f"Duration     : {duration}")
print(f"Language     : {language}")
print(f"Ticket Price : {ticket_price}")
