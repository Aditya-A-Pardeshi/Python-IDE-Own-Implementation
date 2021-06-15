from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import tkinter.messagebox as tmsg
import subprocess



file_path = ""


def set_file_path(path):
	global file_path
	file_path = path


def open_file():
	path = askopenfilename(filetypes=[("Python Files", "*.py")])
	with open(path, "r") as file:
		code = file.read()
		editor.delete("1.0", END)
		editor.insert("1.0", code)
		set_file_path(path)


def save_as():
	if file_path == "":
		path = asksaveasfilename(filetypes=[("Python Files", "*.py")])
	else:
		path = file_path
	with open(path, "w") as file:
		code = editor.get("1.0", END)
		file.write(code)
		set_file_path(path)


def run():
	if file_path == "":
		save_prompt = Toplevel()
		text = Label(save_prompt, text="Please save your code")
		text.pack()
		return

	command = f"python {file_path}"
	process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output, error = process.communicate()
	code_output.insert("1.0", output)
	code_output.insert("1.0",  error)


def help():
	tmsg.showinfo("Help Box","Its a simple IDE for Python Programming Language..You just need to type your code Above and the output of the code will be displayed Below")


def rate():
	value=tmsg.askquestion("Was you Experience Good?","You used Aditya's Python IDE how was your experience?")
	if value=="yes":
		msg="Ohh...Great...Thank-You..."
	else:
		msg="Please tell me what went wrong...I will look after it..."

	tmsg.showinfo("Experience",msg)



compiler = Tk()
compiler.title("Python IDE")

compiler.geometry("700x500")

compiler.minsize(200,400)

compiler.maxsize(600,700)

my_label=Label(text="This IDE is Designed by Aditya Pardeshi")
my_label.pack()

menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)

file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)

menu_bar.add_cascade(label="File", menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label="Run", command=run)
menu_bar.add_cascade(label="Run", menu=run_bar)



help_bar = Menu(menu_bar, tearoff=0)
help_bar.add_command(label="Help", command=help)
menu_bar.add_cascade(label="Help", menu=help_bar)

rate_bar = Menu(menu_bar, tearoff=0)
rate_bar.add_command(label="Rate", command=rate)
menu_bar.add_cascade(label="Rate Us", menu=rate_bar)


compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

code_output = Text(height=10)
code_output.pack()

compiler.mainloop()