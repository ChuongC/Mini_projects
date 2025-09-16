while True:
    try:
        age = int(input("Nhập tuổi của bạn (từ 1 đến 200): "))
        if 1 <= age <= 200:
            break
        else:
            print("Tuổi phải nằm trong khoảng từ 1 đến 200.")
    except ValueError:
        print("Please try again with number")

while True:
    voucher = input("Có voucher không? (yes/no): ").strip().lower()
    if voucher in ["yes", "no"]:
        break
    else:
        print("Xin vui lòng trả lời 'yes' hoặc 'no'.")

is_child = age < 18
is_adult = 18 <= age <= 59
is_senior = age >= 60



discount = 0

if (is_child or is_senior) and voucher == "yes":
    discount = 0.20
if is_adult and voucher == "yes":
    discount = 0.10
if (is_child or is_senior) and voucher == "no":
    discount = 0.15


PRICE = 649000
discounted_price = PRICE * (1 - discount)

print(f"Bạn được giảm {discount*100:.0f}%, tổng giá tiền là: {discounted_price:.0f} VND")



