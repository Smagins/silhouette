from colorama import Fore
import requests
from bs4 import BeautifulSoup
import os
import webbrowser
import time

passw = input(Fore.YELLOW + "[Password]")

if passw == "635241zQ":

    os.system("cls||clear")

    print(Fore.RED + " ▄▀▀▀▀▄  ▄▀▀█▀▄   ▄▀▀▀▀▄    ▄▀▀▄ ▄▄   ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▀█▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀█▄▄▄▄ ")
    print(Fore.RED + "█ █   ▐ █   █  █ █    █    █  █   ▄▀ █      █ █   █    █ ▐  ▄▀   ▐ █    █  ▐ █    █  ▐ ▐  ▄▀   ▐ ")
    print(Fore.RED + "   ▀▄   ▐   █  ▐ ▐    █    ▐  █▄▄▄█  █      █ ▐  █    █    █▄▄▄▄▄  ▐   █     ▐   █       █▄▄▄▄▄  ")
    print(Fore.RED + "▀▄   █      █        █        █   █  ▀▄    ▄▀   █    █     █    ▌     █         █        █    ▌  ")
    print(Fore.RED + " █▀▀▀    ▄▀▀▀▀▀▄   ▄▀▄▄▄▄▄▄▀ ▄▀  ▄▀    ▀▀▀▀      ▀▄▄▄▄▀   ▄▀▄▄▄▄    ▄▀        ▄▀        ▄▀▄▄▄▄   ")
    print(Fore.RED + " ▐      █       █  █        █   █                         █    ▐   █         █          █    ▐   ")
    print(Fore.RED + "        ▐       ▐  ▐        ▐   ▐                         ▐        ▐         ▐          ▐        ")

    print(Fore.BLUE + "[1] Социальная Инженерия")
    print(Fore.BLUE + "[2] Копирование Сайта для создания IPLogger ссылки")
    print(Fore.BLUE + "[3] открыть IpLogger")
    print(Fore.YELLOW + "[4] Закрыть утилиту")

    run = True

    while run:
        choose = input(Fore.RED + "==>")
        if choose == "1":
            print(Fore.BLUE+"Первое правило: Если прибавить к своей просьбе причину, то отказ человека очень сильно уменьшается\nВторое правило:Хвалить человека, и обещать ему в том что он заинтересован\nГрубо говоря есть 3 пунка:\n1)Заболтать\n2)Заинтересовать\n3)Наебать\nСамое главное это то, за что можно зацепиться\nЕсть книга 'Искусство Обмана' написанная бывшим хакером Кевином Митником, где подробно рассказаны шаги и некоторые фишки социальной инженерии.\nТебе скинуть ссылку? [Да/Нет]")
            yesNo = input(Fore.RED + "#")
            if yesNo == "Да" or yesNo == "да":
                webbrowser.open("https://royallib.com/book/mitnik_kevin/iskusstvo_obmana.html",new=2)
            if yesNo == "Нет" or yesNo == "нет":
                print(Fore.BLUE+"Надумаешь, не стесняйся, бери")
        if choose == "2":
            url = input(Fore.YELLOW+"[URL]:")

            sas = requests.get(url)

            print(sas.text)
        if choose == "3":
            webbrowser.open("https://iplogger.org/ru/", new=2)
        if choose == "4":
            run = False
        if choose == "5":
            print(Fore.RED + "Добро пожаловать на DoxBin детка!")
            time.sleep(3)
            webbrowser.open("https://doxbin.com/", new=2)
        if choose == "1488":
            print(Fore.BLUE+"Пасхалко?)")
    
