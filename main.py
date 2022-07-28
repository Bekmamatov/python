# numbers=[10,2,3,1001,34,67,100]
# for i in numbers:#Цикл for перебирает каждый элемент в списке numbers 
#     if i % 2==0:#Делаем проверку на четность и нечетность с помощью условий if,else,elif
#         print(i,"четная")
# else:
#     print(i,"нечетная")

# for adilet in range(1001):#Делаем генерацию цифр от 0 до 100 шагом 2,то есть генерируем честные числа 
#     print(adilet)#Выводим ответ 

# for i in range(1001):#Генерируем число от 0 до 1000
#     if i %2==0:#С ромощью условий проверяем на четность и нечетность
#         print(i)#Выводим ответ



# hello="HelloW World"#Создаем строку для цикла for 
# for h in hello :#Проходимся по строке с помощью цикла for
    # if h == "W":#Деллаем условие чтобы узнать есть ли W в нашей строке 
    #     print("OK")

# cars=('Toyota','Lexus','Honda','Nissan')#Создаем кортеж 
# for i in cars:#Проходимся ро каждому элементу в кортеж 
#     print(i)#Выводим результат

# numbers=[]
# for i in range(1,1001):
#     numbers.append(i)
# print(numbers)

# n=0 
# user_input=int(input("Введите число : "))
# while True:
#     n+=1
#     print("Hacking", n)
#     if n==user_input:
#         print("Hacked!!!")
#         break

# for i in range(1,6):
#     print(i,"0")

# for i in range(10):
#     print(123)

# for i in range(497):
#     if i %2==0:
#         print(i)



# student={'name':'Adilet','age':17}#Создаем словарь с фигурной скобкой
# #student=['Adilet','Kurmanbek']
# print(len(student))
# print(student['age'])#Выводим значение 17 с помощью клююча age
# student['age']=18#Обновляем значение с помощью ключа 
# print(student)#Выводим словарь 
# student['address']="Masalieva 46"#Добавляем значение в список,если есть нужный ключ,то он его обновит
# print(student)#Выводим ключ 
# student.setdefault("school","Osh52")#С помощью метода setdefault добавляем ключ и значение 
# print(student)#Выводим словарь 
# del student['address']#Удаляем ключ и значение тоже удалится 
# print(student)#Выводим словарь 
# student.pop('age')#С помощью метода pop удаляем ключ и значение
# print(student)#Выводим словарь 

# lexus={'brand':'Lexus','model':'LX570','color':'white'}
# print(lexus.keys())
# print(lexus.values())
# print(lexus.items())
# for key,value in lexus.items():
#     print(key,Value)



# contact={'Adilet':'0776548756'}
# while True:
#     command=input("1-Добавить в контакт,2-искать контакт,3-удалить контакт,4-посмотреть все контакты: ")
#     if command=="1":
#         add_name=input("Введите имя: ")
#         add_number=input("Введите номер: ")
#         if add_name.title()not in contact:
#             contact.setdefault(add_name.title(),add_number)
#             print("Контакт успешно добавлен")
#         else:
#             print("Такой контакт уже существует.Вы хотите обновить номер? ")
#             user_input=input("1-да,2-нет: ")
#             if user_input=="1":
#                 new_number=input("Введите новый номер: ")
#                 contact[add_name]=new_number
#                 print("Контакт",add_name,"успешно обновлен")
#     elif command=="2":
#         find_number=input("Введите имя которую вы хотите найти:")
#         if find_number.title() in contact:
#             print("Контакт",find_number,"найден",contact[find_number.title()])
#         else:
#             print("Контакт не найден")
#     elif command=="3":
#         delete_number=input("Введите имя которую вы хотите удалить: ")
#         if delete_number in contact:
#             contact.pop(delete_number)
#             print("Контакт",delete_number,"успешно удален")
#         else:
#             print("Такого контакта нету")
#     elif command=="4":
#         for k,v in contact.items():
#             print(k,v)
#     else:
#         print("Такой команды не существует")


# numbers={1,2,3,4,5,6,7,8,9}#Создаем множество с фигурной скобкой 
# print(numbers)#Выводим сет 


# names={'Musk','Mirbek','Adilet'}#В множествах хранится только уникальные объекты
# print(names)


# numbers=[1,2,3,4,5,6,7]#Создаем словарь 
# set_numbers=set(numbers)#Преевращаем словарь  set
# print(set_numbers)

# objects={True,10,5.06,"Hello",(1,2,3)}#В множествах невозможно хранить типы данных как list,dict,set
# print(objects)#Выводим множество 


# cars={"Audi","Mersedes","Nissan","Rolls Royce"}#Создем множество с марками машин
# print(cars)
# cars.add("Tesla")#Добавляем в множество 
# print(cars)
# cars.remove("Audi")#Удалить элемент из множества
# print(cars)
# cars.pop()#Удаляет сдучайный эдемент из множеств
# print(cars)
# for c in cars:#Множесто,как и любую другую коллекцию,итерируем циклом for:
#     print(c)


# names=[]
# surname=[]
# emails={'adi@gmail.com'}
# while True:
#     print("Добро пожаловать в нашу программу!Введите свои данные для регистрации")
#     user_name=input("Введите свое имя: ")
#     user_surname=input("Введите свою фамилию: ")
#     user_email=input("Введите свою почту: ")
#     if user_email not in emails:
#         names.append(user_name)
#         surname.append(user_surname)
#         emails.add(user_email)
#         print("Вы успешно зарегистрировались!")
#     else:
#         print("Ваща почта есть в нашей базе.Введите другую")
#         print(emails)


# lst_1=["Goole","Amazon","Tesla"]
# lst_2=["Samsung","LG","Google","Amazon"]
# lst_3=set(lst_1+lst_2)
# print(lst_3)

# cars=["Audi","Mersedes","Nissan","Rolls Royce","Audi"]
# frozen_cars=frozenset(cars)
# print(frozen_cars)
# frozen_cars.remove("Audi")
# print(frozen_cars)


# while True:
#     try:
#         num_1=int(input("Введите первое число: "))
#         operation=input("1-сложить,2-вычитать,3-умножить,4-делить: ")
#         num_2=int(input("Введите второе число: "))
#         if operation=="+":
#             print(num_1+num_2)
#         elif operation=="-":
#             print(num_1-num_2)
#         elif operation=="*":
#             print(num_1*num_2)
#         elif operation=="/":
#             try:
#                 print(num_1/num_2)
#             except ZeroDivisionError:
#                 print("Деление на ноль нельзя!Учи математику!")
#         else:
#             print("Неправильная операция")
#     except ValueError:
#         print("Введите целое число")



# try:
#     name="Hello"
#     print(name)
# except:
#     print(Error)


# try:
#     hello="Hi"
#     print(hello[10])
# except:
#     print("Erorrr")

# try:
#     print(10/0)
# except:
#     raise SyntaxError("Деление на ноль")
# finally:
#     print("Я всегда буду работать"




# X = int(input())
# # if X % 2==0:
#     int_type='чётный'
# else:
#     int_type='нечётный'
# print(int_type)
# name = "Adilet" if 9>10 else "Kurmanbek"
# int_type = "чётный" if X%2 ==0 else "Не чётный"
# print(int_type)
# print(X%2)


                                                                                        #25/07/2022
                                                                                    
# number=int(input("Введите число: "))
# if number % 2==0:
#     print(number,"четное")
# else:
#     print(number,"нечетная")



# numbers=[]
# for i in range(0,101):
#     if i % 2==0:
#         numbers.append(i)
# print(numbers)




# number=int(input("Введите число: " ))
# result='четное'if number %2==0 else 'нечетное'
# print(result)



# number=int(input("Введите число: "))
# print('четное') if number % 2== 0 else print('нечетное')




# numbers=[i for i in range(0,101)if i %2==0]
# print(numbers)




# petrol={
#     'Ai 100':55,
#     'Ai 95':50,
#     'Ai 92':45,
#     'Ai 80':40,
#     'DT':35
# }

# new_petrol={}
# for k,v in petrol.items():
#     new_petrol.setdefault(k,v+10)
# print(new_petrol)

#####################################
# new_petrol={k:v+10 for k,v in petrol.items()}
# print(new_petrol)


# def replay():
#     print("Hello World")
#     print("IT-RUN")
#     print("Adilet")

# replay()

# def add():
#     num_1=int(input("Введите первое число: "))
#     num_2=int(input("Введите второе число: "))
#     print(num_1+num_2)
# add()

#Функция в программировании представлет собой особый участок кода,
#Который можно вызывать,обратившись к нему по имени,которым он был назван.При вызове происходит выполнение команд тела функции.


# def mult(num1, num2):#Параметры
#     print(num1*num2)

# mult(10,10)#Аргументы





# def calc(num1,num2,operation):
#     if operation=="+":
#         print(num1+num2)
#     elif operation=="-":
#         print(num1-num2)
#     elif operation=="*":
#         print(num1*num2)
#     elif operation=="/":
#         try:
#             print(num1/num2)
#         except ZeroDivisionError:
#             print("Делить на ноль нельзя!")
#     else:
#         print("Неправилтная комманда!")

# calc(10,30,"+")
# calc(95,45,"-")
# calc(30,2,"*")
# calc(210,3,"/")

################################################
# while True:
#     def update():
#         a = input("Скажите что-то: ")
#         if "?" in a:
#             print("Конечно")
#         b=input("Скажите что нибудь: ")
#         if "!" in b:
#             print("Успокойся")
#         c=input("Говорите:")
#         if "" in c:
#             print("Как классно когда ты молчишь.Продолжай в том же духе!")
#         d=input("СУЙЛО: ")
#         if "" in d:
#             print("Ну и что")
#     update()



# def welcome(name="Asan"):
#     print("Добро пожаловать",name)

# welcome("Adilet")



# print(10*10)
# print(10*"IT")

# lst_1=[1,2,3,4,5]
# lst_2=[2,3,4,5,6, *lst_1]
# print(set(lst_2))



# def workers(name1,name2,name3):
#     print("Добро пожаловать",name1)
#     print("Добро пожаловать",name2)
#     print("Добро пожаловать",name3)

# workers("Kurmanbek","Adilet","Nurbolot")
##########################################


# def workers(*names):
#     for name in names:
#         print("Добро пожаловать",name)

# workers("Kurmanbek","Adilet","Nurbolot","Diana","Fahridin","Aibala")

# def transation(**words):
#     print(words)

# transation(USA="США",RUSSIA="РОССИЯ")



# f=open('python.txt','w',encoding='utf-8')
# f.write("Python-высокоуровневый язык программирования")#С помощью метода write записываем текст в файл
# f.close()#Обузятельно закрываем файл после открытия 

# fl=open('python.txt','r',encoding='utf-8')
# print(fl.read())
# fl.close()

# py=open('back.py','w',encoding='utf-8')
# py.write("print('Hello world')")
# py.close

# login=input("Введите логин: ")
# password=input("Введите пароль: ")
# f=open('passwords.txt','a+',encoding='utf-8')
# f.write(f"{login,password}\n")
# f.close


# with open('itrun.txt','w',encoding='utf=8')as f:
#     f.write("Python the best!")

# with open('itrun.txt','r',encoding='utf-8')as re:
#     print(re.read())




















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































