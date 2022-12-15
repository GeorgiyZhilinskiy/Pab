import sys

lambda_CX1 = lambda t: 64.496 + 0.0659625*t +0.224306*pow(10,-2)*pow(t,2) - 0.105729*pow(10,-4)*pow(t,3)
lambda_CX2 = lambda t: 64.496 + 0.066027*t + 0.2241304*pow(10,-2)*pow(t,2) - 0.10560396*pow(10,-4)*pow(t,3)
lambda_CX3 = lambda t: 64.4724 + 8.1564207 * pow(10,-2)*t + 2.3034122*pow(10,-4)*pow(t,2.8) - 2.6492852*pow(10,-5)*pow(t,3.3) + 2.4826037 * pow(10,-8)*pow(t,4.5)
lambda_CX4 = lambda t: 64.18 + 0.1348*t + 5.31*pow(10,-4)*pow(t,2)
lambda_CX5 = lambda t: 63.308 + 0.133*t + 7.22*pow(10,-4)*pow(t,2)

# пункт 1
def FuncCX1(t):
    return 64.496 + 0.0659625*t +0.224306*pow(10,-2)*pow(t,2) - 0.105729*pow(10,-4)*pow(t,3)
def FuncCX2(t):
    return 64.496 + 0.066027 * t + 0.2241304 * pow(10, -2) * pow(t, 2) - 0.10560396 * pow(10, -4) * pow(t, 3)
def FuncCX3(t):
    return 64.4724 + 8.1564207 * pow(10, -2) * t + 2.3034122 * pow(10, -4) * pow(t, 2.8) - 2.6492852 * pow(10, -5) * pow(t,3.3) + 2.4826037 * pow(10, -8) * pow(t, 4.5)
def FuncCX4(t):
    return 64.18 + 0.1348*t + 5.31*pow(10,-4)*pow(t,2)
def FuncCX5(t):
    return 63.308 + 0.133*t + 7.22*pow(10,-4)*pow(t,2)

t = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
EZN = [64.44, 65.4, 66.74, 68.36, 70.22, 72.24, 74.32, 76.51, 78.74, 80.86]

# Вычисляем значения функций в при заданных аргументах
CX1 = list(map(FuncCX1, t))
CX2 = list(map(FuncCX2, t))
CX3 = list(map(FuncCX3, t))
CX4 = list(map(FuncCX4, t))
CX5 = list(map(FuncCX5, t))

# Выводим результат, а для lambda  функций считаем срозу при выводе
print("Выводим результат полученный обычными функциями", "\n")
print("EZN= ", list(EZN), "\n")
print("СХ1= ", list(CX1), "\n")
print("СХ2= ", list(CX2), "\n")
print("СХ3= ", list(CX3), "\n")
print("СХ4= ", list(CX4), "\n")
print("СХ5= ", list(CX5), "\n")

print("Выводим результат полученный lambda функциями", "\n")
print("EZN= ", list(EZN), "\n")
print("СХ1= ", list(map(lambda_CX1, t)), "\n")
print("СХ2= ", list(map(lambda_CX2, t)), "\n")
print("СХ3= ", list(map(lambda_CX3, t)), "\n")
print("СХ4= ", list(map(lambda_CX4, t)), "\n")
print("СХ5= ", list(map(lambda_CX5, t)), "\n")

# Определяем наиболее подходящую форулу
# Наиболее подходящей будем считать формулу, дающую наименьшую погрешность в заданных значений аргумента (температур)
# Отклонение формулы от экспериментальных хначений (погрешностью) считаем MAX|EZN(t)-CXi(t)|, t пробегает значения 0, 10, 20, 30, 40, 50, 60, 70, 80, 90

# Вычисление отклонения между списками одинаковой длины
def vmathdifference(List1, List2):
  n = len(List1)
  m = len(List2)
  # не проверяем, что второй список длиннее
  d = 0.0
  if n>0:
     i = 0
     while i < n:
       d = max(d, abs(List1[i]-List2[i]))
       i = i + 1
     return d
  else:
    return -1

d = vmathdifference (list(EZN), list(CX1))
Nopt = 1
if (vmathdifference (list(EZN), list(CX2)) < d):
    d = vmathdifference (list(EZN), list(CX2))
    Nopt = 2
if (vmathdifference (list(EZN), list(CX3))  < d):
    d = vmathdifference (list(EZN), list(CX3))
    Nopt = 3
if (vmathdifference (list(EZN), list(CX4)) < d):
    d = vmathdifference (list(EZN), list(CX4))
    Nopt = 4
if (vmathdifference (list(EZN), list(CX5)) < d):
    d = vmathdifference (list(EZN), list(CX5))
    Nopt = 5

# Выводим номер наиболее подходящей формулы и отклонение
print("Наиболее подходящая формула СХ", str(Nopt), "\n")
print("Отклонение наиболее подходящей формулы от эксп. данных ", str(d), "\n")

# Функция вывода строки таблицы в файл
# Сначала выводится тестовое название строки (description), потом табличные значения с разделителем tab


#
# ЧИТАЕМ ДАННЫЕ ИЗ КОНСОЛИ (1) ИЛИ ФАЙЛВ (2) И ПИШЕМ В ФАЙЛ
#
while 1:
    try:
        print("Укажите источник данных. Консоль (1) или файл (2)")
        source = int(input())
        if (source == 1 or source  == 2 ):
            break
        else:
            print("Для выбора источника данных введите 1 или 2")
    except:
        print("Для выбора источника данных введите 1 или 2")

list_t = [] # в данный список будем считывать значения температур из консоли или из файла
list_CX = [] # в данный список будем считывать значения концентраций из консоли или из файла

if ( source == 2 ) :
    # expdata_file содержит экспериментальные данные
    # expdata_file в первой строке должен содержать краткое обозначение для температур и единицу измерения
    # expdata_file во второй строке список температур для которых получено экспериментальные значения, разделенные пробелами
    # expdata_file в третьей строке должен содержать краткое обозначение для измеренных результетов и единицу измерения
    # expdata_file в четвертой строке список измеренных концентраций в процессе эксперимента, разделенные пробелами
    try:
        with open("Lab6_text_file.txt", encoding = 'utf-8', mode = "r") as expdata_file:
            # Тут надо проверить, что файл читается, что количество значений температур и количество концентраций одинаковое
            line_ = expdata_file.readline() # читаем 1-ю строку c заголовком
            line_ = expdata_file.readline()  # читаем 2-ю строку со значениями температур
            list_t = list(map(float, line_.split(" ")))
            line_ = expdata_file.readline()  # читаем 3-ю строку с заголовком
            line_ = expdata_file.readline()  # читаем 4-ю строку со значениями концентраций
            list_CX = list(map(float, line_.split(" ")))
            expdata_file.close()
            if (len(list_t) > len(list_CX)):
                print("Неправильный список экспериментальных данных, возможно не все данные заполнены")
                sys.exit()
    except FileNotFoundError:
        print("Файл Lab6_text_file.txt с исходными данными не найден")
        sys.exit()
    except IOError:
        print("Ошибка ввода-вывода")
        sys.exit()
    except ValueError:
        print("Неправильный формат данных, используйте числа с разделителем точка")
        sys.exit()
else:
    while 1:
        try:
            print("Введите количество значений измерений:")
            n = int(input('-->> '))
            if (n > 0):
                break
            else:
                print("Количество измерений должно быть больше 0")
        except:
            print("Количество измерений должно быть целым числом больше 0")
    i = 0
    while i < n:
        while 1:
            try:
                print("Введите результат", i, " измерения температуры ")
                a = float(input('-->> '))
                print("Введите результат", i, " измерения концентрации ")
                b = float(input('-->> '))
                list_t.append(a)
                list_CX.append(b)
                i = i + 1
                break
            except:
                print("Данные измерений должны быть действительными числами. Используйте разделитель точка")
try:
    CX1 = list(map(FuncCX1, list_t))
    CX2 = list(map(FuncCX2, list_t))
    CX3 = list(map(FuncCX3, list_t))
    CX4 = list(map(FuncCX4, list_t))
    CX5 = list(map(FuncCX5, list_t))

    d = vmathdifference (list(list_CX), list(CX1))
    Nopt = 1
    if (vmathdifference (list(list_CX), list(CX2)) < d):
        d = vmathdifference (list(list_CX), list(CX2))
        Nopt = 2
    if (vmathdifference (list(list_CX), list(CX3))  < d):
        d = vmathdifference (list(list_CX), list(CX3))
        Nopt = 3
    if (vmathdifference (list(list_CX), list(CX4)) < d):
        d = vmathdifference (list(list_CX), list(CX4))
        Nopt = 4
    if (vmathdifference (list(list_CX), list(CX5)) < d):
        d = vmathdifference (list(list_CX), list(CX5))
        Nopt = 5
except  ArithmeticError:
    print("Арифметические ошибки. Попробуйте другие значения")
    sys.exit()
    
def writetabline(file_, descript, list_):
    try:
        file_.write("\n")
    except:
        print("Жилинский, неправильный аргумент file_")
        return -1
    file_.write(str(descript))
    i = 0
    try:
        while i < len(list_):
            file_.write("\t")
            file_.write(str(list_[i]))
            i = i + 1
        return 0
    except:
        print("Жилинский, неправильный аргумент list_, должен быть список")
        return -1

# Количество знаков после запятой для вывода
pr = [2]*len(list_t)

# Вывод в файл результатов расчета
ResFile = open("Lab6_res_file.txt", encoding = 'utf-8', mode = "w")
ResFile.write("Результат формул для заданных значений аргумента:")
writetabline(ResFile, "t, oC   ", list_t)
writetabline(ResFile, "CXэк., %", list(list_CX))
writetabline(ResFile, "CX1, %  ", list(map(round, CX1, pr)))
writetabline(ResFile, "CX2, %  ", list(map(round, CX2, pr)))
writetabline(ResFile, "CX3, %  ", list(map(round, CX3, pr)))
writetabline(ResFile, "CX4, %  ", list(map(round, CX4, pr)))
writetabline(ResFile, "CX5, %  ", list(map(round, CX5, pr)))
ResFile.write("\n")
ResFile.write("\n")

ResFile.write("Наиболее подходящая формула СХ")
ResFile.write(str(Nopt))
ResFile.write("\n")
ResFile.write("Отклонение наиболее подходящей формулы от эксп. данных ")
ResFile.write(str(d))
ResFile.close()
