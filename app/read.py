
def get_maxId(filename):
    try:
        s = open(filename, "r", encoding='utf-8')
        out = s.readlines()
        s.close()
        max_id = -1  # будет -1 если нет записей в файле
        for n in out:
            # первая колонка это id
            idstr = (n.split(";"))[0]
            if idstr.isdigit():  # если первый элемент число
               if max_id < int(idstr):
                   max_id = int(idstr)
        # print(max_id)
        return int(max_id)
    except:
        print("! ошибка, проверить путь и содержимое файла")
        return None


def csv_downl(filename):
  try:
    with open(filename, "r", encoding='utf-8', newline="") as file:
        lines = file.readlines()[1:]
        dlNotes = {}
        for line in lines:
            lst = line.split(';')
            dlNotes[int(lst[0])] = {'заголовок': lst[1],'текст': lst[2], 'дата/время': lst[3]}
        return dlNotes
  except FileNotFoundError:
      print(f"файл не найден, и был создан {filename}")
      return None
