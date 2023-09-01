import eel

from parser.parser import search_car_func


@eel.expose
def result_search(num):
	num = num.replace(" ", "").upper()
	result = search_car_func(num)

	if result is not None:
		car_title, vin_code, description, search_car, owner_car_count, info_list = result

		formatted_info = f"Назва: {car_title}\n\n"
		formatted_info += f"VIN Code: {vin_code}\n\n"
		formatted_info += f"Опис: {description}\n\n"
		formatted_info += f"Розшук: {search_car}\n\n"
		formatted_info += f"Кількість власників: {owner_car_count}\n\n"


		for i, item in enumerate(info_list, start=1):
			formatted_info += f"{i}: {item}\n"

		return formatted_info
    
	else:
		return "Ошибка🤧"

eel.init("web")
eel.start("main.html", size = (500, 600), resizable=False)