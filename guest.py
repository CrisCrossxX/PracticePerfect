filename = 'guest.txt'

message = input("what's your name again? ")
with open(filename, 'a') as file_object:
    file_object.write(message)
