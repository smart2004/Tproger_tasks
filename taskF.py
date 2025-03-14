# Write code to transfer any integer number into string,
# It may be applied in any number system.

def int_to_str(num, base):
    if base < 2 or base > 36:
        raise ValueError('Основание системы счисления должно быть в диапазоне от 2 до 36')
