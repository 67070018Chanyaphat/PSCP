"""digital_wallet"""
def digital_check():
    """check from identify"""
    name = input()
    thai_check = input()
    home_check = input()
    age = float(input())
    salary_peryear = float(input())
    bank = float(input())
    user = ""
    status = ""
    describe1 = ""
    describe2 = ""
    #######################
    if thai_check in ("Yes","True") and home_check in ("Yes","True"):
        if age >= 16 and bank <= 500000:
            if salary_peryear <= 840000:
                status = "Congratulations!"
                describe1 = "is qualified to receive a digital wallet amount of 10,000 baht"
                describe2 = ", sponsored by all taxpayers in Thailand."
            else:
                status = "Unfortunately,"
                describe1 = "is not qualified."
                describe2 = ""
        else:
                status = "Unfortunately,"
                describe1 = "is not qualified."
                describe2 = ""
    else:
        status = "Unfortunately,"
        describe1 = "is not qualified."
        describe2 = ""
    pass_person = status+" "+name+" "+describe1+describe2
    print(pass_person)
digital_check()
