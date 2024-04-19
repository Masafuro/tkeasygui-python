import subprocess
import TkEasyGUI as eg
import sys

WEB_SITE = "https://github.com/kujirahand/tkeasygui-python/"
# define layout
layout=[
    [eg.Text(f"{eg.__doc__.strip()}", color="navy")],
    [eg.Frame(f"Version", expand_x=True, layout=[
        [
            eg.Text(f"TkEasyGUI:",size=(10,1), text_align="right"),
            eg.Button(f"v{eg.__version__}", key="-b1-"),
            eg.Button("Web")
        ],
    ])],
    [eg.Frame("System info:", layout=[
       [eg.Multiline(f"{eg.get_system_info()}", key="-sys-info-", size=(40, 5), expand_x=True)],
        [eg.Button("Copy")],
    ])],
    [eg.Column(layout=[[eg.Button("OK"), eg.Button("Close")]], text_align="right", expand_x=True),],
]
# window create
with eg.Window("Version info", layout=layout, font=("", 14), row_padding=5) as window:
    # event loop
    for event, values in window.event_iter():
        print("#", event, values)
        if event == "OK":
            eg.popup("Thank you.")
            break
        if event == "Close":
            break
        if event in ["-b1-", "-b2-", "-b3-"]:
            btn: eg.Button = window[event]
            label = btn.get_text()
            eg.set_clipboard(label)
            eg.popup(f"Copied to clipboard:\n{label}")
        if event == "Copy":
            text = window["-sys-info-"].get_text()
            eg.set_clipboard(text)
            eg.popup(f"Copied to clipboard.")
        if event == "Web":
            if eg.is_mac():
                subprocess.call(f"open {WEB_SITE}", shell=True)
            else:
                subprocess.call(f"start {WEB_SITE}", shell=True)
