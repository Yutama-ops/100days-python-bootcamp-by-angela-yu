first = "yutama"
last = "budiman"
def formate_name(f_name, l_name):
    full_name = f_name + " " + l_name
    return full_name.title()

fn = formate_name(first, last)

print(fn)