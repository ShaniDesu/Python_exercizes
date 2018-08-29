def get_vat(payment, percent=18):
    try:
    	print(percent)
    	payment = float(payment)
    	percent = float(percent)
    	vat = payment / 100 * percent
    	vat = round(vat, 2)
    	return "Сумма НДС: {}".format(vat)
    except (TypeError, ValueError):
    	return "Проверьте правильность ввода"


result = get_vat(570, "10")
	print (result)