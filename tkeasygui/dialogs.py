"""
TkEasyGUI dialogs
"""
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import tkinter.simpledialog as simpledialog
from tkinter import colorchooser

import tkeasygui as eg


#------------------------------------------------------------------------------
# Dialogs
#------------------------------------------------------------------------------
# like PySimpleGUI
def popup(message: str, title: str = "") -> None:
    """
    Display a message in a popup window.
    
    #### Example:
    ```py
    eg.popup("I like an apple.", "Information")
    ```
    """
    # messagebox.showinfo(title, message)
    win = eg.Window(title, layout=[[eg.Text(message)], [eg.Button("OK")]], modal=True)
    while win.is_alive():
        event, _ = win.read()
        if event in (None, "OK"):
            break
    win.close()

def popup_ok(message: str, title: str="") -> None:
    """Display a message in a popup window.(Alias popup)"""
    popup(title, message)

def popup_buttons(message: str, title: str = "Question", buttons: list[str] = ["OK", "Cancel"]) -> str:
    """
    Popup window with user defined buttons. Return button's label.

    #### Example:
    ```py
    color = eg.popup_buttons(
        "Which color do you like?", 
        "Question",
        buttons=["red","yellow","green"])
    print(color)
    ```
    """
    result = buttons[-1]
    # create window
    win = eg.Window(title, layout=[
        [eg.Text(message)],
        [eg.Button(s, width=9) for s in buttons],
    ], modal=True)
    # event loop
    while win.is_alive():
        event, _ = win.read()
        if event in buttons:
            result = event
            break
    win.close()
    return result

def popup_yes_no(message: str, title: str = "Question", yes_label: str="Yes", no_label: str="No") -> str:
    """
    Display a message in a popup window with Yes and No buttons. Return "Yes" or "No".

    #### Example:
    Ask user question, [Yes] or [No]
    ```py
    a = eg.popup_yes_no("Do you like Sushi?", "Question")
    print(a) # "Yes" or "No"
    ```
    Ask user question in Japanes [はい] or [いいえ]
    ```py
    ja_a = eg.popup_yes_no("寿司は好き?", "質問", yes_label="はい", no_label="いいえ")
    print(ja_a) # "はい" or "いいえ"
    ```
    """
    # return "Yes" if messagebox.askyesno(title, message) else "No"
    return popup_buttons(message, title, buttons=[yes_label, no_label])

def popup_yes_no_cancel(message: str, title: str = "Question") -> str:
    """Display a message in a popup window with Yes and No buttons. Return "Yes" or "No" or "Cancel"."""
    return popup_buttons(message, title, buttons=["Yes", "No", "Cancel"])

def popup_get_text(message: str, title: str = "", default: str = "") -> (str|None):
    """Display a message in a popup window with a text entry. Return the text entered."""
    return simpledialog.askstring(title, message, initialvalue=default)

def popup_input(message: str, title: str = "", default: str = "") -> (str|None):
    """Display a message in a popup window with a text entry. Return the text entered."""
    result = None
    win = eg.Window(title, layout=[
        [eg.Text(message)],
        [eg.Input(default, key="-user-", width=40)],
        [eg.Button("OK", width=9), eg.Button("Cancel", width=9)]
    ], modal=True)
    while win.is_alive():
        event, values = win.read()
        if event == "OK":
            result = values["-user-"]
            break
        if event == "Cancel":
            break
    win.close()
    return result

def popup_scrolled(message: str, title: str = "", size: tuple[int,int]=[40, 5], readonly: bool=False, font: tuple[str, int]|None=None) -> str|None:
    """Display a message in a popup window with a text entry. Return the text entered."""
    win = eg.Window(title, layout=[
        [eg.Multiline(message, key="-text-", size=size, readonly=readonly, font=font)],
        [eg.Button("OK", width=9), eg.Button("Cancel", width=5)]
    ], modal=True)
    result = None
    while win.is_alive():
        event, _ = win.read()
        if event == "OK":
            result = win["-text-"].get()
            break
        if event == "Cancel":
            break
    win.close()
    return result

def popup_listbox(items: list[str], message: str = "", title: str = "", size: tuple[int,int]=(20, 7), font: tuple[str, int]|None=None, multiple:bool = False) -> str|None:
    """Display Listbox in a popup window"""
    select_mode = eg.LISTBOX_SELECT_MODE_BROWSE if multiple is False else eg.LISTBOX_SELECT_MODE_MULTIPLE
    win = eg.Window(title, layout=[
        [eg.Text(message)],
        [eg.Listbox(values=items, key="-list-", size=size, font=font, select_mode=select_mode)],
        [eg.Button("OK", width=9), eg.Button("Cancel", width=5)]
    ], modal=True)
    result = None
    while win.is_alive():
        event, _ = win.read()
        if event == "Cancel":
            result = None
            break
        if event == "OK":
            selected = win["-list-"].get()
            if multiple:
                result = selected
            else:
                if len(selected) == 1:
                    result = selected[0]
            break
    win.close()
    return result

def popup_error(message: str, title: str="Error") -> None:
    """Display a message in a popup window with an error icon."""
    messagebox.showerror(title, message)

def popup_warning(message: str, title: str="Warning") -> None:
    """Display a message in a popup window with an warning icon."""
    messagebox.showwarning(title, message)

def popup_info(message: str, title: str="Warning") -> None:
    """Display a message in a popup window with an warning icon."""
    messagebox.showwarning(title, message)

def popup_get_file(message: str="", title: str|None=None, initial_folder: str="", save_as: bool=False, multiple_files: bool=False, file_types: tuple[tuple[str, str]]=(("All Files", "*.*"),), no_window: bool|None=None, **kw) -> (str|tuple[str]|None):
    """Popup a file selection dialog. Return the file selected."""
    if title is None:
        title = message
    if save_as:
        result = filedialog.asksaveasfilename(
            title=title,
            initialdir=initial_folder,
            filetypes=file_types,
            **kw)
    else:
        result = filedialog.askopenfilename(
            title=title, 
            initialdir=initial_folder,
            filetypes=file_types,
            multiple=multiple_files, # type: ignore
            **kw)
    return result

def popup_get_folder(message: str="", title: str|None=None, default_path: str="", no_window: bool|None=None, **kw) -> (str|None):
    """Popup a folder selection dialog. Return the folder selected."""
    if title is None:
        title = message
    return filedialog.askdirectory(title=title, initialdir=default_path, **kw)

def popup_color(title: str="", default_color: str|None=None) -> (str|None):
    """Popup a color selection dialog. Return the color selected."""
    col = colorchooser.askcolor(title=title, color=default_color)
    if col[1] is None:
        return default_color
    return f"{col[1]}".upper()

def popup_notify(message: str, title: str="Notification") -> None:
    """Popup a information"""
    show_message(message, title)

#------------------------------------------------------------------------------
# TKinter
def ask_yes_no(message: str, title: str="Question") -> bool:
    """Display a message in a popup window with Yes and No buttons. Return True or False. (use Tkinter)"""
    return messagebox.askyesno(title, message)

def ask_ok_cancel(message: str, title: str="Question") -> bool:
    """Display a message in a popup window with OK and Cancel buttons. Return True or False. (use Tkinter)"""
    return messagebox.askokcancel(title, message)

def ask_retry_cancel(message: str, title: str="Question") -> bool:
    """Display a message in a popup window with Retry and Cancel buttons. Return True or False. (use Tkinter)"""
    return messagebox.askretrycancel(title, message)

def show_message(message: str, title: str="Information") -> None:
    """show message in a popup window"""
    messagebox.showinfo(title, message)

def show_info(message: str, title: str="Information") -> None:
    """show message in a popup window"""
    messagebox.showinfo(title, message)

def msgbox(message: str, title: str="Message") -> None:
    """show message in a popup window like VB"""
    messagebox.showinfo(title, message)

