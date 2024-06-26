# importing modules
import PIL
import numpy

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from numpy import imag
from table_of_elements import table_of_elements as tb

# class for the entire interface

print(PIL.__version__)
print(numpy.__version__)


class MpgCalculatorGUI:

    # class variables
    def __init__(self):
        # description for the interface
        self.root = tk.Tk()
        self.root.title("MPG Calculator")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.config(bg="#BDD2FA")

        # label for the interface
        self.header = tk.Label(
            self.root,
            text="Example: C 1 H 2",
            font=("monospace", 15),
            bg="#BDD2FA",
            border=0,
        )
        self.header.pack(padx=10, pady=10)

        # description for the textbox
        self.textBox = tk.Text(
            self.root, height=1, font=("monospace", 15), background="#BDD2FA"
        )
        self.textBox.pack(padx=10, pady=10)

        # description for the image
        self.image_a = ImageTk.PhotoImage(Image.open("assets/Group 1.png"))
        self.image_b = ImageTk.PhotoImage(Image.open("assets/Group 2.png"))

        # buttons for calcution and clearing the console
        self.calcButton = tk.Button(
            self.root, text="Calculate", image=self.image_a, command=self.showResult
        )
        self.clearButton = tk.Button(
            self.root, text="Clear", image=self.image_b, command=self.clearConsole
        )
        self.calcButton.place(x=10, y=110, width=240, height=70)
        self.clearButton.place(x=252, y=110, width=240, height=70)

        # variables for the process
        self.splitted_characters = []
        self.string_elements = []
        self.integers_atoms = []
        self.is_element_present = False
        self.total_mole_per_gram = 0

        # variables for displaying the results
        self.chemical_formula_string = ""

        # protocol for closing the window
        self.root.protocol("WM_DELETE_WINDOW", self.sureClosing)

        # executes the code
        self.root.mainloop()

    # interface methods
    # function to clear the console and also setting the values to default
    def clearConsole(self):
        self.textBox.delete(1.0, tk.END)
        self.splitted_characters = []
        self.string_elements = []
        self.integers_atoms = []
        self.is_element_present = False
        self.total_mole_per_gram = 0
        self.chemical_formula_string = ""
        self.string_total_mole_per_gram = ""

    # asking user i wanting to quit for the last time
    def sureClosing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()
            self.clearConsole()

    # function to display the process in the interface
    def displayProcess(self):
        self.recent_calculation_label = tk.Label(
            self.root,
            text="*RECENT COMPUTATIONS*",
            font=("monospace", 15),
            bg="#BDD2FA",
        )
        self.recent_calculation_label.place(x=10, y=200)

        self.chemical_formula_label = tk.Label(
            self.root, text="Chemical Formula: ", font=("monospace", 15), bg="#BDD2FA"
        )
        self.chemical_formula_label.place(x=10, y=230)
        self.formula_label = tk.Label(
            self.root,
            text=self.chemical_formula_string,
            font=("monospace", 15),
            bg="#BDD2FA",
        )
        self.formula_label.place(x=230, y=230)

        self.total_mole_per_gram_label = tk.Label(
            self.root,
            text="Total Moles Per Gram: ",
            font=("monospace", 15),
            bg="#BDD2FA",
        )
        self.total_mole_per_gram_label.place(x=10, y=270)

        self.string_total_mole_per_gram = str(self.total_mole_per_gram) + " g/mol"
        self.mole_per_gram_label = tk.Label(
            self.root,
            text=self.string_total_mole_per_gram,
            font=("monospace", 15),
            bg="#BDD2FA",
        )
        self.mole_per_gram_label.place(x=270, y=270)

    # function to make a string for the chemical formula
    def chemicalFormulaString(self):
        if self.is_element_present == True:
            for i, e in enumerate(self.string_elements):
                self.chemical_formula_string += e + str(self.integers_atoms[i])

    # End of interface methods

    # calculation methods
    # functions and methods
    def splitter(self, chemical_formula):
        self.splitted_characters = chemical_formula.split()

    def convertCharacters(self):
        for character in self.splitted_characters:
            try:
                self.integers_atoms.append(int(character))
            except ValueError:
                self.string_elements.append(character.capitalize())

    def validateCharacter(self):
        for element in self.string_elements:
            if element in tb.elements:
                self.is_element_present = True
            else:
                messagebox.showinfo(
                    title="ERROR",
                    message="Please make sure to provide spaces for elements along with the number of atoms!",
                )

    def calculateMolePerGram(self):
        for index, atom in enumerate(self.integers_atoms):
            try:
                mole_per_gram = (
                    self.integers_atoms[index]
                    * tb.elements[self.string_elements[index]]
                )
            except IndexError:
                messagebox.showinfo(
                    title="ERROR", message="Please put valid Chemical Formula!"
                )
                self.clearConsole()
            else:
                self.total_mole_per_gram += mole_per_gram
                self.displayProcess()

    def showResult(self):
        self.splitter(self.textBox.get("1.0", tk.END))
        self.convertCharacters()
        self.validateCharacter()
        self.chemicalFormulaString()
        if self.is_element_present:
            self.calculateMolePerGram()
            self.clearConsole()
        else:
            messagebox.showinfo(
                title="ERROR", message="Please put valid chemical formula"
            )
            self.clearConsole()


mpgCalculatorGui = MpgCalculatorGUI()
