#Imports
import tkinter as tk
#constants
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = tuple(letters + letters.lower()) # = 54
#classes
class Coder:
    def __init__(self) -> None:
        self._key = None
        self._seed = None
        self._Glossary = None

    def _SerializeKey(self):
        s = 0
        for keyletter in key:
            idx = 0
            for letter in letters:
                idx += 1
                if keyletter == letter:
                    s += idx
                    break
        self._seed = s

    def _DefineGlossary(self):
        #Glossary must have a length of 54 because len(letters) -> 54
        self._Glossary = []
        idx = self._seed % len(letters)
        for _ in range(len(letters)):
            if idx == len(letters): idx = 0
            self._Glossary.append(letters[idx])
            idx +=1
        self._Glossary = tuple(self._Glossary)
        
class Encoder(Coder):
    def __init__(self) -> None:
        super().__init__()
        self._text = None    
    
    def __Encrypt(self):
        NewText = ''
        for TextLetter in self._text:
            idx = -1
            if TextLetter == " ":
                NewText += u"\u2005"
                continue
            for letter in letters:
                idx += 1
                if TextLetter == letter:
                    NewText += str(self._Glossary[idx])
                    break
        return NewText

    def Encode(self,key,text):
        self._key = key
        self._text = text
        self._SerializeKey()
        self._DefineGlossary()
        return self.__Encrypt()

class Decoder(Coder):
    def __init__(self) -> None:
        super().__init__()
        self._text = None

    def __Decrypt(self):
        newtext = ''
        for LetterInText in self._text:
            idx = -1
            if LetterInText == u"\u2005":
                newtext += u"\u2005"
                continue
            for LetterInGlossary in self._Glossary:
                idx += 1
                if LetterInText == LetterInGlossary:
                    newtext += letters[idx]
                    break
        return newtext

    def Decode(self,key,text):
        self._text = text
        self._key = key
        self._SerializeKey()
        self._DefineGlossary()
        return self.__Decrypt()
    
class Window:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.geometry('600x600')

    def open(self):
        self.contents()
        self.window.mainloop()
        return
class EncodeWindow(Window):
    def __init__(self) -> None:
        super().__init__()

    def contents(self):
        tk.Entry(master=self.window).pack()
        tk.Entry(master=self.window).pack()

class DecodeWindow(Window):
    def __init__(self) -> None:
        super().__init__()

    def contents(self):
        pass
class MainWindow(Window):
    def __init__(self) -> None:
        super().__init__()
        self.__open_window = False

    def __EncodeOpen(self):
        print(self.__open_window)
        if self.__open_window == False:
            self.__open_window = True
            window = EncodeWindow()
            window.open()

            self.__open_window = False
        print('test')
            

    def __DecodeOpen(self):
        if self.__open_window == False:
            self.__open_window = True
            window = DecodeWindow()
            window.open()
            self.__open_window = False

    def contents(self):
        EncodeButton = tk.Button(master=self.window,text="Encode",command=self.__EncodeOpen)
        EncodeButton.pack()
        DecodeButton = tk.Button(master=self.window,text="Decode",command=self.__DecodeOpen)
        DecodeButton.pack()
        tk.Button(master=self.window,text='Exit',command=self.window.destroy).pack()
        
# Functions
def Condition(inp):
    if not inp: return False
    for i in inp:
        if i not in letters + (""," "):
            return False
    return True

def GetKey():
    inp = ""
    while not(Condition(inp)):
        inp = str(input("Give a key: "))
    return inp

#main
if __name__ == '__main__':
    encoder = Encoder()
    decoder = Decoder()
    MW = MainWindow()
    
    MW.open()

#testing
    key = GetKey()
    text = str(input("Give text\n"))
    encoded = encoder.Encode(key,text)
    
    decoded = decoder.Decode(key,encoded)

    print(f"Encoded: {encoded}\nDecoded: {decoded}")