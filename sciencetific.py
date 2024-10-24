"""Scientific"""
def to_sci(text):
    """Convert normal notation to scientific notation."""
    left_digit = text[:text.find(".")].strip()
    right_digit = text[text.find(".") + 1:].strip()
    power = 0

    if 1 <= float(text) < 10:
        return f"{left_digit}" + f".{right_digit}" * bool(right_digit) + f" x 10^{power}"

    if float(text) >= 10:
        power = len(left_digit) - 1
        if not right_digit:
            left_digit = str(int(left_digit[::-1]))[::-1]
        left_digit = left_digit.replace(".", "")
        return (f"{left_digit[0]}" + "." * (len(left_digit) > 1) +
                f"{left_digit[1:]}{right_digit} x 10^{power}")

    for i in right_digit:
        power += 1
        if i != "0":
            break

    right_digit = str(int(right_digit))
    return f"{right_digit[0]}" + "." * bool(len(right_digit) > 1) + \
        f"{right_digit[1:]} x 10^-{power}"

def to_norm(text):
    """Convert scientific notation to normal notation."""
    if "." not in text[:text.find("x")]:
        text = text[:text.find("x")].strip() + "." + text[text.find("x"):].strip()

    left_digit = text[:text.find(".")].strip()
    right_digit = text[text.find(".") + 1:text.find("x")].strip()
    power = int(text[text.find("^") + 1:].strip())

    if power < 0:
        left_digit = "0" * abs(power) + left_digit
        return f"{left_digit[0]}.{left_digit[1:]}{right_digit}"

    if power > 0:
        right_digit = right_digit.ljust(power, "0")
        return f"{left_digit}{right_digit[:power]}.{right_digit[power:]}"

    return left_digit + "." + right_digit

def main():
    """Main function."""
    text = str(input()).strip()
    negative = False

    if text[0] == "-":
        negative = True
        text = text[1:]

    if "x" in text:
        result = to_norm(text)
    else:
        text += "." * (text.count(".") < 1)
        if not float(text):
            print(0)
            return
        result = to_sci(text)

    if not result[result.find(".") + 1:]:
        result = result.replace(".", "")

    print(("-" if negative else "") + result)

main()
