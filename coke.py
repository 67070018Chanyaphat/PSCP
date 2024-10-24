def calculate_min_cost():
    # Read inputs
    a = int(input().strip())  # Price of one bottle
    b = int(input().strip())  # Caps needed for discount
    c = int(input().strip())  # Discounted price when trading caps
    d = int(input().strip())  # Number of bottles needed

    # Case where no bottles are needed
    if d == 0:
        print(0)
        return

    # If b is 0, you can never use caps, must buy at full price
    if b == 0:
        print(d * a)
        return

    # Minimum cost starts with buying all at full price
    min_cost = d * a

    # Track the number of caps and bottles bought
    caps = 0
    bottles_bought = 0

    # Loop until we need to buy bottles
    while bottles_bought < d:
        # Buy a new bottle at full price
        bottles_bought += 1
        caps += 1  # Gain a cap for the bottle bought

        # Calculate cost if we only buy at full price
        if bottles_bought <= d:
            min_cost = min(min_cost, bottles_bought * a + (d - bottles_bought) * a)

        # If we have enough caps to exchange for a discounted bottle
        while caps >= b and bottles_bought < d:
            # Trade in caps for a discounted bottle
            caps -= b  # Use the required caps
            bottles_bought += 1  # Get another bottle

            # Calculate cost with discounted bottles
            if bottles_bought <= d:
                min_cost = min(min_cost, (bottles_bought * c) + (d - bottles_bought) * a)

    print(min_cost)

calculate_min_cost()
