"""Meteorite"""
def main():
    """Meteorite"""
    weight = float(input()) 
    broken = int(input()) 
    safe = float(input()) 
    shoot = 0
    rocket = 0
    while weight >= safe:
        weight /= broken
        shoot += 1 
    racket = broken**shoot
    print(racket)
main()