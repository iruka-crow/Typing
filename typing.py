"""
Typing Practice Program v1

指定されたキーボードの文字をいかに早く打てるかを計測するプログラム
文字の場所を覚えるときに使えます。

1. 母音モード
    母音のみ出題

2. 子音モード
    子音のみ出題

3. 全複合モード
    母音、子音、感嘆符と数字も含んで出題

4. 日本語かなモード
    日本語かな一文字を出題

5. 英文入力モード
    簡単な英文で練習

6. 日本語文入力モード [[[未実装]]]
    簡単な日本語文で練習
"""

import time,random

#一文字のときのワードチェッカー
def check_letter_match(desired_letter, input_letter):
    # 入力文字と求める文字を大文字に変換して比較
    desired_letter = desired_letter.lower()
    input_letter = input_letter.lower()

    if desired_letter == input_letter:
        return True
    else:
        return False

bvowels = [97,105,117,101,111]
bconsonant = [x for x in range(97,123)]
alphabet = list(map(chr,bconsonant+bvowels))
for i in bvowels:
    bconsonant.pop(bconsonant.index(i))
vowels = list(map(chr,bvowels))
consonant = list(map(chr,bconsonant))
alphabet.append('!')
alphabet.append('?')

#日本語
# 「あ」から「ん」までのひらがなのUnicodeコードポイント範囲
hiragana_start = ord("あ")
hiragana_end = ord("ん")

hiragana_list = [chr(code) for code in range(hiragana_start, hiragana_end + 1)]

# 濁点のひらがなを追加
dakuten_hiragana = [
    "が", "ぎ", "ぐ", "げ", "ご",
    "ざ", "じ", "ず", "ぜ", "ぞ",
    "だ", "ぢ", "づ", "で", "ど",
    "ば", "び", "ぶ", "べ", "ぼ",
    "ぱ", "ぴ", "ぷ", "ぺ", "ぽ"
]

# ひらがなリストに濁点のひらがなを追加
hiragana_list.extend(dakuten_hiragana)
#簡単に打てないひらがなリスト
non_lists = ['ゐ','ゑ','ぃ','ぅ','ぇ','ぉ','っ','ゃ','ゅ','ょ']
for i in non_lists:
    hiragana_list.pop(hiragana_list.index(i))


#設定 [問題数=30]
setting = [30]

def mode1():
    #母音モード
    print("\n\n")
    print("母音モード：\n始めるにはエンターキーを押す...")
    inp = input()
    ans_word = ""
    ans_sum = 0
    #開始
    print()
    t_start = time.time()
    for i in range(setting[0]):
        ans_word = vowels[random.randint(0,4)]
        print("\r "+ans_word,end=' ')
        inp = input(">> ")
        ans_sum += 1 if check_letter_match(ans_word,inp) else 0
    t_end = time.time()
    print("--終了!!-\n")
    print(f'time: %3ds\n正解数: %3d/%3d\n' % (t_end - t_start,ans_sum,setting[0]))
    print()
    return 0
def mode2():
    #子音モード
    print("\n\n")
    print("子音モード：\n始めるにはエンターキーを押す...")
    inp = input()
    ans_word = ""
    ans_sum = 0
    #開始
    print()
    t_start = time.time()
    for i in range(setting[0]):
        ans_word = consonant[random.randint(0,20)]
        print("\r "+ans_word,end=' ')
        inp = input(">> ")
        ans_sum += 1 if check_letter_match(ans_word,inp) else 0
    t_end = time.time()
    print("--終了!!-\n")
    print(f'time: %3ds\n正解数: %3d/%3d\n' % (t_end - t_start,ans_sum,setting[0]))
    print()
    return 0
def mode3():
    #複合モード
    print("\n\n")
    print("複合モード：\n始めるにはエンターキーを押す...")
    inp = input()
    ans_word = ""
    ans_sum = 0
    #開始
    print()
    t_start = time.time()
    for i in range(setting[0]):
        ans_word = alphabet[random.randint(0,27)]
        print("\r "+ans_word,end=' ')
        inp = input(">> ")
        ans_sum += 1 if check_letter_match(ans_word,inp) else 0
    t_end = time.time()
    print("--終了!!-\n")
    print(f'time: %3ds\n正解数: %3d/%3d\n' % (t_end - t_start,ans_sum,setting[0]))
    print()
    return 0
def mode4():
    #日本語モード
    print("\n\n")
    print("日本語モード：\n始めるにはエンターキーを押す...")
    inp = input()
    ans_word = ""
    ans_sum = 0
    #開始
    print()
    t_start = time.time()
    for i in range(setting[0]):
        ans_word = hiragana_list[random.randint(0,96)]
        print("\r "+ans_word,end=' ')
        inp = input(">> ")
        ans_sum += 1 if check_letter_match(ans_word,inp) else 0
    t_end = time.time()
    print("--終了!!-\n")
    print(f'time: %3ds\n正解数: %3d/%3d\n' % (t_end - t_start,ans_sum,setting[0]))
    print()
    return 0
def mode5():
    #英文入力モード
    
    #英文セット
    english_sentences = [
        "Hello, how are you?",
        "I love programming.",
        "This is a test sentence.",
        "Python is a versatile language.",
        "The quick brown fox jumps over the lazy dog.",
        "Learning new things is always exciting.",
        "I enjoy listening to music in my free time.",
        "Coding is a valuable skill in today's world.",
        "She plays the piano beautifully.",
        "Reading books is a great way to relax.",
        "The sun is shining brightly today.",
        "I need to buy groceries after work.",
        "He is a talented artist.",
        "Do you want to go for a walk?",
        "She has a beautiful smile.",
        "We're going on a vacation next week.",
        "It's important to stay hydrated.",
        "The conference is scheduled for tomorrow.",
        "He won the first prize in the competition.",
        "I have a lot of work to do.",
        "She's a great cook.",
        "I can't believe it's already December.",
        "He always tells funny jokes.",
        "She's a dedicated teacher.",
        "Let's meet at the coffee shop.",
        "The movie starts at 7 PM.",
        "I like to go for a run in the morning.",
        "This restaurant serves delicious food.",
        "They have a lovely garden.",
        "She's a talented singer.",
        "I'm looking forward to the weekend.",
        "The book was so interesting that I couldn't put it down.",
        "He's a reliable friend.",
        "The weather is perfect for a picnic.",
        "She's a successful entrepreneur.",
        "I'm feeling a bit tired today.",
        "The museum is closed on Mondays.",
        "He's a passionate photographer.",
        "Let's make a plan for the future.",
        "I'll be there in 10 minutes.",
        "The city is known for its cultural diversity.",
        "I have a busy day ahead of me.",
        "She's a talented dancer.",
        "I enjoy spending time with my family.",
        "The concert was amazing.",
        "I have to finish this report by tomorrow.",
        "She's an excellent student.",
        "I like to watch the sunset.",
        "He's a skilled carpenter.",
        "I'll call you later.",
        "The restaurant is fully booked tonight.",
        "I have a lot of hobbies.",
        "She's a kind-hearted person.",
        "I'll be right back.",
        "The mountain is covered in snow.",
        "I have a sweet tooth.",
        "She's a fashion designer.",
        "I need to clean my room.",
        "He's a great basketball player.",
        "I'm excited about the upcoming trip.",
        "She's a wonderful actress.",
        "I like to read science fiction novels.",
        "The dog is barking loudly.",
        "I have a craving for pizza.",
        "She's an adventurous traveler.",
        "I'll take a break now.",
        "The cat is sleeping on the couch.",
        "I have a lot of responsibilities at work.",
        "She's a skilled writer.",
        "I'll see you tomorrow.",
        "The beach is so peaceful.",
        "I enjoy watching documentaries.",
        "He's a computer programmer.",
        "I need to do the laundry.",
        "She's a caring nurse.",
        "I'm running out of time.",
        "The garden is full of colorful flowers.",
        "I have a good sense of humor.",
        "She's a talented pianist.",
        "I'll be careful.",
        "The car is parked in the garage.",
        "I have a lot of dreams and goals.",
        "She's a dedicated volunteer.",
        "I'll do my best.",
        "The river flows gently.",
        "I have a busy schedule this week.",
        "She's a creative artist.",
        "I like to cook homemade meals.",
        "The movie theater is crowded.",
        "I have a passion for photography.",
        "She's a strong leader.",
        "I'll see you soon.",
        "The forest is full of wildlife.",
        "I enjoy listening to classical music.",
        "He's a talented chef.",
        "I need to finish this project.",
        "She's a reliable colleague.",
        "I'm feeling inspired today.",
    ]
    print("\n\n")
    print("英文モード：\n始めるにはエンターキーを押す...")
    inp = input()
    ans_sentence = ""
    ans_sum = 0
    #開始
    print()
    t_start = time.time()
    for i in range(setting[0]):
        ans_sentence = english_sentences[random.randint(0,97)]
        print("\r "+ans_sentence,end=' ')
        inp = input(">> ")
        ans_sum += 1 if check_letter_match(ans_sentence,inp) else 0
    t_end = time.time()
    print("--終了!!-\n")
    print(f'time: %3ds\n正解数: %3d/%3d\n' % (t_end - t_start,ans_sum,setting[0]))
    print()
    return 0
def mode6():
    #日本語文入力モード
    pass

while True:
    print("タイピング練習プログラム")
    inp = input("モード選択 >> ")
    if inp == "exit":
        break
    elif inp == "1":
        mode1()
    elif inp == "2":
        mode2()
    elif inp == "3":
        mode3()
    elif inp == "4":
        mode4()
    elif inp == "5":
        mode5()
    elif inp == "6":
        mode6()
    elif inp == "setting":
        inp = input(f"回数を指定：現在は%3d回です。\n>>>" % setting[0])
        try:
            inp = int(inp)
            setting[0] = inp
            print(f'回数を%3d回に変更しました。\n' % setting[0])
            continue
        except:
            print("有効な数字(整数)を入力してください")
            continue