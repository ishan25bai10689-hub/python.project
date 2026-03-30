print("-------- PERSONAL HEALTH CHECK SYSTEM --------\n")

# Taking user details
user_name = input("What's your name? ")
user_age = int(input("Your age: "))
body_weight = float(input("Weight (kg): "))
body_height = float(input("Height (m): "))
user_gender = input("Gender (M/F/O): ").strip().upper()
lifestyle = input("Lifestyle (sedentary/moderate/active/athlete): ").strip().lower()

print("\nAnalyzing your data...\n")

# Macronutrients & calories
if lifestyle == "sedentary":
    cal_need = body_weight * 28
    protein_need = body_weight * 1.0
    carb_need = body_weight * 3
    fat_need = body_weight * 0.6

elif lifestyle == "moderate":
    cal_need = body_weight * 30
    protein_need = body_weight * 1.3
    carb_need = body_weight * 4
    fat_need = body_weight * 0.8

elif lifestyle == "active":
    cal_need = body_weight * 33
    protein_need = body_weight * 1.6
    carb_need = body_weight * 5
    fat_need = body_weight * 1.0

elif lifestyle == "athlete":
    cal_need = body_weight * 38
    protein_need = body_weight * 2.0
    carb_need = body_weight * 6.5
    fat_need = body_weight * 1.2

else:
    print("Please enter a valid lifestyle type!")
    exit()

# BMI and weight analysis
bmi_value = round(body_weight / (body_height ** 2), 2)
ideal_wt = round(22 * (body_height ** 2), 2)
gap = round(body_weight - ideal_wt, 2)

if bmi_value < 18.5:
    status = "Underweight"
elif bmi_value < 25:
    status = "Fit"
elif bmi_value < 30:
    status = "Overweight"
else:
    status = "Obese"

# Vitamins suggestion
vitamin_data = {}

if user_gender == "M":
    vitamin_data = {"Iron": "8 mg", "Calcium": "1000 mg", "Vitamin C": "90 mg", "Vitamin D": "600 IU"}
elif user_gender == "F":
    vitamin_data = {"Iron": "18 mg", "Calcium": "1200 mg", "Vitamin C": "75 mg", "Vitamin D": "600 IU"}
else:
    vitamin_data = {"Iron": "10 mg", "Calcium": "1000 mg", "Vitamin C": "85 mg", "Vitamin D": "600 IU"}

# Output section
print("========== YOUR HEALTH REPORT ==========\n")
print(f"Hey {user_name}, here’s your summary:\n")

print(f"BMI Score: {bmi_value} ({status})")
print(f"Ideal Weight: {ideal_wt} kg")
print(f"Difference: {gap} kg\n")

print(f"Daily Protein: {protein_need} g")
print(f"Daily Carbs: {carb_need} g")
print(f"Daily Fats: {fat_need} g")
print(f"Calories Needed: {cal_need} kcal")

# Water & sleep
water = round(body_weight * 0.033, 2)
print(f"Water Intake: {water} liters/day")

if user_age < 18:
    sleep_need = "8–10 hrs"
elif user_age <= 25:
    sleep_need = "7–9 hrs"
else:
    sleep_need = "7–8 hrs"

print(f"Sleep Recommendation: {sleep_need}")

# Vitamins display
print("\nImportant Nutrients:")
for key, val in vitamin_data.items():
    print(f"{key} → {val}")

# Health score logic
health_points = 100

if status != "Fit":
    health_points -= 20
if lifestyle == "sedentary":
    health_points -= 15
if user_age < 18:
    health_points -= 5

print(f"\nOverall Health Score: {health_points}/100\n")

# Suggestions
if status == "Underweight":
    print(">>> Suggested Plan: Gain Weight")
    print("- Eat more calories (+300 to 500)")
    print("- Include protein foods like paneer, milk, nuts")
    print("- Increase meal frequency")
    print("- Try basic strength workouts")

    extra_wt = abs(gap)
    daily_surplus = round(extra_wt * 7700 / 7)

    print(f"Extra Calories Needed per Day: {daily_surplus}")

elif status == "Overweight" or status == "Obese":
    print(">>> Suggested Plan: Lose Weight")
    print("- Cut down junk and sugar")
    print("- Stay hydrated")
    print("- Do cardio regularly")

    extra_wt = abs(gap)
    daily_deficit = round(extra_wt * 7700 / 7)

    print(f"Calories to Burn Daily: {daily_deficit}")

else:
    print(">>> Suggested Plan: Maintain")
    print("- Keep balanced diet")
    print("- Exercise regularly")
    print("- Sleep well")

# Risk message
print("\nHealth Insight:")
if bmi_value > 30:
    print("High risk of health issues")
elif bmi_value < 18.5:
    print("Low energy & immunity risk")
else:
    print("You are in a healthy range")

print("\n-------- END OF REPORT --------")
print("Thanks for using this system!")
