"""Bonus"""
def cal_bonus():
    """how much of bonus from salary/years of work/month of work"""
    salary_current = int(input())
    ago_years = int(input())
    ago_month = int(input())
    if ago_month >= 10:
        ago_years+=(ago_month//10)
    ago_years = min(20, ago_years)
    Cal_bonus = min(1000000,salary_current*ago_years)
    if Cal_bonus < 5000:
        Cal_bonus = max(Cal_bonus,5000)
    print(Cal_bonus)
cal_bonus()
