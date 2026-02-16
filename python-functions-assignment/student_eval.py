# Function 1: Greeting function
def get_greeting(name):
    return f"Hello {name}! Here is your performance report."


# Function 2: Score statistics
def calculate_stats(scores):
    num_subjects = len(scores)
    average_score = sum(scores) / num_subjects
    return num_subjects, average_score


# Function 3: Pass / Fail evaluator
def check_result(avg):
    if avg >= 50:
        return "Pass"
    else:
        return "Fail"


# Function 4: Main function
def main():
    try:
        # Input section
        student_name = input("Enter the student's name: ")

        # Taking scores as input
        scores_input = input("Enter scores separated by spaces: ")
        scores = [int(score) for score in scores_input.split()]

        # Calling functions
        greeting = get_greeting(student_name)
        subjects, average = calculate_stats(scores)
        result = check_result(average)

        # Final output
        print(greeting)
        print("------ Performance Summary ------")
        print(f"Subjects      : {subjects}")
        print(f"Average Score : {average:.2f}")
        print(f"Final Result  : {result}")
    except ValueError:
        print("Invalid input. Please enter numeric scores separated by spaces.")


# Program entry point
if __name__ == "__main__":
    main()
