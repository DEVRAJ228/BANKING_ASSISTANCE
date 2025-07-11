from googletrans import Translator

# Language mapping dictionary
LANGUAGES = {
    1: ('hi', 'हिंदी'),
    2: ('ta', 'தமிழ்'),
    3: ('te', 'తెలుగు'),
    4: ('bn', 'বাংলা'),
    5: ('gu', 'ગુજરાતી'),
    6: ('kn', 'ಕನ್ನಡ'),
    7: ('ml', 'മലയാളം')
}

def select_language():
    """Display language selection menu and return language code"""
    print("\n" + "="*50)
    print("भाषा चुनें / Choose language:")
    for num, (code, name) in LANGUAGES.items():
        print(f"{num}. {name}")
    
    while True:
        try:
            choice = int(input("Enter choice (1-7): "))
            if 1 <= choice <= 7:
                return LANGUAGES[choice][0]
            print("Invalid choice! Please enter 1-7")
        except ValueError:
            print("Please enter a number")

def translate_text(text, dest_lang='hi'):
    """Translate text to target language"""
    try:
        translator = Translator()
        return translator.translate(text, dest=dest_lang).text
    except:
        return text  # Return original if translation fails
