storona_1 = int(input("Введите количество ячеек на первой стороне шоколадки: "))
storona_2 = int(input("Введите количество ячеек на второй стороне шоколадки: "))
storona_otlom_kuska =int(input("Какой кусок шоколада ты хочешь отломать? "))
if storona_otlom_kuska == storona_2 or storona_otlom_kuska == storona_1:
    print("Ставь кофе, шоколадка твоя")
else:
    print("Что то пошло не так и ты останешься без шоколада")