# Outfit Recommender (Basic Version)
# Author: Jisin

def recommend_outfit(weather, occasion):
    if weather == "sunny":
        if occasion == "casual":
            return "T-shirt, shorts, and sunglasses 😎"
        elif occasion == "formal":
            return "Light shirt, trousers, and loafers 👔"
    elif weather == "rainy":
        if occasion == "casual":
            return "Raincoat, jeans, and waterproof shoes ☔"
        elif occasion == "formal":
            return "Blazer, formal pants, and umbrell
