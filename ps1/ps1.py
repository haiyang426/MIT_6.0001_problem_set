if __name__ == "__main__":
    portion_down_payment = 0.25
    current_saving = 0
    r = 0.04

    #problem a & b
    # annual_salary = int(input("Enter your annual salary"))
    # portion_saved = float(input("Enter the percent of your salary to save, as a decimal"))
    # total_cost = int(input("Enter the cost of your dream house"))
    # semi_annual_raise = float(input("Enter the semi annual raise, as a decimal:"))

    start_annual_salary = int(input("Enter the starting salary"))
    semi_annual_raise = 0.07
    total_cost = 1000000

    monthly_salary = start_annual_salary/12
    month = 0

    high_rate = 10000
    low_rate = 0
    step = 0

    while low_rate <= high_rate:
        portion_saved = (high_rate+low_rate)//2
        step += 1
        current_saving = 0
        month = 0
        monthly_salary = start_annual_salary/12

        while month < 36:
            month += 1
            current_saving += current_saving*r/12 + monthly_salary*(portion_saved/10000)
            if month % 6 == 0:
                monthly_salary = monthly_salary*(1+semi_annual_raise)

        print(current_saving - total_cost*portion_down_payment)
        if abs(current_saving - total_cost*portion_down_payment) <= 100:
            break
        if current_saving < (total_cost*portion_down_payment):
            low_rate = portion_saved + 1
        else:
            high_rate = portion_saved - 1

    if abs(current_saving - total_cost*portion_down_payment) <= 100:
        print("best saving rate", portion_saved)
        print("step in bisection", step)
    else:
        print("it is not possible to pay the down payment in three years")
