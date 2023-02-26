storona_1 = int(input("Введите количество ячеек на первой стороне шоколадки: "))
storona_2 = int(input("Введите количество ячеек на второй стороне шоколадки: "))
i_want_choco =int(input("Сколько кусочков шоколада ты хочешь отломать? "))
if storona_2 * storona_1 > i_want_choco and (i_want_choco % storona_1 == 0 or i_want_choco % storona_2 == 0):
    print("Ставь кофе, шоколадка твоя")
else:
    print("Что то пошло не так и ты останешься без шоколада")