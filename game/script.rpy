# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    config.searchpath.extend(['game/audio'])

    def dismiss_callback():
        renpy.play("audio/advance.wav")
        return True

    config.say_allow_dismiss = dismiss_callback

define mc = Character("[mcname]")
define ss = Character("Sensei")
define tu = Character("[tutorname]")

# The game starts here.

transform midright:
    xalign 0.75

transform midleft:
    xalign 0.25

label splashscreen:
    $ renpy.pause(0.25)

    play sound splash
    scene black 
    $ renpy.pause(1, hard=True)

    show text "{size=+20}オーサムチーム"
    with dissolve
    $ renpy.pause(2, hard=True)

    hide text with dissolve
    show text "{size=+20}Presents"
    $ renpy.pause(1, hard=True)

    hide text with dissolve
    $ renpy.pause(1, hard=True)

    return

label start:
    $ totalrightanswers = 0
    $ thistestrightanswers = 0
    $ tutorname = "pocky sensei"
    $ mcname = renpy.input("What is your name?").strip()
    play sound advance
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

    voice "ss01.wav"
    ss "[mcname], you have been failing at Japanese, this can't go on."

    voice "ss02.wav"
    ss "I can't teach you well enough so I have found you a tutor."
 
    show ss at offscreenright 
    with ease
    with Pause(1.0) 

    show ss at offscreenright
    show tu happy at offscreenleft
    with None
    
    show ss at midright
    show tu happy at midleft
    with ease

    ss "[mcname], this is [tutorname]."

    voice "tu01.wav"
    tu "Nice to meet you [mcname]. Let's begin your training."

    show ss at offscreenright
    show tu happy at center
    with ease
    
    hide ss

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
            voice "tu02.wav"
            tu "no"


    scene bg classroom 2
    with fade
    with Pause(0.25)

    show tu happy at center
    with dissolve

    voice "tu05.wav"
    tu "Let’s start with some vocabulary!"

    menu test_1_question_1:
        tu "What verb would best complete this sentence?　すしを"
        "ねます":
            mc "ねます"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the correct answer was 食べます"
        "つくります":
            mc "つくります"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the correct answer was 食べます"
        "食べます（たべます）":
            mc "食べます"
            voice "tu03.wav"
            tu "Yes! That's correct, good job!"
            $ thistestrightanswers += 1
        "飲みます（のみます）":
            mc "飲みます"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the correct answer was 食べます"
        
    menu test_1_question_2:
        tu "Which hiragana matches the kanji：「新しい」　くるまですれ。"
        "あたらしい":
            mc "あたらしい"
            voice "tu03.wav"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "あだらしい":
            mc "あだらしい"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was あたらしい"
        "あらたしい":
            mc "あらたしい" 
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was あたらしい"
        "あらだしい":
            mc "あらだしい" 
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was あたらしい"

    menu test_1_question_3:
        tu "What is the reading of this kanji in the sentence: あしたは「雨」ですか。"
        "ゆき":
            mc "ゆき"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was あめ"
        "はれ":
            mc "はれ"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was あめ"
        "くもり":
            mc "くもり"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was あめ"
        "あめ":
            mc "あめ"
            voice "tu03.wav"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1

    menu test_1_question_4:
        tu "Which kanji represents the hiragana：「そと」で　まちましょう。"
        "外":
            mc "外"
            voice "tu03.wav"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "言":
            mc "言"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was 外"
        "中":
            mc "中"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was 外"
        "頃":
            mc "頃"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was 外"
    
    menu test_1_question_5:
        tu "Which hiragana matches the kanji：しゃしんは　はこ　の「中」に　あります。"
        "そば":
            mc "そば"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was なか"
        "そと":
            mc "そと"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was なか"
        "なか":
            mc "なか"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "よこ":
            mc "よこ"
            tu "Sorry that’s wrong, the right answer was なか"

    voice "tu06.wav"
    tu "You are doing a great job."

    menu test_1_question_6:
        tu "Figure out the correct sentence ending：しつもんが"
        "あります。":
            mc "あります。"
            voice "tu03.wav"
            tu "Perfect! Keep it up!"
            $ thistestrightanswers += 1
        "います。":
            mc "います。"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was あります。"

    voice "tu07.wav"
    tu "Almost there! Three questions left after you finish this one."

    menu test_1_question_7:
        tu "Figure out which hiragana best suits the sentence：ここは　（＿＿＿＿）です。　べんきょできません。"
        "くらい":
            mc "くらい"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was うるさい"
        "さむい":
            mc "さむい"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was うるさい"
        "うるさい":
            mc "うるさい"
            voice "tu03.wav"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "あぶない":
            mc "あぶない"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was うるさい"

    menu test_1_question_8:
        tu "Which particle should fill in the blank? これ「＿＿」えんぴつです。"
        "に":
            mc "に"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was は"
        "を":
            mc "を"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was は"
        "は":
            mc "は"
            voice "tu03.wav"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "や":
            mc "や"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was は"

    menu test_1_question_9:
        tu "Figure out which hiragana best suits the sentence：あそこで　タクシーに「＿＿＿＿＿」。"
        "のりました":
            mc "のりました"
            voice "tu03.wav"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "あがりました":
            mc "あがりました"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was のりました"
        "つきました":
            mc "つきました"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was のりました"
        "はいりました":
            mc "はいりました"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was のりました"

    menu test_1_question_10:
        tu "Which particle should fill in the blank? 弟　（おとうと）は　へや　「＿」そうじを　しました。"
        "が":
            mc "が"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was に"
        "を":
            mc "を"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was に"
        "に":
            mc "に"
            voice "tu03.wav"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "の":
            mc "の"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was に"

    $ totalrightanswers += thistestrightanswers

    if thistestrightanswers >= 7:
        voice "tu08.wav"
        tu "Good job! It seems like you've learned a lot." 
        voice "tu09.wav"
        tu "I'll see you tomorrow!"
    else:
        voice "tu10.wav"
        tu "You failed..."
        voice "tu11.wav"
        tu "Unfortunately the session is over so you'll have to try again tomorrow."

    scene bg bedroom e evening
    "I enjoyed that, let's see if I can improve some more..."

    scene bg bedroom e night
    with fade
    "Wow, I spent so much time studying, I guess I should go to sleep."

    scene bg bedroom e morning
    with fade
    "That was some nice sleep. I'll do well at school today."

    show black
    with fade
    with Pause(0.25)

    scene bg classroom 1
    with fade
    
    show ss

    voice "ss03.wav"
    ss "There will be a test tomorrow, so please be prepared."
    "This is my chance!"

    show black
    with fade
    with Pause(0.25)

    scene bg bedroom a
    with fade

    show tu happy
    mc "I have a test tomorrow"
    
    voice "tu12.wav"
    tu "Well, let's start then."

    $ thistestrightanswers = 0

    menu test_2_question_1:
        tu "Figure out which hiragana matches the kanji：この　いすは「小さい」です。"
        "ちいさい":
            mc "ちいさい"
            voice "tu03.wav"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "ちさい":
            mc "ちさい"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was ちいさい"
        "しいさい":
            mc "しいさい"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was ちいさい"
        "しさい":
            mc "しさい"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was ちいさい"
        
    menu test_2_question_2:
        tu "あしたは「火曜日」です。"
        "どようび":
            mc "どようび" 
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was かようび"
        "すいようび":
            mc "すいようび"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was かようび"
        "かようび":
            mc "かようび"
            voice "tu03.wav"
            tu "Yes! That's correct, good job!"
            $ thistestrightanswers += 1
        "にちようび":
            mc "にちようび"
            voice "tu04.wav"

    menu test_2_question_3:
        tu "せいとは「百人」です。"
        "ひゃくにん":
            mc "ひゃくにん"
            voice "tu03.wav"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "びゃくにん":
            mc "びゃくにん"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was ひゃくにん"
        "ひゃくじん":
            mc "ひゃくじん"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was ひゃくにん"
        "びゃくじん":
            mc "びゃくじん"
            voice "tu04.wav"
            tu "Sorry that’s wrong, the right answer was ひゃくにん"

    menu test_2_question_4:
        tu "Figure out which kanji represents the hiragana：「魚」が　たくさん　いますよ。"
        "ねこ":
            mc "ねこ"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was さかな。"
        "とり":
            mc "とり"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was さかな。"
        "いぬ":
            mc "いぬ"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was さかな。"
        "さかな":
            mc "さかな"
            voice "tu03.wav"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
    
    menu test_2_question_5:
        tu "Figure out which hiragana matches the kanji：たまごを「三つ」とって　ください。"
        "いつつ":
            mc "いつつ"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was みっつ。"
        "みっつ":
            mc "みっつ"
            voice "tu03.wav"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "さんつ":
            mc "さんつ"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was みっつ。"
        "ごつ":
            mc "ごつ"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was みっつ。"

    menu test_2_question_6:
        tu "Now, pick the right katakana for the phrase：この「わいしゃつ」をください。"
        "ウイシャソ":
            mc "ウイシャソ"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was ワイシャツ。"
        "ウイシャツ":
            mc "ウイシャツ"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was ワイシャツ。"
        "ワイシャソ":
            mc "ワイシャソ"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was ワイシャツ。"
        "ワイシャツ":
            mc "ワイシャツ"
            voice "tu03.wav"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1

    voice "tu07.wav"
    tu "Almost there! Three questions left after you finish this one."

    menu test_2_question_7:
        tu "Pick the right kanji for the phrase：わたしのくには「かわ」がおおいです。"
        "花":
            mc "花" 
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was 川。"
        "山":
            mc "山"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was 川。"
        "川":
            mc "川"
            voice "tu03.wav"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "木":
            mc "木"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was 川。"

    menu test_2_question_8:
        tu "Which kanji is in the phrase? やんさんの「がっこう」はどこですか。"
        "宇校":
            mc "宇校"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was 学校。"
        "学校":
            mc "学校"
            voice "tu03.wav"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "宇枚":
            mc "宇枚"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was 学校。"
        "学枚":
            mc "学枚"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was 学校。"

    menu test_2_question_9:
        tu "Figure out which hiragana best suits the sentence：このざっしを「みて」ください。"
        "見て":
            mc "見て"
            voice "tu03.wav"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "買て":
            mc "買て"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was 見て。"
        "貝て":
            mc "貝て"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was 見て。"
        "目て":
            mc "目て"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was 見て。"

    menu test_2_question_10:
        tu "Which kanji goes with the phrase? このカメラは「たかい」ですね。"
        "高い":
            mc "高い"
            voice "tu03.wav"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "安い":
            mc "安い"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was 高い。"
        "古い":
            mc "古い"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was 高い。"
        "新い":
            mc "新い"
            voice "tu04.wav"
            tu "Sorry, that's wrong, the right answer was 高い。"

    if thistestrightanswers == 10:
        voice "tu13.wav"
        tu "You got all 10 questions right! You're a master!"
    elif thistestrightanswers >= 7:
        voice "tu14.wav"
        tu "You're doing great! Let's see how you do tomorrow."
    else:
        voice "tu15.wav"
        tu "You failed. I'm sorry, there's not much more I can do for you."
    
    scene bg bedroom e night
    with dissolve

    mc "I hope I'm ready for tomorrow."

    show black
    with dissolve
    with Pause(0.25)

    scene bg classroom 1
    with dissolve

    show ss
    with dissolve

    voice "ss04.wav"
    ss "Okay class! Put everything under your desk except for a pencil..."
    
    voice "ss05.wav"
    ss "And Start!"

    show ss at offscreenright
    with ease

    $ thistestrightanswers = 0

    menu test_3_question_1:
        "Pick the hiragana that goes with the phrase：ちかくに「山」があります。"
        "かわ":
            mc "かわ"  
        "やま":
            mc "やま"
            $ thistestrightanswers += 1
        "いけ":
            mc "いけ"
        "うみ":
            mc "うみ"
    
    menu test_3_question_2:
        "Pick the hiragana that goes with the phrase：このホテルは「多い」です。"
        "すくない":
            mc "すくない"
        "おおい":
            mc "おおい"
            $ thistestrightanswers += 1
        "せまい":
            mc "せまい"
        "ひろい":
            mc "ひろい"
    
    menu test_3_question_3:
        "Pick the hiragana that goes with the phrase：ともだちといっしょうに「学校」にいきます。"
        "がこう":
            mc "がこう"
        "がこお":
            mc "がこお"
        "がっこう":
            mc "がっこう"
            $ thistestrightanswers += 1
        "がっこお":
            mc "がっこお"
    
    menu test_3_question_4:
        "Pick the hiragana that matches the kanji：えんぴつが「六本」あります。"
        "ろくほん":
            mc "ろくほん"
        "ろくぽん":
            mc "ろくぽん"
        "ろっぼん":
            mc "ろっぼん"
        "ろっぽん":
            mc "ろっぽん"
    
    menu test_3_question_5:
        "Pick the hiragana that matches the kanji：この「新聞」はいくらですか。"
        "しんむん":
            mc "しんむん"
        "しんぶん":
            mc "しんぶん"
            $ thistestrightanswers += 1
        "しむん":
            mc "しむん"
        "しぶん":
            mc "しぶん"
    
    menu test_3_question_6:
        "Pick the hiragana that matches the kanji：このカメラは「安い」です。"
        "たかい":
            mc "たかい"
        "やすい":
            mc "やすい"
            $ thistestrightanswers += 1
        "おもい": 
            mc "おもい"
        "かるい":
            mc "かるい"

    menu test_3_question_7:
        "Pick the hiragana that matches the kanji：かさは「外」にあります。"
        "いえ":
            mc "いえ"
        "なか":
            mc "なか"
        "そと":
            mc "そと"
            $ thistestrightanswers += 1
        "にわ":
            mc "にわ"
     
    menu test_3_question_8:
        "Which hiragana matches the kanji：「新しい」　くるまですれ。"
        "あたらしい":
            mc "あたらしい"
            $ thistestrightanswers += 1
        "あだらしい":
            mc "あだらしい"
        "あらたしい":
            mc "あらたしい" 
        "あらだしい":
            mc "あらだしい" 

    menu test_3_question_9:
        "Which kanji represents the hiragana：「そと」で　まちましょう。"
        "外":
            mc "外"
            $ thistestrightanswers += 1
        "言":
            mc "言"
        "中":
            mc "中"
        "頃":
            mc "頃"

    menu test_3_question_10:
        "Figure out which hiragana best suits the sentence：ここは　（＿＿＿＿）です。　べんきょできません。"
        "くらい":
            mc "くらい"
        "さむい":
            mc "さむい"
        "うるさい":
            mc "うるさい"
            $ thistestrightanswers += 1
        "あぶない":
            mc "あぶない"

    menu test_3_question_11:
        "Which particle should fill in the blank? これ「＿＿」えんぴつです。"
        "に":
            mc "に"
        "を":
            mc "を"
        "は":
            mc "は"
            $ thistestrightanswers += 1
        "や":
            mc "や"

    menu test_3_question_12:
        "あしたは「火曜日」です。"
        "どようび":
            mc "どようび"
        "すいようび":
            mc "すいようび"
        "かようび":
            mc "かようび"
            $ thistestrightanswers += 1
        "にちようび":
            mc "にちようび"

    menu test_3_question_13:
        "What is the reading of this kanji in the sentence: あしたは「雨」ですか。"
        "ゆき":
            mc "ゆき"
        "はれ":
            mc "はれ"
        "くもり":
            mc "くもり"
        "あめ":
            mc "あめ"
            $ thistestrightanswers += 1

    menu test_3_question_14:
        "せいとは「百人」です。"
        "ひゃくにん":
            mc "ひゃくにん"
            $ thistestrightanswers += 1
        "びゃくにん":
            mc "びゃくにん"
        "ひゃくじん":
            mc "ひゃくじん"
        "びゃくじん":
            mc "びゃくじん"

    menu test_3_question_15:
        "Figure out the correct sentence ending：しつもんが"
        "あります。":
            mc "あります。"
            $ thistestrightanswers += 1
        "います。":
            mc "います。"

    menu test_3_question_16:
        "Pick the right kanji for the phrase：わたしのくには「かわ」がおおいです。"
        "花":
            mc "花"
        "山":
            mc "山"
        "川":
            mc "川"
            $ thistestrightanswers += 1
        "木":
            mc "木"

    menu test_3_question_17:
        "Figure out which hiragana best suits the sentence：あそこで　タクシーに「＿＿＿＿＿」。"
        "のりました":
            mc "のりました"
            $ thistestrightanswers += 1
        "あがりました":
            mc "あがりました"
        "つきました":
            mc "つきました"
        "はいりました":
            mc "はいりました"

    menu test_3_question_18:
        "Which particle should fill in the blank? 弟　（おとうと）は　へや　「＿」そうじを　しました。"
        "が":
            mc "が"
        "を":
            mc "を"
        "に":
            mc "に"
            $ thistestrightanswers += 1
        "の":
            mc "の"

    menu test_3_question_19:
        "What verb would best complete this sentence?　すしを"
        "ねます":
            mc "ねます"
        "つくります":
            mc "つくります"
        "食べます（たべます）":
            mc "食べます"
            $ thistestrightanswers += 1
        "飲みます（のみます）":
            mc "飲みます"

    menu test_3_question_20:
        "Figure out which hiragana matches the kanji：この　いすは「小さい」です。"
        "ちいさい":
            mc "ちいさい"
            $ thistestrightanswers += 1
        "ちさい":
            mc "ちさい"
        "しいさい":
            mc "しいさい"
        "しさい":
            mc "しさい"
        
    menu test_3_question_21:
        "Figure out which kanji represents the hiragana：「魚」が　たくさん　いますよ。"
        "ねこ":
            mc "ねこ"
        "とり":
            mc "とり"
        "いぬ":
            mc "いぬ"
        "さかな":
            mc "さかな"
            $ thistestrightanswers += 1
    
    menu test_3_question_22:
        "Figure out which hiragana matches the kanji：たまごを「三つ」とって　ください。"
        "いつつ":
            mc "いつつ"
        "みっつ":
            mc "みっつ"
            $ thistestrightanswers += 1
        "さんつ":
            mc "さんつ"
        "ごつ":
            mc "ごつ"

    menu test_3_question_23:
        "Which hiragana matches the kanji：しゃしんは　はこ　の「中」に　あります。"
        "そば":
            mc "そば"
        "そと":
            mc "そと"
        "なか":
            mc "なか"
            $ thistestrightanswers += 1
        "よこ":
            mc "よこ"

    menu test_3_question_24:
        "Figure out which hiragana best suits the sentence：このざっしを「みて」ください。"
        "見て":
            mc "見て"
            $ thistestrightanswers += 1
        "買て":
            mc "買て"
        "貝て":
            mc "貝て"
        "目て":
            mc "目て"

    menu test_3_question_25:
        "Which kanji goes with the phrase? このカメラは「たかい」ですね。"
        "高い":
            mc "高い"
            $ thistestrightanswers += 1
        "安い":
            mc "安い"
        "古い":
            mc "古い"
        "新い":
            mc "新い"

    menu test_3_question_26:
        "Now, pick the right katakana for the phrase：この「わいしゃつ」をください。"
        "ウイシャソ":
            mc "ウイシャソ"
        "ウイシャツ":
            mc "ウイシャツ"
        "ワイシャソ":
            mc "ワイシャソ"
        "ワイシャツ":
            mc "ワイシャツ"
            $ thistestrightanswers += 1

    menu test_3_question_27:
        "Which kanji is in the phrase? やんさんの「がっこう」はどこですか。"
        "宇校":
            mc "宇校"
        "学校":
            mc "学校"
            $ thistestrightanswers += 1
        "宇枚":
            mc "宇枚"
        "学枚":
            mc "学枚"

    if thistestrightanswers >= 23:
        jump good_end
    else:
        jump bad_end

    return

label good_end:
    show tu at offscreenleft
    with Pause(0.25)

    show ss at midright
    with ease

    voice "ss06.wav"
    ss "良くできました。 You got [thistestrightanswers]/27 correct!"

    show tu happy at midleft
    with ease

    voice "tu16.wav"
    tu "You've done great!"

    scene black
    with dissolve
    show text "{size=+30}Good End"
    with Pause(5)
    return

label bad_end:
    $ renpy.pause(0.25)

    scene black
    with dissolve
    show ss at center
    with ease
    
    voice "ss07.wav"
    ss "You are so bad at japanese"
    voice "ss08.wav"
    ss "It's time for you to die"

    $ main_playlist.append("kanashimi.mp3")
    play music "kanashimi.mp3"
    scene black
    with dissolve
    show text "{size=+30}Bad End"
    with Pause(5)
    scene black with dissolve
    with Pause(2)
    return