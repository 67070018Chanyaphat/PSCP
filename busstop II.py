"""BusStop I"""
def main():
    """Main function to manage bus stops."""
    max_people = int(input())
    count_station = int(input())

    bus_sit = []
    count_people = 0
    stations = {}
    for _ in range(count_station):
        station_data = list(map(int, input().split()))
        station_number = station_data[0]
        if station_number not in stations:
            stations[station_number] = []
        stations[station_number].extend(station_data[1:])

    for station in sorted(stations.keys()):
        bus_sit = [sit for sit in bus_sit if sit > station]

        for destination in stations[station]:
            if len(bus_sit) < max_people:
                if destination > station:
                    bus_sit.append(destination)
                    count_people += 1

    print(count_people)

main()
