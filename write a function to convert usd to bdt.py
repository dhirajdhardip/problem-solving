def converter(usd_value, rate):
    taka_value = usd_value * rate
    print(usd_value, "USD =", round(taka_value, 2), "TAKA", "(Rate:", rate, ")")
    return taka_value

usd_value = float(input("Enter the USD amount: "))
rate = float(input("Enter today's USD to TAKA rate: "))

taka_value = converter(usd_value, rate)
