# have_classToday = False
# have_classTomorrow = False
# learn = "Learning is Essential"
#
# if have_classToday:
#     print("It's mathematics")
#     print("Learn very hard")
# elif have_classTomorrow:
#     print("Rest a little bit")
#     print("Learn ahead")
# else:
#     print("Relax and enjoy for sometime")
#     print("But make sure you learn")
# print(learn.upper())

# Exercise
# PRICE OF A HOUSE IS $1M if buyer has good credit,put down 10% else put down 20%. print the down credit
Price = 1000000
Has_GoodCredit = True

if Has_GoodCredit:
    down_payment = 0.1 * Price
else:
    down_payment = 0.2 * Price
print(f"Down Payment: ${int(down_payment)}")
