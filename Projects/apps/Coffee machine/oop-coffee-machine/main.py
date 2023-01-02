
from secrets import choice
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

on = True
cm = CoffeeMaker()
mm = MoneyMachine()
itms = Menu()

while on:
	choice = input("What you want ?(espresso/latte/cappuccino) :")
	if choice == 'off':
		exit()
	elif choice == 'report':
		print(cm.report())
		print(mm.report())
	else:
		drink = itms.find_drink(choice)
		if mm.make_payment(drink) and mm.make_payment:
			cm.make_coffee(drink)

		
	choice=input('Want to continue ? y/n...')
	if choice!='y':
		on=False