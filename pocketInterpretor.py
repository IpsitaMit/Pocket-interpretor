from cProfile import label
# from gettext import bind_textdomain_codeset
from operator import length_hint
from re import L
from tkinter import *
from PIL import ImageTk,Image
from googletrans import Translator

trans=Translator()
main_window = Tk()

translated_txt=StringVar()

#labels
Label(main_window, text= "Text").grid(row=0,column=0)
Label(main_window, text= "Language").grid(row=2,column=0)
show=Label(main_window,textvariable= translated_txt).grid(row=5)
#text input
name=Entry(main_window, width= 50, borderwidth=5)
age=Entry(main_window, width=50, borderwidth=5)

lang = {'af': 'afrikaans','sq': 'albanian','am': 'amharic','ar': 'arabic','hy': 'armenian','az': 'azerbaijani','eu': 'basque','be': 'belarusian','bn': 'bengali','bs': 'bosnian','bg': 'bulgarian','ca': 'catalan','ceb': 'cebuano','ny': 'chichewa','zh-cn': 'chinese (simplified)','zh-tw': 'chinese (traditional)','co': 'corsican','hr': 'croatian','cs': 'czech','da': 'danish','nl': 'dutch','en': 'english','eo': 'esperanto','et': 'estonian','tl': 'filipino','fi': 'finnish','fr': 'french','fy': 'frisian','gl': 'galician','ka': 'georgian','de': 'german','el': 'greek','gu': 'gujarati','ht': 'haitian creole','ha': 'hausa','haw': 'hawaiian','iw': 'hebrew','he': 'hebrew','hi': 'hindi','hmn': 'hmong','hu': 'hungarian','is': 'icelandic','ig': 'igbo','id': 'indonesian','ga': 'irish','it': 'italian','ja': 'japanese','jw': 'javanese','kn': 'kannada','kk': 'kazakh','km': 'khmer','ko': 'korean','ku': 'kurdish (kurmanji)','ky': 'kyrgyz','lo': 'lao','la': 'latin','lv': 'latvian','lt': 'lithuanian','lb': 'luxembourgish','mk': 'macedonian','mg': 'malagasy','ms': 'malay','ml': 'malayalam','mt': 'maltese','mi': 'maori','mr': 'marathi','mn': 'mongolian','my': 'myanmar (burmese)','ne': 'nepali','no': 'norwegian','or': 'odia','ps': 'pashto','fa': 'persian','pl': 'polish','pt': 'portuguese','pa': 'punjabi','ro': 'romanian','ru': 'russian','sm': 'samoan','gd': 'scots gaelic','sr': 'serbian','st': 'sesotho','sn': 'shona','sd': 'sindhi','si': 'sinhala','sk': 'slovak','sl': 'slovenian','so': 'somali','es': 'spanish','su': 'sundanese','sw': 'swahili','sv': 'swedish','tg': 'tajik','ta': 'tamil','te': 'telugu','th': 'thai','tr': 'turkish','uk': 'ukrainian','ur': 'urdu','ug': 'uyghur','uz': 'uzbek','vi': 'vietnamese','cy': 'welsh','xh': 'xhosa','yi': 'yiddish','yo': 'yoruba','zu': 'zulu'}


def on_click():
    translated_txt.set("")
    n=name.get()
    a=age.get()
    l=list(lang.values())    
    k=list(lang.keys())
    # Label(main_window,text=  f"name = {k[l.index(n)]} \nage = {k[l.index(a)]}").grid(row=3)
    out=trans.translate(n,dest=k[l.index(a)])
    translated_txt.set(out.text)

def show_in_entry(ent):
    # temp=ent.get()
    ent.delete(0,END)
    # ent.insert(0,temp+val.get())
    ent.insert(0,lang[val.get()])

def disp(p):
    global val
    val=StringVar()

    for i in lang.keys():        
        Radiobutton(frame,text=lang[i],value=i, variable=val,tristatevalue="@123ab", command=lambda:show_in_entry(p)).pack()


def close_list(btn1,btn2,r,c):
    btn1.grid_forget()
    btn2.grid(row=r,column=c)
    frame.grid_forget()

def show_list(ent,btn1,btn2,r,c):
    global frame
    frame=LabelFrame(main_window,padx=20,pady=20)
    frame.grid(row=r+1,column=c-1)
    btn1.grid_forget()
    btn2.grid(row=r,column=c)
    disp(ent)   




 #buttons
submit=Button(main_window, text="submit",command=on_click)
# name_search=Button(main_window, text="options",command=lambda:show_list(name,name_search,name_done,0,2))
# name_done=Button(main_window, text="done",command=lambda:close_list(name_done,name_search,0,2))
age_search=Button(main_window, text="options",command=lambda:show_list(age,age_search,age_done,2,2))
age_done=Button(main_window, text="done",command=lambda:close_list(age_done,age_search,2,2))


#placing on screen
name.grid(row=0,column=1)
age.grid(row=2,column=1)
submit.grid(row=4,column=1)
# name_search.grid(row=0,column=2)
age_search.grid(row=2,column=2)



main_window.mainloop()
