import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.BLUE+Back.YELLOW+Style.DIM+"Hello World")
print(Fore.GREEN+Back.CYAN+Style.BRIGHT+"This is a test project of using colorama")
print(Fore.BLACK+Back.WHITE+Style.DIM+"This library is very easy to use!")

'''
Некоторые из наиболее важных атрибутов и методов библиотеки Colorama включают в себя:

-Метод init(): этот метод инициализирует библиотеку Colorama и должен вызываться в начале любого скрипта.
-Класс Fore: этот класс предоставляет набор констант для цветов текста. Примеры: Fore.RED и Fore.GREEN.
-Класс Back: этот класс предоставляет набор констант для цветов фона. Примеры: Back.RED и Back.GREEN.
-Класс Style: этот класс предоставляет набор констант для текстовых стилей, таких как Style.BRIGHT и Style.DIM.(честно,
я не особо понял, в чем разница этих стилей)
-Метод init(autoreset=True): этот метод сбрасывает настройки цвета в конце каждого print, 
чтобы последующий вывод не окрашивался по ошибке.


'''