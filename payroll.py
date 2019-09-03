from datetime import date

def overtime(hours):
    if hours <= 40:
        hrs = hours
        ot = 0
    if hours > 40:
        ot = hours - 40
        hrs = 40
    return hrs, ot

def grosspay(hours, overtimeHours, payrate):
    regularPay = hours*payrate
    overtimePay = overtimeHours*payrate*2.5
    grossPayAmount = regularPay + overtimePay
    return grossPayAmount

def incomeTax(grossPaying):
    incomeTaxAmount = grossPaying*0.3
    return incomeTaxAmount

def netPay(grossPaying, incomeTax):
    netPaying = grossPaying - incomeTax
    return netPaying


def main():
    today = date.today()
    stop = False
    customer = str

    while stop == False:
        customer = input("Please enter the name of employee or '1' to exit: ")
        if customer == '1':
            print("Program closed")
            stop == True
            exit()
        else:
            employee_id = input("Please enter employee ID: ")
            gender = input("Please enter the gender of employee (M or F): ")
            phone = input("Please enter the contact number of employee: ")
            print()
            hours = float(input("Please enter total worked hours: "))
            payrate = float(input("Please enter your hourly payrate: $" ))
            print()
            date1 = input("Enter 'Paying From' date in DD-MM-YYYY Format: ")
            date2 = input("Enter 'Paying Upto' date in DD-MM-YYYY Format: ")

            hrs, ot = overtime(hours)

            grosspaying = grosspay(hrs, ot, payrate)

            incomeTaxAmount = incomeTax(grosspaying)

            netPaying = netPay(grosspaying, incomeTaxAmount)
            print()
            print()
            print('#'*73)
            print('\t\t\t\t\t\t\t\t\t')
            print(' Danny\'s IceCream Parlour\t\t\t\tABN: 222.333.145')
            print('\t\t\t\t\t\t\t\t\t')
            print(' Employee: ',customer,' \t\t\t\t\t\t')
            print(' \t\t\t\t\t Payment Date: ',today,' \t')
            print(' Gross Pay: $',grosspaying,'\t\t\t\t\t\t \t')
            print(' Net Pay: $',netPaying,' \t\t\t\t\t\t \t')
            print('\t\t\t  Pay Period from: ',date1,' To ',date2,'\t')
            print('\t\t\t\t\t\t\t\t\t')
            print(' Item \t\t\t Total Hours \t Calculated Rate \t Type \t')
            print(' --------------------------------------------------------------------- ')
            print(' Base Hourly @',payrate,' \t ',hours,'(',ot,' OT) \t $',grosspaying,' \t Wages \t')
            print(' PAYG Withholding \t   ___ \t\t\t -$',incomeTaxAmount,' \t Tax \t')
            print('\t\t\t\t\t\t\t\t\t')
            print(' *OT: Over Time\t\t\t\t\t\t\t')
            print('#'*73)
            print()
            print()


if __name__ == "__main__":
    main()

