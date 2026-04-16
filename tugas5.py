DISCOUNT_THRESHOLD = 100000
DISCOUNT_RATE = 0.1

def calculate_total(price1, price2, price3):
    return price1 + price2 + price3

def apply_discount(total):
    if total > DISCOUNT_THRESHOLD:
        return total - (total * DISCOUNT_RATE)
    return total

def print_result(total, final_total):
    print("Total:", total)
    if total != final_total:
        print("Diskon 10% diterapkan")
    print("Bayar:", final_total)

total = calculate_total(50000, 30000, 40000)
final_total = apply_discount(total)
print_result(total, final_total)