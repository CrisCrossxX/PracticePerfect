prompt = "What's your name again? Enter 'quit' at any time."
filename = 'guest_book.txt'

with open(filename, 'a') as f:
        while True:
            message = input(prompt)
            if message == 'quit':
                break
            else:
                print(f"Hello {message}, thanks for joining us!")
                f.write(f"{message}\n")
