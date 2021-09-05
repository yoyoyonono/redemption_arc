# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[mcname]")
define ss = Character("Sensei")
define tu = Character("[tutorname]")

# The game starts here.

transform midright:
    xalign 0.75

transform midleft:
    xalign 0.25

label start:
    $ totalrightanswers = 0
    $ thistestrightanswers = 0
    $ tutorname = "pocky sensei"
    $ mcname = renpy.input("What is your name?").strip()
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    "Hi, I'm [mcname], and I'm a Junior student at Thomas Jefferson High School."

    "The school year has just begun and I've already failed all three assignments in japanese."

    scene bg classroom 1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ss

    # These display lines of dialogue.

    ss "[mcname], you have been failing at Japanese, this can't go on."

    ss "I can't teach you well enough so I have found you a tutor."
 
    show ss at offscreenright with moveoutright

    with Pause(1.0) 

    show ss at offscreenright
    show tu happy at offscreenleft
    with None
    
    show ss at midright
    show tu happy at midleft
    with ease

    ss "[mcname], this is [tutorname]."
    
    tu "Nice to meet you [mcname]. Let's begin your training."

    show ss at offscreenright
    show tu happy at center
    with ease

    menu intro_response:
        "Nice to meet you too, let's start!":
            mc "Nice to meet you too, let's start!"
        "Alright!":
            mc "Alright!"
        "よろしくおねがいします":
            mc "よろしくおねがいします"
        "UwU":
            mc "UwU"
            show tu angry
            tu "no"


    scene bg classroom 2
    with fade
    with Pause(0.25)

    show tu happy at center
    with dissolve

    tu "Let’s start with some vocabulary!"

    menu test_1_question_1:
        tu "What verb would best complete this sentence?　すしを"
        "ねます":
            mc "ねます"
            tu "Sorry that’s wrong, the correct answer was 食べます"
        "つくります":
            mc "つくります"
            tu "Sorry that’s wrong, the correct answer was 食べます"
        "食べます（たべます）":
            mc "食べます"
            tu "Yes! That's correct, good job!"
            $ thistestrightanswers += 1
        "飲みます（のみます）":
            mc "飲みます"
            tu "Sorry that’s wrong, the correct answer was 食べます"
        
    menu test_1_question_2:
        tu "Which hiragana matches the kanji：「新しい」　くるまですれ。"
        "あたらしい":
            mc "あたらしい"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "あだらしい":
            mc "あだらしい"
            tu "Sorry that’s wrong, the right answer was あたらしい"
        "あらたしい":
            mc "あらたしい" 
            tu "Sorry that’s wrong, the right answer was あたらしい"
        "あらだしい":
            mc "あらだしい" 
            tu "Sorry that’s wrong, the right answer was あたらしい"

    menu test_1_question_3:
        tu "What is the reading of this kanji in the sentence: あしたは「雨」ですか。"
        "ゆき":
            mc "ゆき"
            tu "Sorry that’s wrong, the right answer was あめ"
        "はれ":
            mc "はれ"
            tu "Sorry that’s wrong, the right answer was あめ"
        "くもり":
            mc "くもり"
            tu "Sorry that’s wrong, the right answer was あめ"
        "あめ":
            mc "あめ"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1

    menu test_1_question_4:
        tu "Which kanji represents the hiragana：「そと」で　まちましょう。"
        "外":
            mc "外"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "言":
            mc "言"
            tu "Sorry that’s wrong, the right answer was 外"
        "中":
            mc "中"
            tu "Sorry that’s wrong, the right answer was 外"
        "頃":
            mc "頃"
            tu "Sorry that’s wrong, the right answer was 外"
    
    menu test_1_question_5:
        tu "Which hiragana matches the kanji：しゃしんは　はこ　の「中」に　あります。"
        "そば":
            mc "そば"
            tu "Sorry that’s wrong, the right answer was なか"
        "そと":
            mc "そと"
            tu "Sorry that’s wrong, the right answer was なか"
        "なか":
            mc "なか"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "よこ":
            mc "よこ"
            tu "Sorry that’s wrong, the right answer was なか"

    tu "You are doing a great job."

    menu test_1_question_6:
        tu "Figure out the correct sentence ending：しつもんが"
        "あります。":
            mc "あります。"
            tu "Perfect! Keep it up!"
            $ thistestrightanswers += 1
        "います。":
            mc "います。"
            tu "Sorry that’s wrong, the right answer was あります。"


    tu "Almost there! Three questions left after you finish this one."

    menu test_1_question_7:
        tu "Figure out which hiragana best suits the sentence：ここは　（＿＿＿＿）です。　べんきょできません。"
        "くらい":
            mc "くらい"
            tu "Sorry that’s wrong, the right answer was うるさい"
        "さむい":
            mc "さむい"
            tu "Sorry that’s wrong, the right answer was うるさい"
        "うるさい":
            mc "うるさい"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "あぶない":
            mc "あぶない"
            tu "Sorry that’s wrong, the right answer was うるさい"

    menu test_1_question_8:
        tu "Which particle should fill in the blank? これ「＿＿」えんぴつです。"
        "に":
            mc "に"
            tu "Sorry, that's wrong, the right answer was は"
        "を":
            mc "を"
            tu "Sorry, that's wrong, the right answer was は"
        "は":
            mc "は"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "や":
            mc "や"
            tu "Sorry, that's wrong, the right answer was は"

    tu "This is your second to last question."

    menu test_1_question_9:
        tu "Figure out which hiragana best suits the sentence：あそこで　タクシーに「＿＿＿＿＿」。"
        "のりました":
            mc "のりました"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "あがりました":
            mc "あがりました"
            tu "Sorry that’s wrong, the right answer was のりました"
        "つきました":
            mc "つきました"
            tu "Sorry that’s wrong, the right answer was のりました"
        "はいりました":
            mc "はいりました"
            tu "Sorry that’s wrong, the right answer was のりました"

    menu test_1_question_10:
        tu "Which particle should fill in the blank? 弟　（おとうと）は　へや　「＿」そうじを　しました。"
        "が":
            mc "が"
            tu "Sorry, that's wrong, the right answer was に"
        "を":
            mc "を"
            tu "Sorry, that's wrong, the right answer was に"
        "に":
            mc "に"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "の":
            mc "の"
            tu "Sorry, that's wrong, the right answer was に"

    $ totalrightanswers += thistestrightanswers

    if thistestrightanswers >= 7:
        tu "Good job! It seems like you've learned a lot." 
        tu "I'll see you tomorrow!"
    else:
        tu "You failed..."
        tu "Unfortunately the session is over so you'll have to try again tomorrow."

    scene bg bedroom e evening
    "I enjoyed that, let's see if I can improve some more..."

    scene bg bedroom e night
    with fade
    "Wow, I spent so much time studying, I guess I should go to sleep."

    scene bg bedroom e morning
    with fade
    "dude's gonna say something here because why not"

    scene bg classroom 1
    with fade
    
    show ss

    ss "There will be a test tomorrow, so please be prepared."
    "This is my chance!"

    scene bg bedroom a
    with fade

    show tu happy
    mc "I have a test tomorrow"
    tu "Well, let's start then."

    $ thistestrightanswers = 0

    menu test_2_question_1:
        tu "Figure out which hiragana matches the kanji：この　いすは「小さい」です。"
        "ちいさい":
            mc "ちいさい"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "ちさい":
            mc "ちさい"
            tu "Sorry that’s wrong, the right answer was ちいさい"
        "しいさい":
            mc "しいさい"
            tu "Sorry that’s wrong, the right answer was ちいさい"
        "しさい":
            mc "しさい"
            tu "Sorry that’s wrong, the right answer was ちいさい"
        
    menu test_2_question_2:
        tu "あしたは「火曜日」です。"
        "どようび":
            mc "どようび"
            tu "Sorry that’s wrong, the right answer was かようび"
        "すいようび":
            mc "すいようび"
            tu "Sorry that’s wrong, the right answer was かようび"
        "かようび":
            mc "かようび"
            tu "Yes! That's correct, good job!"
            $ thistestrightanswers += 1
        "にちようび":
            mc "にちようび"

    menu test_2_question_3:
        tu "せいとは「百人」です。"
        "ひゃくにん":
            mc "ひゃくにん"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "びゃくにん":
            mc "びゃくにん"
            tu "Sorry that’s wrong, the right answer was ひゃくにん"
        "ひゃくじん":
            mc "ひゃくじん"
            tu "Sorry that’s wrong, the right answer was ひゃくにん"
        "びゃくじん":
            mc "びゃくじん"
            tu "Sorry that’s wrong, the right answer was ひゃくにん"
    menu test_2_question_4:
        tu "Figure out which kanji represents the hiragana：「魚」が　たくさん　いますよ。"
        "ねこ":
            mc "ねこ"
            tu "Sorry, that's wrong, the right answer was さかな。"
        "とり":
            mc "とり"
            tu "Sorry, that's wrong, the right answer was さかな。"
        "いぬ":
            mc "いぬ"
            tu "Sorry, that's wrong, the right answer was さかな。"
        "さかな":
            mc "さかな"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
    
    menu test_2_question_5:
        tu "Figure out which hiragana matches the kanji：たまごを「三つ」とって　ください。"
        "いつつ":
            mc "いつつ"
            tu "Sorry, that's wrong, the right answer was みっつ。"
        "みっつ":
            mc "みっつ"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "さんつ":
            mc "さんつ"
            tu "Sorry, that's wrong, the right answer was みっつ。"
        "ごつ":
            mc "ごつ"
            tu "Sorry, that's wrong, the right answer was みっつ。"

    menu test_2_question_6:
        tu "Now, pick the right katakana for the phrase：この「わいしゃつ」をください。"
        "ウイシャソ":
            mc "ウイシャソ"
            tu "Sorry, that's wrong, the right answer was ワイシャツ。"
        "ウイシャツ":
            mc "ウイシャツ"
            tu "Sorry, that's wrong, the right answer was ワイシャツ。"
        "ワイシャソ":
            mc "ワイシャソ"
            tu "Sorry, that's wrong, the right answer was ワイシャツ。"
        "ワイシャツ":
            mc "ワイシャツ"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1

    tu "Almost there! Three questions left after you finish this one."
    menu test_2_question_7:
        tu "Pick the right kanji for the phrase：わたしのくには「かわ」がおおいです。"
        "花":
            mc "花"
            tu "Sorry, that's wrong, the right answer was 川。"
        "山":
            mc "山"
            tu "Sorry, that's wrong, the right answer was 川。"
        "川":
            mc "川"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "木":
            mc "木"
            tu "Sorry, that's wrong, the right answer was 川。"

    menu test_2_question_8:
        tu "Which kanji is in the phrase? やんさんの「がっこう」はどこですか。"
        "宇校":
            mc "宇校"
            tu "Sorry, that's wrong, the right answer was 学校。"
        "学校":
            mc "学校"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "宇枚":
            mc "宇枚"
            tu "Sorry, that's wrong, the right answer was 学校。"
        "学枚":
            mc "学枚"
            tu "Sorry, that's wrong, the right answer was 学校。"

    tu "This is your second to last question. "

    menu test_2_question_9:
        tu "Figure out which hiragana best suits the sentence：このざっしを「みて」ください。"
        "見て":
            mc "見て"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "買て":
            mc "買て"
            tu "Sorry, that's wrong, the right answer was 見て。"
        "貝て":
            mc "貝て"
            tu "Sorry, that's wrong, the right answer was 見て。"
        "目て":
            mc "目て"
            tu "Sorry, that's wrong, the right answer was 見て。"

    menu test_2_question_10:
        tu "Which kanji goes with the phrase? このカメラは「たかい」ですね。"
        "高い":
            mc "高い"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "安い":
            mc "安い"
            tu "Sorry, that's wrong, the right answer was 高い。"
        "古い":
            mc "古い"
            tu "Sorry, that's wrong, the right answer was 高い。"
        "新い":
            mc "新い"
            tu "Sorry, that's wrong, the right answer was 高い。"

    if thistestrightanswers == 10:
        tu "You got all 10 questions right! You're a master!"
    elif thistestrightanswers >= 7:
        tu "You're doing great! Let's see how you do tomorrow."
    else:
        tu "You failed. I'm sorry, there's not much more I can do for you."
    
    scene bg bedroom e night
    with dissolve

    mc "I hope I'm ready for tomorrow."

    scene bg classroom 1
    with dissolve

    return
