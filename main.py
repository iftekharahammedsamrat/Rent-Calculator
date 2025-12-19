## Input Section
# Total Rent Amount
# Total food ordered for snaking
# Electricity Units Spend
# Amount Per Unit

## Output Section
# Total Amount you've to pay

# Lets Work with Input Section
from colorama import Fore, Style

try:
    total_rent = int(input("How much your Total Rent :      "))
    total_food = int(input("How many food ordered for snacking? :       "))
    electricity = int(input("Total Electricity Usages (Unit) :      "))
    electricity_price = int(input("Enter Amount Per Unit :      "))
    persions = int(input("Enter Total Number of Persions : "))
except:
    print("Something is Wrong....")

total_amount = (total_rent + total_food  + electricity * electricity_price)  / persions
print(Fore.GREEN + f"Your Total Payable is {total_amount :.2f}" + Style.RESET_ALL)