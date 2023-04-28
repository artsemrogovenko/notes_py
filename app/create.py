import datetime
from datetime import datetime 
#tagEdit=datetime.now().strftime("%d/%m/%y %H:%M")

def add_note(notes,maxidfile):
    numberNote = 0
    for key in notes.keys():
        if numberNote <= key:
            numberNote = key + 1 
    
    if maxidfile != None:
       if numberNote<=maxidfile:
        numberNote = maxidfile+1

    title=input("Введите заголовок заметки ")
    body=""
    while len(body) == 0:
        body=input("Введите тело заметки ")
    notes[numberNote]={'заголовок':title, 'текст':body, 'дата/время':datetime.now().strftime("%d/%m/%y %H:%M")}

   
def edit_note(notes,number):
    print(notes[number])
    edit=input("заменить заголовок? Y/N ").lower()
    if edit=='y':
            notes[number]['заголовок'] = input("Новый заголовок:")
            notes[number]['дата/время'] = datetime.now().strftime("%d/%m/%y %H:%M")
    edit=input("заменить тело заметки? Y/N ").lower()
    if edit=='y':
            notes[number]['текст'] = input("Новый текст:")
            notes[number]['дата/время'] = datetime.now().strftime("%d/%m/%y %H:%M")
