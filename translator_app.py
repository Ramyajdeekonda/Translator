from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")
        self.root.geometry("800x400")
        self.root.config(bg='ghost white')

        # Create Translator object
        self.translator = Translator()

        # Language options
        self.language_options = {
            'Telugu': 'te',
            'English': 'en',
            'Hindi': 'hi',
            'Tamil': 'ta',
            'Spanish': 'es',
            'French': 'fr',
            'German': 'de',
            'Chinese': 'zh-cn'
        }

        # GUI Elements
        Label(self.root, text="Language Translator", font="Arial 20 bold", bg='ghost white').pack(pady=10)

        # Input Frame
        input_frame = Frame(self.root, bg='ghost white')
        input_frame.pack(pady=5)

        Label(input_frame, text="Source Language:", font='arial 12 bold', bg='ghost white').pack(side=LEFT, padx=5)
        self.src_lang = ttk.Combobox(input_frame, values=list(self.language_options.keys()), width=20)
        self.src_lang.set('English')
        self.src_lang.pack(side=LEFT, padx=5)

        # Output Frame
        output_frame = Frame(self.root, bg='ghost white')
        output_frame.pack(pady=5)

        Label(output_frame, text="Target Language:", font='arial 12 bold', bg='ghost white').pack(side=LEFT, padx=5)
        self.dest_lang = ttk.Combobox(output_frame, values=list(self.language_options.keys()), width=20)
        self.dest_lang.set('Telugu')
        self.dest_lang.pack(side=LEFT, padx=5)

        # Text Areas
        Label(self.root, text="Enter Text:", font='arial 12 bold', bg='ghost white').pack(pady=5)
        self.src_text = Text(self.root, font='arial 12', height=5, width=60)
        self.src_text.pack(pady=5)

        # Translate Button
        translate_btn = Button(self.root, text="Translate", font='arial 12 bold', 
                             pady=5, command=self.translate_text)
        translate_btn.pack(pady=10)

        Label(self.root, text="Translation:", font='arial 12 bold', bg='ghost white').pack(pady=5)
        self.dest_text = Text(self.root, font='arial 12', height=5, width=60)
        self.dest_text.pack(pady=5)

    def translate_text(self):
        try:
            # Get the source and target language codes
            src_lang_code = self.language_options[self.src_lang.get()]
            dest_lang_code = self.language_options[self.dest_lang.get()]

            # Get the text to translate
            text = self.src_text.get(1.0, END).strip()

            # Perform translation
            translated = self.translator.translate(text, 
                                                src=src_lang_code,
                                                dest=dest_lang_code)

            # Clear previous translation and insert new translation
            self.dest_text.delete(1.0, END)
            self.dest_text.insert(END, translated.text)

        except Exception as e:
            self.dest_text.delete(1.0, END)
            self.dest_text.insert(END, f"Error: {str(e)}")

if __name__ == "__main__":
    # Create main window
    root = Tk()
    app = TranslatorApp(root)
    root.mainloop() 