# Приложение "клавиатурный тренажер"
В этом репозитории лежит код для проекта 1 по Python, представляющий собой реализацию приложения "клавиатурный тренажер". 
## Начнем с запуска программы через консоль:
1. Установите python версии 3 и выше.
2. Установите нужные библиотеки через pip install:kaleido(нужно для plotly), tkinter, time, pandas, pylab, plotly, matplotlib, pyplot.
3. Склонируйте репозиторий локально в любую удобную папку
4. Откройте консоль(cmd, терминал linux, wsl и т.д)
5. Перейдите в папку, куда сохранили репозиторий
6. Введите `python3 main.py`
## Также можно запустить через IDE(на примере PyCharm):
1. Склонируйте репозиторий локально
2. Откройте программу main.py или папку через IDE
3. IDE скорее всего предложит установить недостающие библиотеки(наведитесь на библиотеки, которые подсвечивает красным и IDE предложит установить её) или установите их вручную, как в пункте 2 в консольном варианте
4. Запускаем программу main.py
## Как использовать приложение:
После запуска откроется окошко приложения, в нем будет:
1. Текстовая зона - это текст, который нужно напечатать
2. Поле для ввода - это поле, куда нужно вводить текст из текстовой зоны
3. Кнопка "Очистить историю статистики" - кнопка, при нажатии на которую статистика предыдущих запусков стирается
4. Кнопка "Показать статистику" - кнопка, при нажатии на которую появляется график скорости печати от номера попытки для отслеживания прогресса
5. Кнопка "Показать heatmap" - кнопка, при нажатии на которую появляется heatmap ошибок(heatmap сохраняется в папку data под названием heatmap.png)
6. Кнопка "Загрузить задания" - кнопка для загрузки собственного задания, задание должно быть с расширением .gna, а также в формате "задание1---задание2---задание3"
   
