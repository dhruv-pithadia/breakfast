import random

def run_fuzzy_logic(hunger, time, goal, activity, preference):
    """
    Applies simple fuzzy-style logic to map user inputs to:
    - Meal Category (Light, Medium, Medium-Heavy, Heavy)
    - Suggested Dish
    - Image path
    - Fun Tagline
    """

    # Convert inputs to numeric scores
    score = 0
    score += int(hunger)  # 1–3
    score += int(time)    # 1–3
    score += {"weight_loss": 1, "maintenance": 2, "weight_gain": 3}[goal]
    score += {"low": 1, "medium": 2, "high": 3}[activity]

    # Determine meal category based on fuzzy score
    if score <= 6:
        category = "light"
    elif score <= 9:
        category = "medium"
    elif score <= 11:
        category = "medium-heavy"
    else:
        category = "heavy"

    # Dish data
    dish_list = {
        "light": {
            "veg": [
                "Fruit Bowl", "Vegetable Soup", "Poha", "Upma",
                "Cucumber Sandwich", "Oats Porridge", "Idli with mint chutney"
            ],
            "nonveg": [
                "Boiled Egg Plate", "Egg Salad", "Tuna Lettuce Wrap"
            ]
        },
        "medium": {
            "veg": [
                "Sprout Salad", "Aloo Paratha (1 pc) with curd", "Methi Thepla",
                "Banana Peanut Butter Sandwich", "Vegetable Maggie",
                "Moong Dal Cheela", "Avocado Toast"
            ],
            "nonveg": [
                "Omelette + Toast", "Egg Fried Rice (small portion)", "Chicken Sandwich (grilled)"
            ]
        },
        "medium-heavy": {
            "veg": [
                "Paneer Bhurji + Roti", "Vegetable Pulao", "Masala Dosa",
                "Sabudana Khichdi", "Pasta with veggies",
                "Mini Veg Burrito", "Veggie Burger (small)"
            ],
            "nonveg": [
                "Chicken Pulao", "Egg Bhurji + Toast", "Grilled Chicken Wrap"
            ]
        },
        "heavy": {
            "veg": [
                "Chole Bhature", "Stuffed Paratha (2 pcs)", "Pav Bhaji",
                "Aloo Poori", "Masala Pav", "Rava Dosa + Chutney", "Mac & Cheese"
            ],
            "nonveg": [
                "Chicken Biryani", "Egg Curry + Rice", "Full English Breakfast (bacon, sausage, eggs)"
            ]
        }
    }

    # Fun meal taglines
    taglines = {
        "light": "Keep it light and fresh 🌱",
        "medium": "Balance is key ⚖️",
        "medium-heavy": "Fuel up with flavor 🍛",
        "heavy": "Power up like a boss 💪"
    }

    # Choose a dish
    selected_dish = random.choice(dish_list[category][preference])
    
    # Generate image path
    folder_name = selected_dish.lower().replace(" ", "_").replace("(", "").replace(")", "").replace("+", "plus").replace("&", "and").replace(",", "").replace("-", "_")
    category_folder = category.replace(" ", "-")
    image_path = f"images/{category_folder}/{folder_name}/{folder_name}.jpg"

    # Return meal type, dish, image, and fun line
    return category.capitalize(), selected_dish, image_path, taglines[category]