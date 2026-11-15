# Author: Enrique Vigil
# Date: 11.14.26
# Assignment: Assignment_10 - Files

def main():
    # asks the user for the files name
    filename = input("Please enter the name of the file: ")

    try:
        # opens the file
        with open(filename, "r") as file:
            # displays the first five lines
            for count in range(5):
                line = file.readline()

                # ends if the end of the file is reached
                if line == "":
                    break

                # avoidd adding an extra line
                print(line, end="")

    except OSError:
        print("Error: The file couldn't be opened.")


# runs the program
if __name__ == "__main__":
    main()
