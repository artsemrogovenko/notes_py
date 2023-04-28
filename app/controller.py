from app import create
from app import view
from app import read
from app import write

notes={}

loop=True

def start():
    filepath="notes.csv"
    temp=0
    while loop:    
     try:   
            
            op=int(input("\
        1 Добавление заметки\n\
        2 Редактирование заметки\n\
        3 Список заметок\n\
        4 Просмотр конкретной заметки\n\
        5 Обновить файл\n\
        6 Дописать заметки из файла\n\
        8 Удалить заметку\n\
        0 Выход из программы\n"))
            if op == 1:
                if temp == 0:
                    num=read.get_maxId(filepath)                    
                create.add_note(notes,num)
                temp=2
            elif op == 2:     
                number=input_num()
                if id_valid(notes,number):
                    create.edit_note(notes,number)
            elif op == 3:
                view.view_list(notes)
            elif op == 4:
                number=input_num()
                if id_valid(notes,number):
                    view.note_value(notes,number)
            elif op == 5:
                # защита от затирания
                if temp > 0:
                    write.csv_export(notes,filepath)
                    print("Файл перезаписан")
                    temp=0                    
            elif op == 6:                    
                    if read.csv_downl(filepath) != None:
                        notes.update(read.csv_downl(filepath))                        
                        temp=1
                    else:
                        write.csv_export(notes,filepath)
            elif op == 8:
                number=input("Удаление заметки, ввести номер .. для отмены любая строка ")
                if number.isdigit():
                    if id_valid(notes, int(number)):
                        del notes[int(number)]
                        print("успех")
                    else:
                        print("ничего не удалено")
            elif op == 0:
                exit()
     except Exception :
             print("ошибка ввода")
    start()


def input_num():
 while True:
    try:
        number=int(input("id заметки "))
        return number
    except ValueError:
        print('ошибка ввода, попробуй еще')
        continue
    
    
def id_valid(journal, note):
    if note in journal:
       return True
    else:
        print("такой локальной заметки нет")
        return False