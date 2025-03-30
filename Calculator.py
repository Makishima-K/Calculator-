import tkinter as tk
import math


window = tk.Tk()

window.geometry('500x600')
window.resizable(False,False)

window.title('Calculator')
photo = tk.PhotoImage(file='png.png')
window.iconphoto(False,photo)



spec = ['/','+','-','*']
spec2 = ['+','-']
spec3 = ['/','*']


def clear():
    ent.delete(0,tk.END)
    ent.insert(0,'0')

def de():
    ent.delete(len(ent.get())-1,tk.END)

def g(a):
    if len(ent.get())==0:
        ent.insert(tk.END, f"{a}")
        return
    
    if ent.get()=='ERR2':
        #print('122222222222')
        ent.delete(0,tk.END)
        ent.insert(tk.END, f"{a}")
        return
       
    if ent.get()=='ERR1':
        ent.delete(0,tk.END)
        ent.insert(tk.END, f"{a}")
        return    


    if ent.get()== '0':
        ent.delete(0,tk.END)
        ent.insert(tk.END, f"{a}")
        return


    j = ent.get()
    if j[len(ent.get())-1]in spec and a in spec:
        ent.insert(len(ent.get())-1, f"{a}")
        ent.delete(len(ent.get())-1,tk.END)
        return

    ent.insert(tk.END, f"{a}")


def g2(a):
    h=len(ent.get())
    for i in reversed(ent.get()):
        h-=1
        if i in spec:
            ent.insert(h+1, f"{a}")
            return
            break
            
        
    ent.insert(0, f"{a}")

# main

#quet 
# 1) sqrt  ^
# 2) * /
# 3) +

# err sqrt<0 and 2/0

def sqr(a):
    h=0
    text = a
    chek = False
    d = 0
    b = 0
    k = []
    x =0

    for i in text:
        h+=1
        if i == '√':
            d = h-1
            chek = True
        if chek:
            if i in spec:
                if i =='-' and h == 2:
                    #print('///////////////')
                    continue
                chek = False
                #print(text)
                
                b = h-1
                #print(b,d)
                #print(text[d:b])
                k.append([text[d+1:b],d,b])
            if h==len(a):
                #print(text)
                
                b = h+1
                #print(b,d)
                #print(text[d:b])

                k.append([text[d+1:b],d,b])         
    for i in k:
        
        x = i[0]
#        print(i[0],'8888888888888888888888888888')
        #print(i,'8888888888888888888888888888')
        x = float(x)
        if x< 0:
            print('ERR1')
            return 'ERR1'
        x = math.sqrt(x)
#        print((text,x,i[1],i[2]),'!!!!!!!!!!!!!!!!!!!!!!')
        text = switcher(text,x,i[1],i[2])
#        print(text)
    print(text)
    return text



#print('-----------------------')
def upp(a):
    h=0
    text = a
    chek = False
    d1 = 0
    d2 =0
    b = 0
    k = []
    x =0
    z=0
    tt =True
    while tt:
        tt =False
        h = 0
        d1 = 0
        d2 =0
        b = 0
        x =0
        z=0
#        print('------------------')
        for i in text:
            
            h+=1
            if i in spec and chek == False:
                d1 = h
#                print('1  ',i,h)
            if i == '^':
                d2 = h-1
                chek = True
                tt = True
#                print('//////',d2)
            if chek:
                if i in spec:
                    chek = False
                    
                    
                    b = h-1
                    #print(d1,d2,b)
                    #k.append([text[d1:b],d1,b,d2])
                    x = text[d1:d2]
                    
                    z = text[(d2+1):b]
                    #print(text[d1:b],'-----------------------------------',text[d1:d2],'----------',text[(d2+1):b])
                    x = float(x)
                    z = float(z)
                    x = x**z
                    x = round(x,3)
                    text = switcher(text,x,d1,b)
                    #print(text)
                    #d1 = h
                    break
                #print(h,len(text))
                if h==(len(text)):
                    chek = False
                    
                    b = h+1

                    x = text[d1:d2]
                    #print(text[d1:b],'-----------------------------')
                    #print(d1,d2)
                    print(d1,d2,b)
                    z = text[(d2+1):b]
                    #print(x,z)
                    x = float(x)
                    z = float(z)
                    
                    x = x**z
                    x = round(x,3)
                    text = switcher(text,x,d1,b)
                    print(text)
                    break
                    #k.append([text[d1:b],d1,b,d2])
    return text

def um(a):
    h = 0
    text = a
    chek = False
    d1 = 0
    d2 = 0
    b = 0
    k = 0
    x = 0
    z = 0
    tt = True
    
    while tt:
        tt = False
        h = 0
        d1 = 0
        d2 = 0
        b = 0
        x = 0
        z = 0
        
        for i in text:
            h += 1
            if i in spec2 and chek == False:
                if i =='-' and h == 1:
                    continue
                d1 = h

            if i == '/' and chek == False:
                d2 = h - 1
                chek = True
                tt = True
                k = 1
                continue
            if i == '*' and chek == False:
                d2 = h - 1
                chek = True
                tt = True
                k = 2
                continue
            if chek and k == 1:
                if i in spec and k == 1:
                    if h == d2+2 and i =='-':
                        continue
                    chek = False
                    b = h - 1
                    x = text[d1:d2]
                    z = text[(d2+1):b]
                    x = float(x)
                    z = float(z)
                    x = x / z
                    text = switcher(text, x, d1, b)
                    break
                if h == len(text):
                    chek = False
                    b = h + 1
                    x = text[d1:d2]
                    z = text[(d2+1):b]
                    x = float(x)
                    z = float(z)
                    x = x / z
                    text = switcher(text, x, d1, b)
                    break
            if chek and k == 2:
                if i in spec:
                    if h == d2+2 and i =='-':
                        continue
                    chek = False
                    b = h - 1
                    x = text[d1:d2]
                    z = text[(d2+1):b]
                    x = float(x)
                    z = float(z)
                    x = x * z
                    text = switcher(text, x, d1, b)
                    break
                if h == len(text):
                    chek = False
                    b = h + 1
                    x = text[d1:d2]
                    z = text[(d2+1):b]
                    x = float(x)
                    z = float(z)
                    x = x * z
                    text = switcher(text, x, d1, b)
                    break
    return text


            

def plu(a):
    h = 0
    text = a
    chek = False
    d1 = 0
    d2 = 0
    b = 0
    k = 0
    x = 0
    z = 0
    tt = True
    
    while tt:
        tt = False
        h = 0
        d1 = 0
        d2 = 0
        b = 0
        x = 0
        z = 0
        
        for i in text:
            h += 1
            

            if i == '-' and chek == False and (h-1) != 0:
                #print(i)
                d2 = h - 1
                chek = True
                tt = True
                k = 1
                continue
            if i == '+' and chek == False:
                d2 = h - 1
                chek = True
                tt = True
                k = 2
                continue
            if chek and k == 1:
                if i in spec and k == 1:
                    if h == d2+2 and i =='-':
                        continue
                    chek = False
                    b = h - 1
                    #print(text[d1:b],'-----------------------------------',text[d1:d2],'----------',text[(d2+1):b])

                    
                    x = text[d1:d2]
                    z = text[(d2+1):b]
                    x = float(x)
                    z = float(z)
                    x = x - z
                    text = switcher(text, x, d1, b)
                    break
                if h == len(text):
                    chek = False
                    b = h + 1
                    x = text[d1:d2]
                    z = text[(d2+1):b]
                    x = float(x)
                    z = float(z)
                    x = x - z
                    text = switcher(text, x, d1, b)
                    break
            if chek and k == 2:
                if i in spec:
                    if h == d2+2 and i =='-':
                        continue
                    chek = False
                    b = h - 1
                    x = text[d1:d2]
                    z = text[(d2+1):b]
                    x = float(x)
                    z = float(z)
                    x = x + z
                    text = switcher(text, x, d1, b)
                    break
                if h == len(text):
                    chek = False
                    b = h + 1
                    x = text[d1:d2]
                    z = text[(d2+1):b]
                    x = float(x)
                    z = float(z)
                    x = x + z
                    text = switcher(text, x, d1, b)
                    break
    return text







                

def switcher(text,swap,d,b):
    swap = round(swap,3)
    swap = str(swap)
    text = text[:d]+swap+text[b:]
    return text




def is_valid_expression(expr):
    valid_chars = "0123456789+-*/√.^ "
    operators = "+-*/"
#    print('11111111111')
    # Проверяем, содержит ли выражение только допустимые символы
    for char in expr:
        if char not in valid_chars:
            return False

    # Проверяем, начинается и заканчивается ли выражение корректно
    if expr[0] in "*/" or expr[-1] in operators:
        return False

    # Проверяем, нет ли подряд идущих операторов кроме допустимых (+- и -+)
    if '++' in expr:
        return False
    
    if '*/' in expr:
        return False
    if '+*' in expr:
        return False
    if '**' in expr:
        return False
    if '/*' in expr:
        return False
    if '//' in expr:
        return False
    if '/+' in expr:
        return False
    if '-*' in expr:
        return False
    if '-/' in expr:
        return False
    if '*+' in expr:
        return False
#    if '*-' in expr:
#        return False

    return True



def enter(a):
    
    b= a
    t = is_valid_expression(b)
    if t == False:
        finall('ERR0')
        return 

    print(b)
    if '/0' in b:
        finall('ERR2')
        return 
    if '√' in b:
        print('sql')
        b = sqr(b)
        if b == 'ERR1':
            finall('ERR1')
            return 
    if '^' in b:
        print('upp')
        b = upp(b)
        print(b)

    if '/' in b or '*' in b:
        print('Um')
        b = um(b)
        print(b)

    if '+' in b or '-' in b:
        print('Plus')
        
        b = plu(b)
        print(b)
    finall(b)
    

def finall(a):
#    text = ent.get(4,9)
#    print(text)

    ent.delete(0,tk.END)
    ent.insert(0,a)



# clear




#Style

# Нейтральная тема
theme_neutral = {
    "color_digits": "#D3D3D3",  # Светло-серый для цифр и точки
    "color_functions": "#696969",  # Тёмно-серый для функциональных кнопок
    "color_equals": "#32CD32",  # Лаймовый зелёный для кнопки "="
    "background_color": "#F5F5F5",  # Очень светлый серый для фона
    "button_relief": "raised",  # Тип рельефа кнопок
    "text_color_digits": "#333333",  # Тёмно-серый текст на светлом фоне
    "text_color_functions": "#FFFFFF",  # Белый текст на тёмно-сером
    "text_color_equals": "#FFFFFF"  # Белый текст на лаймовом зелёном
}
# Тёмная тема
theme_dark = {
    "color_digits": "#2F4F4F",  # Тёмно-бирюзовый серый для цифр и точки
    "color_functions": "#483D8B",  # Тёмно-сланцевый синий для функциональных кнопок
    "color_equals": "#FF1493",  # Яркий розовый для кнопки "="
    "background_color": "#1C2526",  # Очень тёмный серо-голубой для фона
    "button_relief": "raised",  # Тип рельефа кнопок
    "text_color_digits": "#FFFFFF",  # Белый текст на тёмном фоне
    "text_color_functions": "#FFFFFF",  # Белый текст на тёмно-синем
    "text_color_equals": "#FFFFFF"  # Белый текст на ярком розовом
}
# Холодная тема
theme_cool = {
    "color_digits": "#B0E0E6",  # Пудрово-голубой для цифр и точки
    "color_functions": "#4682B4",  # Стальной синий для функциональных кнопок
    "color_equals": "#00CED1",  # Яркий бирюзовый для кнопки "="
    "background_color": "#F0FFFF",  # Лазурный (очень светлый голубой) для фона
    "button_relief": "raised",  # Тип рельефа кнопок
    "text_color_digits": "#333333",  # Тёмно-серый текст на светлом фоне
    "text_color_functions": "#FFFFFF",  # Белый текст на стальном синем
    "text_color_equals": "#333333"  # Тёмно-серый текст на бирюзовом
}

# Тёплая тема
theme_warm = {
    "color_digits": "#FFE4B5",  # Мокко (тёплый светло-бежевый) для цифр и точки
    "color_functions": "#FF4500",  # Оранжево-красный для функциональных кнопок
    "color_equals": "#FFD700",  # Золотистый жёлтый для кнопки "="
    "background_color": "#FFF5EE",  # Seashell (очень светлый персиковый) для фона
    "button_relief": "raised",  # Тип рельефа кнопок
    "text_color_digits": "#2F2F2F",  # Тёмно-серый текст для читаемости на светлом фоне
    "text_color_functions": "#FFFFFF",  # Белый текст на оранжево-красном
    "text_color_equals": "#2F2F2F"  # Тёмно-серый текст на золотистом
}


color_digits = "#F5F5DC"  # Бежевый для цифр и точки
color_functions = "#FF6347"  # Томатный красный для функциональных кнопок
color_equals = "#FFA500"  # Оранжевый для кнопки "="
background_color = "#FFF8DC"  # Светло-бежевый фон калькулятора
button_relief = "raised"  # Тип рельефа кнопок
text_color = "black" 
size = 3
border_size = 3  # Размер рамок

font_size = ('Arial', 15)  # Размер шрифта кнопок



window.configure(bg=background_color)



ent = tk.Entry(window, justify="right", font=font_size, fg=text_color)  # Добавляем fg=text_color
ent.insert(0, "0")
ent.grid(row=0, column=0, padx=1, pady=1, columnspan=4)

btn_clear = tk.Button(window, width=size, height=size-1, command=clear, text='C', bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_clear.grid(row=0, column=5, padx=size, pady=size)

btn_1x = tk.Button(window, width=size, height=size-1, text='1/x', command=lambda: g2("1/"), bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_1x.grid(row=1, column=0, padx=size, pady=size)

btn_x2 = tk.Button(window, width=size, height=size-1, text='x^2', command=lambda: g("^2"), bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_x2.grid(row=1, column=1, padx=size, pady=size)

btn_sqrt = tk.Button(window, width=size, height=size-1, text='√x', command=lambda: g2("√"), bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_sqrt.grid(row=1, column=2, padx=size, pady=size)

btn__x = tk.Button(window, width=size, height=size-1, text='-x', command=lambda: g2("-"), bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn__x.grid(row=1, column=3, padx=size, pady=size)

btn_plus = tk.Button(window, width=size, height=size-1, text='+', command=lambda: g("+"), bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_plus.grid(row=2, column=3, padx=size, pady=size)

btn_minus = tk.Button(window, width=size, height=size-1, text='-', command=lambda: g("-"), bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_minus.grid(row=3, column=3, padx=size, pady=size)

btn_del = tk.Button(window, width=size, height=size-1, text='/', command=lambda: g("/"), bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_del.grid(row=4, column=3, padx=size, pady=size)

btn_um = tk.Button(window, width=size, height=size-1, text='*', command=lambda: g("*"), bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_um.grid(row=5, column=3, padx=size, pady=size)

btn_point = tk.Button(window, width=size, height=size-1, text='.', command=lambda: g("."), bg=color_digits, relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_point.grid(row=5, column=0, padx=size, pady=size)

btn_ent = tk.Button(window, width=size, height=size-1, text='=', command=lambda: enter(ent.get()), bg=color_equals, relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_ent.grid(row=5, column=2, padx=size, pady=size)

btn_1 = tk.Button(window, width=size, height=size-1, text='1', command=lambda: g("1"), bg=color_digits, relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_1.grid(row=2, column=0, padx=size, pady=size)

btn_2 = tk.Button(window, width=size, height=size-1, text='2', command=lambda: g("2"), bg=color_digits, relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_2.grid(row=2, column=1, padx=size, pady=size)

btn_3 = tk.Button(window, width=size, height=size-1, text='3', command=lambda: g("3"), bg=color_digits, relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_3.grid(row=2, column=2, padx=size, pady=size)

btn_4 = tk.Button(window, width=size, height=size-1, text='4', command=lambda: g("4"), bg=color_digits, relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_4.grid(row=3, column=0, padx=size, pady=size)

btn_5 = tk.Button(window, width=size, height=size-1, text='5', command=lambda: g("5"), bg=color_digits, relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_5.grid(row=3, column=1, padx=size, pady=size)

btn_6 = tk.Button(window, width=size, height=size-1, text='6', command=lambda: g("6"), bg=color_digits, relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_6.grid(row=3, column=2, padx=size, pady=size)

btn_7 = tk.Button(window, width=size, height=size-1, text='7', command=lambda: g("7"), bg=color_digits, relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_7.grid(row=4, column=0, padx=size, pady=size)

btn_8 = tk.Button(window, width=size, height=size-1, text='8', command=lambda: g("8"), bg=color_digits, relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_8.grid(row=4, column=1, padx=size, pady=size)

btn_9 = tk.Button(window, width=size, height=size-1, text='9', command=lambda: g("9"), bg=color_digits, relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_9.grid(row=4, column=2, padx=size, pady=size)

btn_0 = tk.Button(window, width=size, height=size-1, text='0', command=lambda: g("0"), bg=color_digits, relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_0.grid(row=5, column=1, padx=size, pady=size)

btn_d = tk.Button(window, width=size, height=size-1, text='Del', command=lambda: de(), bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_d.grid(row=1, column=5, padx=size, pady=size)


btn_d_t = tk.Button(window, width=size, height=size-1, text='D', command=lambda: theme(window, theme_dark), bg='grey', relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_d_t.grid(row=6, column=0, padx=size, pady=size)

btn_w_t = tk.Button(window, width=size, height=size-1, text='W', command=lambda: theme(window, theme_warm), bg='grey', relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_w_t.grid(row=6, column=1, padx=size, pady=size)

btn_c_t = tk.Button(window, width=size, height=size-1, text='C', command=lambda: theme(window, theme_cool), bg='grey', relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_c_t.grid(row=6, column=2, padx=size, pady=size)

btn_n_t = tk.Button(window, width=size, height=size-1, text='N', command=lambda: theme(window, theme_neutral), bg='grey', relief=button_relief, bd=border_size, font=font_size, fg=text_color)
btn_n_t.grid(row=6, column=3, padx=size, pady=size)

labelERR0 = tk.Label(window, font=('Arial', 14), text='ERR0 -> Sintax error', bg=background_color, fg=text_color)
labelERR0.grid(row=0, column=6, sticky='w')

labelERR1 = tk.Label(window, font=('Arial', 14), text='ERR1 -> √x x<0', bg=background_color, fg=text_color)
labelERR1.grid(row=1, column=6, sticky='w')

labelERR2 = tk.Label(window, font=('Arial', 14), text='ERR2 -> n/x x=0', bg=background_color, fg=text_color)
labelERR2.grid(row=2, column=6, sticky='w')

labelDark = tk.Label(window, font=('Arial', 14), text='D -> Theme dark', bg=background_color, fg=text_color)
labelDark.grid(row=3, column=6, sticky='w')

labelWarm = tk.Label(window, font=('Arial', 14), text='W -> Theme Warm', bg=background_color, fg=text_color)
labelWarm.grid(row=4, column=6, sticky='w')

labelCold = tk.Label(window, font=('Arial', 14), text='C -> Theme Cold', bg=background_color, fg=text_color)
labelCold.grid(row=5, column=6, sticky='w')

labelNeutral = tk.Label(window, font=('Arial', 14), text='N -> Theme Neutral', bg=background_color, fg=text_color)
labelNeutral.grid(row=6, column=6, sticky='w')

def theme(window, theme_dict):
    """
    Applies a theme to the calculator's UI elements.

    Args:
        window (tk.Tk): The main Tkinter window.
        theme_dict (dict): A dictionary containing theme settings.
    """
    color_digits = theme_dict["color_digits"]
    color_functions = theme_dict["color_functions"]
    color_equals = theme_dict["color_equals"]
    background_color = theme_dict["background_color"]
    button_relief = theme_dict["button_relief"]
    text_color_digits = theme_dict["text_color_digits"]
    text_color_functions = theme_dict["text_color_functions"]
    text_color_equals = theme_dict["text_color_equals"]

    # Apply theme to Entry widget
    ent.config(fg=text_color_digits, bg=background_color)
    window.config(bg=background_color)
    labelERR0.config(bg=background_color, fg=text_color_digits)
    labelERR1.config(bg=background_color, fg=text_color_digits)
    labelERR2.config(bg=background_color, fg=text_color_digits)

    labelDark.config(bg=background_color, fg=text_color_digits)
    labelWarm.config(bg=background_color, fg=text_color_digits)
    labelCold.config(bg=background_color, fg=text_color_digits)
    labelNeutral.config(bg=background_color, fg=text_color_digits)

    # Apply theme to Buttons
    btn_clear.config(bg=color_functions, relief=button_relief, fg=text_color_functions)
    btn_1x.config(bg=color_functions, relief=button_relief, fg=text_color_functions)
    btn_x2.config(bg=color_functions, relief=button_relief, fg=text_color_functions)
    btn_sqrt.config(bg=color_functions, relief=button_relief, fg=text_color_functions)
    btn__x.config(bg=color_functions, relief=button_relief, fg=text_color_functions)
    btn_plus.config(bg=color_functions, relief=button_relief, fg=text_color_functions)
    btn_minus.config(bg=color_functions, relief=button_relief, fg=text_color_functions)
    btn_del.config(bg=color_functions, relief=button_relief, fg=text_color_functions)
    btn_um.config(bg=color_functions, relief=button_relief, fg=text_color_functions)
    btn_point.config(bg=color_digits, relief=button_relief, fg=text_color_digits)
    btn_ent.config(bg=color_equals, relief=button_relief, fg=text_color_equals)
    btn_1.config(bg=color_digits, relief=button_relief, fg=text_color_digits)
    btn_2.config(bg=color_digits, relief=button_relief, fg=text_color_digits)
    btn_3.config(bg=color_digits, relief=button_relief, fg=text_color_digits)
    btn_4.config(bg=color_digits, relief=button_relief, fg=text_color_digits)
    btn_5.config(bg=color_digits, relief=button_relief, fg=text_color_digits)
    btn_6.config(bg=color_digits, relief=button_relief, fg=text_color_digits)
    btn_7.config(bg=color_digits, relief=button_relief, fg=text_color_digits)
    btn_8.config(bg=color_digits, relief=button_relief, fg=text_color_digits)
    btn_9.config(bg=color_digits, relief=button_relief, fg=text_color_digits)
    btn_0.config(bg=color_digits, relief=button_relief, fg=text_color_digits)
    btn_d.config(bg=color_functions, relief=button_relief, fg=text_color_functions)
    btn_d_t.config(bg='grey', relief=button_relief, fg=text_color_functions)
    btn_w_t.config(bg='grey', relief=button_relief, fg=text_color_functions)
    btn_c_t.config(bg='grey', relief=button_relief, fg=text_color_functions)
    btn_n_t.config(bg='grey', relief=button_relief, fg=text_color_functions)

theme(window, theme_neutral)




window.mainloop()
