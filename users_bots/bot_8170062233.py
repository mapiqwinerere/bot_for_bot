import TgBotMapi as tbm

tg = tbm.TgBot('8170062233')       

f = {}
names_funcs = {}
def start_func(message):
    global tg

    tg.message('Привет. Данный бот является мини справочником по курсу математики 7 класса, а также демонстрацией возможности проекта Ткаченко Олега.', message)

names_funcs['start'] = start_func
    
def information_func(message):
    global tg

    tg.message('Введите /math для чтения тем /algebra для сведений по алгебре /geometry для сведений по геометрии', message)

names_funcs['information'] = information_func
    

def algebra_menu_but_0(message):
    global tg

    tg.message("Линейное уравнение с одной переменной — это уравнение вида ax + b = 0, где x — переменная, a и b — некоторые числа. Решение: x = -b/a (если a не равно 0).", message)
algebra_menu_dict = {}
algebra_menu_dict["0"] = algebra_menu_but_0

def algebra_menu_but_1(message):
    global tg

    tg.message("Многочлен — это сумма одночленов. Пример: 3x²y - 5xy + 7", message)
algebra_menu_dict["1"] = algebra_menu_but_1

def algebra_menu_but_2(message):
    global tg

    tg.message("(a+b)^2=a^2+2ab+b^2-(a-b)^2=a^2-2ab+b^2-a^2-b^2=(a-b)(a+b)-(^2 - возведение во вторую степень)", message)
algebra_menu_dict["2"] = algebra_menu_but_2

def algebra_menu_but_3(message):
    global tg

    tg.message("a^m * a^n = a^(m+n)-a^n / a^n = a^(m-n)-(a^m)^n = a^mn-(^ - возведение в  степень)", message)
algebra_menu_dict["3"] = algebra_menu_but_3

f['algebra_menu'] = 0
def algebra_menu_func(message):
    global algebra_menu_kb
    global f

    if f['algebra_menu'] == 0:
        algebra_menu_kb = tbm.Keyboard(
        buts=['Уравнения', 'Многочлены', 'Формулы сокр. умножения', 'Степени'],
        values=list(algebra_menu_dict.values()),
        row_width=2,
        name="algebra_menu",
        text="Алгебра 7 класс. Выберите тему:",
        message=message,
        bot=tg)

        f['algebra_menu'] = 1

    algebra_menu_kb.send()

names_funcs['algebra'] = algebra_menu_func


def geometry_menu_but_0(message):
    global tg

    tg.message("Треугольник — это геометрическая фигура, образованная тремя отрезками, которые соединяют три точки, не лежащие на одной прямой. Виды треугольников классифицируются по длинам сторон (равносторонний, равнобедренный, разносторонний) и по величине углов (остроугольный, прямоугольный, тупоугольный). Признаки равенства треугольников (SSS, SAS, ASA, AAS) позволяют определить, являются ли два треугольника конгруэнтными.", message)
geometry_menu_dict = {}
geometry_menu_dict["0"] = geometry_menu_but_0

def geometry_menu_but_1(message):
    global tg

    tg.message("Параллельными называются прямые, которые лежат в одной плоскости и никогда не пересекаются. Существует несколько признаков параллельности прямых, основанных на углах, образующихся при пересечении двух прямых третьей прямой (секущей). При пересечении параллельных прямых секущей образуются пары равных (накрест лежащие, соответственные) и в сумме равных 180° (односторонние) углов.", message)
geometry_menu_dict["1"] = geometry_menu_but_1

def geometry_menu_but_2(message):
    global tg

    tg.message("Смежными называются два угла, имеющие одну общую сторону, а две другие стороны являются продолжениями друг друга. Сумма смежных углов всегда равна 180°. Вертикальными называются два угла, образованные пересечением двух прямых, и не имеющие общих сторон. Вертикальные углы всегда равны между собой.", message)
geometry_menu_dict["2"] = geometry_menu_but_2

def geometry_menu_but_3(message):
    global tg

    tg.message("Окружность — это геометрическая фигура, представляющая собой множество всех точек плоскости, равноудаленных от заданной точки, называемой центром. Круг — это часть плоскости, ограниченная окружностью, включая саму окружность и ее внутреннюю область. Радиус — это отрезок, соединяющий центр окружности с любой точкой на окружности, а диаметр — это отрезок, проходящий через центр окружности и соединяющий две точки на окружности (диаметр равен двум радиусам). Хорда — это отрезок, соединяющий две любые точки на окружности.", message)
geometry_menu_dict["3"] = geometry_menu_but_3

f['geometry_menu'] = 0
def geometry_menu_func(message):
    global geometry_menu_kb
    global f

    if f['geometry_menu'] == 0:
        geometry_menu_kb = tbm.Keyboard(
        buts=['Треугольники', 'Параллельные прямые', 'Смежные и верт. углы', 'Окружность'],
        values=list(geometry_menu_dict.values()),
        row_width=2,
        name="geometry_menu",
        text="Геометрия 7 класс. Выберите тему:",
        message=message,
        bot=tg)

        f['geometry_menu'] = 1

    geometry_menu_kb.send()

names_funcs['geometry'] = geometry_menu_func


def math_menu_but_0(message):
    global tg

    tg.message("На тему алгебры присутствуют следующие темы: -Уравнения-Многочлены-Формулы сокр. умножения-Степени", message)
math_menu_dict = {}
math_menu_dict["0"] = math_menu_but_0

def math_menu_but_1(message):
    global tg

    tg.message("На тему геометрии присутствуют следующие темы: -Треугольники-Параллельные прямые-Смежные и верт. углы-Окружность", message)
math_menu_dict["1"] = math_menu_but_1

f['math_menu'] = 0
def math_menu_func(message):
    global math_menu_kb
    global f

    if f['math_menu'] == 0:
        math_menu_kb = tbm.Keyboard(
        buts=['Алгебра', 'Геометрия'],
        values=list(math_menu_dict.values()),
        row_width=2,
        name="math_menu",
        text="Выберите о списке тем какого раздела математики вы хотите узнать:",
        message=message,
        bot=tg)

        f['math_menu'] = 1

    math_menu_kb.send()

names_funcs['math'] = math_menu_func


def sqrt_menu_but_0(message):
    global tg

    tg.message_edit("Не правильно", message)
sqrt_menu_dict = {}
sqrt_menu_dict["0"] = sqrt_menu_but_0

def sqrt_menu_but_1(message):
    global tg

    tg.message_edit("Правильно", message)
sqrt_menu_dict["1"] = sqrt_menu_but_1

f['sqrt_menu'] = 0
def sqrt_menu_func(message):
    global sqrt_menu_kb
    global f

    if f['sqrt_menu'] == 0:
        sqrt_menu_kb = tbm.InlineKeyboard(
        buts=['11', '12'],
        values=list(sqrt_menu_dict.values()),
        row_width=2,
        name="sqrt_menu",
        text="Чему равен корень из 144",
        message=message,
        bot=tg)

        f['sqrt_menu'] = 1

    sqrt_menu_kb.send()

names_funcs['sqrt'] = sqrt_menu_func


tg.handlers(list(names_funcs.keys()), list(names_funcs.values()))

tg.start_bot()