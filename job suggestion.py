print("\tJOB SUGGESTION")

# Collect user input for skill and experience
skill = input("Tell me your skill (tech/marketing/creative): ").lower()
experience = input("Tell me your experience level (beginner/intermediate/expert): ").lower()

# Job suggestions based on user input
if skill == "tech" and experience == "beginner":
    job = "Junior Web Developer"
elif skill == "tech" and experience == "intermediate":
    job = "Software Developer"
elif skill == "tech" and experience == "expert":
    job = "Senior Software Engineer"

elif skill == "marketing" and experience == "beginner":
    job = "Marketing Assistant"
elif skill == "marketing" and experience == "intermediate":
    job = "Marketing Manager"
elif skill == "marketing" and experience == "expert":
    job = "Marketing Director"

elif skill == "creative" and experience == "beginner":
    job = "Junior Graphic Designer"
elif skill == "creative" and experience == "intermediate":
    job = "Graphic Designer"
elif skill == "creative" and experience == "expert":
    job = "Creative Director"

else:
    job = "*Sorry, we don't have a suggestion for this combination.*"

print("Job Suggestion:", job)