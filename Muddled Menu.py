"""Muddled Menu"""
def process_menu(food):
    """Recursive function to process the menu commands."""
    txt = input().strip()

    if txt == "DONE":
        return food

    if txt == "SOMETHING'S WRONG":
        return process_menu([])

    if txt == "CLOSED":
        return []

    if "Can't do:" in txt:
        _, item = txt.split(": ")
        if item in food:
            food.remove(item)
        return process_menu(food)


    dish, pos = txt.split(" #")
    if pos == "N":
        food.append(dish)
    else:
        food.insert(int(pos) - 1, dish)
    return process_menu(food)

def main():
    """Main function to handle the full menu input process."""
    food = process_menu([])
    print(f"Full Course: {food} Reversed: {food[::-1]}")

main()
