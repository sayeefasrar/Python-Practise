import cs50


while True:
    print("Please enter your desired height: ", end="")
    height = cs50.get_int()
    if height == 0:
        break

    if (height > 0 and height <= 23):
        for j in range(height):
            for i in range(height - 1, j, -1):

                print(" ", end="")

            for k in range(j + 1):
                print("#", end="")

            print("  ", end="")

            for m in range(j + 1):
                print("#", end="")
            print()
        break