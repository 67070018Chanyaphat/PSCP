"""digitalllll"""
def digital():
    """Moneyyyyy"""
    name = input()
    national = input()
    homeinthai = input()
    age = float(input())
    income = float(input())
    balance = float(input())
    con1 = national in ('True','Yes') and homeinthai in ('True','Yes')
    con2 = age >= 16 and balance <= 500000
    con3 = income <= 840000
    con4 = balance <= 500000
    if con1 and con2 and con3 and con4:
        print(f"Congratulations! {name} is qualified to receive a digital wallet \
amount of 10,000 baht, sponsored by all taxpayers in Thailand.")
    else:
        print(f'Unfortunately, {name} is not qualified.')
digital()
