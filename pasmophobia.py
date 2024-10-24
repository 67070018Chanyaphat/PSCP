def identify_ghost(evidence1, evidence2, evidence3):
    # Ghosts and their evidence
    ghost_evidence = {
        "Banshee": ["EMF Level 5", "Fingerprints", "Freezing Temperatures"],
        "Demon": ["Spirit Box", "Ghost Writing", "Freezing Temperatures"],
        "Jinn": ["EMF Level 5", "Spirit Box", "Ghost Orb"],
        "Mare": ["Spirit Box", "Ghost Orb", "Ghost Writing"],
        "Phantom": ["EMF Level 5", "Ghost Orb", "Freezing Temperatures"],
        "Poltergeist": ["Spirit Box", "Fingerprints", "Ghost Writing"],
        "Revenant": ["EMF Level 5", "Fingerprints", "Ghost Writing"],
        "Shade": ["EMF Level 5", "Ghost Orb", "Ghost Writing"],
        "Spirit": ["Spirit Box", "Fingerprints", "Ghost Writing"],
        "Wraith": ["EMF Level 5", "Spirit Box", "Freezing Temperatures"],
        "Yurei": ["Ghost Orb", "Ghost Writing", "Freezing Temperatures"]
    }

    # Normalize evidence to handle 'No evidence'
    evidence = set([e for e in [evidence1, evidence2, evidence3] if e != "No evidence"])

    possible_ghosts = []
    for ghost, ev in ghost_evidence.items():
        if evidence.issubset(ev):
            possible_ghosts.append(ghost)
    
    if possible_ghosts:
        return "\n".join(sorted(possible_ghosts))
    else:
        return "Not yet discovered"

# Input evidence
evidence1 = input().strip()
evidence2 = input().strip()
evidence3 = input().strip()

# Identify the ghost type
result = identify_ghost(evidence1, evidence2, evidence3)

# Output the result
print(result)
