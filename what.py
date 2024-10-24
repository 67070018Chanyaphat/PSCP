def shark_zone(name):
    """Determine the zone based on the given name"""
    shark_zones = {
        "GREAT WHITE SHARK": "THE SHALLOW ZONE",
        "TIGER SHARK": "THE SHALLOW ZONE",
        "HAMMERHEAD SHARK": "THE SHALLOW ZONE",
        "BULL SHARK": "THE SHALLOW ZONE",
        "THRESHER SHARK": "THE SHALLOW ZONE",
        "MAKO SHARK": "THE TWILIGHT ZONE",
        "GOBLIN SHARK": "THE TWILIGHT ZONE",
        "MEGAMOUTH SHARK": "THE TWILIGHT ZONE",
        "GREENLAND SHARK": "THE TWILIGHT ZONE",
        "FRILLED SHARK": "THE TWILIGHT ZONE",
        "COOKIECUTTER SHARK": "THE MIDNIGHT ZONE",
        "LANTERN SHARK": "THE MIDNIGHT ZONE",
        "VELVET BELLY LANTERN SHARK": "THE MIDNIGHT ZONE",
        "DUMPLING SHARK": "THE MIDNIGHT ZONE",
        "BRAMBLE SHARK": "THE MIDNIGHT ZONE"
    }

    # ตรวจสอบว่ามีคำว่า 'shark' ในชื่อหรือไม่
    if "SHARK" in name:
        return shark_zones.get(name, "ZONE JAI MA KLUNG RAK DUAY KAN MAI.")
    else:
        return "ZONE JAI MA KLUNG RAK DUAY KAN MAI."

# Input and Output examples
print(shark_zone("MAHI-MAHI"))  # Output: ZONE JAI MA KLUNG RAK DUAY KAN MAI.
print(shark_zone("MAKO SHARK"))  # Output: THE TWILIGHT ZONE
print(shark_zone("BULL SHARK"))  # Output: THE SHALLOW ZONE
