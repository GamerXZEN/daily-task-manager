try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectanlge length: "))
    if width == length:
        exit('Dp not enter squares next time.')
    area = width * length
    print(area)
except ValueError:
    print("Please enter a number")