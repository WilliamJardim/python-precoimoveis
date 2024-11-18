import json;
import random;
num_samples = 5000;

random.seed(-5);

# Define ranges and possible values for features, now with realistic patterns
def generate_realistic_price(age, area, bedrooms, bathrooms, floors, has_garage, has_garden, location_score):
    # Base price influenced by area, location, and amenities
    base_price = (area * 200) + (location_score * 10000) + (bedrooms * 5000) + (bathrooms * 3000)
    # Adjustments for additional factors
    base_price += (floors * 2000) + (has_garage * 15000) + (has_garden * 10000)
    # Depreciation based on age
    base_price *= max(0.5, 1 - (age / 100))
    # Add noise for realism
    return round(base_price + random.uniform(-20000, 20000))

def generate_realistic_bought(price, location_score, has_garden, has_garage, income_level):
    # Ajusta a probabilidade de compra com base no preço, renda e outros fatores
    base_probability = (income_level / 100000) - (price / 500000)
    
    # Fatores adicionais para aumentar a chance de não compra
    probability = max(0.05, min(0.95, base_probability + (location_score / 10) + (has_garden * 0.2) + (has_garage * 0.1)))
    
    # Adiciona variação para tornar a decisão menos determinística
    if random.uniform(0, 1) < probability:
        return 1  # Comprou
    else:
        return 0  # Não comprou

# Generating dataset
realistic_dataset = []
for _ in range(num_samples):
    age = random.randint(0, 50)
    area = random.randint(500, 5000)
    bedrooms = random.randint(1, 6)
    bathrooms = random.randint(1, 5)
    floors = random.randint(1, 3)
    has_garage = random.choice([0, 1])
    has_garden = random.choice([0, 1])
    location_score = random.uniform(1, 10)
    income_level = random.randint(30000, 200000)

    # Generate price and bought based on patterns
    price = generate_realistic_price(age, area, bedrooms, bathrooms, floors, has_garage, has_garden, location_score)
    bought = generate_realistic_bought(price, location_score, has_garden, has_garage, income_level)

    # Append to dataset
    realistic_dataset.append({
        "id": _,
        "age": age,
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "floors": floors,
        "has_garage": has_garage,
        "has_garden": has_garden,
        "location_score": round(location_score, 2),
        "income_level": income_level,
        "price": price,
        "bought": bought
    })

# Write the realistic dataset to a JSON file
realistic_output_path = "./realistic_real_estate_dataset.json"
with open(realistic_output_path, "w") as file:
    json.dump(realistic_dataset, file, indent=4)

print(realistic_output_path);
