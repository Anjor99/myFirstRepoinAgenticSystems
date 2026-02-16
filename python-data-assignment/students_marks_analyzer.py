# Taking scores as input
scores_input = input("Enter scores separated by spaces: ")
scores = [int(score) for score in scores_input.split()]

while len(scores) < 8:
    print("Please enter scores for at least 8 subjects.")
    scores_input = input("Enter scores separated by spaces: ")
    scores = [int(score) for score in scores_input.split()] 

print(scores)
print(f"First 3 scores: {scores[:3]}")
print(f"Last 3 scores: {scores[-3:]}")
print(f"Average score: {sum(scores) / len(scores)}")
print(f"Highest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")