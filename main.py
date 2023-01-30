from tkinter import *


# Функция для открытия файла
def open_file(file, mode):
    try:
        data_read = open(file, mode, encoding='utf-8')
        return data_read
    except:
        quit()


# Функция для отображения
def showing():
    data_file = open_file('data.txt', 'r')
    data = []
    for line in data_file.readlines():
        data.append(line)
    data_file.close()
    win = Toplevel()
    win.geometry('600x500')
    win['bg'] = 'black'
    win.grab_set()
    win.resizable(width=False, height=False)
    top_label = Label(win, text='Номер инвентарный  Номер бухгалтерский Номер ответсвенное лицо',
                      width=600,
                      height=2,
                      font='Arial 10',
                      background='lightgray', )
    top_label.pack()

    for line in data:
        line = line.replace(' ', '\t', 3)
        l1 = Label(win, text=line,
                   width=100, height=2,
                   bg='black', fg='white')
        l1.pack()


# Функция для добавления новой записи
def add_new():
    win = Toplevel()
    win.geometry('600x500')
    win['bg'] = 'black'
    win.grab_set()
    win.resizable(width=False, height=False)
    top_label = Label(win, text='Добавление записи',
                      width=600,
                      height=2,
                      font='Arial 12',
                      background='lightgray', )
    top_label.pack()
    top_list = ['Введите номер', 'Введите инвентарный номер',
                'Введите бухгалтерский номер', 'Введите ответственное лицо']
    l1 = Label(win, text=top_list[0],
               width=50, height=1,
               font='Arial 10',
               bg='black', fg='white',
               pady=10)
    l1.pack()
    input1 = Entry(win, width=50, bg='lightgray')
    input1.pack()
    l2 = Label(win, text=top_list[1],
               width=50, height=1,
               font='Arial 10',
               bg='black', fg='white',
               pady=10)
    l2.pack()
    input2 = Entry(win, width=50, bg='lightgray')
    input2.pack()
    l3 = Label(win, text=top_list[2],
               width=50, height=1,
               font='Arial 10',
               bg='black', fg='white',
               pady=10)
    l3.pack()
    input3 = Entry(win, width=50, bg='lightgray')
    input3.pack()
    l4 = Label(win, text=top_list[3],
               width=50, height=1,
               font='Arial 10',
               bg='black', fg='white',
               pady=10)
    l4.pack()
    input4 = Entry(win, width=50, bg='lightgray')
    input4.pack()

    def add_new_to_file():
        str_data = ''.join([input1.get(), ' ', input2.get(), ' ', input3.get(), ' ', input4.get()])
        str_add = '\n' + str_data
        data_write = open_file('data.txt', 'a')
        data_write.seek(2)
        data_write.write(str_add)
        data_write.close()
        end_label = Label(win, text='Новая запись добавлена',
                          width=50, height=1,
                          font='Arial 10',
                          bg='black', fg='white',
                          pady=10)
        end_label.pack()

    btn = Button(win, command=add_new_to_file,
                 text='Готово',
                 height=2, width=20,
                 background='lightgray',
                 activebackground='yellow')
    btn.pack(pady=20)


# Функция для удаления новой записи
def delete():
    win = Toplevel()
    win.geometry('600x500')
    win['bg'] = 'black'
    win.grab_set()
    win.resizable(width=False, height=False)
    top_label = Label(win, text='Удаление записи',
                      width=600,
                      height=2,
                      font='Arial 12',
                      background='lightgray', )
    top_label.pack()
    top_list = ['Введите номер', 'Введите инвентарный номер',
                'Введите бухгалтерский номер', 'Введите ответственное лицо']
    l1 = Label(win, text=top_list[0],
               width=50, height=1,
               font='Arial 10',
               bg='black', fg='white',
               pady=10)
    l1.pack()
    input1 = Entry(win, width=50, bg='lightgray')
    input1.pack()
    l2 = Label(win, text=top_list[1],
               width=50, height=1,
               font='Arial 10',
               bg='black', fg='white',
               pady=10)
    l2.pack()
    input2 = Entry(win, width=50, bg='lightgray')
    input2.pack()
    l3 = Label(win, text=top_list[2],
               width=50, height=1,
               font='Arial 10',
               bg='black', fg='white',
               pady=10)
    l3.pack()
    input3 = Entry(win, width=50, bg='lightgray')
    input3.pack()
    l4 = Label(win, text=top_list[3],
               width=50, height=1,
               font='Arial 10',
               bg='black', fg='white',
               pady=10)
    l4.pack()
    input4 = Entry(win, width=50, bg='lightgray')
    input4.pack()

    def delete_from_file():
        str_data = ''.join([input1.get(), ' ', input2.get(), ' ', input3.get(), ' ', input4.get()])
        data_del = open_file('data.txt', 'r')
        lines = data_del.readlines()
        lines[-1] = lines[-1] + '\n'
        data_del.close()
        str_del = str_data
        lines.remove(str_del + '\n')
        lines[-1] = lines[-1].rstrip()
        changed_data = open_file('data.txt', 'w')
        for line in lines:
            changed_data.write(line)
        changed_data.close()
        end_label = Label(win, text='Запись удалена',
                          width=50, height=1,
                          font='Arial 10',
                          bg='black', fg='white',
                          pady=10)
        end_label.pack()

    btn = Button(win, command=delete_from_file,
                 text='Готово',
                 height=2, width=20,
                 background='lightgray',
                 activebackground='yellow')
    btn.pack(pady=20)


def main():
    root = Tk()
    root.title('Inventory')
    root.geometry('600x500')
    root.resizable(width=False, height=False)
    root['bg'] = 'black'

    l1 = Label(root, text='Выберите пункт', width=600, height=2, font='Arial 20', background='lightgray')
    l1.pack()
    btn1 = Button(root, command=showing,
                  text='Просмотр всех данных',
                  height=4, width=40,
                  background='lightgray',
                  activebackground='yellow')
    btn1.pack(pady=10)

    btn2 = Button(root, command=add_new,
                  text='Добавление записи',
                  height=4, width=40,
                  background='lightgray',
                  activebackground='yellow')
    btn2.pack(pady=10)

    btn3 = Button(root, command=delete,
                  text='Удаление записи',
                  height=4, width=40,
                  background='lightgray',
                  activebackground='yellow')
    btn3.pack(pady=10)

    btn4 = Button(root, command=root.destroy,
                  text='Выход из программы',
                  height=4, width=40,
                  background='lightgray',
                  activebackground='yellow')
    btn4.pack(pady=10)

    root.mainloop()


if __name__ == '__main__':
    main()
