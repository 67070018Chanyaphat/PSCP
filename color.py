def mix_colors(color1, color2):
    # Define the color mixing rules
    color_mixing_rules = {
        ("red", "yellow"): "Orange",
        ("yellow", "red"): "Orange",
        ("red", "blue"): "Violet",
        ("blue", "red"): "Violet",
        ("yellow", "blue"): "Green",
        ("blue", "yellow"): "Green"
    }
    
    # Normalize colors to lowercase for comparison
    color1 = color1.strip().lower()
    color2 = color2.strip().lower()
    
    # Set of primary colors
    primary_colors = {"red", "yellow", "blue"}
    
    # Check if both colors are primary colors
    if color1 not in primary_colors or color2 not in primary_colors:
        return "Error"
    
    # Return the mixed color if valid
    return color_mixing_rules.get((color1, color2), "Error")

# Read inputs
color1 = input().strip()
color2 = input().strip()

# Get the result
result = mix_colors(color1, color2)

# Output the result
print(result)
