import idlelib.colorizer as ic
import idlelib.percolator as ip
import re
import tkinter as tk

root = tk.Tk()
root.title('Python Syntax Highlighting')

text = tk.Text(root)
text.pack()

cdg = ic.ColorDelegator()
# cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat(), re.S)
# cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter|myword)\b|' + ic.make_pat(), re.S)
# Define a pattern to match both 'MYGROUP' and 'MYWORD' with the custom tags
cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|\b(?P<MYWORD>myword)\b|' + ic.make_pat(), re.S)

cdg.idprog = re.compile(r'\s+(\w+)', re.S)

cdg.tagdefs['MYGROUP'] = {'foreground': '#7F7F7F', 'background': '#FFFFFF'}
cdg.tagdefs['MYWORD'] = {'foreground': '#FF00FF', 'background': '#FFFFFF'}

# These five lines are optional. If omitted, default colours are used.
cdg.tagdefs['COMMENT'] = {'foreground': '#FF0000', 'background': '#FFFFFF'}
cdg.tagdefs['KEYWORD'] = {'foreground': '#007F00', 'background': '#FFFFFF'}
cdg.tagdefs['BUILTIN'] = {'foreground': '#7F7F00', 'background': '#FFFFFF'}
cdg.tagdefs['STRING'] = {'foreground': '#7F3F00', 'background': '#FFFFFF'}
cdg.tagdefs['DEFINITION'] = {'foreground': '#007F7F', 'background': '#FFFFFF'}
print(cdg.tagdefs)

ip.Percolator(text).insertfilter(cdg)

root.mainloop()