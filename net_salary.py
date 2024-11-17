#inputs
name = input("Enter your name: ")
working_hours = input('Working hours: ')
sss_contribution = input('SSS contribution: ')
philhealth_contribution = input('Philhealth contribution: ')
housing_loan = input('Housing loan: ')

rate_per_hour = 500
gross_salary = float(working_hours) * rate_per_hour
#output
info = f"""
=============EMPLOYEE INFORMATION=============
Employee Name: {name} \n
Rendered hours: {working_hours} \n
Rate per Hour: {rate_per_hour} \n
Gross Salary: {gross_salary} \n
"""
print(info)
tax = 500
deduction_total = float(sss_contribution) + float(philhealth_contribution) + float(housing_loan) + tax

print (f"""
=============EMPLOYEE INFORMATION=============


SSS: {sss_contribution} \n
Philhealth: {philhealth_contribution} \n
Other Loan: {housing_loan} \n
Tax : {tax} \n  
Total Deductions: {deduction_total} \n
===============================================
Net Salary: {gross_salary - deduction_total}
""")