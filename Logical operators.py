 # printing "eligible for loan" if an applicant has high income and good credit using AND OR NOT operators

has_HighIncome = True
has_GoodCredit = True

if has_HighIncome and has_GoodCredit:
    print("Eligible for Loan")

if has_HighIncome or has_GoodCredit:
    print("Eligible for Loan")

if has_HighIncome and not has_GoodCredit:
    print("Eligible for Loan")