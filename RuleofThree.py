"""rule of three"""
def checkkhumkar(price, weight, ratio, k_price, k_weight, k_ratio):
    """ Check """
    if not k_ratio:
        return price,weight,ratio

    if ratio > k_ratio:
        return k_price,k_weight,k_ratio

    if ratio < k_ratio:
        return price,weight,ratio

    if ratio == k_ratio:
        if price < k_price:
            return price,weight,ratio
        return k_price,k_weight,k_ratio

def main():
    """start"""
    n_howmuch = int(input())
    k_price = 0
    k_weight = 0.0
    k_ratio = 0.0
    for _ in range(n_howmuch):
        price = float(input())
        weight = float(input())
        ratio = price / weight
        k_price,k_weight,k_ratio = checkkhumkar( price,weight,ratio,k_price,k_weight,k_ratio )
    print(f"{k_price:.2f} {k_weight:.2f}")
main()
