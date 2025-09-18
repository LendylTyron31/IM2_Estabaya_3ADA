def converter(usd):
    inr_rate = 88.05
    gbp_rate = 0.73325
    cny_rate = 7.11507

    inr = usd * inr_rate
    gbp = usd * gbp_rate
    cny = usd * cny_rate

    return inr, gbp, cny


while True:
    user_input = input("Enter dollar ($) (* to exit): ").split("@")

    if user_input == "*":
        print("Bye")
        break

 
    print("Dollar($) Indian Rupee(R) British Pound(£) China(Y)")

    for x in user_input:
        usd = float(x)   
        inr, gbp, cny = converter(usd)
        print(usd, "   ",round(inr, 2),"      ", round(gbp, 2),"          ", round(cny, 2))