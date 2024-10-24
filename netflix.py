'''NETFLIX'''
def convert(word):
    '''convert yes no to true false'''
    passing = False
    if word == 'Yes':
        passing = True
    return passing
def main():
    '''doc'''
    num1 = int(input())
    num2 = int(input())
    package1 = 0
    package2 = 0
    package3 = 0
    package4 = 0
    r1 = convert(input())
    r2 = convert(input())
    r3 = convert(input())
    r4 = convert(input())
    r5 = convert(input())
    while num1 > 0 or num2 > 0:
        premsupreme = ((r4 or r3) and (num1 >= 3 or num2 >= 3))
        stansupreme = r3 and (num1 >= 2 or num2 >= 2)
        if r5 or premsupreme:
            num1 -= 4
            num2 -= 4
            package4 += 1
        elif r4 or stansupreme:
            num1 -= 2
            num2 -= 2
            package3 += 1
        elif r3:
            num1 -= 1
            num2 -= 1
            package2 += 1
        elif r2 or r1 or num1 > 0 or num2 > 0:
            num1 -= 1
            num2 -= 1
            package1 += 1
    total = 0
    if package4:
        total += package4*419
        print(f'Premium x {package4}')
    if package3:
        total += package3*349
        print(f'Standard x {package3}')
    if package2:
        total += package2*279
        print(f'Basic x {package2}')
    if package1:
        total += package1*99
        print(f'Mobile x {package1}')
    print(f'Total = {total} THB')
main()
