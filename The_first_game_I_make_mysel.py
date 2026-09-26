import time
def the_fn_game():
	while True:
		input_orders_game=input("             ")
		if input_orders_game=="start" or input_orders_game=="ابداء":
			print("اللعبة تبداء الان")
		elif input_orders_game=="box":
			print("اللاعب يضرب بوكس")
		elif input_orders_game=="stop":
			print("اللعبة انتهت")
			break
		else:
			print("هذا الامر غير معرف")
		time.sleep(1)
the_fn_game()