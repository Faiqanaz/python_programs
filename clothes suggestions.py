print("\tCLOTHING SUGGESTION")

# Collect user input for weather, occasion, and gender
weather = input("Tell me the weather type (cold/hot): ").lower()
occasion = input("Tell me the occasion type (casual/formal): ").lower()
gender = input("Tell me your gender (male/female): ").lower()

# Clothing suggestions based on user input for Western style
if weather == "cold" and occasion == "casual" and gender == "male":
    clothing = "Warm coat, jeans, and a beanie"
elif weather == "cold" and occasion == "casual" and gender == "female":
    clothing = "Sweater, jeans, and a scarf"

elif weather == "cold" and occasion == "formal" and gender == "male":
    clothing = "Blazer, wool trousers, and a tie"
elif weather == "cold" and occasion == "formal" and gender == "female":
    clothing = "Wool coat over formal dress and boots"

elif weather == "hot" and occasion == "casual" and gender == "male":
    clothing = "T-shirt, shorts, and a baseball cap"
elif weather == "hot" and occasion == "casual" and gender == "female":
    clothing = "Lawn suit and chaifoon dupatta"

elif weather == "hot" and occasion == "formal" and gender == "male":
    clothing = "Light suit with a tie"
elif weather == "hot" and occasion == "formal" and gender == "female":
    clothing = "Light summer dress with heels"

else:
    clothing = "*Sorry, we don't have a suggestion for this combination, but you could choose a comfortable outfit.*"

print("Clothing Suggestion:", clothing)