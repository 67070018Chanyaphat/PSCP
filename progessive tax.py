"""progessive"""
import math
def main():
    """start"""
    sum_salary = int(input())
    sum_tax = 0
    if 0 <= sum_salary <= 150000:
        pass
    else:
        if 150000 < sum_salary <= 300000:
            sum_salary -= 150000
            sum_tax+= sum_salary*0.05
        elif 300000 < sum_salary <= 500000:
            sum_salary -= 150000
            sum_tax+= 150000*0.05
            sum_salary -= 150000
            sum_tax+= sum_salary*0.10
        elif 500000 < sum_salary <= 750000:
            sum_salary -= 150000
            sum_tax+= 150000*0.05
            sum_salary -= 150000
            sum_tax+= 200000*0.10
            sum_salary -= 200000
            sum_tax+= sum_salary*0.15
        elif 750000 < sum_salary <= 1000000:
            sum_salary -= 150000
            sum_tax+= 150000*0.05
            sum_salary -= 150000
            sum_tax+= 200000*0.10
            sum_salary -= 200000
            sum_tax+= 250000*0.15
            sum_salary -= 250000
            sum_tax+= sum_salary*0.20
        elif 1000000 < sum_salary <= 2000000:
            sum_salary -= 150000
            sum_tax+= 150000*0.05
            sum_salary -= 150000
            sum_tax+= 200000*0.10
            sum_salary -= 200000
            sum_tax+= 250000*0.15
            sum_salary -= 250000
            sum_tax+= 250000*0.20
            sum_salary -= 250000
            sum_tax+= sum_salary*0.25
        elif 2000000 < sum_salary <= 4000000:
            sum_salary -= 150000
            sum_tax+= 150000*0.05
            sum_salary -= 150000
            sum_tax+= 200000*0.10
            sum_salary -= 200000
            sum_tax+= 250000*0.15
            sum_salary -= 250000
            sum_tax+= 250000*0.20
            sum_salary -= 250000
            sum_tax+= 1000000*0.25
            sum_salary -= 1000000
            sum_tax+= sum_salary*0.30
        elif sum_salary > 4000000:
            sum_salary -= 150000
            sum_tax+= 150000*0.05
            sum_salary -= 150000
            sum_tax+= 200000*0.10
            sum_salary -= 200000
            sum_tax+= 250000*0.15
            sum_salary -= 250000
            sum_tax+= 250000*0.20
            sum_salary -= 250000
            sum_tax+= 1000000*0.25
            sum_salary -= 1000000
            sum_tax+= 2000000*0.30
            sum_salary -= 2000000
            sum_tax+= sum_salary*0.35

    print(f"{math.floor(sum_tax)}")
main()
