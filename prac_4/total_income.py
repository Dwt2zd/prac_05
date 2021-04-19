"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = get_month_number(incomes)
    report_printing(incomes, months)


def report_printing(incomes, months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


def get_month_number(incomes):
    months = int(input("How many months? "))
    for month in range(1, months + 1):
        income = float(input("Enter income for month {:2}: ".format(month)))
        incomes.append(income)
    return months


main()