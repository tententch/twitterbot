import pythainlp
import pandas as pd
import string 
import re

file_errors_location = 'howtoting.xlsx'
df1 = pd.read_excel(file_errors_location)
df=df1['text']
df2=df1['test']




def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
    



def clean(string_):
    
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    
    SChar = '!@#$%^&*()-=<>?/~%`~:. '

    for char in SChar:
        string_ = string_.replace(char, "")

    for char in string_:
        check = isEnglish(char)
        if check == True:
            string_ = string_.replace(char, "")
    string_ = emoji_pattern.sub(r'', string_)
    
    #print(string_)
    return string_




j=0
result = ''
for i in range(len(df)):
        if 'RT' not in df[i] and 'นายก' not in df[i]:
            j+=1
            test = clean(df[i])
            test = pythainlp.word_tokenize(test)
            for k in range(len(test)):
                #print(test[k])
           
                result = result+' '+test[k]
            result = result+'\n'
            
for i in range(len(df2)):
        if 'RT' not in str(df2[i]):
            j+=1
            test = clean(str(df2[i]))
            test = pythainlp.word_tokenize(test)
            for k in range(len(test)):
                #print(test[k])
           
                result = result+' '+test[k]
            result = result+'\n'
        
if 'ฮา ว ทู ทิ้ง' in result:
    result = result.replace('ฮา ว ทู ทิ้ง', "เรื่อง นี้")

print(result)    

with open("test.txt", "w", encoding='utf-8') as text_file:
    text_file.write(result)

