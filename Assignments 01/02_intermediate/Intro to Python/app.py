# 🚀 Planetary Weight Calculator

print("🌍 Welcome to the Planetary Weight Calculator! 🚀")
print("--------------------------------------------------")

# Milestone #1 & #2: Get Earth weight and planet input
earth_weight = float(input("Enter your weight on Earth (in kg): "))
planet = input("Enter a planet (e.g., Mars, Jupiter, Venus): ")

# Planetary gravity ratios relative to Earth
gravity_factors = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Calculate and display the planetary weight
if planet in gravity_factors:
    converted_weight = round(earth_weight * gravity_factors[planet], 2)
    print(f"\n🌌 The equivalent weight on {planet}: {converted_weight} kg")
else:
    print("\n❌ Sorry, that's not a recognized planet in our list.")
