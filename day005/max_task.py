student_scores = [150,142,185,120,175,200,100,90,80,110,160,130]
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print("The highest score is:", highest_score)

print(max(student_scores) == highest_score)