"""Impostor"""
import json

def update_player_status(person, tmp):
    """Update player status from JSON input."""
    try:
        person.update(json.loads(tmp))
    except json.JSONDecodeError:
        print("Invalid JSON input. Please try again.")

def main():
    """Impostor Game Status Tracker."""
    person = {}
    dead = {}
    alive = {}
    impostors_count = 0

    while True:
        tmp = input()
        if tmp.upper() == "END":
            break
        if tmp.upper() == "START":
            continue
        if tmp[0] == "{":
            update_player_status(person, tmp)
        else:
            if tmp in person:
                dead[tmp] = person[tmp]
            else:
                print(f"Player {tmp} does not exist.")

    alive = {name: role for name, role in person.items() if name not in dead}

    impostors_count = sum(1 for role in alive.values() if role == "Impostor")

    print(f"{impostors_count} Impostor Remains")
    print("***Alive***")
    for name in sorted(alive):
        print(f"{name} : {alive[name]}")
    print("***Dead***")
    for name in sorted(dead):
        print(f"{name} : {dead[name]}")

if __name__ == "__main__":
    main()
