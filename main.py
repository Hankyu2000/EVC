# Expected Value Calculator for Class number
# Formula by Ishikawa
# Developed by Yuduki
# Supported by Our Group Member.
import math as math
import fractions as frac
import tkinter

def main():
    amount_of_class = input("クラス何個？(デフォルト値:5)")
    if amount_of_class is None or not amount_of_class.isdigit() :
        amount_of_class = 5
        print("デフォルト値の5で実行します。")
    else:
        amount_of_class = int(amount_of_class)
    target_number = input("学籍番号のka22以降の数字を入力")
    target_number = int(target_number)
    forward_to_target = target_number - 1
    class_possibility = frac.Fraction(1, amount_of_class)
    c = frac.Fraction(0, 1)
    for x in range(0, target_number):
        temp = frac.Fraction(1, 1)
        temp = temp * math.comb(forward_to_target, x)
        print("exec" + str(forward_to_target) + "C" + str(x))
        temp = temp * (class_possibility ** x) * ((1 - class_possibility) ** (forward_to_target - x))
        print(temp * x)
        c = c + temp * x
    print(float(c) + 1)
    print(bin(int(c)))


if __name__ == "__main__":
    main()

