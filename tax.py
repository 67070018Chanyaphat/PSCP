"""tax"""
def calculate_tax(years, cc):
    """Calculate car tax based on engine size and age of the car."""
    if cc <= 600:
        total_tax = cc * 0.50
    elif cc <= 1800:
        total_tax = (600 * 0.50) + ((cc - 600) * 1.50)
    else:
        total_tax = (600 * 0.50) + (1200 * 1.50) + ((cc - 1800) * 4.00)

    if years >= 10:
        total_tax *= 0.50
    elif years == 9:
        total_tax *= 0.60
    elif years == 8:
        total_tax *= 0.70
    elif years == 7:
        total_tax *= 0.80
    elif years == 6:
        total_tax *= 0.90

    return total_tax

def main():
    """Main function to read input and calculate the tax."""
    years = int(input())
    cc = int(input())
    car_tax = calculate_tax(years, cc)
    print(f"{car_tax:.2f}")

if __name__ == "__main__":
    main()
