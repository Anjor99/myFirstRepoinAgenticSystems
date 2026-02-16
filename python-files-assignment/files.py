# Function to read numbers from file
def read_numbers(filename):
    numbers = []

    with open(filename, "r") as file:
        log_message("-" * 30)
        log_message("File opened successfully")

        for line in file:
            line = line.strip()
            if line:
                try:
                    numbers.append(int(line))
                except ValueError:
                    log_message(f"Invalid integer found: {line}")
                    print(f"Invalid integer found: {line}")

    log_message(f"Read {len(numbers)} numbers")
    return numbers



# Function to compute statistics
def compute_stats(numbers):
    total_count = len(numbers)
    total_sum = sum(numbers)
    average = total_sum / total_count

    log_message("Computation completed")

    return total_count, total_sum, average


# Function to write logs (append mode)
def log_message(message):
    with open("python-files-assignment/results.log", "a") as log_file:
        log_file.write(message + "\n")


# Main function
def main():
    try:
        # Step 1: Read data
        numbers = read_numbers("python-files-assignment/numbers.txt")

        # Step 2: Compute results
        count, total, avg = compute_stats(numbers)

        # Step 3: Write results to log
        log_message(f"Total numbers: {count}")
        log_message(f"Sum: {total}")
        log_message(f"Average: {avg}")
        log_message("Processing completed")
        log_message("-" * 30 + "\n")  # Separator for readability

        print("Processing finished. Check results.log")

    except FileNotFoundError:
        log_message("Error: numbers.txt not found")
        print("numbers.txt file not found.")


# Program entry point
if __name__ == "__main__":
    main()
