date = input("What is today's date (MM-DD-YYYY): ")
rating = input("How do you rate your mood today (1-10): ")
thoughts = input('Let your thoughts flow: ')

with open(date, 'w') as file:
    file.write(f'Rating: {rating}\n\n')
    file.write(thoughts)

