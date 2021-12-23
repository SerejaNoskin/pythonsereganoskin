import sys
import math

def get_coef(index, prompt):
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
    while True:
        try:
            coef_str=input()
            coef = float(coef_str)
        except ValueError:
            print("Введите верный коэффициент:")
            continue
        if index==1 and coef==0.0:
            print("Коэффициент не может быть равен 0")
        else:
            break
    
    # Переводим строку в действительное число
    
    return coef


def get_roots(a, b, c):
    
    result = []
    D = b*b - 4*a*c
    
    if D == 0.0:
        root = -b /(2.0*a)
        result.append(root)
        if root < 0:
            root==0
        else:
            F5=math.sqrt(root)
            F0=-F5
            if F0==F5:
                result.append(F0)
            else:
                result.append(F0)
                result.append(F5)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        if root1 < 0:
            root1==0
        else:
            F1=math.sqrt(root1)
            F2=-F1
            if F2==F1:
                result.append(F1)
            else:
                result.append(F1)
                result.append(F2)
        if root2 < 0:
            root2==0
        else:
            F3=math.sqrt(root2)
            F4=-F3
            if F3==F4:
                result.append(F3)
            else:
                result.append(F3)
                result.append(F4)
        
    return result
    

def main():
    a = get_coef(1, 'Введите коэффициент А:')
    
    
 
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a,b,c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {} и {} и {}'.format(roots[0], roots[1],roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {} и {} и {} и {}'.format(roots[0], roots[1],roots[2],roots[3]))

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

