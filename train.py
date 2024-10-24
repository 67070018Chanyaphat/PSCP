"""283"""
def main():
    """main"""
    first, last = input().split(", ")
    station = {}
    while True:
        name = input()
        if name == "Done":
            break
        name, kilo = name.split(", ")
        station[name] = float(kilo)
        if first in station and last in station:
            break
    if not first in station or not last in station:
        print("Error")
    else:
        print(f"{abs(station[first]-station[last]):.2f}")

main()
