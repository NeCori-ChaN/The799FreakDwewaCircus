

#default Arlequimrota = 0
#default Pierrotrota = 0

define ca = Character("Carol", color="#90c2da", what_color="#90c2da")
define doc = Character(_("Doctor"), color="#e74c3c", what_color="#e74c3c")
define j = Character("Jester", color="#961ee6", what_color="#961ee6")
define v = Character(_("The Poison"), color="#b2ffd2", what_color="#b2ffd2")
define co = Character(_("Columbina"), color="#ffb2d2", what_color="#ffb2d2")
define d2 = Character(_("Unknown 2"))
define n = Character("Neko", color="#2f63f3", what_color="#2f63f3")

init python:
    nomes_com_cena_extra = ["columbina", "colombina"]


label sonho:
    stop music fadeout 0.5
    show screen site_oficial
    pause
    hide screen site_oficial
    
    play music "audio/musicas/sonho.mp3"  fadein 2.0 volume 0.5
    scene black
    $ player_pronouns = None
    $ persistent.p_sujeito = None
    $ persistent.p_objeto = None
    $ persistent.p_possessivo = None
    $ persistent.p_genero = None
    $ mc_nome = ""
    $ conversap = False
    $ envenenada = False
    $ bolo = False

    narrator "{color=#3325f7}Hello, dear visitor, good to see you again."
    narrator "{color=#3325f7}But you’re very far… come closer."

    narrator "{color=#3325f7}Now, what are your pronouns again?"
    show maodbil:
        xpos 1200
        ypos -300
    show maoebil:
        xpos -500
        ypos -300

    with dissolve
    show ela: 
        xalign 0.4
        yalign 0.6
    show ele:
        xalign 0.5
        yalign 0.6
    show elu:
        xalign 0.6
        yalign 0.6
    with dissolve

    if player_pronouns is None:
        call escolha_pronomes from _call_escolha_pronomes_1
    else:
        pass
    
    
    hide maodbil
    hide maoebil
    show maodbil at movimento_vindodir
    show maoebil at movimento_vindoesq
    pause 0.35
    play sound "audio/efeitos/pegar.mp3" volume 0.2
    if persistent.p_sujeito == "she":
        show ela:
            xalign 0.5
            yalign 0.6
        hide ele
        hide elu
        with dissolve
    elif persistent.p_sujeito == "he":
        hide ela
        hide elu
        with dissolve
    elif persistent.p_sujeito == "they":
        show elu:
            xalign 0.5
            yalign 0.6
        hide ela
        hide ele
        with dissolve

    show maodbil at movimento_voltandodir
    show maoebil at movimento_voltandoesq

    narrator "{color=#3325f7}And your name?"

label nomedenovo:
   
    call screen input_box

    if mc_nome == "":

        if persistent.p_genero == "feminino":
            $ persistent.mc_titulo = "mistress"
        elif persistent.p_genero == "masculino":
            $ persistent.mc_titulo = "master"
        else:
            $ persistent.mc_titulo = "sovereign"

        if persistent.mc_titulo == "mistress":
            $ mc_nome = _("Mestra")
        elif persistent.mc_titulo == "master":
            $ mc_nome = _("Mestre")
        else:
            $ mc_nome = _("Monarca")

    python:
        nome_check = mc_nome.lower()
        nome_invalido = False
        cena_extra = False

        if nome_check in nomes_especiais:
            frase = nomes_especiais[nome_check]
            char = personagens[nome_check]
            renpy.say(char, frase)

            
            if nome_check != "neko":
                nome_invalido = True

        if nome_check in nomes_com_cena_extra:
                    cena_extra = True
    if cena_extra:
        jump nome_columbinad2
    if nome_invalido:
        $ mc_nome = "" 
        jump nomedenovo

    narrator "{color=#3325f7}Of course it was, [mc_nome]. I thought you’d tell me a different one this time."
    hide elu
    hide ela
    hide ele
    with dissolve

    narrator "{color=#3325f7}Sure, so let’s recap a few things."
    narrator "{color=#3325f7}I remember, you helped Pierrot that day, but did you help with his injury at the café?"

    show balcao:
        alpha 0.05
    show idlesangue:
        alpha 0.05
        xalign 0.5
    with dissolve
    show pitutot:
        xalign 0.35
        yalign 0.6
    show pitutof:
        xalign 0.62
        yalign 0.6 
    with dissolve
    
    menu:
        "Yes":
            
            $ conversap = True
            show maodbil at movimento_vindodir2 zorder 10
            show maoebil at rejeitado_esquerda zorder 10
            play sound "audio/efeitos/pegar.mp3" volume 0.2
            pause 0.8
            hide pitutot 
            show pitutof at escolhido_tutorial

        "No":
            play sound "audio/efeitos/pegar.mp3" volume 0.2
            show maodbil at rejeitado_direita zorder 10
            show maoebil at movimento_vindoesq2 zorder 10
            pause 0.8
            hide pitutof
            show pitutot at escolhido_tutorial
    pause 1.0
    hide pitutof
    hide pitutot
    hide balcao
    hide idlesangue
    with slowdissolve

    narrator "{color=#3325f7}Good."

    show tendaverde:
        alpha 0.05
    show arlemaca:
        alpha 0.05
        zoom 2.5
        xalign 0.5
        yalign 0.1
    with dissolve

    narrator "{color=#3325f7}And in Harlequin’s tent, did you enjoy his company?"

    show arle:
        xalign 0.6
        yalign 0.6
    show arletutof:
        xalign 0.4
        yalign 0.6
    with dissolve
    menu:
        "Yes":
            show maodbil at rejeitado_direita zorder 10
            show maoebil at movimento_vindoesq2 zorder 10
            play sound "audio/efeitos/pegar.mp3" volume 0.2
            pause 0.8
            hide arle
            show arletutof at escolhido_tutorial
            narrator "{color=#3325f7}Really?{w=0.2} I didn’t see that coming,{w=0.2} maybe not even him."
        "No":
            show maodbil at movimento_vindodir2 zorder 10
            show maoebil at rejeitado_esquerda zorder 10
            play sound "audio/efeitos/pegar.mp3" volume 0.2
            pause 0.8
            hide arletutof
            show arle at escolhido_tutorial

            narrator "{color=#3325f7}It was expected."

    pause 0.3
    hide arle
    hide arletutof
    hide arlemaca
    hide tendaverde
    with dissolve
    narrator "{color=#3325f7}Did you eat anything from the circus that day?"

    show comida with dissolve:
        alpha 0.05
    menu:
        "Yeah, I ate":
            $ envenenada = True
            narrator "{color=#3325f7}Hahaha."
            hide comida with dissolve
            show maodbil at fimtutorial
            show maoebil at fimtutorial
            
            narrator "{color=#3325f7}Very well, good luck, dear guest."

            jump sequestro

        "No, I didn’t eat":
            hide comida with dissolve
            narrator "{color=#3325f7}Hmmm..."
            show circo:
                alpha 0.05
            show inclinado_e_corado:
                alpha 0.1
                xalign 0.5
            with dissolve

            narrator "{color=#3325f7}And about Pierrot, did you let him visit you the other day?"
            menu:
                "Yeah, I did":
                    hide circo
                    hide inclinado_e_corado
                    with dissolve

                    narrator "{color=#3325f7}How kind, so now..."
                    show maodbil at fimtutorial
                    show maoebil at fimtutorial
                    narrator "{color=#3325f7}It’s time to wake."
                    jump devolta_emcasa
                "Actually, no":
                    $ bolo = True
                    hide inclinado_e_corado
                    show pitenso:
                        alpha 0.1
                        xalign 0.5
                        yalign 0.5
                    show bolo at balanco_organico:
                        alpha 0.1
                        xalign 0.5
                        yalign 1.0
                    with dissolve
                    
                    narrator "{color=#3325f7}No?"
                    hide pitenso
                    hide bolo
                    hide circo
                    with dissolve

                    narrator "{color=#3325f7}Why not?{nw=0.2}"
                    pause 0.2
                    show maodbil at fimtutorial
                    show maoebil at fimtutorial
                    narrator "{color=#3325f7}I mean, your time is up, time to wake."
                    jump sequestro
                

label sequestro:
    stop music fadeout 2.0
    hide screen piscando
    hide screen abrir_olhos
    hide screen efeito_veneno with dissolve
    pause 1.0

    scene tendav at groggy_shake
    show piscar1

    pause 0.5

    show piscar
    pause 0.5

    mc "Ugh... my head... Where the hell am I?"

    if envenenada == True:
        scene black with slowdissolve
        show screen efeito_veneno
        show piscar
        pause 0.5

        show pegueivc at groggy_shake
        show piscar1 zorder 50
        

        p "{i}It feels so {b}unbelievably{/b} good to hold you like this."
        p "{sc=3}{color=#ffaf54}Finally mine."

        show screen piscando
        pause 0.2
        show screen desmaio
        pause 0.2
        hide screen desmaio 
        show pegueivcb at groggy_shake
        hide pegueivc
        hide piscar1
        hide screen piscando
        show piscar1
        pause 0.5

        
        p "{sc=1}{color=#ffaf54}{b}And to leave me here,{w=0.1} on the edge of losing control."
        p "{sc=2}{color=#ffaf54}{b}My hands ache to explore every inch of you."

        show screen piscando
        pause 0.2
        show screen desmaio
        pause 0.2
        hide pegueivcb
        hide screen desmaio
        show faminto at groggy_shake
        hide piscar1
        hide screen piscando
        show piscar1
        pause 0.5
        p "{sc=2}{color=#ffaf54}{b}Even though I’m completely obsessed with you right now."
        p "{b}...I want your eyes on mine."
    
    else:
        scene black with slowdissolve
        show screen efeito_veneno
        show piscar
        pause 0.5

        show pegueivcbad at groggy_shake
        show olhos_bad at groggy_shake
        show piscar1 zorder 50
        p "I almost... almost lost you [titulo_pierrot]."
        p "You just needed... to stop fighting me."

        show screen piscando
        pause 0.2
        show screen desmaio
        pause 0.2
        hide screen desmaio 
        hide olhos_bad
        show pegueivcbadb at groggy_shake
        show olhos_bad at groggy_shake:
            xpos 0.54  # 55% da tela na horizontal
            ypos 0.5
            anchor (0.5, 0.5)
        hide pegueivcbad
        hide piscar1
        hide screen piscando
        show piscar1
        p "I’ll take good care of you, I promise."
        p "{sc=1}{color=#ffaf54}Even if you try to run again..."

        show screen piscando
        pause 0.2
        show screen desmaio
        pause 0.2
        hide pegueivcbadb
        hide screen desmaio
        show faminto at groggy_shake
        hide piscar1
        hide screen piscando
        show piscar1
        pause 0.5
        p "{sc=1}{color=#ffaf54}My sweet angel..."
    
    play music "audio/musicas/sequestro.mp3" fadein 2.0 volume 0.3
    hide screen efeito_veneno
    scene black with dissolve
    pause 0.5
    scene tendav with dissolve
    mc "He... did this? This is really happening? I need to--"

    play sound "audio/efeitos/correntes2.mp3" 
    with hpunch
    pause 0.2

    narrator "You feel something wrapped around your ankle, it's chained to the bed."

    mc "No, no, no…"

    play sound "audio/efeitos/passos.mp3" volume 0.2

    mc "(I can't get it off!!)" with hpunch

    show tendavsomb with dissolve
    pause 0.5
    scene tendavzoom

    #stop music fadeout 2.0 #ligar isso junto com reprodução de nvageador
    
    show sombrap:
        xpos 1000
        yalign 0.5
    with dissolve
    pause 0.3
    hide sombrap
    show sombrap:
        xpos 500
        yalign 0.5
    with dissolve
    pause 0.3

    show sombrap:
        xalign 0.5
        yalign 0.5

    pause 0.5
    #show preto #precisa estar ativo junto com a reprodução do navegador
    play movie "images/olhe.webm"
    #$ renpy.movie_cutscene("images/olhe.webm") #navegador
    #play music "audio/musicas/sequestro.mp3" fadein 2.0 volume 0.3 #ligar junto com navegador

    scene black with dissolve

    narrator "Your voice fades when your eyes meet his."
    play sound "audio/efeitos/toque.mp3" volume 0.2
    narrator "He slowly sets a tray of food near the bed so slowly it feels like he’s afraid even the slightest movement might scare you more."

    scene tendab:
        zoom 1.2
        xalign  0.5
        yalign 0.5
    with dissolve
    show pierrotolhos:
        zoom 1.2
        xalign 0.5
        yalign 0.5
    with dissolve

    p "You’re finally awake, [titulo_pierrot]!"
    p "I’ve missed seeing the color of your eyes, and hearing your voice speaking to me."

    scene tendab
    show pcalma with dissolve
    
    narrator "Your body pulls back on instinct, and you press against the headboard. He raises his hands gently, trying to calm you."

    p "Ah, of course… you must be afraid right now..."
    p "It’s alright, [titulo_pierrot]. I won’t hurt you."

    mc "You… you drugged me!"

    p "[mc_nome]..."

    mc "And then you kidnapped me!!"
    play sound "audio/efeitos/guizo.mp3" volume 0.5
    show encaraclose2:
        zoom 1.5
        xalign 0.6
        yalign 0.3
    with hpunch 
    show olhosarregalados:
        zoom 1.5
        xalign 0.6
        yalign 0.3
    show olhosvidrados at tilt_olhos:
        zoom 1.5
        xalign 0.479
        yalign 0.32
    hide pcalma
        
    pause 0.2
    
    p "I!... I..."

    hide olhosvidrados
    show olhosvidrados at tilt_olhos:
        zoom 1.5
        xalign 0.5
        yalign 0.32

    p "No..."

    if envenenada == True:
        p "I didn’t know there would be something in the food that day..."

    else:
        p "I had no choice... you were going to leave me. I needed to calm you down, so we could talk."
    
    p "Please, [titulo_pierrot], don’t scream, alright?"

    hide olhosvidrados
    show olhosvidrados at tilt_olhos:
        zoom 1.5
        xalign 0.479
        yalign 0.32
    p "{cps=20}The others… {w=0.2}{/cps}they’re nearby. Just… listen to me."
    p "I saw you vulnerable, [titulo_pierrot], and it made..."

    hide olhosarregalados
    hide olhosvidrados
    show encaraclose2:
        zoom 1.5
        xalign 0.6
        yalign 0.2
    show sorrisoencara2:
        zoom 1.5
        xalign 0.6
        yalign 0.2  
    with dissolve

    p "... {cps=12}My body tremble in {bt=1}{color=#ffaf54}so many ways-{nw=1}"

    hide sorrisoencara2
    hide encaraclose2
    play sound "audio/efeitos/guizo.mp3" volume 0.5
    show encaraclose2 at pulinho:
        zoom 1.5
        xalign 0.6
        yalign 0.3
    show olhosarregalados at pulinho:
        zoom 1.5
        xalign 0.6
        yalign 0.3
    p "I-I mean..."
    hide encaraclose2
    hide olhosvidrados
    hide olhosarregalados
    show pdelu with dissolve
    p "You felt it too, didn’t you? After you ate, your body became…"
    p "{cps=20}Receptive,{w=0.2} light and yielding."

    show pdelu2 with dissolve
    hide pdelu

    p "But then I saw how the world looked at you in that moment."
    p "Like prey. I saw those hungry eyes trying to devour you, yearning to touch you."
    show pdelu3 with dissolve
    hide pdelu2
    p "{cps=10}It drove me mad."
    p "{b}I had to bring you somewhere safe, somewhere under my watch."

    narrator "He reaches out to touch you."

    menu:
        "Step back":
            play sound "audio/efeitos/guizo.mp3" volume 0.5
            hide pdelu3
            show pcalma with dissolve
        "Allow him":
            play sound "audio/efeitos/guizo.mp3" volume 0.5
            hide pdelu3
            show encaraclose2
            show sorrisoencara2
            with dissolve
           
    p "I had to hide you, before anyone tried to lay a hand on [titulo_pierrot]." 
    p "Because if someone dared touch you, someone other than me…"
    play sound "audio/efeitos/guizo.mp3" volume 0.5

    hide sorrisoencara2
    show encaraclose2 with dissolve:
        xalign 0.5
        yalign 0.5
        zoom 1.1
    show olhosarregalados:
        xalign 0.5
        yalign 0.5
        zoom 1.1
    show olhosvidrados at tilt_olhos:
        xalign 0.53
        yalign 0.32
    hide pcalma
    p "I don’t know what I might’ve done."

    mc "{color=#a0b0c0}(He’s terrifying. He says such sweet things, with this dark... hungry tone?)"

    hide olhosvidrados
    hide olhosarregalados
    show sorrisoencara2:
        zoom 1.1
        xalign 0.5
        yalign 0.5

    p "I’m so glad you woke up, [mc_nome]! I was starting to get worried."
    mc "Worried? But I’m the one who…"
    p "You were breathing so slowly, so still… it was like…"

    hide sorrisoencara2
    show olhosarregalados:
        xalign 0.5
        yalign 0.5
        zoom 1.1
    show olhosvidrados:
        xalign 0.53
        yalign 0.32
   
    p "…like you were going to disappear forever, like..." #she did…
    p "{sc=1}{color=#ffaf54}N-no, I’d never hurt you like that! Believe me, back then I- {nw=3}"
    hide olhosvidrados
    hide encaraclose2
    hide olhosarregalados
    show encaraclose2 at pulinho
    show olhosarregalados at pulinho
    show olhosvidrados2 at pulinho:
        xalign 0.53
        yalign 0.32

    play sound "audio/efeitos/guizo.mp3" volume 0.5
    des "{color=#961ee6}Where’s Pierrot??"

    hide olhosvidrados2
    show olhosvidrados2 with dissolve:
        xalign 0.553
        yalign 0.328
    
    p "Please, [titulo_pierrot] listen to me. Place your trust in me."

    scene black  with dissolve
    play sound "audio/efeitos/pegar.mp3"
    narrator "He places a mask gently over your face and leans in, resting his forehead against it."
    
    scene ptes with dissolve
    p "I give you my word I shall return. If you wish for me to let go, I shall."
    p "But please, wait just a moment. And should anyone enter, say nothing."
    p "Do not breathe too heavily. Pretend you are merely a doll. You will be safe, yes?"
    p "{cps=15}{b}Do not move."
    
    narrator "He binds your hands with a rope, but it’s far too loose."

    scene tendab with dissolve

    mc "{color=#a0b0c0}(He faked tying me up? What was that all about? Maybe I should-)"

    play sound "audio/efeitos/correntes2.mp3" 
    with hpunch

    narrator "As you try to move your leg, the weight of the chain pulls back."

    mcp "(Oh, right. I can’t get out of bed. I just have to…{w=0.3} wait.)"

    play sound "audio/efeitos/passos.mp3"
    narrator "You hear footsteps coming closer."

    mcp "(Is he back already? Should I stay quiet like he asked?)"

    stop music fadeout 2.0
    
    show arles1 with dissolve

    pause 0.5
    a "Hmm?"
    play music "audio/musicas/sequestro2.mp3" fadein 1.0 volume 0.3

    a "Well, well… what do we have here?"

    mcp "(That’s not him…)"

    a "I knew he was hiding something… but this is way more fun than I thought!"

    hide arles1
    show arles2 with dissolve

    a "I must be really lucky today!"
    a "{cps=15}Tied up to a bed, in a place you were {b}never{/b} supposed to be ♪"

    play sound "audio/efeitos/lencois.mp3" volume 0.2

    narrator "He climbs onto the bed and slowly makes his way toward you."

    a "He warned you, didn’t he?"

    play sound "audio/efeitos/facapeq.mp3"
    pause 0.3
    play sound "audio/efeitos/mascara.mp3"
    show arlefaca with dissolve
    hide arles2

    a "Here,{w=0.3} if you scream, things will get {b}really{/b} bad for you."

    mcp "(His mask... it just opened?? And his tongue... {cps=10}it's green?)"

    a "Guess it still tastes sweet ♪"

    hide arlefaca
    show arlep with dissolve
    a "Hm? You're already shaking?"
    hide arlep
    play sound "audio/efeitos/mascara.mp3"
    show arleling with dissolve
   
    a "Oh,{w=0.3} you hadn’t seen that yet, huh?"
    a "Wanna see more? {i}I could show you later."
    a "Now the real question is…"

    hide arleling
    show arlep with dissolve
    a "{b}What should I do with you?"
    a "Ugh, it’s so hard to choose."

    menu:
        "Scream":
            stop music
            play sound "audio/efeitos/pegar.mp3"
            show arlep2:
                zoom 1.1
                xalign 0.5

            show maoarle
            hide arlep
            with hpunch

            a "You really are stubborn, aren’t you?"
            a "If anyone’s going to break you, [titulo_arlequim], it better be {b}me{/b} and not them."
            a "So you’d better not scream, got it?"
            play music "audio/musicas/sequestro2.mp3" fadein 1.0 volume 0.3
            a "I wouldn’t mind hearing it, but I don’t like sharing."

        "Keep quiet":
            $ renpy.music.set_volume(0.15, delay=2.0, channel="music")
            show arlep3 with dissolve:
                zoom 1.1
                xalign 0.5
            hide arlep
            a "Oh? Are you pretending to be a doll?"
            a "How much did he tell you? Now I’m curious."

            show arlep with dissolve:
                zoom 1.1
                xalign 0.5
            hide arlep3
            $ renpy.music.set_volume(0.3, delay=2.0, channel="music")
            a "But you’re not fooling me, your body’s way too tense, your arms are trembling."

            show arlep at zoomrapido2
            pause 0.3
            show black with dissolve

            play sound "audio/efeitos/pegar.mp3"
            narrator "He pushes your body down against the mattress."

            show mordida with dissolve
            narrator "And sinks his teeth into your neck. You tense up, but stay silent."
            $ marca_arlequim = True

            a "{i}I know you’re in there ♪"

            narrator "You feel something warm and wet glide over the spot where he bit you."

            a "Well, well, such resistance."
            a "I’m impressed."

    scene tendab with dissolve
    show arlep with dissolve:
        zoom 2.0
        xalign 0.5
        yalign 0.5
    play sound "audio/efeitos/facapeq.mp3"
    narrator "He slides the knife along your skin, you feel the cold blade touch your neck and trail down your chest, but he doesn’t cut you."

    show arlep2 with dissolve:
        zoom 2.0
        xalign 0.5
        yalign 0.5
    hide arlep
    a "You’re doing so well, didn’t even flinch."
    a "But your skin tells on you, all those little goosebumps. Was it the blade’s cold kiss?"
    a "Or was it knowing you’re completely at my mercy?"

    show arlep3o:
        zoom 2.0
        xalign 0.5
        yalign 0.5

    show olhoa at tilt_olhosv:
        zoom 2.0
        xalign 0.5
        yalign 0.13
    with dissolve
    hide arlep2
    a "No escape...{w=0.3} {cps=15}{i}and no eyes of your loyal guard dog watching over you."
    a "Still quiet? Oh, this game is really turning me on..."

    narrator "You're still trying to process what just happened, your body trembling with hesitation."

    menu:
        "Please go away":
            hide arlep3o
            show arlep with dissolve
            hide olhoa
            
            mc "{sc=1}Please... go away Harlequin."
            narrator "You whisper so softly that the mask nearly muffles your voice entirely."

            show arlep2 with dissolve
            
            a "{cps=10}\"Please\"?"
            a "You sound so sweet when you beg like that."

            show arlesu with dissolve
            hide arlep
            hide arlep2

            play sound "audio/efeitos/pegar.mp3"
            narrator "He leans in and whispers."

            a "But let me remind you. {cps=15}{b}I wasn’t the one who tied you up."
            a "{cps=30}I’m just here because {b}someone else{/b} left you all alone… with the {i}wrong predator."

        "Hold his hand":
            $ renpy.music.set_volume(0.15, delay=2.0, channel="music")
            $ toquegentil = True
            play sound "audio/efeitos/pegar.mp3"
            hide arlep3o
            hide olhoa
            show arle_surpreso with dissolve
            narrator "You reach for his hand, trembling, a quiet plea for him to stop."

            a "{cps=10}{size=50}..."

            show arledes:
                zoom 1.1
                xalign 0.5
                yalign 0.5
            show olhoa at tilt_olhos:
                xalign 0.5
                yalign 0.3
            with hpunch
            hide arle_surpreso

            $ renpy.music.set_volume(0.3, delay=2.0, channel="music")

            a "Oh?{w=0.2} You're trembling so much this time, my dear."
            
            show arlep 
            hide arledes
            with dissolve
            hide olhoa
            a "Are you asking me to stop, or just to {i}slow down?"

            narrator "You lower your head, and notice{cps=15} he's holding back a laugh."

            show arledes
            hide arlep
            show olhoa at tilt_olhos:
                xalign 0.5
                yalign 0.3
            with hpunch
    
            a "Alright, I’ll let you catch your breath, {b}just this once."
            a "I know when your eyes are begging for me."

            hide asur2
            hide olhoa
            hide arledes with dissolve
            

            a "But next time, you won’t get a break."
            
            hide arlep
            show arlesu with dissolve
            hide arledes
            hide arlep2
            
            play sound "audio/efeitos/pegar2.mp3"
            narrator "He comes closer, and you hold onto his hand hesitantly."
            show arlesu2 with dissolve
            hide arlesu
            narrator "His poisonous stare burns into you, while his smile grows with twisted delight."

            a "Shhh."
            a "Don’t move."

            play sound "audio/efeitos/pegar.mp3"
            narrator "He gently places his hand over yours."

            mcp "(Is he… trying to comfort me?)"

            a "I have to admit. I’m really starting to like the way you look at me."

            mcp "(Maybe not...)"

    
    play sound "audio/efeitos/facapeq.mp3"
    scene tendab with dissolve
    pause 0.5
    play sound "audio/efeitos/correntes2.mp3"
    show arlep
    mcp "(He... let me go? Why?)"

    a "Why? Is that what you’re thinking? Because this way’s more fun."
    a "I don’t like prey all tied up. I like the hunt. And the best part-"
    show arlep3
    hide arlep
    a "Is gonna be the look on his face when he finds out."

    show arlep2:
        zoom 1.2
        xalign 0.5
        yalign 0.5
    hide arlep3
    stop music
    a "Run kitten." with hpunch

    scene tendab at zoomrapido3
    pause 0.4

label fuga:
    play sound "audio/musicas/drama.mp3" volume 0.1
    scene black
    pause 0.3
    scene entretendas at correndo(0.15)
    mcp "(This isn’t just an act, something’s seriously wrong with those two!)"

    show carol0 at zoomrapido4:
        xalign 0.5
        yalign 0.5
    with dissolve

    pause 0.2

    scene entretendas:
        zoom 1.5
        xalign 0.5
        yalign 0.5

    play sound "audio/efeitos/cair.mp3"
    show carol0 with vpunch:
        zoom 1.8
        xalign 0.5
        yalign 0.5


    show black with fade

    mc "Ouch!"
    
    hide black with dissolve

    pause 0.5

label carol:
    show entretendas with dissolve
    mc "Sorry, I... I don’t..."

    show carol0 with dissolve:
        zoom 1.8
        xalign 0.5
        yalign 0.5
    play sound "audio/efeitos/efeitosus.mp3" volume 0.3
    show carol1 with dissolve:
        zoom 1.8
        xalign 0.5
        yalign 0.5
    hide carol0
    pause 0.2

    show carol2 with dissolve:
        zoom 1.8
        xalign 0.5
        yalign 0.5
    hide carol1
    
    pause 0.1

    show carol with dissolve:
        zoom 1.8
        xalign 0.5
        yalign 0.5
    hide carol2
    
    des "{color=#90c2da}Don’t miss the attractions, you’re gonna love it, visitor."
    show carololhos at deslizarsutil_dir2
    with dissolve
    hide carol
    mc "What...?"
    mc "C-Carol?"

    ca "Don’t miss the--{nw=0.5}"

    play sound "audio/efeitos/pegar.mp3"
    show bmask with dissolve
    hide carololhos
    b "Oh! How embarrassing, darling your mask just slipped off."
    
    scene entretendas with dissolve
    show carol0 with dissolve:
        xalign 0.2
        yalign 1.0
        zoom 0.95
    
    show bilheteiro at deslizar_bil
    with dissolve

    play music "audio/musicas/doll.mp3" fadein 3.0 volume 0.1

    b "Don't worry about her, visitor. She's just playing her part."
    b "Around here, no one ever breaks character. Not for anything."
    b "But, you look kinda shaken."
    b "Are you enjoying the promotional attractions? Or did something happen?"

    mc "I-I… I…"
    hide bilheteiro
    play sound "audio/efeitos/pegar.mp3" volume 0.5
    show b 2 with dissolve:
        zoom 1.2
        xalign 0.5
        yalign 0.5
  
    narrator "He shifts his posture after locking eyes with you for a moment."

    b "Are you lost, visitor? This area’s really close to the restricted zone."
    b "Which way did you come from?"

    menu:
        "{sc=1.5}I think I got lost":
            hide b 2
            show bil 2 with dissolve:
                zoom 1.5
                xalign 0.5
                yalign 0.4
            hide b 2
            
        "{sc=1.5}I was just passing by":
            hide b 2
            show bil 2 with dissolve:
                zoom 1.5
                xalign 0.5
                yalign 0.4
            hide b 2
    play sound "audio/efeitos/pegar.mp3" volume 0.5
    narrator "Your voice falters, and he doesn't buy it."

    b "That's...{w=0.5}{cps=15} alright, visitor. These things happen."
    hide bil 2
    show b 3 at deslizar_bil
    with dissolve

    b "Please, come with me let me guide you to the exit."

    mcp "(I'm pretty sure the exit isn’t that way...)"

    mc "N-no, it’s okay! The exit’s this way, right? I can go on my own."
    hide b 3
    show bilmao
    show olhobil at fade_in_olho

    play sound "audio/efeitos/pegar.mp3"
    narrator "He grabs your wrist firmly." with hpunch
    
    b "{b}I insist."

    pause 0.5
    hide olhobil
    show pbil with hpunch
    play sound "audio/efeitos/guizo.mp3" volume 0.5
    mcp "(Pierrot??)"

    b "Pierrot? What are you..."
    play sound "audio/efeitos/guizo.mp3" volume 0.5
    if envenenada == True:
        show sanguesim zorder 10
    if convite_aceito == True:
        show sanguesim zorder 10

    show psim
    hide sangueluva
    hide pbil 
    
    
    if player_pronouns == "they":
        b "Are [persistent.p_sujeito] with you?"
    else:
        b "Is [persistent.p_sujeito] with you?"
    
    play sound "audio/efeitos/guizo.mp3" volume 0.5
    show psim2
    hide psim
    
    pause 0.3
    show psim #with dissolve
    hide psim2 #with dissolve

    if envenenada == True:
        mcp "(I-Is that… blood?)"
        
    elif convite_aceito == True:
        mcp "(I-Is that… blood?)"
    
    if player_pronouns == "they":
        b "That look, Pierrot… they're scared."
    else:
        b "That look, Pierrot… [persistent.p_sujeito]'s scared."

    b "It's like [persistent.p_sujeito] saw the part of the circus {b}we don’t show."

    show treta 0 with dissolve
    hide sanguesim
    hide psim
    hide bilmao

    if player_pronouns == "they":

        p "{sc=1}{color=#ffaf54}{size=20}Circus of horrors. Of course they're scared."
    else:
        p "{sc=1}{color=#ffaf54}{size=20}Circus of horrors. Of course [persistent.p_sujeito]’s scared."

    show treta 1 with dissolve
    
    stop music
    voice "audio/dublagem/bilheteiro.mp3"
    b "{b}Do not speak."

    b "In that case..."
    hide treta
    if envenenada == True:
        show b 2 with dissolve:
            xalign 0.8
        show plados with dissolve:
            zoom 1.2
            xpos -200
            yalign 0.8
    elif convite_aceito == True:
        show b 2 with dissolve:
            xalign 0.8
        show plados with dissolve:
            zoom 1.2
            xpos -200
            yalign 0.8
        
    else:
        show b 2 with dissolve:
            xalign 0.8
        show plado2 with dissolve:
            zoom 1.2
            xpos -200
            yalign 0.8

    b "I'm certain our guest will be thrilled to return for the nightly attractions, won’t [persistent.p_sujeito]?"
    b "Give [persistent.p_objeto] your ticket, Pierrot. Or I’ll have to offer mine."
    b "If everything’s fine, [persistent.p_sujeito]’ll be delighted to join us again, right, guest?"

    narrator "Pierrot stares at you and subtly nods."

    mcp "(Maybe… it’s better to play along. I don’t know what’s going on here, but if I leave, I won’t have to come back.)"

    mc "Sure! I’d... love to."
    hide b 2
    show bilheteiro with dissolve:
        xalign 0.8

    b "Perfect. We look forward to your return, guest."

    hide bilheteiro with dissolve
    hide carol0 with dissolve
    hide plado 
    hide plados 
    hide plado2

    play sound "audio/efeitos/guizo.mp3" volume 0.5
    show psad with dissolve:
        zoom 1.5
        xalign 0.5
        yalign 0.5

    mc "..."

    if convite_aceito == True:
        
        show psad2 with dissolve:
            zoom 1.5
            xalign 0.5
            yalign 0.5
        hide psad 
        
        narrator "He tries to touch your shoulder but holds back, afraid you’ll run."
        mcp "(I don’t know what happened back there, but he seems okay)"
        mc "Harlequin is… {nw=0.5}"
        p "{size=20}Breathing."

        mc "I… just need to go home for a bit, okay?"
        show psad with dissolve:
            zoom 1.3
            xalign 0.5
            yalign 0.5
        hide psad2
        p "You’re scared..."
        p "{cps=5}..."
        p "S-Sure."
        show psad2 with dissolve:
            zoom 1.3
            xalign 0.5
            yalign 0.5
        show psadolhos at olhospulse:
            zoom 1.3
            #xalign 0.5
            yalign 0.5
        
    else:
        mc "Please, don’t… just let me go home. I think that was too much for my head."
        hide psad
        show psad2 with dissolve:
            zoom 1.3
            xalign 0.5
            yalign 0.5
        show psad with dissolve:
            zoom 1.3
            xalign 0.5
            yalign 0.5
        
        show psadolhos at olhospulse:
            zoom 1.3
            #xalign 0.5
            yalign 0.5
    play sound "audio/efeitos/guizo.mp3" volume 0.5
    narrator "He nods, and you step away."

    hide psad with dissolve
    p "{size=20}I’ll wait for you there."

    jump casa_pos_eventos
    

label devolta_emcasa:
    stop music
    scene black

    scene quartodia
    show abrir_olhos
    with dissolve

    hide abrir_olhos
    with dissolve

    mcp "(Ugh, what a weird feeling… I felt like I was being watched last night.)"

    mcp "(I guess Pierrot and Harlequin’s performances really got into my head.)"
    mcp "(I’ve got the day off today. I was thinking of watching something, but...)"
    mcp "(I kinda want to see Pierrot. Maybe I’ll stop by the circus and watch him work.)"

    play sound "audio/efeitos/pegar.mp3"

    narrator "You change into a comfy shirt and notice the pins on the collar."

    show expression Solid("#000000C0") as escurecer with dissolve
    show pins with dissolve:
        xalign 0.5
        yalign 0.0

    mcp "(Pierrot and Harlequin’s pins! They seemed to care a lot about these yesterday.)"
    mcp "(I think I’ll… put them away for now. Feels like if I wear one, I’ll definitely catch their attention.)"

    hide escurecer
    hide pins with dissolve
    play sound "audio/efeitos/pegar.mp3" volume 0.5
    narrator "You check your pockets and find something."
    mcp "(Pierrot’s ticket!)"

    show expression Solid("#000000C0") as escurecer with dissolve
    show screen ingresso_vermelhofurado with dissolve
    mcp "(I really like his photo on the back of the ticket. It’s kinda dark… but I like that.)"
    mcp "(I’ll keep this too. It’s already punched, so I can’t use it again.)"
    mcp "(But it might be nice to save it since it seems kind of \"special.\")"

    hide escurecer
    hide screen ingresso_vermelhofurado with dissolve
    if curativo == True:
        mcp "(The flower Pierrot gave me!)"

        play sound "audio/efeitos/panfleto.mp3" volume 0.3
        show expression Solid("#000000C0") as escurecer with dissolve
        show florpapel with dissolve:
            xalign 0.5
            yalign 0.5

        mcp "(It’s dark now, and it smells like...{w=0.3}{cps=12} iron, I guess.)"
        mc "{size=45}{cps=10}..."
        mcp "(Well, I won’t think too much about it for now, maybe it’s just in my head.)"
        mc "{cps=12}Hahah..."
        mcp "{cps=20}(Maybe not…)"

        play sound "audio/efeitos/panfleto.mp3" volume 0.3

        hide escurecer
        hide florpapel with dissolve

        mcp "(Still... I’ll keep it.)"
        
        play sound "audio/efeitos/pegar.mp3" volume 0.3
        show florpapelp with dissolve
        $ floremcasa = True
    mc "Let’s see how he’s doing!"

label circorua:
    play music "audio/musicas/circorua.mp3" fadein 2.0 volume 0.1
    scene rua with dissolve
    show bil with dissolve
    mcp "(During the day they do street acts to promote the circus, from what I’ve noticed.)"
    mcp "(And at night, they have the real performances and all that. It’s funny how the whole vibe of this place changes during the day.)"

    narrator "You walk closer to the entrance of the circus and spot performers trying to grab people’s attention as they tell spooky stories."
    narrator "Alongside them, masked clowns in bright pink costumes hand out flyers."

    if conversap == True:
        mc "Harlequins and Jesters, huh? At least that’s what Pierrot said, though."
        mc "I don’t really see the difference."
        play sound "audio/efeitos/pegar.mp3" volume 0.3
        show screen oi_arlequim
        pause 0.2
        show aanima

        a "He said that? Oh my, he actually talked to you?"

        mc "Wha-?! Where did you come from??"
        mcp "(I didn’t even notice I said that out loud!)"
        hide aanima
        show frente2 with dissolve:
            zoom 1.1
            xalign 0.5
            yalign 0.5
       

        a "So, you heard his voice. Interesting ♪"

        mcp "(Ugh, I hope that doesn’t get Pierrot in trouble…)"
        
        show frente3 with dissolve:
            zoom 1.1
            xalign 0.5
            yalign 0.5
        hide frente2

        a "{i}Aww, look at that guilty little face! Don’t worry, [titulo_arlequim], maybe I’ll keep your secret."
        a "But no, those aren’t Harlequins. They’re {b}Fools."
        hide frente3
        show alado with dissolve:
            zoom 1.1
            xalign 0.5
            yalign 0.5
    
        a "Of course he would compare me to some street fool."

        menu:
            "Ask about the fools":
                mc "Fools?"
                hide alado with dissolve
                
                narrator "He smiles at your curiosity, stops behind you and leans in to whisper, guiding your gaze toward the fools."
                a "There’s only one Harlequin, one Pierrot, and one Jester in our circus."
                a "{bt=1}{color=#41d623}{i}Those little darlings in pink? Hah! They’re {color=#e61ee6}Fools{color=#41d623} ♪"
                mcp "(There’s something disturbingly sadistic in the way he explains it.)"
                a "{cps=20}Oh,{w=0.3} you’re not wearing my pin.{/cps} That really breaks my heart, you know?"
                play sound "audio/efeitos/pegar.mp3" volume 0.3
                narrator "His fingers brush the collar of your blouse."
            "Drop it":
                hide alado
                show frente with dissolve:
                    zoom 1.1
                    xalign 0.5
                    yalign 0.5
                a "So, what else did he tell you?"
                a "Have you seen what’s behind his mask?"

                mc "No. And don’t drag me into your fight I’m not trying to cause trouble for anyone."

                a "But you’re curious about them, aren’t you?"
                mc "..."

                show frente3 with dissolve:
                    zoom 1.1
                    xalign 0.5
                    yalign 0.5
                hide frente
                a "Hmm… {i}silence.{/i} Always the most honest reply."
                show atisti with dissolve:
                    zoom 1.1
                    xalign 0.5
                    yalign 0.5
                hide frente3
                a "{cps=20}Oh,{w=0.3} you’re not wearing my pin.{/cps} That really breaks my heart, you know?"

                hide atisti with dissolve
                narrator "He steps behind you, leaning in to whisper while keeping his gaze fixed on the performance."

    else:
        mc "The cast looks bigger."
        mc "There weren’t this many people handing out flyers at first."

        show screen oi_arlequim
        pause 0.2
        show aanima

        a "There really weren’t."

        mc "Wha-?! Where did you come from??"
        mcp "(I didn’t even notice I said that out loud!)"

        a "Forgive me, [titulo_arlequim]. You just looked so charming, all focused on the show. Having fun?"

        mc "I think so, things are really… Different at your circus."

        hide aanima
        show frente with dissolve:
            zoom 1.1
            xalign 0.5
            yalign 0.5

        a "How sweet when you say {i}“different,” what you really mean is..."

        show frente2 with dissolve:
            zoom 1.1
            xalign 0.5
            yalign 0.5
        hide frente

        a "{b}Freakish{/b}, isn’t it?"

        show atisti with dissolve:
            zoom 1.1
            xalign 0.5
            yalign 0.5
        hide frente2

        a "{cps=20}Oh,{w=0.3} you’re not wearing my pin.{/cps} That really breaks my heart, you know?"

        hide atisti with dissolve #aqui

        narrator "He stops behind you, leaning in to whisper while keeping his gaze fixed on the performance."

    a "No need to look at me. Watch the show like I’m not even here, dear."
    a "We attract less attention that way."

    mcp "(You’re a green dot in the middle of the street there’s no way to stand out more than this.)"

    show arle_atras with dissolve

    a "I love that curious look in your eyes, and I know...{w=0.3}{cps=15} you came here for Pierrot."
    a "You like the way we send shivers down your spine, don’t you?"

    play sound "audio/efeitos/pegar2.mp3" volume 0.5

    narrator "You feel his body press lightly against your back."

    mc "Maybe that’s because you guys get way too close, don’t you think?"

    hide arle_atras with dissolve 
    a "{cps=30}{i}Hmm… isn’t that the best part?"
    a "Maybe...{w=0.3}{cps=20} I was a little rude the last time we met. Don’t get me wrong."
    a "{cps=30}I think your eyes enchanted me, and I wanted to get so close that I crossed a line, didn’t I?"
    a "{cps=30}But tell me, did you think about me too? Or..."
    a "{cps=35}Am I the only {i}fool{/i} caught in your spell?"

    mcp "(His voice, sounds different...)"

    a "That’s just my nature, my dear. I like making your heart {b}race{/b}, stirring your reactions."
    a "But subtle? That’s not me, unlike a lovesick Pierrot."

    mcp "(His voice actually sounds, warmer? If I turn around now...)"
    mcp "(Will he be smiling that cynical smile?)"

    play sound "audio/efeitos/pegar.mp3"
    narrator "His face is too close, like he’s hearing you and wants to keep your cruel doubt alive."
    narrator "You can’t look at him and he doesn’t give you a chance to pull away."

    mcp "(If I turn, I’ll be way too close to him.)"

    narrator "You feel his hand hesitantly reach toward yours but it quickly pulls back."

    a "If I held your hand right now... would you pull away?"
    a "{cps=20}Or are you waiting for me to make the first move again?"

    narrator "He trails his claw along the collar of your blouse, right where the green heart pin used to be."
    hide bil with dissolve

    a "[mc_nome], do you want to feel my heart beating for you?"
    a "Want me to show you how I feel? Come with me..."
    a "I’ll make your heart beat in time with mine."
    a "{i}But maybe, you’ll lose your breath."

    show arletenda with dissolve

    narrator "He steps back, slipping between the circus tents, subtly looking at you, giving a silent invitation."

    mcp "(I get chills every time he comes close, every time he talks to me like that.)"

    mcp "(What does he really mean by it?)"

    menu:
        "Move away":
            $ naoseguir = True
            narrator "You see Harlequin’s mischievous smile from a distance, but you don’t follow him."
            mcp "(He really had a wicked grin.)"
            mcp "(Better go the other way, maybe I can still find Pierrot around here.)"
            play music "audio/musicas/doll.mp3" fadein 5.0 volume 0.1
            scene entretendas with dissolve

            mc "{size=40}{cps=10}..."
            mcp "(But, what was he actually trying to imply?)"
            stop music
            play sound "audio/efeitos/cair.mp3"
            scene black with hpunch
            mc "Ouch!"

            mcp "(I was so lost in my thoughts that I bumped into someone.)"

            jump carol

        "Follow him":
            $ convite_aceito = True
            narrator "His words echo in your mind, your skin tingles, and you can't hide your curiosity."
            mcp "(I want to see where this leads...)"

            play music "audio/musicas/sequestro.mp3" fadein 5.0 volume 0.1
            scene entretendas with dissolve:
                xzoom -1
            mcp "(I'm sure he was around here. How does he move without making a sound with those bells?)"

    scene vcveio
    show maoa
    with dissolve
    play sound "audio/efeitos/pegar2.mp3" volume 0.5
    narrator "You feel something brush against your back. He leans down, resting his face on your shoulder."
    a "So, you took my invite? Brave."
    a "Were you more curious about \"hearing my heart\" or \"losing your breath\"?"

    hide maoa with dissolve
    show vcveio2 with dissolve
    play sound "audio/efeitos/pegar.mp3"
    narrator "He grabs your waist, pulling you closer." with hpunch
    
    mc "Of course, you were mocking me…"

    a "Mocking? Huhum no, [mc_nome]."
    a "I haven’t lied to you. I’m always clear about what I want."

    narrator "You feel his claws dig into your waist a little harder."

    a "And you’ve already figured that out, haven’t you?"

    mc "I think it’s pretty easy to figure out what you want."

    a "Then how about we turn the lights off? I like it when you get lost."
    a "{i}{sc=1}{color=#41d623}When you can’t see where my fingers will end up."
    a "And since you came to me… {i}let’s play ♪"

label natenda:
    play sound "audio/efeitos/pegar2.mp3" volume 0.2
    stop music
    scene black with vpunch

    narrator "You’re pulled inside the tent."

    scene tendalust with dissolve
    show capa with dissolve

    a "Look at you..."
    play sound "audio/efeitos/puxarcorda.mp3" volume 0.2
    show arlecapat with dissolve
    play sound "audio/efeitos/pegar.mp3" volume 0.1
    hide capa
    
    pause 1.2
    a "Your heart’s already beating at the pace I like."

    scene tendalust2 with dissolve
    play music "audio/musicas/sequestro2.mp3" fadein 5.0 volume 0.1
    a "Too dark for your eyes, isn’t it? But the perfect grounds for me."

    mc "T-that’s not funny, Harlequin! It’s way too dark in here."

    show artenda with dissolve
    show olhoa at tilt_olhos:
        xalign 0.5
        yalign 0.32

    a "{i}I know{/i}, you can’t see me, but I see you."
    a "Every detail. And trust me, it’s better this way."

    show sus with dissolve
    hide artenda
    hide olhoa
    narrator "The cold mask brushes against your skin, and two hot trails run down the length of your neck."

    a "Ah… exactly how I imagined you’d taste. I could lose myself in this."

    mc "Did you just lick me??"

    a "That’s all you’re worried about? Mm…"
    a "{cps=15}You have no idea how much deeper this can go."

    show artenda #with dissolve
    hide sus
    show olhoa at fade_in_olho:
        xalign 0.5
        yalign 0.32

    play sound "audio/efeitos/mesa.mp3" volume 0.5
    narrator "You step back and bump into what feels like a table." with vpunch

    narrator "He grabs your wrist and tilts your chin up."

    play sound "audio/efeitos/pegar.mp3"
    show expression Solid("#000000C0") as escurecer zorder 10
    show maoarle with hpunch

    a "You’re not afraid of monsters in the dark, are you?"

    play sound "audio/efeitos/efeitosus.mp3" volume 0.2
    narrator "You feel something coil and slide around your ankles."

    mc "W-What the hell is that??"

    a "Shhh… I can almost hear your heart screaming ♪"

    play sound "audio/efeitos/friccaointensa.mp3" volume 0.05
    narrator "Something seizes your other wrist, your waist, your thighs like living ropes pulling you closer to him."

    hide maoarle with dissolve
    hide escurecer with dissolve
    

    mcp "(Something’s wrong, I can feel his hands gripping me, but what are these things touching me??)"

    mc "H-how are you doing this?"
    play sound "audio/efeitos/pegar2.mp3" volume 0.5
    show sus with dissolve
    hide artenda
    hide olhoa

    a "You know, he lies to you. Hides and whispers passion when you’re not listening."
    a "Me? I don’t need to lie, I can show you a little... more."
    a "Do you want to see… what we really are?"

    play sound "audio/efeitos/puxarcorda.mp3"
    narrator "The \"ropes\" tighten and wind around you harder."
    play sound "audio/efeitos/friccao.mp3"
    show artenda with dissolve:
        zoom 1.2
        xalign 0.5
        yalign 0.5
    hide sus with dissolve
    show olhoa at fade_in_olho:
        zoom 1.2
        xalign 0.5
        yalign 0.28
    
    a "Ah… your eyes right now..."
   
    show artenda with dissolve:
        zoom 1.4
        xalign 0.5
        yalign 0.5

    show olhoa:
        zoom 1.4
        xalign 0.5
        yalign 0.25
    a "Wide, desperate, clinging to every scrap of light, as if it could save you."
    a "{i}It’s almost adorable ♪"
    
    play sound "audio/efeitos/pegar.mp3"
    narrator "He calmly presses your body against the table."

    show artenda with dissolve:
        zoom 1.5
        xalign 0.5
        yalign 0.4

    show olhoa at tilt_olhos:
        zoom 1.5
        xalign 0.5
        yalign 0.28

    play sound "audio/efeitos/friccaointensa.mp3" volume 0.05
    narrator "The \"ropes\" slither like snakes, brushing against your skin."

    mcp "(What the hell are these things all over me??)"

    mc "Harlequin you’re freaking me out! what- {nw=1.0}"

    a "\"What’s{cps=12} touching me?\""
    a "Oh, darling trust me, it’s better if we stay in the dark."
    a "What you feel crawling over your body..."
    a "{b}It’s me."

    a "And I really want to feel your skin right now."

    play sound "audio/efeitos/efeitosus.mp3" volume 0.2
    show nmask with dissolve
    hide artenda
    hide olhoa

    menu:
        "Hit him":
            play sound "audio/efeitos/toque.mp3"
            hide nmask
            show nmask3 with hpunch
            
            a "{i}Wild ♪"
            play sound "audio/efeitos/pegar2.mp3"
            hide nmask3
            show nmask2 with dissolve:
                zoom 1.2
                xalign 0.5
                yalign 0.5

            narrator "He pins your wrists to the table."

            a "Ah... {cps=12}[mc_nome], [mc_nome]..."
            a "You knew exactly where this road would end, and still, you walked it."
            a "You followed me."
            a "Go ahead, pretend you didn’t want this."
            a "Pretend you didn’t ache for my hands to trap you like this."
            a "You want me to devour you, but you’re too afraid to admit it."
            a "That’s fine, I can read your hunger better than you can."

            play sound "audio/efeitos/friccaointensa.mp3" volume 0.05

            narrator "The \"ropes\" start to slide into your clothes."
            mc "H-Harlequin!!"

        "Allow":
            hide nmask
            show nmask2 with dissolve
            play sound "audio/efeitos/pegar.mp3"
            narrator "You clutch at the \"ropes\" winding over your body."
            mcp "(It’s warm… kind of soft, the tips are thin and move like they’re alive.)"
            mcp "(Just, what the hell am I holding? What is he doing to me?)"

            hide nmask2
            play sound "audio/efeitos/pegar2.mp3" volume 0.3
            show sus2 with dissolve
                
            a "Mmm… gripping me so tight, are you? I might think you’re enjoying this."

            play sound "audio/efeitos/friccaointensa.mp3" volume 0.05

            narrator "The \"ropes\" start to slide into your clothes."

            a "But don’t worry I’m not letting you go anyway."

            play sound "audio/efeitos/friccao.mp3" volume 0.2
            narrator "He brushes his lips against your skin."

            mcp "(It’s different from before, his lips are warm.)"

            a "I’m going to leave my mark ♪"
            a "So you remember exactly who made your body burn first."

            play sound "audio/efeitos/efeitosus.mp3" volume 0.2
            narrator "He bites down, sharp teeth sinking into your skin, and you have to choke down the sound in your throat." with vpunch
            $ marca_arlequim = True

    hide sus2
    show nmask2 with dissolve
    pause 0.2
    show achei with dissolve
    stop music fadeout 2.5
    mcp "(Pierrot?)"
    play sound "audio/efeitos/sacarfaca.mp3" volume 0.1
    show facs with dissolve

    pause 0.5

    show achei2 with dissolve
    hide achei
    hide facas

    pause 0.5

    show achei3 with dissolve
    show maop with dissolve
    pause 0.1
    play sound "audio/efeitos/golpecortante.mp3" volume 0.3
    show achei4
    show sanguinho with hpunch
    pause 0.5
    play sound "audio/efeitos/cair.mp3" volume 0.2
    scene tendalux2 with dissolve
    mcp "(I need to get out of here.)"

    scene tendalux2 at zoom_luzes
    pause 0.2

    jump fuga

label casa_pos_eventos:
    play music "audio/musicas/coracao.mp3" fadein 1.0 volume 0.3
    scene sala at tilt_glitch
    with dissolve

    mc "What was all that??"
    mc "I-I… I don’t even know where to start freaking out!" with hpunch

    scene sala

    if envenenada == True:
        mc "{sc=1}He kidnapped me!! And what if he did something to me?"
        mc "How did things escalate this much?"
        mc "C-Carol is there! What’s happening in that place??"
        mc "{sc=1}S-she looked.... looked..."
        mc "{cps=15}Like a doll...?"

    elif convite_aceito == True:
        mc "Harlequin… what the hell was he doing to me?"
        mc "Okay, I knew he wanted something… in that way."
        mc "{sc=1}But those things touching me… that wasn’t normal!"
        mc "And then Pierrot! {sc=2}My god, did Pierrot stab him??"
        mc "{sc=2.5}Oh god, there’s blood on my shirt too!"
        mc "{sc=1}And then Carol… She was there! Completely oblivious to everything!"
        mc "{sc=1}What’s happening in that place?"

    else:
        mc "C-Carol is there! What’s happening in that place??"
        mc "She didn’t recognize me! She was acting weird with this empty look."
        mc "And that Ticket Taker… He wouldn’t let me talk to her."
        mc "That conversation with Pierrot wasn’t normal at all, something’s really wrong there."

    play sound "audio/efeitos/portacorrer.mp3" volume 0.2
    mc "Maybe I...{nw=1.0}"
    mcp "(Shit, did I leave the balcony door open?)"

    scene sala at zoomrapido3
    pause 0.3
    scene quartodia
    if floremcasa == True:
        show florpapelp
    with dissolve
    stop music fadeout 1.0

    mc "N-No, it’s not open."

    play sound "audio/efeitos/portafechar.mp3"volume 0.1
    pause 0.2

    scene quartoporta with dissolve:
        zoom 1.1
        xalign 0.5
        yalign 0.5
    show piequarto:
        zoom 1.1
        xalign 0.5
        yalign 0.5

    play music "audio/musicas/comele.mp3" fadein 2.5 volume 0.1
    mc "Pierrot...."

    p "M-[titulo_pierrot]... I can explain everything."

    hide piequarto
    show psad2 with dissolve:
        zoom 1.3
        xalign 0.5
        yalign 0.5

    if envenenada or bolo == True:
        mc "Then why was my missing friend there, looking like a \"doll\" to begin with??"
    else:
        mc "Then why was my missing friend there, looking like a zombie to begin with??"

    hide psad2
    play sound "audio/efeitos/guizo.mp3" volume 0.5
    show pitenso at pulinho:
        zoom 1.3
        xalign 0.5
        yalign 0.5
    
    p "Except for that."

    scene quartoporta with dissolve
    show psad2 with dissolve

    narrator "You take a step back."

    hide psad2
    show pierrot inclinadodelu with dissolve
    hide psad2
    p "Don’t run away, [titulo_pierrot]..."
    p "I might end up liking pulling you back…"
    p "Just hear me out first!"

    hide pierrot inclinadodelu
    show psad2 with dissolve:
        zoom 1.1
        xalign 0.5
        yalign 0.5
    
    p "Please."

    menu: 
        "Stand still":
            play sound "audio/efeitos/guizo.mp3" volume 0.5
            show encaraclosesorriso 
            with dissolve
            hide psad2
            pause 0.5
            show black with slowdissolve
            play sound "audio/efeitos/pegar.mp3"
            narrator "He gently pushes you down onto the mattress in silence."

            play sound "audio/efeitos/lencois.mp3"
            pause 3.0

            p "Thank you..."

            show fiquecomigo with dissolve

            p "Thank you, [titulo_pierrot]. I shall…"
            p "I shall try to be gentle, and restrain myself for your sake, is that alright?"


        "Try to run":
            stop music
            play sound "audio/efeitos/guizo.mp3" volume 0.5
            pause 0.2
            play sound "audio/efeitos/pegar.mp3"
            show encaraclose with hpunch
            show olhos_arregalados
            hide psad2

            pause 0.2
            show black
            play sound "audio/efeitos/cama.mp3" volume 0.5
            narrator "You feel him grab your wrist firmly and throw you onto the bed"

            p "Sorry!!"
            play sound "audio/efeitos/lencois.mp3"
            pause 3.0

            show fiquecomigo with dissolve

            p "{sc=1}{color=#ffaf54}Forgive me! Do not…{w=0.2} run,{w=0.2} [titulo_pierrot]…"
            p "I cannot allow you to flee with such frightened eyes."
            play music "audio/musicas/comele.mp3" fadein 2.5 volume 0.1

    p "I feel your fear, as if I could taste its sweetness with my tongue."
    p "I see it, you know… what does that do to me?"
    p "{sc=1}{color=#ffaf54}{b}It makes my body burn,{w=0.2} throb, yet it terrifies me to think..."
    p "{sc=2}{color=#ffaf54}...You might no longer be able to look at me."
    p "{sc=1}{color=#ffaf54}It makes me want to hold you tighter, to break you with my heat."
    p "{sc=0.5}{color=#ffaf54}Until you forget that anything else in the world exists {b}besides me!"
    p "{sc=2.5}{color=#ffaf54}Suffocating every thought of yours with my presence."
    p "{sc=2}{color=#ffaf54}And your eyes cling to my image as much..."
    p "{b}{size=35}As I want to cling to you right now."

    p "If you run again, I don’t know if I could stop…{w=0.2} not again…"
    p "{sc=1}{color=#ffaf54}{b}Would that make you scream?"

    p "I could end up addicted to pulling you {b}harder and harder until you surrender…"
    p "{sc=1}{color=#ffaf54}But I also want so much to see you stay..."
    p "{sc=1}{color=#ffaf54}Stay... because you want me too…"
    p "I could do anything for you if you gave me the chance!"
    p "{b}Even if I had to crawl through darkness until I lose my mind."
    p "{b}And set the rest of the world on fire."

    narrator "You feel his breath, heavy against you. His hands tremble slightly, as if he’s holding himself back."
    
    mcp "{cps=20}(Pierrot… something inside him feels so broken.)"

    mcp "{cps=20}(It’s beautiful…{w=0.2} but also sad.)"

    p "I can’t tell you anything about your friend right now, but if you want her…"
    p "I… I’ll bring her back to you.{w=0.2} Just not now."
    p "Because {b}he{/b} saw you looking at her too much."

    mc "Pierrot, what’s happening in that place?"

    play sound "audio/efeitos/guizo.mp3" volume 0.5

    scene fiquecomigo2 with dissolve

    p "I can’t say. If you know more, they’ll get suspicious."
    p "I don’t want them coming after you, so the less you know, the less your eyes will give you away to them."

    narrator "You feel your heart racing."

    mcp "(Them?)"

    p "Your heart’s racing… such a sweet sound…"
    p "Trust me, [titulo_pierrot], I know you’re scared, but you need to go back to the circus today."

    mc "{b}What?? Are you serious? After all this??" with vpunch

    p "I know, I know. But if you don’t go today, {b}he{/b}’ll remember."
    p "The others will get suspicious, and they’ll come for you anyway."
    p "B-but as long as you have my red ticket, you’ll be fine!"
    p "Just keep it with you and walk around the circus."
    p "You don’t even need to go on the rides if you don’t want to!"

    mc "{cps=5}{i}Sigh…{/i}{/cps}{w=0.2}\nPierrot…"

    mcp "(Even after everything, it’s hard to stay mad at him)"
    mcp "(He really seems to be trying to protect me from something.)"

    mc "Why are you doing all this?"

    show pierrot pq with dissolve
    voice "audio/dublagem/pierrot1.mp3"
    p "Why?? Hah…"

    show euteamo with dissolve
    show pupilacoracao at olhos_pulsando
    voice "audio/dublagem/pierrot2.mp3"
    p "{b}{cps=0}Because I love you, [titulo_pierrot]!!"
    voice "audio/dublagem/pierrot3.mp3"
    p "{sc=2}{color=#ffaf54}{cps=100}I love you, I love you! I love you so much it hurts, it burns!!"
    p "{sc=2}{color=#ffaf54}{cps=100}Like hellfire in my chest!"
    p "{sc=2}{color=#ffaf54}{cps=100}When your eyes met mine that day."
    p "{sc=2}{color=#ffaf54}{cps=100}It was like my whole existence was screaming for you!!"
    p "{sc=2}{color=#ffaf54}{cps=100}Screaming your name, [mc_nome]!"
    p "{sc=2}{color=#ffaf54}{cps=100}So loud and desperate it echoed through my soul!!"
    p "{sc=2}{color=#ffaf54}{cps=100}You felt it, didn’t you?? Please-- {nw=1.0}"

    hide euteamo
    show pierrot pera with dissolve
    hide pupilacoracao

    mc "{size=50}{cps=10}..."
    mcp "(It’s still too soon for me to answer that, I need a little time after all this madness.)"

    show sentiu with dissolve
    p "You’re blushing…"
    p "Did my words… reach you, [titulo_pierrot]?"
    mc "You’re intense, did you know that?"
    p "I didn’t mean to embarrass you, [mc_nome]."
    p "Do you want me to leave, give you some space?"
    p "I know you need to calm down for tonight."

    menu:
        "Yes, I need some space.":
            $ arlequim_ficanoquarto = True
            mc "I think I need a little time to think…"
            show ohno with dissolve
            p "Alright, I can give you that."
            p "I’ll see you there…"

            scene quarto
            if floremcasa == True:
                show florpapelp
            with dissolve
            show psad with dissolve
            mc "I’ll be there, Pierrot."
            p "Thank you, [titulo_pierrot]."

            scene quartoaberto
            if floremcasa == True:
                show florpapelp
            with dissolve

            play sound "audio/efeitos/portacorrer.mp3" volume 0.3
            narrator "He opens the balcony door as if it were the front door and steps outside."

            mc "Pierrot? We’re on the second floor!"

            play sound "audio/efeitos/portacorrer.mp3" volume 0.3
            scene quarto
            if floremcasa == True:
                show florpapelp
            with dissolve
            mc "Yeah, of course… he just jumped."
            mc "I shouldn’t even be surprised."


        "No, you can stay.":
            $ pierrot_ficanoquarto = True

            mc "You can stay, I guess… Just…"
            mc "Stay quiet while I try to get my head straight, okay?"

            show black with dissolve
            play sound "audio/efeitos/lencois.mp3"
            narrator "He smiles brightly and jumps onto you, resting against your chest."

            scene podeficar with dissolve 
            p "Very well, I’ll be quiet again, anything you wish [titulo_pierrot]!"

            narrator "He rubs his face against you, while his body slowly relaxes at the sound of your heartbeat."

            menu:
                "Stay like this":
                    pass

                "Pet him":
                    play sound "audio/efeitos/guizo.mp3" volume 0.5
                    show pet with dissolve:
                        zoom 2.0
                        xalign 0.3
                        yalign 0.0
                    mcp "(Huh? There’s something… weird under his hat.)"

                    narrator "His body tenses over yours, and he practically holds his breath."

                    mc "Sorry, I won’t do that again."

                    mcp "(His scent is so subtle and pleasant...)"

                    show pp with dissolve
                    show coracoes with dissolve

    mcp "(Things have gotten kinda crazy ever since Pierrot showed up.)"

    if envenenada == True:
        mcp "(He kidnapped me, but that doesn’t bother me, I can feel he didn’t do anything besides tying me up.)"
        mcp "(And now he seems like he’s trying to protect me.)"
        mcp "(Even though he looks pretty unstable at times. Should I really trust him?)" #esse caminho foi testado
    
    elif convite_aceito == True:
        mcp "(I really felt a strange danger when Harlequin pulled me, but Pierrot showed up to \"defend me\".)"
        mcp "(I still don’t know what’s up with Harlequin… that mysterious guy.)"
        mcp "(He doesn’t have Pierrot’s sweet warmth. He’s more like an icy shiver running down my spine.)"
        mcp "(And… pulling my body toward him. Do I like that?)" #testado

    else:
        mcp "(Carol was there, but those eyes, the way she talked, it wasn’t anything like her usual self.)"
        mcp "(And the way that ticket guy pulled her away? Something’s really off.)"
        mcp "(Maybe those disappearances do have something to do with the circus after all.)"
        mcp "(Pierrot and Harlequin, are they actually dangerous?)" #testado tambem
    
    mc "{i}Sighs..."

    mcp "(I don’t know why those two suddenly seem so interested in me.)"
    mcp "(But I’ll wait a little longer before deciding anything about them.)"
    mcp "(First, I’ll do what Pierrot asked and go to the circus tonight.)"
    mcp "(And then I can think about what to do about… those two.)"

    mc "I’ve got so many questions…"

    if naoseguir == True:
        scene black with slowdissolve
        pause 0.2
        jump circodoshorrores

    if arlequim_ficanoquarto == True:
        jump visita_arlequim

    if pierrot_ficanoquarto == True:
        p "I know."

        mc "Alright, I guess we can go and just get this over with."
        p "Very well."

    if marca_arlequim == True:

        scene black with dissolve

        p "What?..."
        scene pq with dissolve

        p "He… marked you."

        narrator "You run your hand over your neck, remembering that awkward bite."

        mc "A-ah… well..."

        p "{cps=15}May I…{w=0.5} cover it?"

        mc "Cover it? I--{nw=0.5}"

        p "With my mark. Let me replace his with mine."
        mc "Pierrot, are you seriously asking me to let you bite me?"
        scene pq with dissolve:
            zoom 1.1
            xalign 0.5
            yalign 0.5
        p "Yes."

        mc "That was pretty direct."
        mc "Is this really that important to you?"

        play sound "audio/efeitos/guizo.mp3" volume 0.5
        narrator "He nods."

        menu:
            "Agree":
                scene mordidap with dissolve

                p "If it hurts too much, you can ask me to stop [titulo_pierrot]."
                play sound "audio/efeitos/pegar2.mp3" 
                scene mordidap2 with dissolve
                mcp "(Ugh… He’s got way too sharp teeth.)"
                mcp "(Ok, that’s hurting more now!!!)"
                mc "Pierrot!?" with vpunch

                scene quarto
                if floremcasa == True:
                    show florpapelp
                with dissolve
                play sound "audio/efeitos/guizo.mp3" volume 0.5
                show pqueixo with dissolve
                p "I apologize..."
                p "Now, when you feel that warmth on your neck..."
                
                hide pqueixo
                play sound "audio/efeitos/guizo.mp3" volume 0.5
                show inclinadoecorado with dissolve
                p "You’ll remember {b}me{/b}, not him."
                mc "S-Sure, I guess."

            "Deny":
                $ mordida_negada = True
                mc "I better not…"
                mc "I can’t go around with marks on my neck. I’ll cover it with something."

                show pf2 with dissolve

                p "{b}{color=#ff0000}He’ll pay for this…"

                scene quarto
                if floremcasa == True:
                    show florpapelp
                with dissolve
                show psad2 with dissolve

                mcp "(I’ve never heard him sound this furious before.)"

    mc "Well, it’s time to go." 

    if mordida_negada == True:
        jump circodoshorrores

    if pierrot_ficanoquarto == True:
        p "I’ll follow you from a distance, [titulo_pierrot], and as soon as my performance is over."
        p "I’ll come to you."

        show quarto
        if floremcasa == True:
            show florpapelp
        with dissolve
        play sound "audio/efeitos/guizo.mp3" volume 0.5
        show inclinado_e_corado with dissolve 

        mc "Alright, you owe me a lot of explanations."
        mc "So, see you there."
        p "See you my love."

        play sound "audio/efeitos/portacorrer.mp3" volume 0.3
        show quartoaberto
        if floremcasa == True:
            show florpapelp
        with dissolve
        hide inclinado_corado 
        mc "Pierrot? We’re on the second floor!"

        mc "Yeah, of course… he just jumped."
        mc "I shouldn’t even be surprised."

        play sound "audio/efeitos/portacorrer.mp3" volume 0.3
        scene quarto
        if floremcasa == True:
            show florpapelp
        with dissolve
        pause 0.2

    scene black with slowdissolve
    pause 0.2   
    jump circodoshorrores


label visita_arlequim:
    stop music fadeout 1.0
    play sound "audio/efeitos/portacorrer.mp3" volume 0.3
    scene quartoaberto
    if floremcasa == True:
        show florpapelp
    with dissolve

    a "Finally he’s gone."
    show alado with dissolve 
    a "It was almost cruel of you not to ask more about me, [titulo_arlequim]."

    play music "audio/musicas/comoutro.mp3" fadein 1.5 volume 0.1

    if convite_aceito == True:

        menu:
            "Apologize":
                mc "I’m sorry! I got scared."
                mc "Are you okay?"

                hide alado 
                show arlefrente2 with dissolve 
                
                a "How sweet, worried about me?"

                mc "What do you think??"

                a "Hah.. That sounds so sweet coming from your mouth."

                show arlefrente3 with dissolve
                hide arlefrente2

                a "But I hate sweets."
                a "Though I might make an exception and taste yours ♪"

                mc "I’m serious, you pervert!!"
                mcp "(He seems on edge this time.)"

                show arlequim aperto with dissolve

                a "Huhum, now you’re almost convincing me, [titulo_arlequim]."

                mc "{size=50}..."

                show arlequim aperto2 with dissolve 

                a "Oh, {i}that look! And if I said I believe those sweet little words."
                a "You gonna spread nice and wide for me, huh?"

                mc "Uhn… You really don’t believe a word of it."
                mc "Alright, this isn’t going anywhere."


            "Hug":
                stop music
                play sound "audio/efeitos/pegar2.mp3" 
                show abraco with dissolve
                show olho_abraco
                a "Quê?"

                mc "Are you okay? I saw blood. I got really worried."
                play sound "audio/efeitos/pegar.mp3"
                show exp1 with dissolve
                hide abraco
                hide olho_abraco
                a "Ah? Worried about me? Huhum. ♪"

                mc "{size=50}..."
                mcp "(There’s something weird when I hug him... it feels like there’s something raised under the fabric.)"
                mcp "(I... don’t know what it is. It’s not hard like bones.)"
                mcp "(And he smells so good.)"

                a "Are you really serious?"
                a "A few stabs aren’t gonna stop me, [titulo_arlequim]. This is just child’s play."
                show exp2 with dissolve 
                a "You can let me go now."
                a "You hear me?"
                play music "audio/musicas/comoutro.mp3" fadein 1.5 volume 0.1
                hide exp2 with dissolve 
                a "If you want me to touch you again so badly, we can--"
                mc "{i}Sigh..."
        
        scene quartoaberto
        if floremcasa == True:
            show florpapelp
        with dissolve
        show arlefrente with dissolve 

        mc "I think you also owe me a lot of explanations about what happened in that tent."

        hide arlefrente
        show alado with dissolve:
            zoom 1.05
            xalign 0.5
            yalign 0.5

        a "We were just having fun, weren’t we?"
        a "Is that your way of asking to pick up where we left off?"
        hide alado
        show arlefrente with dissolve
        mc "D-don’t change the subject! How did you even do all that?"
        mc "And how are you not bleeding after being stabbed once?"

        hide arlefrente
        show alado with dissolve:
            zoom 1.1
            xalign 0.5
            yalign 0.1

        a "Five times, actually.{nw=1.0}"

        hide alado
        show arlefrente with dissolve
        mc "You’ve gotta be kidding me??" with vpunch

        a "Sure, I don’t need to lie."

        hide alado with dissolve
        a "But you already look a little shaken today."
        a "I heard you two talking about visiting our home."

        mc "The circus? Yeah, Pierrot asked me to come back."
        
    else:

        hide alado
        show arlefrente with dissolve

        mc "Harlequin! What happened back there?"

        show arlefrente2 with dissolve 
        a "He lost his mind when he couldn’t find you in the storage room, [titulo_arlequim]."
        a "You should’ve seen the murderous look he can pull off."

        mc "You… did you get hurt?" 

        narrator "He laughs, mockery dripping from his voice."

        mcp "(That on his glove, wasn’t blood after all?)"

        a "Not even a \"Thank you for letting me out, Harlequin. I’m oh-so excited, just for you.\"?"

        mc "I think it’s pretty clear you didn’t let me go out of kindness. You just wanted to piss Pierrot off."

        show arlefrente3 with dissolve
        hide arlefrente2
        a "Ah, yes ♪ I’m starting to think we’d make a deliciously wicked pair."
        a "With a little help from you, the two of us could drive him mad, [titulo_arlequim]."

        mc "God, what’s wrong with you."

        show aperto2 with dissolve
        hide arlefrente3

        a "Don’t lie to me, [mc_nome] weren’t we having fun?"

        mc "Your idea of fun is playing with a knife against my skin?"

        show aperto with dissolve:
            zoom 1.1
            xalign 0.5
            yalign 0.5
        a "My idea of fun is making you moan and shiver, dear. You held back so well…"
        a "I almost couldn’t resist going harder."

        hide aperto with dissolve
        a "{i}Oh! I saw that. ♪"
        a "You hold your breath."

        mc "I’ve got so many questions. And I know you won’t answer any of them."

        a "My green tongue’s still haunting your mind, isn’t it? I told you I could show you even more."

        menu: 
            "So...?":
                show aperto with dissolve
                a "{cps=30}Oh, asking to see more, are we?{w=0.3} {i}Naughty{/i},{cps=20} I’m surprised. ♪"
                a "I’d love to see the look on your face, if I let you peek just a little beneath what the fabrics are hiding."

                hide aperto
                hide aperto2 with dissolve
                show arlefrente2 with dissolve
                a "But, patience [titulo_arlequim], that little taste is not yours this night."
                

            "No, thanks":
                hide aperto2 with dissolve
                show arlefrente2 with dissolve 
                a "Your little act of shyness, it’s adorable, but it doesn’t fool me dear."
                show arlefrente3 with dissolve
                hide arlefrente2
                a "I know exactly how my words make your body respond."
                a "Pierrot may have your heart, but it’s me your body wants."
                hide arlefrente3 with dissolve 

        a "{cps=20}By the way, I overheard your little conversation."

    hide alado
    show arlequim sorrisotorto with dissolve
    hide arlefrente
    
    a "He was right."
    a "For tonight, it’s better your pretty eyes don’t scream your doubts to everyone else."
    a "But tomorrow…"
    hide arlequim sorrisotorto
    show arlefrente2 with dissolve:
        zoom 1.2
        xalign 0.5
        yalign 0.5
    voice "audio/dublagem/arlequim1.mp3"
    a "Tomorrow, if you come chasing after me again."
    voice "audio/dublagem/arlequim2.mp3"
    a "I’ll tell you, I’ll show you, and if you still don’t run, oh my dangerous dear."
    show arlefrente3 with dissolve:
        zoom 1.2
        xalign 0.5
        yalign 0.5
    hide arlefrente2
    voice "audio/dublagem/arlequim3.mp3"
    a "I’ll ruin you in ways that’ll make what happened in the tent look{cps=10} innocent. ♪" #talvez tirar isso aqui
    a "Then our little game is going to go much further."
    a "Well, have fun at the circus today, [mc_nome] {i}I know I will."

    hide arlefrente3 with dissolve
    play sound "audio/efeitos/portacorrer.mp3" volume 0.3
    scene quarto
    if floremcasa == True:
        show florpapelp
    with dissolve
    pause 0.3

    mc "Sigh..."

label circodoshorrores:
    scene black with dissolve
    pause 0.1
    stop music fadeout 1.0
    play music "audio/musicas/circo.mp3" fadein 1.5 volume 0.1
    scene circo with dissolve:
        zoom 1.2
        xalign 0.5
        yalign 0.5

    show bilheteiro with dissolve
    b "Greetings, visitor. May I see your--{w=0.5} ah!"

    hide bilheteiro
    show b 2 with dissolve
    b "The guest with the red ticket, aren’t you?"

    mcp "(Just act natural, I just need to act natural…)"

    menu: 
        "Of course! I said I’d come back!":
            pass
        "Yes! That’s me! I just can’t stay away from this place.":
            b "{cps=10}{size=45}..."
            mcp "(Crap, I laid it on too thick.)"

    hide b 2
    show b 3 with dissolve
    b "Enjoy yourself, guest."
    b "The circus has sharp eyes, it always notices those who seek joy..."
    b "{cps=15}Or those who hide a {i}secret{/i} deep in their hearts."

    mc "Ah… haha… well, I’ll, uh, wander around a bit."
    mcp "(God, he knows that I know.)"

    hide b 3
    show bilheteiro with dissolve

    b "Should you need anything, please, do not hesitate to speak with me."
    b "And one small warning, the pink tent and the black one are beyond the bounds of your ticket."
    b "You won’t be able to enter."

    mc "Sure."

    hide bilheteiro with dissolve 

    mcp "(Since I need to walk around, I’ll check out the other attractions.)"
    mcp "(Looks like Pierrot’s show is in the middle, can’t get in.)"
    mcp "(The Harlequin show’s already over, maybe there’ll be another later.)"
    mcp "(And I’ll probably end up running into him at some point.)"

label tendas1:
    scene circo with dissolve
    menu: 
        "Blue Tent" if not visita_azul:
            $ visita_azul = True
            jump tendaazul
        "{color=#2b2b2b}Blue Tent{/color}" if visita_azul:
            jump tendas1

        "Cyan Tent" if not visita_ciano:
            $ visita_ciano = True
            jump ciano
        "{color=#2b2b2b}Cyan Tent{/color}" if visita_ciano:
            jump tendas1

        "Purple Tent":
            if visita_azul and visita_ciano:
                jump tenda_roxa

            else:
                mc "Looks like this is the last attraction of the night."
                mc "I can check out the others until it’s time for this one."
                jump tendas1

        "Black Tent":
            jump tenda_preta


label ciano:

    scene tendaciano with dissolve

    narrator "You see someone stumbling out of the tent, pale, rubbing their arms with a terrified look."

    mcp "(This looks straight out of a haunted house. Only one person goes in at a time.)"

    show rando with dissolve

    narrator "You’re handed a clipboard with a feather pen to sign."

    mcp "(A contract? What kind of attraction is this?)"

    hide window
    hide text

    play sound "audio/efeitos/panfleto.mp3"
    call screen contract_screen

    play sound "audio/efeitos/panfleto.mp3"
    mcp "(Well, I’m already here anyway, so why not?)"

    narrator "You hand the paper back to the masked one."

    hide rando with dissolve

    scene tendaciano at zoom_meio
    pause 1.0

label doutor:
    $ fala_noespelhododoc = True
    stop music fadeout 1.5
    scene tendadoc with dissolve

    show olhosdoc at  fade_in_olho
    pause 1.8
    play sound "audio/efeitos/luzes.mp3"
    show tendadoc2 with slowdissolve

    doc "Come closer, dear patient, don’t be shy."
    play sound "audio/efeitos/creck.mp3"
    scene tendadoc3 with hpunch

    doc "Oh, that? Don’t mind them."
    doc "I promise they can’t bite you. Well…{w=0.2}{cps=13} not anymore, huhum."

    window hide
    play sound "audio/efeitos/luzes.mp3"
    show luzes_doc
    play sound "audio/efeitos/luzeschao.mp3" volume 0.1

    pause 1.5
    scene tendadoc4 with slowdissolve

    mcp "(No turning back now…)"
    
    scene tendadoc4 at zoom_meio
    pause 0.8
    scene black with dissolve

    doc "Don’t forget to roll up your sleeves, please."

    play music "audio/musicas/doutor.mp3" fadein 1.5 volume 0.2
    scene cadeira with dissolve

    narrator "You smell sweet incense, a scent you’ve never experienced in your life."

    doc "You wanted to run off, didn’t you? It’s fine, no one really likes visiting the Doctor."

    scene cadeira2 with dissolve
    doc "After all, there aren’t any secrets between the Doctor and their patient, right?"

    mc "W-wait, what are you doing?"

    doc "It's part of the procedure. I don’t want you to freak out and run off."
    doc "You could hurt yourself, you know?"
    doc "There are dangerous instruments in an office."
    scene cadeiracima with dissolve
    pause 0.2
    show doc 1 with dissolve
    play sound "audio/efeitos/pegar.mp3"
    doc "On your file, it says you’re not feeling unwell, you’re just, curious about the attraction, right?"

    play sound "audio/efeitos/pegar.mp3" volume 0.2
    show doc 2 with dissolve

    doc "So, you came here to see me, to test whether the fear of being my guinea pig is worth it."

    mc "Guinea... pig?"

    doc "It’s okay, I’m your Doctor, and I’m going to examine every fiber of your being, [mc_nome]."
    play sound "audio/efeitos/pegar.mp3" volume 0.2
    show doc 1 with dissolve
    doc "You’re cold… is your blood pressure dropping?"

    narrator "He holds your wrist firmly, checking your pulse."

    play sound "audio/efeitos/pegar.mp3" volume 0.2

    show doc 2 with dissolve:
        zoom 1.1
        xalign 0.5
        yalign 0.5
    
    doc "Oh, what a firm pulse you have, beating with so much life. If you’ll let me…"

    play sound "audio/efeitos/pegar.mp3" volume 0.2
    show doc 3 with dissolve 

    narrator "You feel the sharp tips pressing against your skin."

    mc "Shouldn’t you be using a stethoscope?"

    doc "You’re not really sick,{w=0.3} I don’t need it.{w=0.3} {i}I can feel it."
    play sound "audio/efeitos/pegar.mp3" volume 0.2
    show doc lado2 with dissolve:
        zoom 1.0
    doc "Ah… your heart… it sounds like a drum."
    show doc lado2b with dissolve
    show docolho at olho_dodr
    doc "{cps=20}{b}Like it’s asking me to open your chest and take a closer look."

    mcp "(What?)"
    doc "You’re breathing too heavily too."
    play sound "audio/efeitos/pegar.mp3" volume 0.2
    show doc 3 with dissolve:
        zoom 1.1
        xalign 0.5
        yalign 0.5

    doc "And your pupils are wide dear patient, unnaturally wide. Hold still."
    doc "{cps=25}Don’t move."

    narrator "You feel something sharp press into your skin as his hands draw closer."

    menu:
        "React":
            stop music
            show doc 3 with hpunch:
                zoom 1.0
            play sound "audio/efeitos/efeitosus.mp3" volume 0.2
            narrator "You recoil when his claws scrape across your flesh."
            
            mc "S-sorry, I…"
            mc "Did... did you just scratch me?"
            mcp "(There’s something cold at my neck, but it doesn’t hurt.)"

            play sound "audio/efeitos/apagao.mp3" volume 0.3
            show doc 3:
                zoom 1.25
            show maodoc with hpunch

            mc "Doctor...?"
            play sound "audio/efeitos/olhosdoc.mp3" volume 0.3
            show doc v with slowdissolve
            play music "audio/musicas/doc2.mp3" fadein 2.0 volume 0.2
            doc "{cps=20}…Look…{w=0.3} what you’ve done…"
            doc "it’s dripping…{w=0.3} leaking like a broken faucet…"
            doc "{b}Ahh, this is good!!"
            doc  "{b}{sc=3}{color=#e74c3c}HHAHAH...."
            doc "{b}{sc=3}{color=#e74c3c}HHHAAAHAHHHAHAHAHA!!!"
            doc "{sc=2}{color=#e74c3c}Good method..."
            doc "{sc=2}{color=#e74c3c}Did you know bloodletting, can have calming effects?"
            doc "{cps=20}{b}For me, of course!"
            
            show doc_animacao with dissolve
            hide maodoc
        

            doc "{b}HAHAHHAHA What a beautiful shade of red!!!"

            mc "Am I… bleeding?"

            doc "{b}{sc=1}{color=#e74c3c}I could… split you wide open…"
            doc "{b}{sc=1}{color=#e74c3c}Just to watch the show… your heart, thrashing…"
            doc "{b}{sc=1}{color=#e74c3c}Desperate to survive!!"
            doc "{b}The taste…"
            doc "{b}Yes!! The taste!!"
            doc "{b}With all that spice of adrenaline, it must be--{nw=1.5}"

            stop music
            mc "DOCTOR!!" with hpunch
            
            scene doc lado
            show doc ladoc with slowdissolve
            play music "audio/musicas/doutor.mp3" fadein 1.0 volume 0.2

            doc "{size=45}{b}{cps=25}..."

        "Still":
            scene doc diag with dissolve
            doc "Your eyes say a lot. Just like every involuntary reaction of your body."
            doc "I noticed the moment you walked in, you were hesitant, curious, and your expectations..."
            doc "Were different from the others."

            mc "What do you mean by that?"

            doc "A normal person would be impressed by this place. But you?"
            doc "You locked your eyes directly on me. I wonder why."

            mc "..."

            doc "Tension, trembling fingers… interesting. Are you nervous?"

            mcp "(This guy, is he gonna notice every little thing I do?)"

            doc "That expression, you’re actually enjoying this, aren’t you? You really are a fascinating test subject."

            mcp "(He’s close… I can smell so many things...)"
            mcp "(Incense,{w=0.2} herbs,{w=0.2} something metallic and…{w=0.2} coffee?)"

            doc "Your body keeps leaning toward me. I’d say you like danger, don’t you? Hmhm."

    scene cadeiracima with dissolve
    show doc diag2 with dissolve

    doc "Ahem. I’ve already got your diagnosis."

    mc "Are you actually examining me?"

    doc "Of course I am. I’m your Doctor, my tasty patient."
    doc "And I can see your heart racing, your skin’s cold, and your eyes…"

    play sound "audio/efeitos/pegar.mp3" volume 0.3

    show doc 1 with dissolve
    doc "Your pupils are blown wide like they’re begging for the light to pierce them."
    doc "You’re scared, and you’re enjoying it, but I’m not here to judge."
    play sound "audio/efeitos/olhosdoc.mp3" volume 0.5
    show doc1olhos at olho_dodr
    doc "I love hearing the blood quicken under your skin."

    play sound "audio/efeitos/efeitosus.mp3" volume 0.5

    show doc injecao with dissolve
    doc "An injection could fix that. You’ll relax."
    doc "Don’t worry you don’t have to hold your voice back."
    doc "This is the place to scream if you want."

    mc "N-no… thanks, I think this is getting a bit far..."

    doc "I promise you’ll feel a lot better."

    menu:
        "Accept":
            mc "If the doctor says so."
            doc "Huhuhum."
            show doc lado2b with dissolve
            doc "I was joking. This is the part where patients usually struggle."
            show doc diag2 with dissolve

        "Deny":
            doc "No? That’s fine, patient."
            doc "Or maybe I already gave you the injection and you didn’t even notice."
            show doc diag2 with dissolve


    doc "So tell me, patient are you feeling more relaxed?"

    call screen doutor_escolhas
        
    doc "Perfect! And you behaved so well."
    play sound "audio/efeitos/pegar.mp3" volume 0.3
    show doc inclinado with dissolve
    doc "Most patients scream and struggle when I show the needle, Huhum."

    mc "So, am I free, doctor?"
    mcp "(Being tied like this is still kinda uncomfortable.)"

    play sound "audio/efeitos/pegar.mp3" volume 0.3

    show doc diag2 with dissolve
    doc "{i}{cps=20}I’m still deciding.{/i}{w=1.0} {/cps}I could keep you here, and listen to your heart wear itself out until exhaustion..."
    doc "Or until your adrenaline just runs dry..."

    mc "Excuse me?"
    play sound "audio/efeitos/pegar.mp3" volume 0.3
    show doc inclinado with dissolve
    doc "Huhuhum. Don’t worry, just a little medical humor."
    doc "I’ll let you go now, but before that..."
    play sound "audio/efeitos/pegar.mp3" volume 0.3

    show doc lado2 with dissolve
    doc "Know that I adore this fake faith of yours."
    doc "{cps=35}You lie, and I pretend to believe.{w=0.5} I lie, and you pretend to {/cps}{cps=10}swallow every word."

    play sound "audio/efeitos/pegar.mp3" volume 0.3

    show doc lado2b with dissolve 
    doc "What a fun game."
    doc "But I see something different in you, your eyes don’t lie the way they should."

    mc "Well, I just like to question things, you know?"

    show doc diag2 with dissolve
    doc "Interesting..."

    mc "So, uhn, could you--"

    doc "Are you hungry? You’ve behaved so well, you deserve a treat. May I see your ticket?"

    mc "Sure, if you let me go I--{nw=1.5}"

    hide doc diag2 with dissolve
    play sound "audio/efeitos/pegar.mp3" volume 0.3
    narrator "He leans in and takes the ticket from your pocket."

    doc "Oh, actually..."
    show doc diag2 with dissolve

    doc "Seems I’ve run out of sweets. I’ll owe you one."

    mc "Hun?"

    scene black with dissolve
    
    narrator "He returns your ticket and starts untying your hands."
    play sound "audio/efeitos/pegar.mp3" volume 0.3
    mcp "(That was weird, he looked kinda hesitant after seeing Pierrot’s ticket.)"
    show mcciano with dissolve
    mc "See ya, doc."

    play sound "audio/efeitos/pegar.mp3"
    show doc aviso with hpunch
    voice "audio/dublagem/doutor.mp3"
    doc "Remember,{w=1.0} make regular visits to your doctor."
    doc "There’s too much adrenaline in your blood…{cps=15} I like that."
    doc "Enjoy your walk, [mc_nome]."

    scene black with dissolve
    stop music fadeout 2.0

label foradatenda:

    mcp "(That was weird… like everything in this circus. For a second, I really thought I’d be stuck in that tent.)"
    play music "audio/musicas/circo.mp3" volume 0.2
    scene circo with dissolve

    narrator "You run your hand over your neck and feel a bandage."

    mcp "(He actually scratched me, but I didn’t even feel it. I didn’t even see him put this bandage on.)"

    mcp "(Still, I want to look around a bit more. Pierrot said I’d be safe, didn’t he?)"

    jump tendas1

label tenda_roxa:
    stop music fadeout 1.5
    play music "audio/efeitos/multidao.mp3"
    scene tendaroxa1 with dissolve
    mcp "(This tent has a stage, maybe something theatrical?)"

    play sound "audio/efeitos/luzes.mp3" volume 0.3
    scene tendaroxa2 with dissolve
    pause 0.3
    show je1 with dissolve
    d "{color=#961ee6}Welcome, welcome! My precious monsters of the day!"
    d "{color=#961ee6}Did you come thirsty for blood? {i}Hungry for terror?"
    show jesa with dissolve
    hide je1
    play sound "audio/efeitos/guizosjester.mp3" volume 0.3
    stop music fadeout 1.5
    d "{color=#961ee6}You know, my dear monsters, this dark garden is the window to the kind of fear you’ve been craving."
    play music "audio/musicas/jester.mp3" fadein 10 volume 0.3
    j "And I, as your noble Jester, couldn’t possibly deny shivers to my starving little monsters, could I?"
    scene je2
    
    j "Tonight, I’ll tell you a story. Hold your gasps it’s just..."

    scene tendaroxa2 with dissolve
    show jes tras1 with dissolve
    j "A harmless story, about... {cps=30}{i}Forbidden love."

    show jes tras2 with slowdissolve  
    show marionetes with slowdissolve
    j "{cps=50}In a forgotten valley,{w=0.2} where the moonlight seemed to hesitate before touching the ground,{w=0.2} the {i}nameless{/i} ones lived."

    show jes tras3 with dissolve
    j "{cps=50}Creatures of hidden shapes,{w=0.2} hungry eyes,{w=0.2} and hearts."
    j "{cps=50}That had long forgotten how to beat for anything beyond {b}hunger."

    hide marionetes
    show msentado with dissolve
    j "{cps=50}But among them,{w=0.2} there she was,{w=0.2} a sweet little flower in a garden of black thorns."
    show mcolu with dissolve
    j "{cps=50}Shaped like a gift from the heavens!{w=0.2} {/cps}{cps=10}{b}Columbina{/b}."

    show glitchroxo
    show screen sobreposicao_texto2(_("{glitch=20}{b}{color=#e61ee6}PlEASE, NO!{/glitch}"))
    pause 1.0
    hide glitchroxo
    show jes palco with dissolve
    j "Delicate, with no claws, almost no fangs."
    j "Just a gentle presence among the shadows, smiling warmly at monsters."
    j "A smile that even lit up the darkness."
    scene mflor at zoom_peça
    with dissolve
    j "And it was for that tender warmth that He, the silent monster, lost himself."
    j "Every day he watched her, her light steps, her kind words."
    j "And the more kindness she gave, the closer he came."
    j "He sighed for her."
    j "Kept for her the broken flowers of the valley."
    j "And tried to hide his claws so she would not wound herself upon his skin."

    scene mflor with dissolve
    pause 0.5
    scene mflor2 with dissolve
    j "But there was the Other."
    scene mflor3 with dissolve
    show jes palco2 with dissolve

    play sound "audio/efeitos/efeitosus.mp3" volume 0.2
    j "A monster with venom in his voice and in his hands."
    scene mflor3 with dissolve:
        zoom 4.0
        xalign 1.0
        yalign 0.3
    j "Who hid within the shadows of lover's meetings."
    j "Who saw the light in the lover’s eyes and felt envy gnawing him from within."

    scene mflor4 with dissolve
    show jes palco2 with dissolve

    v "Why are your eyes never on me? Why can’t it be… me?"

    scene historiaac with dissolve
    j "The venomous monster clenched his claws when she slipped away from his attempts at seduction."
    j "His teeth ground together whenever she pulled back in his presence."

    play sound "audio/efeitos/pegar.mp3" volume 0.3

    scene historiaac2 with dissolve
    j "And every refusal was like a crack splitting his very being."

    co "You make me sigh too… you make my heart race."
    show screen sobreposicao_texto(_("{glitch=30}{b}{color=#e61ee6}But something inside you scares me.{/glitch}"))
    pause 2.0

    j "She was just as kind to him, and even though she sighed in his presence."  
    j "Her heart beat in a different way."
    j "Until one day, the Other grew tired of the game."
    j "Tired of the glances that weren’t meant for him."
    j "Tired of the sound of the lovesick monster’s footsteps drawing near."
    play sound "audio/efeitos/golpecortante.mp3" volume 0.3
    scene mgore0 with hpunch
    v "You know, my sweet flower…"

    scene mgore1 with slowdissolve
    v "Maybe it’s not you that I love."
    v "Maybe this feeling is something else. My heart beats fast for another reason."

    play sound "audio/efeitos/carne.mp3" volume 0.3

    scene mgore2 with vpunch
  
    v "Or maybe… I just want what I can’t have. If I do this, maybe then…"
    play sound "audio/efeitos/carne.mp3" volume 0.3

    scene mgore3 with vpunch
    v "{sc=2}{color=#b2ffd2}I can love you the right way… only my way.{cps=10} Mine."

    show screen sobreposicao_texto(_("{glitch=20}{b}{color=#e61ee6}P-please… don’t {sc=80}{color=#41d623}A.Q.RLE {/glitch}"))
    pause 1.0
    scene mgore4
    pause 0.2
    play sound "audio/efeitos/desmembrar.mp3" volume 0.3
    show monglitch
    pause 0.5

    scene black
    j "And when the lovestruck one arrived, on that starless night, all he found was the poison."
    scene teatro1 with slowdissolve
    j "Found the Other standing there, blood still warm on his hands, a crooked, stained smile on his face."
    play sound "audio/efeitos/pegar.mp3" volume 0.3
    scene teatro2 with dissolve
    show jes palco2 with dissolve
    
    j "Behind him, delicacy lay on the ground like a crushed flower, eyes still open in surprise."
    

    show screen sobreposicao_texto2(_("{glitch=20}{b}{color=#4153f7}Why… did you do that?{/glitch}"))
    show devorar
    pause 0.72
    hide devorar
    v "Are your eyes on me? Uhg."
    show screen sobreposicao_texto(_("{glitch=20}{b}{color=#41d623}Is your {b}hate{/b} on me?{/glitch}"))
    pause 2.0
    v "{sc=5}{color=#b2ffd2}Hah..haahHAHHAhhA!!!"
    v "{sc=1}{color=#b2ffd2}Oh... Rage... Pain!! I love it...{/sc}{sc=5}{color=#b2ffd2}{b} I LOVE IT!"

    show screen sobreposicao_texto2(_("{glitch=20}{b}{color=#41d623}Someone had to do it…{w=0.2} obviously.{/glitch}"))
    pause 0.9
    show screen sobreposicao_texto2(_("{glitch=20}{b}{color=#961ee6}There’s no turning back now.{/glitch}"))
    pause 0.9
    scene black
    pause 0.5
    show screen sobreposicao_texto2(_("{glitch=20}{b}{color=#ffaf54}No... no no no...{/glitch}"))
    pause 0.9
    show screen sobreposicao_texto2(_("{glitch=20}{b}{color=#41d623}{size=50}EAT{/glitch}"))
    pause 0.9
    j "And the valley filled with the cry of the lovestruck monster, a cry not of hunger, but of pain."

    show screen sobreposicao_texto2(_("{glitch=20}{b}{color=#ffaf54}I’ll find a way… we’ll be together forever.{/glitch}"))
    pause 0.5
    
    play sound "audio/efeitos/desmembrar.mp3" volume 0.3
    show mordidam at mordidamz
    pause 0.41
    hide mordidam
    
    scene palcosangue with dissolve
    show jes palco3 with dissolve
    j "A scream that would echo through the centuries, haunting every shadow."
    show jes palco4 with dissolve
    j "Every night, every breath of those who dared to love there."
    j "Because in the valley of monsters, love is just another way to devour each other."

    show screen sobreposicao_texto2(_("{glitch=20}{b}{color=#961ee6}We have no choice.{/glitch}"))

    scene black with slowdissolve

    j "And that day, the nameless shadows grew stronger in the dark."

    scene tendaroxa2
    show jes f1
    with dissolve

    j "The poison? It found that hatred tastes far sweeter than love."
    show jes f2 with dissolve
    pause 0.3
    
    scene black with dissolve

    stop music fadeout 5.0
    mcp "(Once again, another performance that turns my stomach… why does the blood look so real? Why did the scream sound so real??)"
    mcp "(I’ll wait for the crowd to clear out before getting up.)"
    
    d "I always love this show."
    d2 "Right? I love the bloody, macabre acts."
    d "The blood looks so fake, but oh well."

    mcp "(People seem excited. Guess I can leave now.)"

    play sound "audio/efeitos/pegar.mp3" volume 0.3
    pause 0.5
    j "{cps=40}Hello,{w=0.2} visitor."
    scene tendaroxa1 with slowdissolve:
        zoom 1.2
        xalign 0.5
        yalign 0.5
    show asassangue:
        zoom 1.2
        xalign 0.5
        yalign 0.5
    show jes idle with dissolve
    play music  "audio/musicas/jester.mp3" fadein 15 volume 0.1
    j "You look paler than the others. Did my tent get to you… or is something else bothering you?"

    mc "Y-Yeah! Yeah, I’m fine. I was just leaving."

    play sound "audio/efeitos/guizojester2.mp3" volume 0.1

    show jes inclinado with dissolve
    j "I noticed, you know."

    mc "Noticed... what?"

    j "A huge shadow hanging over you in this circus. A shadow with {i}golden eyes."

    mc "I don’t…{w=0.2} know what you’re talking about."

    show jes idle with dissolve
    j "May I see your ticket?"

    mcp "(Here we go again… why do I always get chills when someone asks me that?)"
    show expression Solid("#000000C0") as escurecer with dissolve
    show screen ingresso_vermelhofurado with dissolve
    pause
    hide jes idle
    show jessorriso2 with dissolve:
        zoom 1.2
        xalign 0.5
        yalign 0.5

    hide escurecer
    hide screen ingresso_vermelhofurado with dissolve
    pause 0.5
    show jessorriso1 with dissolve:
        zoom 1.2
        xalign 0.5
        yalign 0.5
    hide jessorriso2

    j "Red, just as I thought. I’ve never seen that ticket in anyone’s hands before."

    mcp "(I don’t know what he’s after, but I don’t like where this is going.)"
    mc "I'm goin--{nw=0.3}"

    show jessorriso1:
        zoom 1.4
        xalign 0.5
        yalign 0.6

    j "{glitch=1}{b}{color=#961ee6}Stay."
    
    hide jessorriso1
    play sound "audio/efeitos/guizojester2.mp3" volume 0.1
    show jes inclinado with dissolve:
        zoom 1.4
        xalign 0.5
        yalign 0.6

    j "You know,{w=0.2}{cps=30} dear thing..."
    j "Eyes say a lot about what goes on in the soul. And yours…{w=0.3} {cps=9}{i}they scream."
    j "Did you come here because you {b}wanted{/b} to, or because {b}someone{/b} sent you?"

    menu:
        "I chose to come.":
            show jes lado with dissolve:
                zoom 1.4
                xalign 0.5
                yalign 0.5
            j "Did you know people’s eyes betray them when they lie? A slight movement to the side."
            j "{i}Huhu,{/i} I’m kidding. Or am I?"
            j "People lie with their mouths. Their eyes never bother."
        "Someone asked me to come.":
            show jes lado with dissolve:
                zoom 1.4
                xalign 0.5
                yalign 0.5
            j "Honesty, such an admirable quality."
            j "I like that."

    scene tendaroxa1
    show asassangue
    show jes idle with dissolve:
        xalign 0.55
    play sound "audio/efeitos/guizojester2.mp3" volume 0.1
    show jes inclinado:
        xalign 0.55
    narrator "You take a step back."

    show jes frame1 with dissolve
    j "{i}Huhum ♪"
    show screen jes_sombras
    pause 0.1
    show jes frame
    j "{cps=50}Fear is curious, isn’t it? {i}It makes us see monsters where there are only shadows."
    show jes lado with dissolve
    j "You know, visitor, there are many kinds of fear."
    show jes lado2 with dissolve
    j "The fool’s fear, the kind that makes you run when the monster draws near."
    show jes idle with dissolve:
        xalign 0.5
    j "The wise fear, the kind that knows it’s too late to run..."
    play sound "audio/efeitos/guizojester2.mp3" volume 0.1
    show jes inclinado with dissolve
    j "And there’s the fear that’s born when you realize you saw something you shouldn’t have."
    pause 0.2
    show olhosjesinclinado at fadeolhojes:
        xalign 0.5
    j "Do you know which one yours is? Your eyes are telling me right now."
    show jes idle with dissolve
    j "Enjoy the rest of the night, sweet visitor. I have a feeling we’ll meet again in this circus."

    stop music fadeout 5.0
    j "Ah!{w=0.2}{cps=20} One last thing."
    show jes close with dissolve
    $ renpy.notify(_("Hidden scene unlocked 🔓"))
    $ persistent.unlocked_scenes["cena_01"] = True
    voice "audio/dublagem/jester.mp3"
    j "Don’t go far, [mc_nome]. I’ll know {i}how to find you{/i} if you try."
   

    jump sobrevivente

label tendaazul:
    scene tendaazul with dissolve

    narrator "Tent of Mirrors: Don’t trust what your eyes see."

    mcp "(Nice marketing. Let’s see what we’ve got here.)"

    stop music fadeout 1.0
    play music "audio/musicas/bilheteiro.mp3" fadein 1.0 volume 0.1
    scene tendaadentro with dissolve
    show pessoas with dissolve

    mcp "(Just one of those mirror houses? Doesn’t really seem like a scary attraction.)"

    stop music
    show black with slowdissolve
    mc "Wha--"
    play music "audio/musicas/bilheteiro.mp3" fadein 5.0 volume 0.1 #quando navegador estiver ativado isso precisa desabilitar
    scene espelhoalma0 with dissolve

    mcp "(Where did everyone go?)"

    show sombratt with dissolve

    b "Hm? My tent doesn’t usually attract that many curious souls, {i}especially{/i} ones who seem so eager to run away."

    mc "How… did you do that? Where did you take them?"

    b "Me?{w=0.2} Perhaps, it’s you who only thought you saw others in here."
    b "You might’ve been alone from the very start, just you and me.{cps=15} Red ticket guest."

    hide sombratt with dissolve
    pause 0.2
    #$ renpy.movie_cutscene("images/bilheteiro/bilespelho.webm") #reprodução de navegador
    play movie "images/bilheteiro/bilespelho.webm"
    pause 1.0
    #play music "audio/musicas/bilheteiro.mp3" fadein 5.0 volume 0.1 #quando navegador esta habilitado, ligar este junto
    scene espelhoalma with dissolve
    show blastframe with slowdissolve

    b "In here, dear guest, you’ll see things you might not want to, whispers from your heart, or maybe warnings from beyond."
    hide blastframe
    show bil espelhof with dissolve
     
    b "{i}\"Don’t trust what your eyes see.\"{/i}{w=0.3} Enjoy!"

    scene espelhoalma2 with slowdissolve

    mc "But what do I--"

    b "Just keep moving forward, guest."
    b "You’ll find the exit eventually. Though I’d recommend not stopping for too long..."
    stop music fadeout 3.0
    b "I’ve heard monsters live in the dark. And mirrors, sometimes show more than they should."
    
    scene labirinto
    show espelhopie: 
        ypos -200
    show espelhoarle:
        xalign 1.0
        yalign 0.3
    show espelhojes:
        xalign 0.2
        yalign 0.1
    show espelhobil:
        xalign 0.32
        yalign 0.3
    show espelhodoc:
        xalign 0.81
        yalign 0.1
    show espelhohum:
        xalign 0.7
        yalign 0.3
    with dissolve
    play music "audio/musicas/bil2.mp3" fadein 5.0 volume 0.25
    play sound "audio/efeitos/sussurros.mp3" fadein 1.0 volume 0.15 fadeout 1.0

    call screen labirinto_espelhos

    mcp "(It’s cold in here. And I can barely see anything beyond the reflections.)"
    mcp "(He tells me not to stop, but you can’t walk fast in this dark without smashing your face on a mirror.)"


label espelhop:
    hide screen labirinto_espelhos
    scene espelhop with dissolve
    show mc with dissolve
    pause 0.2
    play sound "audio/efeitos/efeitosus.mp3" volume 0.2

    show mcreflexop with dissolve

    play sound "audio/efeitos/sussurros.mp3" fadein 1.0 volume 0.15 fadeout 1.0
    mc "What a creepy trick."
    
    mcp "(There’s nothing behind me, but I can almost feel something warm right next to me. Like the mirror shows.)"

    narrator "{cps=30}{color=#ffaf54}Ahh.. [titulo_pierrot]."
    show mcreflexop2 with dissolve
    hide mcreflexop

    mc "Pierrot?"

    narrator "{sc=2}{cps=30}{color=#ffaf54}Can we be together forever!!"

    scene mcreflexop3 with dissolve

    narrator "{sc=3}{cps=30}{color=#ffaf54}Wouldn't you want that? Just you and me, {b}together."
    narrator "{sc=3}{cps=30}{color=#ffaf54}Please say yes."
    narrator "{sc=3}{cps=30}{color=#ffaf54}Please let me hear your sweet voice say it."
    narrator "{sc=3}{cps=30}{color=#ffaf54}Stay with me."
    narrator "{sc=3}{cps=30}{color=#ffaf54}Please [titulo_pierrot]."

    show reflexomp with dissolve
    pause 0.2
    play sound "audio/efeitos/espelhoquebrado.mp3" volume 0.3
    show espelhopquebrado with vpunch 

    mc "!!!"
    mc "I recognize that knife."

    play sound "audio/efeitos/rosnado1.mp3" volume 0.2
    pause 0.5

    mc "I can’t stop."
    scene black with dissolve
    play sound "audio/efeitos/sussurros.mp3" fadein 1.0 volume 0.15 fadeout 1.0

    jump labirinto_loop

label espelhoa:
    scene espelhop with dissolve:
        xzoom -1.0
    show mc with dissolve:
        xpos 90
    pause 0.2

    mcp "(What a cold shiver.)"
    hide mc
    play sound "audio/efeitos/efeitosus.mp3" volume 0.2
    show mcreflexoa with dissolve

    mc "I know those eyes."
    play sound "audio/efeitos/sussurros.mp3" fadein 1.0 volume 0.15 fadeout 1.0

    narrator "{color=#41d623}You, are you really going to let me come close?"
    hide mcreflexoa
    show mcreflexoa2 with slowdissolve
    
    narrator "{color=#41d623}Do you like my warmth? I can see it in your eyes, what you think of me."

    if convite_aceito or toquegentil == True:
        show olhoaespelho with dissolve
    narrator "{color=#41d623}{size=40}{cps=40}...{nw=0.5}"
    narrator "{color=#41d623}Why are you looking at me like that?"

    hide olhoaespelho with slowdissolve
    show mcreflexoa3
    play sound "audio/efeitos/mordida.mp3" volume 0.2
    pause 0.05
    hide mcreflexoa3
    pause 0.05
    show mcreflexoa3
    hide mcreflexoa2

    mc "{cps=15}..."
    play sound "audio/efeitos/sumir.mp3" volume 0.2
    hide mcreflexoa3 with dissolve

    mc "This place gives me the creeps."
    scene black with slowdissolve

    jump labirinto_loop
        
label espelhoj:
    scene espelhoj
    if espelhos_usados["p"]:
        show espelhoquebradop
    with dissolve
    play sound "audio/efeitos/efeitosus.mp3" volume 0.2
    show reflexoj with dissolve

    narrator "{color=#961ee6}A pet? Why would he want a creature this troublesome? Tsk."
    narrator "{color=#961ee6}Look at you, so {b}weak{/b} on your own."
    narrator "{color=#961ee6}You’ve been lucky so far."
    narrator "{color=#961ee6}But luck is a fickle thing. It always runs out, eventually."
    show reflexojester with dissolve

    narrator "{color=#961ee6}And when that day comes, huhum... I’ll have my {i}fun."
    play sound "audio/efeitos/sumir.mp3" volume 0.2
    scene black with slowdissolve

    jump labirinto_loop

label espelhod:
    scene espelhod with dissolve
    play sound "audio/efeitos/efeitosus.mp3" volume 0.2
    show reflexod with dissolve

    narrator "{color=#e74c3c}I’d love to examine this specimen."
    narrator "{color=#e74c3c}I wonder how much this one can endure."
    if fala_noespelhododoc == True:
        narrator "{color=#e74c3c}You walked into my tent with such boldness."

    play sound "audio/efeitos/olhosdoc.mp3" volume 0.2
    show reflexod2 with dissolve
    hide reflexod 
    narrator "{color=#e74c3c}I bet you can handle high doses of adrenaline."
    narrator "{color=#e74c3c}Let me run a few tests. It’ll be… entertaining."
    narrator "{color=#e74c3c}How far can I push before you finally beg?"
    show reflexod3 with dissolve
    hide reflexod2
    narrator "{color=#e74c3c}Or perhaps your heart will give out first, like the other {b}dolls."

    mc "Dolls..."
    play sound "audio/efeitos/sumir.mp3" volume 0.2
    scene black with dissolve
    jump labirinto_loop

label espelhoh:
    stop music fadeout 2.0
    scene espelhoh with dissolve
    mcp "This one’s broken, kind of melted and it reflects words that aren’t written anywhere in the tent."
    play sound "audio/efeitos/risadashorror.mp3" volume 0.2
    show screen vozes_glitch
    pause 0.5
    play music "audio/efeitos/fogo.mp3" fadein 1.0 volume 0.3
    show reflexoh0 with dissolve
    pause 0.2
    show fogonoparquinho with hpunch
    hide reflexoh0

    mcp "(Where is that... noise coming from?)"
    mcp "(It smells like something’s burning, really strong.)"
    stop music fadeout 1.5

    hide fogonoparquinho with dissolve

    mcp "(I need to get out of here.)"
    hide screen vozes_glitch with dissolve
    stop sound fadeout 1.0
    scene black with dissolve

    play music "audio/musicas/bil2.mp3" fadein 5.0 volume 0.25

    jump labirinto_loop

label insistente:
    scene espelhoh with dissolve

    if visitas_espelhoh == 3:
        b "Why do you keep coming back to this broken mirror?"
        b "Rather... sadistic of you, isn’t it?"
        b "Do you enjoy the smell of burning flesh?"
        b "{cps=20}I’m getting closer, guest."
    elif visitas_espelhoh >= 4:
        b "Closer..."
    play sound "audio/efeitos/rosnado2.mp3" volume 0.3
    scene black with dissolve
    pause 2.5
    jump labirinto_loop

label espelhob:
    scene espelhod with dissolve:
        xzoom -1.0
    play sound "audio/efeitos/efeitosus.mp3" volume 0.2
    show bespelho with dissolve

    b "{cps=50}You’re an interesting guest.{w=0.2} I told you not to stop,{w=0.2} yet you wanted to look at every mirror."
    show bilreflexo with dissolve
    
    b "So... the monster caught up to you."
    scene espelhod with dissolve:
        xzoom -1.0
    show reflexob2
    show b 2 with dissolve

    play sound "audio/efeitos/rosnado2.mp3" volume 0.3
    narrator "You feel warm breath against your neck."
    b "{b}Don’t."
    play sound "audio/efeitos/vidro.mp3" loop volume 0.2
   
    show misterioso with dissolve

    b"Don’t look back,{w=0.2} {i}trust me."


    menu:
        "Obey.":
            stop sound 
            hide misterioso with dissolve
            hide b 2
            show bil 2 with dissolve
            
            b "Perfect. I like that you’re obedient, you know your place here."
            b "You’ll be just fine."
        "Turn around.":
            stop sound
            hide misterioso with dissolve
            hide b 2
            show bil mau with dissolve
            show olhobilmau at olhospulse
            show olhobil at fadeolhojes:
                xpos -200
                ypos -100
            play sound "audio/efeitos/pegar.mp3"
            narrator "You feel something enormous grab your head, forcing it forward. {color=#c90c0c}You can’t move." with hpunch
            
            b "I despise{cps=40} the disobedient.{w=0.2} You’re lucky I can’t hurt you."

            hide olhobilmau
            show olhobilmau at olhobilmaupos
                
            play sound "audio/efeitos/guizo.mp3" volume 0.3
            b "{cps=99}Stop right there."
            b "{cps=65}I’m watching you. Step back,{w=0.2} we’re only talking. It depends on you.{w=0.2}"
            b "Don’t you trust me?"
            play sound "audio/efeitos/guizo.mp3" volume 0.3
            mc "What...?"
            hide olhobil
            show olhobilmau:
                xalign 0.5
                yalign 0.5
            play sound "audio/efeitos/rosnado3.mp3" volume 0.2
            b "Quiet. I’m not speaking to you."

            hide olhobilmau
            show bil 2 with dissolve
            play sound "audio/efeitos/pegar.mp3" volume 0.5
            b "Very good."
            b "{cps=50}Now, where were we?{w=0.3}{cps=10} Ah, yes."
            show bil mau with dissolve
            show olhobilmau
            show olhobil with dissolve:
                zoom 0.5
                xpos 440
                ypos 120
            b "Be polite and keep your eyes on me.{w=0.2} We’re having a conversation."
            narrator "You feel your head released."
    
    hide olhobil
    hide olhobilmau
    hide bil 2 
    show b 2 with dissolve
    play sound "audio/efeitos/vidro.mp3" loop volume 0.2
    show misterioso with dissolve
    play sound "audio/efeitos/pegar.mp3" volume 0.5
    pause 0.2
    play sound "audio/efeitos/vidro.mp3" loop volume 0.2
    narrator "Heavy claws pressing down on your shoulder."
    
    mc "{sc=1}What is touching me?"

    b "An illusion."

    mc "{size=50}{cps=15}..."
    hide misterioso with dissolve
    hide b 2
    show bil 2 with dissolve

    stop sound 
    b "This is the part where the other visitors usually say, {i}“What an impressive trick.”"
    b "But not you, right, guest? Your eyes, doubt."

    show bil mau with dissolve
    show olhobilmau
    b "Hah, I suppose by now that doesn’t work on you anymore, does it? That’s fine."

    hide olhobilmau
    show bil maop with dissolve
    play sound "audio/efeitos/pegar.mp3" volume 0.5
    b "It’s me,{w=0.5} guest. I just want to see you a little closer."
    b "After all, not everyone makes it this far. But there’s no need to tremble, {i}I don’t bite."

    mcp "(His voice, it sounds like it’s coming from behind me.)"

    show bil costas with dissolve

    b "I think I’ll keep an eye on you as well."
    b "You can keep going, the mirror at the end of the hall is my personal favorite."
    b "It’s intense."

    play sound "audio/efeitos/sumir.mp3" volume 0.2
    scene espelhod with dissolve:
        xzoom -1.0
    pause 0.1

    scene black with dissolve

    jump labirinto_loop

label espelhoc:
    stop music fadeout 5

    scene espelhoc with dissolve

    pause 0.2
    show reflexoc with dissolve
    show olhosc at olhospulse2

    mcp "(Is this... really a mirror? It’s freezing in front of it.)"
    mcp "(And those eyes, they look like they’re following me.)"

    mc "Hello?"
    mc "Can I leave now? Ticket guy?"
    play music "audio/musicas/suspense.mp3" volume 0.3

    narrator "{sc=2}{color=#e61ee6}{cps=10}{size=45}Come closer.{w}{cps=0} Come closer. Come closer. Come closer. \nCome closer. Come closer. Come closer. Come closer.{nw=0.5}"

    menu:
        "{color=#e61ee6}Run away.":

            $ olhos_fechados_paraela = True
            scene fimdatendab with dissolve
            stop music
            stop sound
            jump semcoragem_paraoespelho

        "{color=#e61ee6}Come closer.":
            scene espelhoc with dissolve:
                zoom 2.0
                xalign 0.5
                yalign 0.0

            show reflexoc2:
                zoom 2.0
                xalign 0.5
                yalign 0.0
            show olhosc:
                zoom 2.0
                xalign 0.5
                yalign 0.0

            pause 0.3

            mc "What--"
        
            play sound "audio/efeitos/golpe.mp3"

            show screen maoc with hpunch

            scene reflexoc2 at zoomcolu:
                zoom 2.0
                xalign 0.5
                yalign 0.0

            pause 0.2
            scene black
            hide screen maoc
    
label cenaoculta2:
    $ persistent.unlocked_scenes["cena_02"] = True
    if not "_from_gallery" in globals():
        $ _from_gallery = False
    scene espelhocbg with dissolve
    play music "audio/musicas/colombina.mp3" fadein 1.5 volume 0.3

    show reflexocolu with dissolve
    show hmns 1 with dissolve:
        xalign 0.7
        yalign 0.5

    show riscos:
        xalign 0.7
        yalign 0.5


    des "{b}She’s pretty, even though she’s one of them."
    des "{b}You’re right."
    des "{i}And if..."

    play sound "audio/efeitos/efeitosus.mp3" volume 0.3
    show reflexopcolu with dissolve
    show reflexoctrupe with dissolve

    show hmns 2 at deslizar_hmns

    show riscos at deslizar_hmns
    show reflexocolu with dissolve:
        xpos 900
    
    des "That one’s a problem."

    scene black with slowdissolve

    des "{b}{size=35}Well, teach him some manners."

    play sound "audio/efeitos/golpecortante.mp3"
    pause 0.3
    play sound "audio/efeitos/golpecortante.mp3"
    pause 0.3
    play sound "audio/efeitos/golpecortante.mp3"

    show sanguefeito with hpunch
    pause 0.3

    scene gaiolas with dissolve
    pause 0.5
    scene black with dissolve

    narrator "{color=#961ee6}Maybe he’ll be the first to fall."
    narrator "{color=#961ee6}And then one by one we’ll wither away in this pit {glitch=2}{sc=80}{color=#41d623}A.Q.RLE{/glitch}"
    narrator "{color=#961ee6}I will, feed him."
    narrator "{color=#41d623}... Wait."

    play sound "audio/efeitos/correntes2.mp3"
    scene gaiolas2 with dissolve
    pause 1.0

    des "One more."

    scene black with dissolve

    narrator "{color=#e61ee6}I’m scared. If they try to touch me again..."
    narrator "{color=#e61ee6}Will you save me?"
    narrator "{color=#41d623}Save...?"

    des "Tomorrow, we’ll {i}relocate{/i} her. The others, we’ll let them starve."
    des "They’re too dangerous to keep."
    des "You’re right, we won’t risk it. She’ll be useful for something."

    scene gaiolas3 with dissolve

    narrator "{color=#4153f7}Moonless night."
    narrator "{color=#e74c3c}Maybe this will be our last one."
    narrator "{color=#e74c3c}I'm so hungry."
    narrator "{color=#4153f7}Me too... how long has it been... since we last ate?"
    play sound "audio/efeitos/correntes2.mp3"
    narrator "{color=#961ee6}I can’t move.{glitch=2}{sc=70}{color=#ffaf54}/P.TOR{/glitch}{/sc}{color=#961ee6} is alive...?"
    narrator "{sc=1}{cps=15}{size=35}{b}{color=#ffaf54}......"
    play sound "audio/efeitos/barrametal.mp3"
    scene gaiolas4 with dissolve
    narrator "{sc=1}{color=#e61ee6}I’m scared."
    narrator "{color=#41d623}You’re the weakest one."
    narrator "{sc=2}{color=#e61ee6}Thank you."

    
    scene mord1 with dissolve
    pause 0.05
    play sound "audio/efeitos/desmembrar.mp3"
    scene mord2 with vpunch
    pause 0.1
    scene black

    narrator "{sc=1}{color=#4153f7}Why... did you do that?"
    narrator "{color=#961ee6}There’s no turning back now."
    narrator "{sc=1}{color=#ffaf54}No... {sc=3}{color=#ffaf54}no... {sc=5}{color=#ffaf54}no..."

    scene insan1 with dissolve
    pause 0.1
    show insan2 
    pause 0.1
    scene black

    narrator "{color=#41d623}{b}{size=45}EAT!"
    narrator "{sc=1}{color=#ffaf54}Why... are you smiling?"
    narrator "{color=#e61ee6}No."
    narrator "{sc=5}{color=#41d623}Hah...{w}HaHahhhahahahha!"
    narrator "{sc=8}{color=#41d623}{b}HAHAHHAHAHHAHAHAHHHHAAAHHH!"
    narrator "{color=#961ee6}Sorry... {glitch=2}{sc=80}{color=#41d623}A.Q.RLE."

    stop music
    narrator "{color=#e61ee6}He wasn’t..."
    pause 1.0

    play music "audio/musicas/bilheteiro.mp3" fadein 30.0 volume 0.05 #desligar aqui quando navegador ativo
    scene reflexocpos with slowdissolve:
        zoom 1.1
        xalign 0.5
        yalign 0.5
    
    show abrir_olhos
    pause 0.71
    hide abrir_olhos
    
    show reflexocpos at groggy_shake:
        zoom 1.1
        xalign 0.5
        yalign 0.5
   
    narrator "Your eyes burn, like you haven’t blinked in a long time."
    narrator "{color=#e61ee6}Thank you."
    narrator "{color=#e61ee6}It’s been so long."
    narrator "{color=#e61ee6}Each one of them crafted their own shield, when remembering that day."
    narrator "{color=#e61ee6}To protect themselves, each in their own distorted way."
   
    narrator "{color=#e61ee6}I just wanted to tell someone."
    scene frame1c with dissolve
    pause 0.2

    play movie "images/aleatorio/obrigada.webm"
    #$ renpy.movie_cutscene("images/aleatorio/obrigada.webm") #para navegador
    scene reflexocpos2

    mc "{sc=2}My god..."
    scene reflexocpos3 with dissolve

    mc "{sc=1}what does that even mean?"

    if _from_gallery:
        window hide
        stop music fadeout 1.0
        stop sound
        hide screen say
        show black with dissolve
        $ _from_gallery = False
        $ renpy.call_screen("cenas_ocultas")
        return

        
label semcoragem_paraoespelho:
    if olhos_fechados_paraela == True:
        scene fimdatendab with dissolve

    else:
        scene fimdatenda with dissolve
    
    mc "The exit!!"

    if olhos_fechados_paraela == True:
        scene fimdatendab at zoom_saidadoespelho 
        pause 0.5

    else:
        scene fimdatenda at zoom_saidadoespelho
        pause 0.5
    scene tendaazul with dissolve

    play music "audio/musicas/circo.mp3" fadein 3.0 volume 0.2
    
    mc "{sc=1}What was all that?..."

    show bilheteiro with dissolve

    b "Congratulations, you made it, guest. You reached the end of my tent."

    mc "{b}You!!{/b}{w=0.3} You were in there, weren’t you!?"

    hide bilheteiro
    show b 2 with dissolve

    b "Hahaha..."
    b "{i} \"Don’t trust your eyes.\" "

    mc "It felt too real to be an illusion!" with hpunch

    hide b 2 
    show bil costas with dissolve
    b "Thank you for entertaining me."
    b "{cps=15}Red ticket guest."

    hide bil costas with dissolve

    mc "And he’s gone."

    narrator "You take a deep breath, trying to calm yourself down."

    jump tendas1
      
label tenda_preta:

    if visitas_preta == 0:
        scene tendapreta
        show clientesespeciais
        with dissolve
        $ visitas_preta += 1

        mcp "(Maybe it’s something VIP, there’s a short line, and they all have black tickets, I think?)"
        mcp "(But wow, even the shortest ones there are still taller than me.)"

        des "{size=35}Damn, look at those weirdos!" with vpunch
        des "You think the circus is hiring more freaks?"
        des "HHAH!"

        show bilheteiro with dissolve:
            xalign 0.0

        b "Hello there, guest with the red ticket. I’m sorry, but as I’ve said before."

        hide bilheteiro
        show b 2 with dissolve:
            xalign 0.0
        b "Your ticket doesn’t allow entry into this area."

        mc "Right, right. I’m leaving."

        scene circo with slowdissolve

        mcp "(He didn’t take his eyes off me until I actually walked away.)"

        jump tendas1

    elif visitas_preta == 1:
        scene tendapreta
        show clientesespeciais
        with dissolve
        $ visitas_preta += 1

        show bil 2 with dissolve

        b "You... heard what I said before, right?"
        b "{b}{cps=20}Your ticket doesn’t allow entry into this tent."

        mc "Ah! right, got it, got it. I was just... uh."
        mc "How can I get that kind of ticket?"
        b "They’re already sold out. Please, return to the common area."

        mc "Right, sorry."
        jump tendas1

    elif visitas_preta == 2:
        $ visitas_preta += 1
        show tendapretaconv 
        if arlequim_ficanoquarto == True:
            show arlequinzinho
        if pierrot_ficanoquarto == True:
            show pierrotzinho
        with dissolve
        
        b "Sorry, I couldn’t get rid of the bag in time."
        j "I noticed, believe me."
        j "But don’t worry, old friend, we always find a way."
        j "You did a great job with what you could. Now keep your eyes open..."
        play sound "audio/efeitos/efeitosus.mp3" volume 0.5
        show tendapretaconv2
        hide arlequinzinho
        hide pierrotzinho
        if arlequim_ficanoquarto == True:
            show arlequinzinho
        if pierrot_ficanoquarto == True:
            show pierrotzinho
        j "Especially{cps=10} for little curious mice..."
        
        mc "!!!"
        jump tendas1

    else:
        show tendapretaconv3 with dissolve
        mcp "(It looks empty now.)"

        jump tendas1

    
label sobrevivente:
    scene tendasnoite with dissolve

    mcp "(What was all that? I felt such an intense sense of threat… just like Pierrot said.)"
    mcp "(Maybe if I knew a bit more, I… I feel like I wouldn’t have walked out of any of those circus tents… I should just leave.)"

    play sound "audio/efeitos/pegar.mp3" 

    scene black with hpunch
    pause 0.5
    mc "???"
    scene abracop with slowdissolve
    pause 0.2
    scene abracop2 with dissolve

    play music "audio/musicas/comele.mp3" fadein 15 volume 0.1
 
    p "My apologies, [titulo_pierrot]. I didn’t mean for you to scream."

    scene abracop3 with dissolve
    play sound "audio/efeitos/guizo.mp3" volume 0.5
    mc "Pierrot..."

    show olho abra1 with dissolve

    p "I’m sorry, [mc_nome], for dragging you into all of this. I never meant to involve you but..."
    show olho abra2 with dissolve
    pause 0.1
    show olho abra2 at olhos_pulsando   #at olhospulse   tilt_olhos 

    p "I’m incapable of staying away from you. Even if it’s to protect you, I simply can’t."
    p "But I promise you, if you stay with me, I won’t let anything bad happen to you."

    mc "I..."

    scene abracop4 with dissolve
    play sound "audio/efeitos/pegar.mp3" volume 0.1
    p "It’s alright, [titulo_pierrot]. You don’t need to answer me now."
    p "You’re scared I can wait."

    scene abracop5 with dissolve
    p "Ohh... Your scent... it’s exquisite."

    mc "Uh... hah!"
    play sound "audio/efeitos/guizo.mp3" volume 0.5
    scene abracop3 with hpunch

    p "F-forgive me!"

    mc "Pierrot, aren’t you mistaking me for someone else? We just met..."
    play sound "audio/efeitos/pegar.mp3" volume 0.1
    scene abracop4 with dissolve
    p "No, [titulo_pierrot], you’re something new in my life, you made my heart beat differently."
    p "I know who you are, and I want to know... more."
    p "Even if we belong to different worlds... I can’t help but love you."

    scene abracop6 with dissolve

    mc "Why?"

    p "Because you, are {b}you."
    p "I can feel it, and nothing in this world could be more real than that."
    p "{cps=50}You are my destiny."

    mc "..."

    p "I’ll let you return home, [titulo_pierrot]. Please, go safely."
    p "I must stay behind to make sure everything is under control."

    scene abracop4 with dissolve

    mc "You really are intense all the time, huh?"

    p "Until tomorrow, [titulo_pierrot]."

    mc "Good night, Pierrot."

    p "Good night, [mc_nome]."

    scene black with dissolve

    stop music fadeout 2.5
    narrator "You take your way home, reflecting on the exhausting day."

    scene cidadenoite with dissolve
    play music "audio/musicas/suspense.mp3" fadein 1.5 volume 0.5
    mcp "(This time, it wasn’t a question, he just said he’d come tomorrow.)"
    mcp "(Which means, no matter what I said at this point, he’d come to me anyway.)"
    mcp "(And… I think I like that.)"
    show cidadenoite2 with dissolve
    pause 0.2
    hide cidadenoite2
    pause 0.1
    show cidadenoite2
    pause 0.1
    mc "!!!"
    mc "Damn..."
    
    mcp "(I’d better hurry...)"

    scene cidadenoite3 with dissolve

    narrator "You feel something heavy as you walk, though you’re not sure if it’s the eerie atmosphere of the circus..."
    show sombrasfim with dissolve
    narrator "Or the weight of new eyes watching you in the dark."

    scene black with slowdissolve
    stop music fadeout 5.0

label fimdejogo:

    show text _("{size=80}{font=Freakshow.ttf}End of Chapter 1") as chapter_end at Position(xalign=0.5, yalign=0.4) with dissolve
    pause 0.2
    show text _("{size=40}Stay tuned for upcoming updates on the official website:\n{a=https://garula.itch.io/the-freak-circus}https://garula.itch.io/the-freak-circus{/a}") as chapter_info at Position(xalign=0.5, yalign=0.55) with dissolve

    pause
    #jump ama
    call screen creditos with dissolve

label cenaoculta1:
    play music "audio/musicas/sonho.mp3" volume 0.1
    scene tendaroxa1 with dissolve
    show jes idle with dissolve:
        xalign 0.7

    j "Bil."

    show bilheteiro with dissolve:
        xalign 0.0
        ypos 100

    b "Yes?"

    j "Keep an eye on our visitor, will you?"

    hide bilheteiro
    show bil maop with dissolve:
        xalign 0.0
        ypos 120

    b "With pleasure, Jester."

    j "Harlequin."

    hide bil maop
    show b 2 with dissolve:
        xalign 0.0
        ypos 120
    show alado with dissolve:
        xpos 1100
        ypos 100
    a "Oh? No nicknames for me?"

    show olhob2 with dissolve:
        xalign 0.0
        ypos 120
    show jes inv with dissolve:
        xalign 0.45

    j "I know where your eyes are. Don’t make me remind you, {b}don’t{/b} break the rules."

    a "What do you take me for?"

    j "Too deceitful for me to trust your words."

    show alado at pulinho2:
        xpos 1100
        ypos 100 

    a "Such hypocrisy, Jester ♪"
    show alado with dissolve:
        xpos 1000
        ypos 100
    a "You think I don’t see that crooked smile behind your mask?"

    j "That little thing might be useful. Who knows."

    show doc ladod with dissolve:
        xalign 0.0

    doc "I agree. If we need to take extreme measures in the end, I want this one."

    if persistent.p_sujeito == "they":
        a "Hah, [persistent.p_sujeito]'ve got hungry eyes, curious about everything this circus breathes. So, if [persistent.p_sujeito] keep coming back to your tent."
    else:
        a "Hah, [persistent.p_sujeito]'s got hungry eyes, curious about everything this circus breathes. So, if [persistent.p_sujeito] keeps coming back to your tent."

    if persistent.p_sujeito == "they":
        a "You’ll keep your claws off [persistent.p_objeto], won’t you?"
    else: 
        a "You’ll keep your claws off [persistent.p_objeto], won’t you?"

    j "You’ve already forgotten that night, haven’t you, Harlequin? Need me to remind you that Pierrot’s claws are sharper?"
    j "He was tamed once, and you know it won’t happen again. Your poison isn’t stronger than him."

    a "Isn’t it? I’d love to find out."
    hide alado with dissolve

    doc "Good luck, Harlequin."

    hide doc ladod with dissolve
    hide b 2
    hide olhob2
    show bil mau with dissolve:
        xalign 0.0
        ypos 120

    show jes lado with dissolve:
        xalign 0.7 
    b "{i}Sighs."
    pause 0.2

    j "Those two are a real headache."

    scene black with slowdissolve
    stop music
    $ renpy.call_screen("cenas_ocultas")
    return


#label ama:

    #scene circo
    
    
    #mc "{color=#2f63f3}Oh, what a tricky question haha… well… maybe he doesn’t really have a preference, he just picks… like you’d choose a product at the store, I’d say. I think that’s the best way to put it."
    #show alado
    #show psad2
    #p "I suppose I’m not particularly fond of people who are unkind to one another."
    
    #pause 


screen creditos:

    add "balcaopi"
    add "coracoes" xpos -0 xzoom -1
    add Solid("#000000C0")
    
    vbox:
        xalign 0.5
        yalign 0.03
        spacing 6
        ysize 240
        text _("Thank you for the support!") size 48 xalign 0.5
        text _("{size=30}{i}Max tier Patreon Pierrot's Love") xalign 0.5 yoffset -20
        text _("{color=#d31507}Lovestruck:") size 70 xalign 0.5 yoffset -25

    frame:
        background None
        xalign 0.5
        yalign 0.8
        ysize 800
       
        hbox:
            spacing 80
            xalign 0.5
            
            vbox:
                style_prefix "pierrot" 
                spacing 10
                #ypos 0.12
                yalign 0.0

                text "⭐ 水夜猫ヤーソ" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                text "⭐ 时一_SY" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                text "⭐ Amaya Orochi"
                text "⭐ Kar"
                text "⭐ GardenCorner"
                text "⭐ Wojtaz"
                text "⭐ Jet"
                text "⭐ Squiggles"
                text "⭐ SpeakNoEvil"
                text "⭐ Rachelliu"
                text "⭐ 白道" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                text "⭐ Lxiao"
                text "⭐ Rena"
                text "⭐ Ciph"
            vbox:
                style_prefix "pierrot" 
                spacing 10
                yalign 0.0

                text "⭐ Tazz"
                text "⭐ Darthsuki"
                text "⭐ SquareRootofDestiny"
                text "⭐ Ramu Morei"
                text "⭐ Pierrot"
                text "⭐ copiklaGrogu"
                text "⭐ 켈쇼토" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                text "⭐ Underground Cosplays"
                text "⭐ XueYing {font=SiYuanHeiTiJiuZiXing-Regular-2.ttf}雪影猫"
                text "⭐ 一隻" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                text "⭐ Lanqy"
                text "⭐ 海鸦" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                text "⭐白身(Shiromi)" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                text "⭐ 咖啡掉水里了" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
            
            vbox:
                style_prefix "pierrot"
                spacing 10
                yalign 0.0

                text "⭐ Golden Soul"
                text "⭐ Iskana"
                text "⭐ Luna月月" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                text "⭐ Mister_Pavel"
                
            

    key "mouseup_1" action Show("creditos2", transition=dissolve) 

screen creditos2:
    add "balcaopi"
    add Solid("#000000dc")

    text _("{color=#f10a0a}⭐ Thank you for the support! ⭐") size 50 xalign 0.5 yalign 0.0
    text _("{size=30}{i}Patreon Supporters") xalign 0.5 yalign 0.06

    frame:
        background None
        xalign 0.5
        ypos 100
        
        hbox:
            spacing 80
            xalign 0.5
  
            vbox:
                #spacing 10
                style_prefix "nome"

                text "Yuki"
                text "Soufanity"
                text "CreativeMushroom"
                text "Lailuka"
                text "Maddie Ainsworth"
                text "TipsyonTea"
                text "Karma"
                text "dinaaaaaaaaa4ka"
                text "Aline"
                text "voiletrulez"
                text "Moonlight"
                text "InsanityWings"
                text "Mae"
                text "Kayla"
                text "Richu Arts"
                text "Leyna Gifford"
                text "mxboxleitner"
                text "Atheer.GM"
                text "Stinky"
                text "Doctor Handsum"
            vbox:
                style_prefix "nome"
                text "fleetingheroics"
                text "deadbait"
                text "Amber particles"
                text "fernsword"
                text "Timor"
                text "Felya"
                text "allie N"
                text "LostMoments"
                text "Umbrella"
                text "AlekiIsLost"
                text "Cowgirl03"
                text "mal"
                text "Lyrashar"
                text "Horrorkid Party Puppy"
                text "茉莉" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                text "GooblDoodl"
                text "Sxiao"
                text "Shelly"
                text "WhySoderpy31"
                text "Karrie Mist"

            vbox:
                style_prefix "nome"
                
                text "Arcanananas"
                text "Moon"
                text "Rachelliu"
                text "小浣熊"  font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                text "Erikuxy"
                text "Chelsea"
                text "Umbre_2"
                text "Mina"
                text "ttyeoktteok 뗙떡" font "NotoSansKR-Regular.ttf"
                text "Mugdie"
                text "Kat"
                text "StarryComet"
                text "Nina"
                text "ItsAnOmen"
                text "an alien"
                text "无名" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                text "Shinobu"
                text "Cxlxstial Bunny"
                text "kms"
                text "ConstantAnxiety"

            vbox:
                style_prefix "nome"

                text "Shi Yiling"
                text "16"
                text "Gooseschroom"
                text "Nana_lyd"
                text "Elegantly Wasted"
                text "Axel Elkins"
                text "Ren"
                text "Lizette"
                text "vmarlow"
                text "Sutaraito"
                text "Wawally"
                text "Freakster"
                text "Ar3na"
                text "Tulip Raindrop"
                text "KitKatelyn"
                text "Aoi"
                text "Malo Xi"
                text "Ayano Sano"
                text "Sammi Lu"
                text "Dustin Saylor"

            vbox:
                style_prefix "nome"
                
                text "Cc"
                text "Leire"
                text "Nana The banana"
                text "idk"
                text "Cryptic"
                text "Lilyn"
                text "Mic_ Doodles"
                text "Logan Mitchell"
                text "Alba"
                text "Oleander"
                text "Jirapat Utanwutipong"
                text "Skaro"
                text "Lazerstrike"
                text "HideouslySweet"
                text "Alisha Benskin"
                text "yuan"
                text "Veyra (hail the Frog)"
                text "Hydra710"
                text "Juli"
                text "Didiputter"
                text "NaNa"

    
    #key "mouseup_1" action [Hide("creditos2"), MainMenu()]
    
    key "mouseup_1" action [Hide("creditos2"), Show("creditos3")]
        
screen creditos3:
    add "balcaopi"
    add Solid("#000000dc")

    text _("{color=#f10a0a}⭐ Thank you for the support! ⭐") size 50 xalign 0.5 yalign 0.0
    text _("{size=30}{i}Patreon Supporters") xalign 0.5 yalign 0.06

    frame:
        background None
        xalign 0.5
        ypos 100
        
        hbox:
            spacing 80
            xalign 0.5
            vbox:
                style_prefix "nome"
                
                text "Moonpurr"
                text "Ensalada De palta"
                text "Сява"
                text "SmolGrump"
                text "X L"
                text "Stella Antonini"
                text "Natalie Green"
                text "Ara"
                text "Veyra"
                text "Akira 明" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                text "SqueeJay"
                text "Lulu"
                text "Nephtty"
                text "Irene Cordero"
                text "ChangKaiShek"
                text "juni"
                text "Teryn Bennett"
                text "Madeline Mitchem"
                text "Misfire"
                text "羽" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"

            vbox:
                style_prefix "nome"
                
                text "Lemon pomelo"
                text "Azurphra"
                text "Sveta"
                text "Pimpollito"
                text "Shaylla"
                text "FantasyGardens"
                text "Star"
                text "Hannah"
                text "Melissa Aston"
                text "Aixa R."
                text "Kitamu Latham-Sampier"
                text "Azzy!"
                text "RollingEevee"
                text "iwiwi"
                text "Vampire Kitten"
                text "Isabel"
                text "Clover"
                text "Rose"
                text "Owiecznosc"
                text "nightfall" 

            vbox:
                style_prefix "nome"
                
                text "Lvene"
                text "bri"
                text "Anonymous"
                text "Zeronine"
                text "NunuDieKatze"
                text "Maya Armas"
                text "Castaspell"
                text "Smallflower"
                text "Brooks"
                text "NyzenRose"
                text "Aphinya"
                text "無無" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                text "CaprisFree"
                text "Holly Anei"
                text "Mya"
                text "Cumqueefa"
                text "Looma"
                text "Syn"
                text "Katty"
                text "Raica" 

            vbox:
                style_prefix "nome"
                
                text "Selktin Mononoke"
                text "ArteofMist"
                text "MadMimes"
                text "Princess Sayu"
                text "BlueMoon1331"
                text "sae"
                text "sustoast"
                text "Abilolxoxo"
                text "Lyong"
                text "Estrella Munoz"
                text "Atheer"
                text "ali_N" 
                text "Unthorn"   #"verd3isonline"
                text "hermit"
                text "Isabel"
                text "Kaylee"
                text "Honey_Bunny"
                text "Melek90"
                text "Princey"
                text "Harvey Shuter"

            vbox:
                style_prefix "nome"
                
                text "Tobi"
                text "FrostDragon"
                text "sugarrys"
                text "Narruka"
                text "Tala Natsu"
                text "Najmah"
                text "Kadyn"
                text "ViryAngel"
                text "coldburns"
                text "Deathbysin" 
                text "Nyrk"
                text "Ashe"
                text "Eemeelee"
                text "Keyla Dragneel"
                text "ellie berger"
                text "Shiromi"
                text "愛門Lovedoor" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                text "S Fong"
                text "nyx_eclipse"
                text "Nia"

    key "mouseup_1" action [Hide("creditos3"), Show("creditos4")]

screen creditos4:
    add "balcaopi"
    add Solid("#000000dc")

    text _("{color=#f10a0a}⭐ Thank you for the support! ⭐") size 50 xalign 0.5 yalign 0.0
    text _("{size=30}{i}Patreon Supporters") xalign 0.5 yalign 0.06

    frame:
        background None
        xalign 0.5
        ypos 100
        
        hbox:
            spacing 80
            xalign 0.5
            vbox:
                style_prefix "nome"
                
                text "Ignis-Illudens"
                text "DemonfoxKyubi"
                text "ﾄｳ ﾕｲ" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                text "June"
                text "Local_Shrub"
                text "MikaRose"
                text "LoneWolf"
                text "あの時のポッポ" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                text "A Moorbs"
                text "Mia Monroy"
                text "Rubi Raccoon"
                text "たん じゅっ" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                text "kutwr"
                text "TH3PUPPET"
                text "Pi_v_ch"
                text "nur atiqahhh"
                text "PinsnNeedles"
                text "Camille" 
                text "Eruri"
                text "Yarli Martinez" #20
                
            

            vbox:
                style_prefix "nome"
                
                text "Venia Arulaq"
                text "Ming"
                text "pocomai"
                text "black vil"
                text "UDAGAWA"
                text "solezmt"
                text "Pumpkin"
                text "Agacia"
                text "Elizabeth Martinez"
                text "dedcoyt 343"
                text "Keisuke"
                text "Rivia :3"
                text "Ana"
                text "Kei Kurono"
                text "Strawberbun"
                text "Amber Milliron"
                text "GrimmHugs0"
                text "candleshadows" #18
                text "凝冰" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                text "。 爽" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                

            vbox:
                style_prefix "nome"

                text "cuti3g0r3"
                text "Tides"
                text "SunnyandSkelly"
                text "猫よりの柴犬" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                text "Ryu"
                text "そちぁ" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                text "URUHA"
                text "MoneyMongrel"
                text "Nikku"
                text "Charlotte Wienand Dain"
                text "Dani"
                text "Smogon69"
                text "Ali"
                text "WetandTiny"
                text "Tellitoby"
                text "Gigi Patino"
                text "Mitsuba"
                text "Mashiyath Haque"
                text "나 나" font "NotoSansKR-Regular.ttf"
                text "Shiva"

            vbox:
                style_prefix "nome"

                text "jinjin catnip"
                text "Antenora"
                text "无分" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                text "cuppacats"
                text "ShyFox1020"
                text "猩红" font "SiYuanHeiTiJiuZiXing-Regular-2.ttf"
                text "catnip–933"
                text "d.colorss"
                text "icarus"
                text "Rini"
                text "KitCat"
                text "YinYanChan"
                text "AllyCatx"
                text "Eren"
                text "Nalu"
                text "Hiro Shima"
                text "RazWare"
                text "WonkyWilly"
                text "Honey Bee"
                text "Yawningcat 1228"

            vbox:
                style_prefix "nome"

                text "Eclipse"
                text "Santana Star 654"
                text "Saephilim"
                text "Erika"
                text "VoidMoth"
                text "Malteada de Mango"
                text "Starshine"
                text "kit"
                text "Dumbibo"
                text "Kurona Queen"
                text "Nat"
                text "scalpel114"
                text "OrderBoi"
                text "Thesleepyvoid"
                text "Mocha"
                text "Freak"
                text "Swammy Wammy"
                text "GettiSpaghetti"
                text "Xander Sharp"
                text "Jack Hawke"


    key "mouseup_1" action [Hide("creditos4"), Show("creditos5")]

screen creditos5:
    add "balcaopi"
    add Solid("#000000dc")

    text _("{color=#f10a0a}⭐ Thank you for the support! ⭐") size 50 xalign 0.5 yalign 0.0
    text _("{size=30}{i}Patreon Supporters") xalign 0.5 yalign 0.06

    frame:
        background None
        xalign 0.5
        #ypos 100
        yalign 0.2
        
        hbox:
            spacing 80
            xalign 0.5
            vbox:
                style_prefix "nome"
                
                text "Pastellilapsi"
                text "Lacy"
                text "SinisterDud3"
                text "The Toymaker Clown"
                text "Hennelenne"
                text "citlali martinez"
                text "Becca Hillburn"
                text "Jun"
                text ""
                text ""
              
                #text  #20

    key "mouseup_1" action [Hide("creditos5"), MainMenu()]