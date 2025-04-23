from collections import Counter

def string_1(text):
        count = 0
        i = 0
        while i < len(text):
            if text[i]== ' ':
                count += 1
            i +=1
        print(f'number of words with space: {count}')

def string_2(text):
        text = Counter(text.lower())
        for letter, count in text.items():
            if letter.isalpha():
                print(f"Letter '{letter}': {count} times")

def string_3(text):
    phrases = [phrase.strip() for phrase in text.split(',')]
    
    sorted_phrases = sorted(phrases, key=lambda x: x.lower())
    
    print("Словосочетания в алфавитном порядке:")
    
    for phrase in sorted_phrases:
        print(phrase)
    print("\n")    
       

def task4():
    text = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her. "
    
    while True:
        try:
            choice = int(input("""number of words with space -> enter 1
amount of each simbil -> enter 2
alphabetically list phrases separated by commas -> enter 3
                               """))
            match choice:
                case 1: string_1(text)
                case 2: string_2(text)
                case 3: string_3(text)
                case _: 
                    print("End of work")
                    break
        except ValueError:
            print("Please enter right number")
            continue
