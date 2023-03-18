import pandas as pd

def excel2txt(excel_path, txt_path):
  words = pd.read_excel(excel_path).values
  
  with open(txt_path, "w") as f:
    for word in words:
      wd = str(word[0]).lower()
      wd = wd.replace('\xa0', ' ')
      f.write(wd + '\n')
# def excel2txt()

