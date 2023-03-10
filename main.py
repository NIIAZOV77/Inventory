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
    data = [['Номер'], ['Инвентарный номер'], ['Бухгалтерский Номер'], ['Ответственное лицо']]
    for line in data_file.readlines():
        data_line = line.rstrip().split(' ', 3)
        for i in range(4):
            data[i].append(data_line[i])

    data_file.close()
    win = Toplevel()
    win.geometry('600x500')
    win['bg'] = 'black'
    win.grab_set()
    win.resizable(width=False, height=False)
    win.title('Просмотр всех данных')
    for i in range(len(data[0])):
        for j in range(4):
            (Label(win, text=data[j][i], font='Arial 10', bg='black', fg='white').grid(row=i, column=j))

        win.grid_columnconfigure(i, minsize=150)


# Функция для изменения данных
def refactoring(mode):
    win = Toplevel()
    win.geometry('600x500')
    win['bg'] = 'black'
    win.grab_set()
    win.resizable(width=False, height=False)
    top_label = Label(win, text='Добавление записи' if mode == 'add_new' else 'Удаление записи',
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
        if input1.get() == '' or input2.get() == '' or input3.get() == '' or input4.get() == '':
            Label(win, text='Ошибка! Пустое значение', bg='black', fg='red', font='Arial 12').pack()
            return 0
        str_data = ''.join([input1.get(), ' ', input2.get(), ' ', input3.get(), ' ', input4.get()])
        str_add = '\n' + str_data
        data_write = open_file('data.txt', 'a')
        data_write.seek(2)
        data_write.write(str_add)
        data_write.close()
        end_label = Label(win, text='Новая запись добавлена',
                          width=50, height=1,
                          font='Arial 12',
                          bg='black', fg='white',
                          pady=10)
        end_label.pack()

    def delete_from_file():
        str_data = ''.join([input1.get(), ' ', input2.get(), ' ', input3.get(), ' ', input4.get()])
        data_del = open_file('data.txt', 'r')
        lines = data_del.readlines()
        lines[-1] = lines[-1] + '\n'
        data_del.close()
        str_del = str_data

        if str_del + '\n' not in lines:
            Label(win, text='Ошибка! Совпадений нет', bg='black', fg='red', font='Arial 12').pack()
            return 0

        lines.remove(str_del + '\n')
        lines[-1] = lines[-1].rstrip()
        changed_data = open_file('data.txt', 'w')

        for line in lines:
            changed_data.write(line)
        changed_data.close()
        end_label = Label(win, text='Запись удалена',
                          width=50, height=1,
                          font='Arial 12',
                          bg='black', fg='white',
                          pady=10)
        end_label.pack()

    btn = Button(win, command=add_new_to_file if mode == 'add_new' else delete_from_file,
                 text='Готово',
                 height=2, width=20,
                 background='lightgray',
                 activebackground='yellow')
    btn.pack(pady=20)


# Функция для добавления новой записи
def add_new():
    refactoring('add_new')


# Функция для удаления новой записи
def delete():
    refactoring('delete')


def main():
    root = Tk()
    root.title('Inventory')
    root.geometry('600x500')
    root.resizable(width=False, height=False)
    root['bg'] = 'black'

    l1 = Label(root, text='Выберите пункт', width=600, height=2, font='Arial 20', background='lightgray')
    l1.pack()

    buttons_data = {'Просмотр всех данных': showing,
                    'Добавление записи': add_new,
                    'Удаление записи': delete,
                    'Выход из программы': root.destroy}

    for text, command in buttons_data.items():
        Button(root, command=command,
               text=text,
               height=4, width=40,
               background='lightgray', font='Arial 12',
               activebackground='yellow').pack(pady=10)

    root.mainloop()


if __name__ == '__main__':
    main()
