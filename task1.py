my_text = 'фбв лиьпалабвипио абв абваотпвба лваивли типотабвпова абв оырмгкл'

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return my_text

my_text = del_some_words(my_text)
print(my_text)