# file name: Program 1.py
# I, Bibi Zulaikha Akbari, student ID: 000912329, clarify that this work is my
# own effort ,and I don't allowed anyone else to copy from it.
# 1: function for square:
def drawSquare(size):
    print("*" * size)
    for i in range(size - 2):
        print("*" + " " * (size - 2) + "*")
    if size > 1:
        print("*" * size)
    return drawSquare

# 2: finction for triangle:
def drawTriangle(size):
    for i in range(1, size + 1):
        print("*" * i)
    return drawTriangle

# 3: function for arrowhead:
def drawArrowhead(size):
    for i in range(1, size, 2):
        print("*" * i)
    for i in range(size, 0, -2):
        print("*" * i)
    return drawArrowhead

# 4: general function to call the shapes and sizes:
def choice():
    shapeCode = int(input("Enter shape code (1 = square, 2 = triangle, 3 = arrow head): "))
    shapeSize = int(input("Enter shape size: "))

    if shapeCode == 1:
        drawSquare(shapeSize)   # calling the function
    elif shapeCode == 2:
        drawTriangle(shapeSize)  # calling the function
    elif shapeCode == 3:
        drawArrowhead(shapeSize)   # calling the function
    else:
        print("Try again and enter shape code (1 = square, 2 = triangle, 3 = arrow head): ")
    return choice()
# ============== main line of code ================
answer = choice()
print(answer)

# I try so many numbers for testing this program and it works, but when I tried even numbers: 6,10,12,
# just in arrow head, it shows one * less at the last line....
# And it's completly works for odd numbers in arrowhead shape.
