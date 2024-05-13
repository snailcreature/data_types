def log(message) -> None:
    """
    Output a string to a log file and the console.
    """
    # Open the log file as log_file in append mode
    with open("log.txt", "a") as log_file:
        # Cast the message to string and write it to the log file
        # with a newline character on the end.
        log_file.write(str(message) + "\n")
    # Close the log file
    log_file.close()
    print(message)

if __name__ == "__main__":
    number: int = 1
    while number != 0:
        number = input("Gimme a number: ")
        try:
            number = int(number)
        except:
            log(number + " was guessed, please enter an integer.")
        else:
            log(number)