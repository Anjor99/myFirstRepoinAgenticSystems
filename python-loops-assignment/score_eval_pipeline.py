# Take the score as input from the user
scores=[]
iterations=int(input("Enter the number of scores to evaluate: "))

for n in range(iterations):
    score=float(input(f"Enter score {n+1}: "))
    scores.append(score)
    
print("\nScore Evaluation Results:")
# Evaluate each score and print the corresponding grade
for score in scores:
    if score >= 50:
        print(f"Score: {score} : Pass")
    else:
        print(f"Score: {score} : Fail")