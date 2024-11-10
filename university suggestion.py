print("\tUNIVERSITY SUGGESTION")

# Collect user inputs for preferred major and location preference
major = input("Tell me your preferred major (engineering/science/business): ").lower()
location = input("Tell me your location preference (local/international): ").lower()

# University suggestions based on user input
if major == "engineering" and location == "local":
    university = "NED University of Engneering and Technology"
elif major == "engineering" and location == "international":
    university = "Massachusetts Institute of Technology (MIT)"
elif major == "science" and location == "local":
    university = "NUST(National University of Science and Technology)"
elif major == "science" and location == "international":
    university = "University of Cambridge"
elif major == "business" and location == "local":
    university = "IBA(Institude of Business Administration)"
elif major == "business" and location == "international":
    university = "Harvard Business School"
else:
    university = "*Sorry, we don't have a suggestion for this combination.*"

print("University Suggestion:", university)