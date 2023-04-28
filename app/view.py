def view_list(journal):
    journal = dict(
        sorted(journal.items(), key=lambda x: x[1].get('дата/время'), reverse=True))
    for i in journal:
        print(f"id {i}:", journal[i]['заголовок'],"->", journal[i]['дата/время'])

def note_value(journal, num):
    for j in journal[num]:
        print(f"{j}:", journal[num][j])
