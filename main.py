import webbrowser
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
from tkinter import ttk
from tkinter import messagebox




compiler = Tk()
compiler.title('Feather Editor')
compiler.geometry("645x500")
compiler.state('zoomed')
file_path = ''

from winotify import Notification
toaster = Notification(app_id="Microsoft",
                       title="Microsoft Alert",
                       msg="Program is running!",
                       duration="short",)




toaster.show()

# Makes a popup if you want open text editor
def popu1():
    pop1 = messagebox.askyesno("Feather Editor", "Do you want to open HEX picker and text editor?")
    if pop1 == 1:
        import PySimpleGUI as sg
        from pathlib import Path
        from tkinter import colorchooser



        smileys = [
            'happy', [':)', 'xD', ':D', '<3'],
            'sad', [':(', 'T_T'],
            'other', [':3']
        ]
        smiley_events = smileys[1] + smileys[3] + smileys[5]

        menu_layout = [
            ['File', ['Open', 'Save', 'ColorPicker', '---', 'Exit']],
            ['Tools', ['Word Count']],
            ['Add', smileys]

        ]

        sg.theme('GrayGrayGray')
        layout = [
            [sg.Menu(menu_layout)],
            [sg.Text('Untitled', key='-DOCNAME-')],
            [sg.Multiline(no_scrollbar=True, size=(40, 30), key='-TEXTBOX-')]
        ]
        root = Tk()
        window = sg.Window('Text Editor', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break

            if event == 'Open':
                file_path = sg.popup_get_file('open', no_window=True)
                if file_path:
                    file = Path(file_path)
                    window['-TEXTBOX-'].update(file.read_text())
                    window['-DOCNAME-'].update(file_path.split('/')[-1])

            if event == 'Save':
                file_path = sg.popup_get_file('Save as', no_window=True, save_as=True) + '.txt'
                file = Path(file_path)
                file.write_text(values['-TEXTBOX-'])
                window['-DOCNAME-'].update(file_path.split('/')[-1])

            if event == 'Word Count':
                full_text = values['-TEXTBOX-']
                clean_text = full_text.replace('\n', ' ').split(' ')
                word_count = len(clean_text)
                char_count = len(''.join(clean_text))
                sg.popup(f'words {word_count}\ncharacters: {char_count}')

            if event in smiley_events:
                current_text = values['-TEXTBOX-']
                new_text = current_text + ' ' + event
                window['-TEXTBOX-'].update(new_text)

            if event == 'ColorPicker':
                def color():
                    top = Toplevel()
                    my_color = colorchooser.askcolor()
                    my_label = Label(root).pack()
                    print(my_label)

                my_button = Button(root, text="Pick a Color", command=color).pack()



        mainloop()
        window.close()

def set_file_path(path):
    global file_path
    file_path = path

# Makes you open files
def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)

# Makes you save files
def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

# Makes you run the code
def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)

# Makes a popup for line editor
def popup():
    response = messagebox.askyesno("Feather Editor", "Do you want to open Line Editor?")

    if response == 1:
        import tkinter as tk
        class LineNumbers(tk.Text):
            def __init__(self, master, text_widget, **kwargs):
                super().__init__(master, **kwargs)

                self.text_widget = text_widget
                self.text_widget.bind('<KeyPress>', self.on_key_press)

                self.insert(1.0, '1')
                self.configure(state='disabled')

            def on_key_press(self, event=None):
                final_index = str(self.text_widget.index(tk.END))
                num_of_lines = final_index.split('.')[0]
                line_numbers_string = "\n".join(str(no + 1) for no in range(int(num_of_lines)))
                width = len(str(num_of_lines))

                self.configure(state='normal', width=width)
                self.delete(1.0, tk.END)
                self.insert(1.0, line_numbers_string)
                self.configure(state='disabled')

        if __name__ == '__main__':
            w = tk.Tk("Feather Editor")
            t = tk.Text(w)
            l = LineNumbers(w, t, width=1)
            l.pack(side=tk.LEFT)
            t.pack(side=tk.LEFT, expand=1)
            w.mainloop()
# popup for info
def popuP():
    messagebox.showinfo("Feather Editor", "This is little text and python editor."
                                          "Created by Merijn. "
                                          "You can contact me at PannekoekPlant#7328 discord")

# Contact list
def popu3():
    response = messagebox.askyesno("Feather Editor", "Do you want to open contact list")
    if response == 1:
        import sqlite3

        root = Tk()
        root.title('Feather Editor')

        root.geometry("400x600")

        # Databases

        # Create a database or connect to one
        conn = sqlite3.connect('address_book.db')

        # Create cursor
        c = conn.cursor()

        # Create table
        '''
        c.execute("""CREATE TABLE addresses (
        		first_name text,
        		last_name text,
        		address text,
        		city text,
        		state text,
        		zipcode integer
        		)""")
        '''

        # Create Update function to update a record
        def update():
            # Create a database or connect to one
            conn = sqlite3.connect('address_book.db')
            # Create cursor
            c = conn.cursor()

            record_id = delete_box.get()

            c.execute("""UPDATE addresses SET
        		first_name = :first,
        		last_name = :last,
        		address = :address,
        		city = :city,
        		state = :state,
        		zipcode = :zipcode 
        		WHERE oid = :oid""",
                      {
                          'first': f_name_editor.get(),
                          'last': l_name_editor.get(),
                          'address': address_editor.get(),
                          'city': city_editor.get(),
                          'state': state_editor.get(),
                          'zipcode': zipcode_editor.get(),
                          'oid': record_id
                      })

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

            editor.destroy()
            root.deiconify()

        # Create Edit function to update a record
        def edit():
            root.withdraw()
            global editor
            editor = Tk()
            editor.title('Update A Record')

            editor.geometry("400x300")
            # Create a database or connect to one
            conn = sqlite3.connect('address_book.db')
            # Create cursor
            c = conn.cursor()

            record_id = delete_box.get()
            # Query the database
            c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
            records = c.fetchall()

            # Create Global Variables for text box names
            global f_name_editor
            global l_name_editor
            global address_editor
            global city_editor
            global state_editor
            global zipcode_editor

            # Create Text Boxes
            f_name_editor = Entry(editor, width=30)
            f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
            l_name_editor = Entry(editor, width=30)
            l_name_editor.grid(row=1, column=1)
            address_editor = Entry(editor, width=30)
            address_editor.grid(row=2, column=1)
            city_editor = Entry(editor, width=30)
            city_editor.grid(row=3, column=1)
            state_editor = Entry(editor, width=30)
            state_editor.grid(row=4, column=1)
            zipcode_editor = Entry(editor, width=30)
            zipcode_editor.grid(row=5, column=1)

            # Create Text Box Labels
            f_name_label = Label(editor, text="First Name")
            f_name_label.grid(row=0, column=0, pady=(10, 0))
            l_name_label = Label(editor, text="Last Name")
            l_name_label.grid(row=1, column=0)
            address_label = Label(editor, text="Address")
            address_label.grid(row=2, column=0)
            city_label = Label(editor, text="City")
            city_label.grid(row=3, column=0)
            state_label = Label(editor, text="State")
            state_label.grid(row=4, column=0)
            zipcode_label = Label(editor, text="Zipcode")
            zipcode_label.grid(row=5, column=0)

            # Loop thru results
            for record in records:
                f_name_editor.insert(0, record[0])
                l_name_editor.insert(0, record[1])
                address_editor.insert(0, record[2])
                city_editor.insert(0, record[3])
                state_editor.insert(0, record[4])
                zipcode_editor.insert(0, record[5])

            # Create a Save Button To Save edited record
            edit_btn = Button(editor, text="Save Record", command=update)
            edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

        # Create Function to Delete A Record
        def delete():
            # Create a database or connect to one
            conn = sqlite3.connect('address_book.db')
            # Create cursor
            c = conn.cursor()

            # Delete a record
            c.execute("DELETE from addresses WHERE oid = " + delete_box.get())

            delete_box.delete(0, END)

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

        # Create Submit Function For database
        def submit():
            # Create a database or connect to one
            conn = sqlite3.connect('address_book.db')
            # Create cursor
            c = conn.cursor()

            # Insert Into Table
            c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                      {
                          'f_name': f_name.get(),
                          'l_name': l_name.get(),
                          'address': address.get(),
                          'city': city.get(),
                          'state': state.get(),
                          'zipcode': zipcode.get()
                      })

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

            # Clear The Text Boxes
            f_name.delete(0, END)
            l_name.delete(0, END)
            address.delete(0, END)
            city.delete(0, END)
            state.delete(0, END)
            zipcode.delete(0, END)

        # Create Query Function
        def query():
            # Create a database or connect to one
            conn = sqlite3.connect('address_book.db')
            # Create cursor
            c = conn.cursor()

            # Query the database
            c.execute("SELECT *, oid FROM addresses")
            records = c.fetchall()
            # print(records)

            # Loop Thru Results
            print_records = ''
            for record in records:
                print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"

            query_label = Label(root, text=print_records)
            query_label.grid(row=12, column=0, columnspan=2)

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

        # Create Text Boxes
        f_name = Entry(root, width=30)
        f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
        l_name = Entry(root, width=30)
        l_name.grid(row=1, column=1)
        address = Entry(root, width=30)
        address.grid(row=2, column=1)
        city = Entry(root, width=30)
        city.grid(row=3, column=1)
        state = Entry(root, width=30)
        state.grid(row=4, column=1)
        zipcode = Entry(root, width=30)
        zipcode.grid(row=5, column=1)
        delete_box = Entry(root, width=30)
        delete_box.grid(row=9, column=1, pady=5)

        # Create Text Box Labels
        f_name_label = Label(root, text="First Name")
        f_name_label.grid(row=0, column=0, pady=(10, 0))
        l_name_label = Label(root, text="Last Name")
        l_name_label.grid(row=1, column=0)
        address_label = Label(root, text="Address")
        address_label.grid(row=2, column=0)
        city_label = Label(root, text="City")
        city_label.grid(row=3, column=0)
        state_label = Label(root, text="State")
        state_label.grid(row=4, column=0)
        zipcode_label = Label(root, text="Zipcode")
        zipcode_label.grid(row=5, column=0)
        delete_box_label = Label(root, text="Select ID")
        delete_box_label.grid(row=9, column=0, pady=5)

        # Create Submit Button
        submit_btn = Button(root, text="Add Record To Database", command=submit)
        submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

        # Create a Query Button
        query_btn = Button(root, text="Show Records", command=query)
        query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

        # Create A Delete Button
        delete_btn = Button(root, text="Delete Record", command=delete)
        delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

        # Create an Update Button
        edit_btn = Button(root, text="Edit Record", command=edit)
        edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        root.mainloop()
# You can escape program
def functie(event):
    exit()


compiler.bind('<Escape>', functie)




def help_1(event):
    top = Toplevel()
    top.title("Feather Editor")
    lbl = Label(top, text="Created By Merijn").pack()
    lll = Label(top, text="Created With Python").pack()

def help_2():
    help = Toplevel()
    lbl = Label(help, text="Commands").pack()
    lll = Label(help, text="Esc | Exit").pack()
def version():
    version = Toplevel()
    lbl = Label(version, text="Version 1.0 Feather Editor").pack()

def help_3():
    help = Toplevel()
    lbl = Label(help, text="Logs").pack()
    lll = Label(help, text="10-5-2022| Added shortcuts for browser").pack()
    lll = Label(help, text="22-4-2022| Added Logs and Help and Contact File").pack()
    lll = Label(help, text="21-4-2022| Fixed Bugs").pack()
    lll = Label(help, text="20-4-2022| Added Line Editor").pack()
    lll = Label(help, text="19-4-2022| Added buttons and worked on design").pack()
    lll = Label(help, text="18-4-2022| Created Feather Editor").pack()


def site():
    import webbrowser

    root = Tk()
    root.geometry("350x200")
    root.title("Feather Editor")

    e = Entry(root, width=50)
    e.pack()
    e.insert(0, "Enter Website: ", )

    def click():
        f = open("testfile.txt", "w")
        f.write(e.get())
        f.close()

        f = open("testfile.txt", "r")
        webbrowser.open(f.read())

    def own():
        f = open("ownsite.txt", "r")
        webbrowser.open(f.read())

    def google():
        webbrowser.open("www.google.com")

    def youtube():
        webbrowser.open("www,youtube.com")

    def facebook():
        webbrowser.open("www.facebook.com")

    def wiki():
        webbrowser.open("www.wikipedia.org")

    def reset():
        global reset
        f = open("ownsite.txt", "w")
        f.write('')
        f.close()

    def add():
        f = open("ownsite.txt", "w")
        f.write(addt.get())
        f.close()

    def addyourown():
        global addt
        top = Toplevel()
        top.geometry("350x200")
        addt = Entry(top, width=50)
        addt.pack()
        addt.insert(0, "Enter Website: ", )

        f = open("ownsite.txt", "w")
        f.write(addt.get())
        f.close()

        menu_bar = Menu(top)

        menu_bar.add_cascade(label='Reset ', command=reset)
        menu_bar.add_cascade(label='Nothing', command=youtube)
        menu_bar.add_cascade(label='Add Site', command=add)

        top.config(menu=menu_bar, )


    menu_bar = Menu(root)

    menu_bar.add_cascade(label='Google', command=google)
    menu_bar.add_cascade(label='Youtube', command=youtube)
    menu_bar.add_cascade(label='Facebook', command=facebook)
    menu_bar.add_cascade(label='Wikipedia', command=wiki)
    menu_bar.add_cascade(label='Run', command=click)

    help = Menu(menu_bar, tearoff=0)
    help.add_command(label='Run own site', command=own)
    help.add_command(label='Add own site', command=addyourown)
    menu_bar.add_cascade(label='Own site', menu=help)

    root.config(menu=menu_bar, )

    root.mainloop()


def weather():
    import json
    import requests
    import os
    import threading
    HEIGHT = 400
    WIDTH = 800

    ############################# function #####################################################################

    def weather(city):
        key = '48a90ac42caa09f90dcaeee4096b9e53'
        # print('Please Wait')
        show['text'] = 'Please wait . . . .'
        try:
            source = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + key)
            data = source.json()
        except:
            show['text'] = "Error ! \nPlease try again"
            return

        a = "name : " + data['name'] + '\n'
        b = "description : " + data['weather'][0]['description'] + '\n'
        c = "coordinate : " + str(data['coord']['lon']) + " , " + str(data['coord']['lat']) + '\n'
        d = "temp : " + str(data['main']['temp']) + 'k' + " \npressure : " + str(
            data['main']['pressure']) + " \nhumidity : " + str(data['main']['humidity'])

        show['text'] = a + b + c + d
        return

    def start_thread():
        threading.Thread(target=lambda: weather(entry.get())).start()

    ############################################################################################################

    root = Tk()

    root.title("weather")
    root.configure(background="black")

    #################### menu ##################################

    m = Menu(root)
    menubar = Menu(m, tearoff=0)
    menubar.add_command(label="exit", command=root.destroy)

    root.config(menu=menubar)

    #########################################################

    ################################ window 1 ###################################

    canvas = Canvas(root, height=HEIGHT, width=WIDTH).pack()

    upper_frame = Frame(root, bg='white')
    upper_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

    entry = Entry(upper_frame, bg="white", bd=0)
    entry.place(relx=0, rely=0, relwidth=0.7, relheight=1)
    Button(upper_frame, text="search", font=40, bd=0, bg="#f2f2f2", command=start_thread).place(relx=0.7, rely=0,
                                                                                                relwidth=0.30,
                                                                                                relheight=1)

    lower_frame = Frame(root, bg="black", bd=3)
    lower_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.65, anchor="n")
    show = Label(lower_frame, bg="#f2f2f2", font=40, )
    show.place(relx=0, rely=0, relwidth=1, relheight=1)

    #####################################################################

    root.mainloop()

menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

menu_bar.add_cascade(label='Run', command=run)

menu_bar.add_cascade(label='Save', command=save_as)

menu_bar.add_cascade(label='Line Editor', command=popup)

help = Menu(menu_bar, tearoff=0)
help.add_command(label='Version', command=version)
help.add_command(label='Commands', command=help_2)
help.add_command(label='Logs', command=help_3)
help.add_command(label='Credit', command=help_1)
menu_bar.add_cascade(label='Help', command=popuP, menu=help)

menu_bar.add_cascade(label='HEX Picker', command=popu1)

menu_bar.add_cascade(label='Contact File', command=popu3)

help = Menu(menu_bar, tearoff=0)
help.add_command(label='Version', command=version)
help.add_command(label='Commands', command=help_2)
help.add_command(label='Credit', command=help_1)

menu_bar.add_cascade(label='Shortcut webbrowsers', command=site)



games = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Weather App', command=weather)


# Dont write under this
compiler.config(menu=menu_bar,)

editor = Text(width=150)
editor.pack()

code_output = Text(height=35, width=150)
code_output.pack()

compiler.mainloop()

