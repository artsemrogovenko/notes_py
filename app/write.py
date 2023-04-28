import csv


def csv_export(journal, filename):
    with open(filename, "w", encoding="utf-8", newline='') as csvfile:

        columns = ['id', 'заголовок', 'текст', 'дата/время']
        csv.writer(csvfile, delimiter=";").writerow(columns)
        # запись каждой заметки
        for note in journal:
            # создается список для заполнения полями
            out = [";" for i in range(len(columns))]
            data = f"{note}"
            # запись отдельного поля
            for obj in journal[note]:
                # узнать индекс столбца в csv
                index = columns.index(obj)
                # если поле заметки совпал с колонкой
                for title in columns:
                    if obj == title:
                        # удалю в тексте точку с запятой replace(';') для правильного чтения в дальнейшем
                        out[index] = ''.join(
                            journal[note][obj].replace(';', ' '))+";"
            data += ''.join(map(str, out))
            csvfile.write(f"{data}\n")
        csvfile.close()
