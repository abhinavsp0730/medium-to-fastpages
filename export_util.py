def save_md(text, path, filename):
    with open(path + '/'+filename+'.md','w') as file:
        file.write(text)