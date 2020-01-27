from tkinter import *

class UserInterface():

    def __init__(self):

        self.__window = Tk()
        #TODO: Keksi nimi ikkunalle
        self.__window.title("English-Spanish Dictionary")

        # Create 6 buttons
        self.__word_button = Button(self.__window, text="Translate a word") \
            .grid(row=0, column=4, columnspan=2, sticky=W + E)
        self.__add_button = Button(self.__window, text="Add") \
            .grid(row=1, column=4, columnspan=2, sticky=W + E)
        self.__remove_button = Button(self.__window, text="Remove") \
            .grid(row=2, column=4, columnspan=2, sticky=W + E)
        self.__open_button = Button(self.__window, text="Open dictionary", command=self.dictionary) \
            .grid(row=3, column=4, columnspan=2, sticky=W + E)
        self.__translate_button = Button(self.__window, text="Translate a text") \
            .grid(row=4, column=4, columnspan=2, sticky=W + E)
        self.__stop_button = Button(self.__window, text="Quit", command=self.__window.destroy) \
            .grid(row=6, rowspan=1, column=4, columnspan=2, sticky=W + S + E)

        # Create 4 labels
        self.__title_label = Label(self.__window, text="English-Spanish Dictionary") \
            .grid(row=0, column=2, columnspan=2, sticky=W + E)
        self.__english_label = Label(self.__window, text="English") \
            .grid(row=2, column=2, columnspan=1, sticky=W + S + E)
        self.__spanish_label = Label(self.__window, text="Spanish") \
            .grid(row=2, column=3, columnspan=1, sticky=W + S + E)
        self.__feedback_label = Label(self.__window, text="TODO") \
            .grid(row=4, column=2, columnspan=2, rowspan=2, sticky=W + E + S)

        # Create 2 entry boxes
        self.__entry1 = Entry(self.__window, width=12)
        self.__entry1.grid(row=3, column=2, sticky=W + E)

        self.__entry2 = Entry(self.__window, width=12)
        self.__entry2.grid(row=3, column=3, sticky=W + E)

        # Create a scrollbar for the text box
        scrollbar = Scrollbar(self.__window)
        scrollbar.grid(row=0, column=1, rowspan=7, sticky=N + S)

        # Create a text box
        self.__text_box = Text(self.__window, yscrollcommand=scrollbar.set, wrap=WORD, width=20, height=10)
        self.__text_box.grid(row=0, column=0, rowspan=7)

        scrollbar.config(command=self.__text_box.yview)

        # Create a dict containing words in English as the key and a Spanish translation as the value

        self.__english_spanish = {
            "hey": "hola", "thanks": "gracias", "home": "casa"
        }
    def dictionary(self):

        for key in self.__english_spanish:
            self.__text_box.insert(END, (key, self.__english_spanish[key], '\n'))

    def start(self):
        self.__window.mainloop()
def main():
    ui = UserInterface()
    ui.start()


main()

