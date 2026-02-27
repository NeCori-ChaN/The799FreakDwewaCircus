
define mc = Character("[mc_nome]")
define p = Character("Pierrot", color="#ffaf54", what_color="#ffaf54")
define a = Character(_("Harlequin"), color="#41d623", what_color="#41d623")
define d = Character(_("Unknown"))
define estranho = Character(_("Strange 1"))
define c = Character(_("Boss"), color="#b35c16", what_color="#b35c16")
define c1 = Character(_("Customer 1"))
define c2 = Character(_("Customer 2"))
define c3 = Character(_("Customer 3"))
define c4 = Character(_("Customer 4"))
define c5 = Character(_("Customer 5"))
define w = Character("Anchor: William B.", color="#54c9ff", what_color="#54c9ff")
define f = Character("Anchor: Fatima B.", color="#54c9ff", what_color="#54c9ff")
define m = Character(_("Woman"))
define b = Character(_("Ticket taker"), color="#4153f7", what_color="#4153f7") #2c1ee6
define des = Character("???")
define narrator = Character(what_color="#8faa7f")
define mcp = Character("[mc_nome]", what_color="#a0b0c0")

init python:
    nomes_com_cena_extra = ["columbina", "colombina"]
define slowdissolve = Dissolve(1.0)

label start:
    show screen site_oficial
    pause
    hide screen site_oficial
    
    # TUTORIAL

    show text _("{size=40}A few quick instructions:")
    pause 1.0

    narrator "Text in this color represents the protagonist’s narration and observations."

    narrator "{color=#a0b0c0}(Text in parentheses shows their thoughts and appears in this color.)"

    show text _("{size=50}Remember to adjust the game volume, some sounds might be louder.\nEnjoy the game!") with dissolve

    pause


    ########

    scene black
    pause 0.5
    show text  _("{size=45}What are your pronouns?"): 
        xalign 0.5 
        yalign 0.2 
    with slowdissolve
    call escolha_pronomes from _call_escolha_pronomes
    hide text
    
    show text _("What name is on your badge?") with slowdissolve

label nomes:
    call screen input_box

    if mc_nome == "":

        if persistent.p_genero == "feminino":
            $ persistent.mc_titulo = "mistress"
            $ mc_nome = _("mistress")
        elif persistent.p_genero == "masculino":
            $ persistent.mc_titulo = "master"
            $ mc_nome = _("master")
        else:
            $ persistent.mc_titulo = "sovereign"
            $ mc_nome = _("sovereign")

        if persistent.mc_titulo == "mistress":
            #BR
            if renpy.game.preferences.language == "portugues":
                $ mc_nome = _("Mestra")
            #CN
            if renpy.game.preferences.language == "chinese":
                $ mc_nome = _("小姐")
            #JP
            if renpy.game.preferences.language == "japanese":
                $ mc_nome = _("お嬢")


        elif persistent.mc_titulo == "master":
            #BR
            if renpy.game.preferences.language == "portugues":
                $ mc_nome = _("Mestre")
            #CN
            if renpy.game.preferences.language == "chinese":
                $ mc_nome = _("先生")
            #JP
            if renpy.game.preferences.language == "japanese":
                $ mc_nome = _("マスター")


        else:
            #BR
            if renpy.game.preferences.language == "portugues":
                $ mc_nome = _("Monarca")
            #CN
            if renpy.game.preferences.language == "chinese":
                $ mc_nome = _("大人")
            #JP
            if renpy.game.preferences.language == "japanese":
                $ mc_nome = _("主")

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
        jump nome_columbinad1
    if nome_invalido:
        $ mc_nome = ""  # limpa o nome atual
        jump nomes
    
    hide text with dissolve 

    mc "Another chilly day to head to work. The weather's been so all over the place lately..."

    scene cidade with dissolve

    play music "audio/musicas/calma.mp3" volume 0.3

    mc "Ugh, this again. They've been talking for a while about some traveling circus coming to town."
    mc "They’ve been around for three days, spamming the town with flyers and random stunts."
    mc "Their style is pretty eccentric, but honestly way better than those typical clowns with the colorful outfits."
    mc "Those ones give me the creeps with their red noses and tacky rainbow wigs."

    play sound "audio/efeitos/panfleto.mp3" volume 0.5
    show panfleto:
        xalign 0.5
        yalign 0.3
    with dissolve

    mc "The freak circus of horrors."

    d "Hey!! Get out of here weirdo!!"

    hide panfleto 

    play sound "audio/efeitos/soco.mp3" volume 0.5
    with hpunch
    
    scene chao with dissolve

    d "Ever since you guys showed up, people have been disappearing! Go back to whatever hellhole you crawled out of!"

    mc "{color=#a0b0c0}(People have been treating them harshly, but just because someone ran off with a lover doesn’t mean it’s the circus’s fault, right?)"
    mc "{color=#a0b0c0}(I mean, I didn’t really pay much attention to the news to get the full story anyway.)"
    mc "{color=#a0b0c0}(But apparently on their first day here, someone went missing, although there are rumors they ran off with a lover.)"

    d "I’m talking to you, you freak! Get out of our town!!"

    mc "{color=#a0b0c0}(Okay, that guy’s really crossing the line now!!)"

    menu:
        "Intervene":

            narrator "{color=#8faa7f}You put yourself in front of the man."
            mc "That’s enough! There’s no need to get violent! He’s just doing his job!"
            d "Working for the devil, maybe."
            mc "I’m calling the police if you keep this up."
            d "Screw that! Open your eyes. I hope they take you too!"
            narrator "{color=#8faa7f}The man walks away."

        "Yell at the man":

            mc "What do you think you’re doing? You can’t just attack someone like that! I’m calling the police!"
            estranho "Yes, that's right. You’re going way too far."
            d "Wake up, you idiots!! They’re the ones kidnapping people!"
            estranho "Stop with the paranoid nonsense. People go missing all the time."
            d "To hell with all of you!!"
            narrator "{color=#8faa7f}The man walks away."

        "Do nothing":
            $ final_rosa = True
            narrator "You watch the scene as the guy yells and kicks the clown. When a crowd starts to gather and watch, the man walks away."
            mc "{color=#a0b0c0}(Poor guy... I hope someone does something.)"
            jump trabalho

label ajudar:

    mc "Are you ok? I'll help you get up."

    scene cidade with dissolve

    show machucado with dissolve

    play sound "audio/efeitos/guizo.mp3" volume 0.5
    mc "{color=#a0b0c0}(Damn, he’s really tall!!)"
    mc "Some people are kind of hot-headed... better not get too close, you know?"

    narrator "{color=#8faa7f}He nods."

    menu:
        "Comfort him.":
            mc "Not everyone flips out like that guy. You’ll be fine, okay?"
            play sound "audio/efeitos/guizo.mp3" volume 0.5
            hide machucado
            show inclinado with dissolve

            narrator "{color=#8faa7f}He walks up and slowly tilting his head, watching you."
        
        "Offer a bandage.":
            $ curativo = True

            play sound "audio/efeitos/pegar.mp3" volume 0.5
            show expression Solid("#000000C0") as escurecer
            show curativo:
                zoom 2.0
                xalign 0.5
                yalign 0.0
            with dissolve

            mc "Here, I’ve got a bandage take it."
            mc "But if it still feels bad, you should see a doctor."

            hide curativo with dissolve
            hide escurecer with dissolve
            hide machucado
            show inclinado_corado with dissolve
            play sound "audio/efeitos/guizo.mp3" volume 0.5
            narrator "{color=#8faa7f}He walks up and takes the bandage while slowly tilts his head, watching you."

            mc "{color=#a0b0c0}(He seems excited about it)"

            play sound "audio/efeitos/guizo.mp3" volume 0.5
            hide inclinado_corado
            show machucado with dissolve

            pause 0.5

    mc "{color=#a0b0c0}(So silent.)"
    mc "Well, I gotta go or I’ll be late. Take care, okay?"

    narrator "{color=#8faa7f}You step back and give a small wave before heading on your way."

label trabalho:

    stop music fadeout 2.0
    play music "audio/musicas/cafeteria.mp3" fadein 2.0 volume 0.1
   
    scene cafe with slowdissolve

    pause 1.0

    show chefe with dissolve

    c "You got here just in time. It’s busier than usual with the cold."
    c "Start as soon as you can, Carol’s running late and I’ve been covering for her."
    c "The orders are already on the counter, please take them to the tables."

    mc "You covered her whole shift? Is she okay?"

    c "I couldn’t reach her. Maybe she’s not feeling well."

    mc "Got it, I’ll get started."

    c "Sure, thanks."

    hide chefe with dissolve

    call screen pratos

label tutorial:

    show expression Solid("#000000C0") as escurecer
    show text _("{size=50}Click on the tables to deliver orders") with dissolve
    pause
    hide text with dissolve

label trabalhando:

    scene cafe with dissolve

    if mesa1_concluida and mesa2_concluida and mesa3_concluida:
        jump posturno
    else:
        call screen mesas
        

label mesa1:

    scene cafe at zoom_mesa1
    pause 1.2

    mc "Good afternoon! Here’s your espresso and macchiato. Can I get you anything else?"

    c1 "Thanks, I was dying for some coffee."
    c2 "Did you see those flyers for the circus?"
    c1 "Yeah, weird, right? It’s been ages since a traveling circus came to town."
    c2 "And the clowns are so creepy..."
    c1 "Probably good for their marketing though..."
    c1 "Oh, sorry! Yeah, we’re all set, we don’t need anything else right now."

    mc "No problem! Just call me if you need anything."
    $ mesa1_concluida = True

    scene cafe with dissolve

    if final_rosa == False:
    
        show evento1

    narrator "{color=#8faa7f}You arrange the trays neatly before making your way to the next table."

    jump trabalhando

label mesa2:

    scene cafe at zoom_mesa2
    pause 1.2

    mc "Here you go, your hot chocolate."

    c3 "Thanks! I’ve really been craving something warm with this chilly weather."

    mc "It got cold all of a sudden, didn’t it?"

    c3 "Yeah, the weather’s all over the place. You leave the house with a jacket and an umbrella, and you still end up sweating by the end of the day, haha."

    mc "For real. If you need anything else, just let me know, okay?"

    c3 "Perfect!"

    $ mesa2_concluida = True

    scene cafe with dissolve
    if final_rosa == False:

        show evento2 with dissolve

    mc "Ouch! This coffee’s hot, I better get it to them quick."

    jump trabalhando

label mesa3:

    scene cafe at zoom_mesa3
    pause 1.2

    mc "A coffee with cheese bread, and a cappuccino with a brownie, right?"

    c4 "That’s right, thanks!"
    c5 "Hey barista, did you see the news?"

    mc "Hm? Not yet today, did something happen?"

    c5 "They're still talking about the one who disappeared."

    mc "Oh, wasn’t that the one who ran off with a lover or something?"

    c4 "No one really knows for sure."
    c5 "I just wanted to say... Be careful if you're leaving late, okay?"
    c5 "This place closes quite late, so... stay alert, alright?"

    mc "Will do. Thanks for the heads-up! And enjoy your coffee!"

    $ mesa3_concluida = True

    scene cafe

    if final_rosa == False:
        show evento3

    mc "It’s really sweet of them to care. Maybe I should start keeping an eye on the news sometimes."
    jump trabalhando

label posturno:

    show chefeserio with dissolve 

    c "Tsk. I’m sick of ripping those flyers off my window, don’t let anyone hand them out in here."
    c "And when you have a minute, go around and pick up the ones scattered around."

    mc "Got it!"
    mc "Hmn.. Some people are being kinda rude to the circus folks, don’t you think?"

    c "The way they act freaks people out. Best to keep them away, bad for business."

    mc "Understood boss."

    hide chefeserio with dissolve

    call screen panfletos 

label cliente_suspeito:

    mc "The customers just keep leaving these on the tables…"
    
    play sound "audio/efeitos/portaloja.mp3" volume 0.5
    pause 1.5
    mc "Welcome!"

    d "Thanks! I’d like a strong, hot coffee."

    mc "I’ll bring it right away."

    scene black with dissolve
    pause 0.5
    play sound "audio/efeitos/prato.mp3"volume 0.5

    scene cafe:
        zoom 1.5
        xalign 0.9
        yalign 1.0 
    with dissolve
    show cliente:
        zoom 1.5
        xalign 0.9
        yalign 1.0 
    with dissolve
    mc "Here’s your coffee."

    d "Thanks. It’s really cold outside."
    d "What’s with those flyers?"

    mc "Oh, someone was handing them out. I had to pick them all up."

    d "How rude to do that in a place of business, right?"

    mc "Yeah, it just creates more work for everyone else."

    d "If you want, I can take them for you. I’ll toss them out when I leave no big deal."
    d "I was gathering some paper for recycling anyway."

    mc "Really? In that case, that’s better than just throwing them away, thanks."
    play sound "audio/efeitos/panfleto.mp3" volume 0.2

    d "No problems dear."

    mc "{cps=40}Do you need anyth--{nw}"
    d "Do you like the circus?"

    mc "Huh? Uh, I think I might be a little too old for that now."

    d "Nonsense. This circus isn’t for kids, they’ve got some pretty creepy stuff."

    mc "So you’ve been to the circus?"
    mc "{color=#a0b0c0}(Even though I don’t really like chatting with people, it’s part of my job to be polite. Still, it’s always a little uncomfortable when customers try to keep me talking.)"

    d "Are you even listening?"

    mc "Sorry?"

    d "Haha, thought so. Anyway, here take this."
    d "Go on, check it out, and then try telling me it didn’t give you chills."

    show expression Solid("#000000C0") as escurecer with dissolve
    show screen ingresso_rosa with dissolve

    mc "N-no! I can’t accept something like that."

    d "Don’t worry, I already went. I was thinking of going again, but I’ll be leaving town soon."

    if final_rosa == True:

        d "Come on, just take it. They’re for tonight."

        mc "W-well... I guess it’s okay."

        jump possivel_final_rosa

    d "Keep it, or sell it if you want."

    mc "Well..."

    hide screen ingresso_rosa with dissolve

    menu:
        "Take it":
            $ ingresso_rosa = True
            hide escurecer

            mc "Thank you, I might try to go one day."
            d "I’ll be glad to know someone used my ticket."

        "Decline":
            hide escurecer

            mc "That’s really kind, but I’m honestly not interested in the circus."
            mc "{color=#a0b0c0}(Or in accepting gifts from strangers…)"
            d "That’s a shame. I’ll try giving it to someone else, then."

label possivel_final_rosa:

    hide screen ingresso_rosa with dissolve
    hide escurecer with dissolve 
    d "Thanks for your time. I’ll let you get back to work."

    mc "Let me know if you need anything else!"

    scene balcao with dissolve

    show chefe with dissolve

    c "As soon as the last customers leave, close everything up and clean the place. We’re closing early today."

    mc "Did something happen?"

    show chefeserio with dissolve
    hide chefe with dissolve
   
    c "I have an unexpected appointment. And since you’re working alone today, I’d rather you didn’t leave too late."
    c "I’ve gotta go now, can you take care of everything?"

    mc "Yes! No problem, leave it to me!"

    c "Call me if anything comes up."

    mc "Will do. See you!"

    hide chefeserio with dissolve
    mc "{color=#a0b0c0}(Nice! Shorter work hours. But I hope Carol’s okay…)"

    d "Hey there, here’s the payment, I’m heading out."
    d "Have a good night!"

    mc "Good night, sir!"

    hide cliente with dissolve

    mc "{color=#a0b0c0}(Perfect! Now I just need to clean the tables and I’m out of here.)"

    if final_rosa == True:

        scene black with dissolve
        pause 0.5

        scene balcao with fade

        mc "Perfect! All clean, now I can go have a little fun."
        jump circo

label apagao:

    play sound "audio/efeitos/guizo.mp3"
    pause 0.5

    mc "Sorry, we’re...{w=0.5} closed."
    mc "Huh? But I heard the bell{cps=10}... Hello?"

    play sound "audio/efeitos/apagao.mp3" volume 0.5
    scene apagao with dissolve
    stop music fadeout 1.0

    mc "{color=#a0b0c0}(I’m not imagining things… Someone could be in here… and they turned off the lights? But I can see the switches from here…)"
    mc "Boss? Is that you?"
    narrator "{size=50}{cps=2}..."
    show paranoia at tilt_glitch
    play music "audio/musicas/coracao.mp3" volume 0.5
    mc "{color=#a0b0c0}(Right… calm down, I’m overthinking this. I’ll just go around the counter and turn them back on.)"
    mc "{color=#a0b0c0}(I can’t shake this feeling that I’m being watched…)"
    play sound "audio/efeitos/guizo.mp3"
    pause 0.5
    mc "{color=#a0b0c0}(Ok! Ok.... First, I’ll... )"

    menu:
        "Turn on the lights":
            hide paranoia 
            jump luzes
        "Pick up a knife":
            $ faca = True
            play sound "audio/efeitos/pegar.mp3"
            narrator "{color=#8faa7f}You take a small kitchen knife."
            
            mc "This makes me feel a bit safer. Now…"

            menu:
                "Check for intruder":
                    narrator "{color=#8faa7f}You carefully scan the store in silence, gripping a small knife in your hand."
                    narrator "{color=#8faa7f}You check under the tables and move toward the counter, but see no one."
                    hide paranoia with slowdissolve
                    mc "{color=#a0b0c0}(Whew… I think I’m just being paranoid.)"
                    mc "{color=#a0b0c0}(Now that I think about it… I heard the bell, but I never heard the door open.)"
                "Turn on the lights":
                    hide paranoia
                    jump luzes
label luzes:
    narrator "{color=#8faa7f}You run to the counter and try turning the lights back on."
    show apagao at zoom_luzes
    scene disjuntor with dissolve
    mc "Damn, it’s the breaker. Okay, stay calm... this is normal. It’s happened before."

    stop music fadeout 1.0
    
    play sound "audio/efeitos/botao.mp3" volume 0.1
    narrator "{color=#8faa7f}You open the panel and reset the breaker."

    scene balcao with dissolve

    mc "{color=#a0b0c0}(Phew, it was all in my head.)"

    play sound "audio/efeitos/portaloja.mp3" volume 0.5
    pause 1.5
    mc "{color=#a0b0c0}(Damn it, I should’ve locked the door.)"

    narrator "{color=#8faa7f}On high alert, you swiftly turn around as you speak once again."
    mc "Sorry, we’re closed!{w=0.2} Ah!! You’re the guy from earlier..."

    play sound "audio/efeitos/guizo.mp3"
    if curativo == True:
        show idlecurativo with dissolve
    else:
        show idlesangue with dissolve

    mc "Oh my, you’re bleeding! A-are you okay?"
    mc "{color=#a0b0c0}(Should I be worried about this guy? He kinda seems harmless… maybe 'cause he's always hurt.)"

    if faca and curativo:
        show inclinadocura with dissolve
        hide idlecurativo
        hide idlesangue
        play sound "audio/efeitos/guizo.mp3"
        narrator "{color=#8faa7f}He stares, curious, at the small knife in your hands."
        narrator "{color=#8faa7f}You smile awkwardly and put the knife away."
        mc "Ah! Hahaha.... Sorry."

    elif faca and not curativo:
        show inclinadosangue with dissolve
        hide idlecurativo
        hide idlesangue
        narrator "{color=#8faa7f}He stares, curious, at the small knife in your hands."
        narrator "{color=#8faa7f}You smile awkwardly and put the knife away"
        mc "Ah! Hahaha.... Sorry."

    elif curativo == True:
        hide idlecurativo
        show flor with dissolve
        mc "Awwn Thanks!"
        mc "Because of the bandage?"
        narrator "{color=#8faa7f}He nods."
        mc "{color=#a0b0c0}(It’s a really well-made paper flower, recently painted red. The paint’s still a little wet.)"
        mc "Still quiet..."

    hide flor with dissolve
    if curativo:
        show idlecurativo
    mc "Well..."

    menu:
        "Ask him to leave":
            mc "I… uhn... I don’t want to be rude, but you can’t stay here. I need to close up, and you might get me in trouble."
            if curativo == True:
                play sound "audio/efeitos/guizo.mp3"
                show sadcu with dissolve
                hide inclinadocura
                hide idlecurativo with dissolve
                hide idlesangue with dissolve
            else:
                play sound "audio/efeitos/guizo.mp3"
                show sadsangue with dissolve
                hide inclinadosangue
                hide idlecurativo with dissolve
                hide idlesangue with dissolve

            narrator "{color=#8faa7f}He gives a sad look and nods before heading out."
            hide sadcu with dissolve
            hide sadsangue with dissolve
            mc "{color=#a0b0c0}(Did someone hurt him again? He’s so tall… it’s strange how people aren’t afraid to mess with a guy like that.)"

            jump mandar_prafora

        "Help with the injury":
            $ conversap = True
            mc "Ugh, I hope I don’t regret this… Sit at the counter, I’ll help you with that."

            if curativo == True:
                hide inclinadocura
                hide idlecurativo
                play sound "audio/efeitos/guizo.mp3"
                show idlecurativo at pulinho
                pause 0.4
                show idlecurativo at zoom_sangue
            else:
                hide idlesangue
                hide inclinadosangue
                play sound "audio/efeitos/guizo.mp3"
                show idlesangue at pulinho
                pause 0.5
                show idlesangue at zoom_sangue

            pause 0.8
            scene black with dissolve
            
            mc "{color=#a0b0c0}(What a weird mask… actually, I’m not sure if it’s a mask or just a ton of makeup…)"

            play sound "audio/efeitos/pegar.mp3"
            narrator "{color=#8faa7f}You grab a paper napkin from the counter and gently wipe his face."

            if curativo == True:
                scene balcaopi with dissolve
            
            else:
                scene balcao with dissolve
                show inclinado_e_corado with dissolve

            mc "You don’t talk… or is that part of the act?"
            narrator "{color=#8faa7f}He seems to glance around before stepping a little closer."

            scene balcao with dissolve
            if curativo == True:
                hide idlecurativo
                show idlesocurativo:
                    xalign 0.5
                    yalign 0.2
                    zoom 1.7
                with dissolve
            else:
                hide inclinado_e_corado
                hide idlesangue
                show idle:
                    xalign 0.5
                    yalign 0.2
                    zoom 1.7
                with dissolve
            
            play sound "audio/efeitos/guizo.mp3"
            d "I can’t be seen talking."
            mc "Ah, so it’s part of the act!"

            d "Yes [titulo_pierrot]. I sincerely appreciate all your help."
            p "I’m the Pierrot nice to meet you!"
            mc "Nice to meet you! I'm [mc_nome]."
            p "{size=20}I know {nw=0.3}"
            mc "But, hm.. A Pierrot? You don’t really look like one."
            mc "Wait what?{nw=0.5}"

            p "{b}Indeed, you are right [titulo_pierrot]!"
            p "We were required to… modernize my attire. But my role, remains unchanged."

            mc "People have been pretty rough with you guys."

            if curativo == True:
                hide idlesocurativo
                play sound "audio/efeitos/guizo.mp3"
                show inclinadosocura:
                    xalign 0.5
                    yalign 0.2
                    zoom 1.7
                with dissolve
            else:
                hide idle
                play sound "audio/efeitos/guizo.mp3"
                show inclinado:
                    xalign 0.5
                    yalign 0.2
                    zoom 1.7
                with dissolve

            p "I suppose we may appear a touch… uncanny. That tends to unsettle people."

            mc "Do the Pierrots out on the street with the flyers perform too?"

            if curativo == True:
                hide inclinadosocura
                show idlesocurativo:
                    xalign 0.5
                    yalign 0.2
                    zoom 1.7
                with dissolve
            else:
                hide inclinado
                show idle:
                    xalign 0.5
                    yalign 0.2
                    zoom 1.7
                with dissolve

            p "Indeed. The circus has but a small cast, we both perform and hand out flyers."

            if curativo == True:
                hide idlesocurativo
                show revirarcurativo:
                    xalign 0.5
                    yalign 0.2
                    zoom 1.7
                with dissolve
            else:
                hide idle
                show revirar:
                    xalign 0.5
                    yalign 0.2
                    zoom 1.7
                with dissolve

            p "Though I must say, I am the only Pierrot, [titulo_pierrot]. The others are Jesters and... {w=0.3}{cps=20}Harlequins..."
            narrator "{color=#8faa7f}He pauses at the last part, rolling his eyes slightly."

            mc "{color=#a0b0c0}(Looks like he doesn’t get along with everyone.)"
            mc "That’s actually kinda cool! So, are the others quiet like you too?"

            if curativo == True:
                hide revirarcurativo
                show idlesocurativo:
                    xalign 0.5
                    yalign 0.2
                    zoom 1.7
                with dissolve
            else:
                hide revirar
                show idle:
                    xalign 0.5
                    yalign 0.2
                    zoom 1.7
                with dissolve

            p "I am the only one who remains silent."
            p "{i}Though I do make an exception when it’s just the two of us."
            mc "Got it. Your secret’s safe with me ♪"

            if curativo == True:

                mc "Hey, your bandage’s coming off. Let me take it off for you."
                mc "There we go!"

                hide idlesocurativo
                hide idle

                play sound "audio/efeitos/guizo.mp3"
                show inclinado_e_corado:
                    xalign 0.5
                    yalign 0.2
                    zoom 1.7
                with dissolve

            p "Thank you [titulo_pierrot]."


            p "And I’ve brought you another small token of appreciation."

            show expression Solid("#000000C0") as escurecer with dissolve
            show screen ingresso_vermelho with dissolve

            mc "A ticket!"
            hide screen ingresso_vermelho
            hide escurecer with dissolve

            if ingresso_rosa == True:

                mc "Don’t worry, I just got one."
                hide inclinado_e_corado
                play sound "audio/efeitos/guizo.mp3"
                show idle:
                    xalign 0.5
                    yalign 0.2
                    zoom 1.7
                with dissolve

                p "You... Obtained a ticket? May I see it, [titulo_pierrot]?"
                mc "Sure, here you go."

                play sound "audio/efeitos/guizo.mp3"
                hide idle
                show bravo:
                    xalign 0.5
                    yalign 0.2
                    zoom 1.5
                with dissolve

                mc "{color=#a0b0c0}(Hmn?)"
                narrator "{color=#8faa7f}He takes the ticket from your hands and holds it up in front of you."

                hide bravo with dissolve
                play sound "audio/efeitos/guizo.mp3"
                show magica:
                    xalign 0.5
                    yalign 0.5
                    zoom 1.8
                

                pause 0.8

                hide magica
                show 7:
                    xalign 0.5
                    yalign 0.5
                    zoom 2.0
                with dissolve

                mc "Whoa, cool trick! But why?"
                narrator "{color=#8faa7f}He places the ticket into your hands." #add

                hide 7
                show idle:
                    xalign 0.5
                    yalign 0.2
                    zoom 1.5
                with dissolve

                p "This ticket is incorrect. You wouldn’t be allowed in with it. Please, take mine instead."

                mc "Incorrect?... You mean it was fake?"

                p "Indeed, counterfeit. Do not accept tickets from strangers, [titulo_pierrot]. I would not want you to encounter trouble at the entrance."

                mc "Uh... right, thanks."
                mc "{color=#a0b0c0}(Why would that guy give me a fake one?)"

            else:
                mc "Are you sure? Won’t this get you in trouble?"

                p "Not at all. We have a few special ones to hand out."
                p "I’d be most delighted if you came to watch me, [titulo_pierrot]."

                mc "Hmm… alright, I’ll take it. Sounds fun, after all."

            p "I assure you, I’ll make you smile during my performance."

            mc "Can’t wait to see it! And sorry to say this, but..."
            mc "My boss told me to close up, we can’t stay too long here."

            hide inclinado_e_corado
            hide idlesocurativo
            hide idle
            play sound "audio/efeitos/guizo.mp3"
            show idle2:
                xalign 0.5
                yalign 0.2
                zoom 1.5
            with dissolve

            p "I completely understand. I had hoped to arrive earlier but, I did not wish to cause you any distress, [titulo_pierrot]."

            mc "{color=#a0b0c0}(Honestly, I can see why some folks would feel uneasy.)"
            mc "It’s alright. This way we got to talk a bit. Now I know you wouldn’t have been able to answer me in public."

            hide idle
            hide idle2
            play sound "audio/efeitos/guizo.mp3"
            show inclinado_e_corado:
                xalign 0.5
                yalign 0.2
                zoom 1.5
            with dissolve

            p "That’s true ♪"
            p "Have a good night, [titulo_pierrot]."

            mc "Good night!"

            hide inclinado_e_corado with slowdissolve
            mc "Well, time to go home."

            jump casa

label mandar_prafora:

    scene cafefora with dissolve

    if curativo == True:
        show idlesocurativo:
            xalign 0.5
            ypos -500
            zoom 2.5
        with dissolve
        with hpunch
        pause 0.3

        hide idlesocurativo
        show pitenso at susto
        play sound "audio/efeitos/guizo.mp3"
        pause 0.5
        hide pitenso
        show sad
    else:
        show idle:
            xalign 0.5
            ypos -500
            zoom 2.5
        with dissolve
        with hpunch
        pause 0.3

        hide idle
        hide idlesocurativo
        show pitenso at susto
        play sound "audio/efeitos/guizo.mp3"
        pause 0.5
        hide pitenso
        show sad
    
    mc "{b}Ahh!!"
    mc "You... you scared me!"

    if curativo == True:
        narrator "He jumps in surprise too, accidentally hitting himself as he raises his hands, sending his bandage flying."
        narrator "His eyes follow it for a moment before he gestures again, trying to calm you down."

    else:
        narrator "He jumps in surprise too, raising his hands as if trying to calm you down."

    mc "B-be careful, I could’ve hurt you."

    hide sad
    play sound "audio/efeitos/guizo.mp3"
    show inclinado_e_corado with dissolve

    narrator "He nods quickly and raises a finger, asking for a moment, then pulls a ticket from his clothes."

    hide inclinado_e_corado
    show 7 with dissolve

    mc "A ticket!"
    
    if ingresso_rosa == True:

        mc "Don’t worry, I just got one."
        show expression Solid("#000000C0") as escurecer with dissolve
        show screen ingresso_rosa with dissolve

        mc "See?"
        hide screen ingresso_rosa
        hide escurecer with dissolve
        hide 7

        play sound "audio/efeitos/guizo.mp3"
        show bravo with dissolve
      
        mc "{color=#a0b0c0}(Hmn?)"
        narrator "He takes the ticket from your hands and holds it up in front of you."

        hide bravo with dissolve
        play sound "audio/efeitos/guizo.mp3"
        show magica:
            xalign 0.5
            yalign 0.5
            zoom 1.8
            
        pause 0.8

        hide magica
        show 7:
            xalign 0.5
            yalign 0.5
            zoom 2.0
        with dissolve

        mc "Whoa, cool trick! But why?"
        narrator "He hands the ticket into your hands"

        mc "Ah, well... I guess that’s alright."

        hide 7
    
    else:
        mc "Is this for me?"

        narrator "He hands the ticket into your hands"

        hide 7
        show idle with dissolve

        mc "{color=#a0b0c0}(Well, I guess there’s no harm in accepting. He’s with the circus, so he must have a few extras.)"
        mc "Thanks! But won’t this get you in trouble?"

        narrator "He leans in slightly and gives a small shake of his head."

        mc "Well, alright. I guess I can stop by tomorrow."

        hide idle

    play sound "audio/efeitos/guizo.mp3"
    show idle at pulinho
    mc "{color=#a0b0c0}(He looks excited.)"
    
    mc "There's 'Pierrot' written by hand on the ticket. Is that your name?"

    narrator "He nods his head frantically."

    mc "Oh! Right, got it."

    mc "I should get going before it gets too late. Good night!"

    narrator "He bows again and gives [persistent.p_objeto] a warm smile as he waves."

    hide idle with slowdissolve

    mc "Well, time to go home."

label casa:

    scene quarto with dissolve

    mc "I got back earlier, but I still feel just as tired as on a normal day. At least my shift starts later tomorrow."
    mc "I'll take a quick shower and crash in bed."

    scene black with dissolve
    play sound "audio/efeitos/chuveiro.mp3" volume 0.5

    mc "I was unsure about the circus, but it might be fun. They have this kind of gothic and eccentric style, and the ticket was pretty expensive."
    mc "I hope it’s okay that I agreed to go."

    stop sound fadeout 2.0

    scene quartoaberto with dissolve

    mc "What a cold wind…"

    play sound "audio/efeitos/portacorrer.mp3" volume 0.5

    scene quarto with dissolve

    mc "Much better!"
    mc "So sleepy… I’ll just watch a bit of TV until I fall asleep…"

    scene quartoapagado with dissolve 

    show tv with dissolve

    show piscar with dissolve

    pause 1.5

    show expression Solid("#00000044") as escurecer

    window hide
    mc "Zzz"
    show estatica
    pause 0.5

    hide escurecer
    play sound "audio/efeitos/guizo.mp3" volume 0.2
    show closesorriso at zoomlento
    play music "audio/musicas/suspense.mp3" fadein 1.0 volume 0.3
    with fade

    p """
    
        {cps=50}Ah [titulo_pierrot],{w=0.5} You… 

        {cps=50}You are even more beautiful in your sleep.

        {cps=50}So fragile… so defenseless...

        {cps=50}You do not even know me… But I know everything about you.

        {cps=50}Every step you take, your routines, your preferences...
        
        {cps=50}Even the way your brow furrows when you are confused... or afraid.

        Ah... utterly adorable.

        """

    show close2 at zoomlento2
    with dissolve
    
    p """
        I knew the moment I saw you… today.

        {b}It was just a glance… but something inside me ignited, and now… 
        
        {b}There is no turning back.

        {b}There is nowhere left to run.

        I needed to see you with my own eyes…

        To be certain that you were real.

        {b}And you are.

        {sc=1}{color=#ffaf54}You must be mine.

        {sc=1}{color=#ffaf54}You will be mine.

        """

    show close2 at zoomrapido
    pause 0.1

    scene black
    stop music

label diaseguinte:
    scene black 
    pause 0.5
    scene quartodia with hpunch

    mc "!!!"
    mc "A nightmare? Wow… what a scare. I guess I was overthinking things yesterday."
    mc "Weird, I don’t remember turning off the TV last night. Was I that tired?"
    mc "{cps=10}..."
    mc "No, I definitely didn’t turn it off… And I have a strange taste in my mouth..."
    mc "Damn, I overslept!!" with vpunch
    mc "I’ll just leave something on the TV while I have breakfast and get ready for work."

    show tv

    w "The circus's popularity has been rising it's become the main event of the season!"
    f "Have you seen the show, William?"
    w "Absolutely! But it's really not for the whole family. It's unlike anything I've ever seen. People are weirded out by the clowns’ design, but they’re incredibly talented."
    f "I actually find them quite adorable. It's worth watching the performance."
    f "But be careful with the food at the stalls some have been shut down. Apparently, a few people were selling food illegally near the circus."
    w "Oh, that always ends up happening."

    mc "Time to go. I just need to find my bag."

    w "Now for a not-so-warm piece of news another girl went missing yesterday morning. She had family issues and never returned home. The family suspects she may have run away after an argument…"

    mc "Where is it, where is it?? I could’ve sworn I tossed my bag around here…"

    show not

    w "However, a bag with her belongings was found near the city bus station. Police are investigating the area."

    mc "Found it!!"

    hide not
    hide tv

    mc "Time to go."

label rua:
    play music "audio/musicas/calma.mp3" volume 0.1
    scene cidade with dissolve

    mc "Ugh, flyers everywhere again, are they polluting the whole city with these things?"

    show normal with dissolve
    d "Care to visit the circus? I bet you’ll be surprised ♪ {w=0.2} Here, take a flyer!"

    mc "No thanks, I already got a ticket."

    d "Oh! Wonderful!! You got one? {w=0.3}Was it{cps=10} a pink one,{w=0.5} then?"

    mc "{color=#a0b0c0}(He started following me... I should’ve just stayed quiet...)"
    mc "It was red, actually."

    hide normal with dissolve
    show frente 

    narrator "He stops in front of you, blocking your way."

    hide frente
    show frente2:
        zoom 1.3
        xalign 0.5
        yalign 0.5
    with dissolve

    d "A red one??"

    pause 0.3

    menu:
        "Ask to pass":
            mc "Excuse me, I don’t want to be late."

            scene cidade:
                zoom 2.0
                xalign 0.5
                yalign 0.5
            with dissolve 

            hide frente
            show normal at deslizar_direita
            narrator "He lets you through, but keeps following you."
        "Ignore him":
            narrator "You walk past him, but he keeps following you."

            scene cidade:
                zoom 2.0
                xalign 0.5
                yalign 0.5
            with dissolve 

            hide frente
            show frente:
                xalign 1.0
            with dissolve

    d "A red one, huh? So that Pierrot gave it to you? Interesting ♪"

    hide frente
    show normal:
        xalign 1.0
    with dissolve

    a "I'm the Harlequin, [titulo_arlequim]."
    a "Ah! I’ve got an idea!"
    a "How about we trade? I give you mine and… you give me that red one."

    show expression Solid("#000000C0") as escurecer
    show screen ingresso_verde with dissolve

    mc "What difference does it make? Why are there different colors?"

    hide escurecer with dissolve
    hide screen ingresso_verde with dissolve

    show plado:
        xalign 0
    with dissolve
    play sound "audio/efeitos/guizo.mp3"

    a "Oh my..."

    hide normal with dissolve
    show alado:
        xalign 1.0
    with dissolve

    a "Speak of the {i}devil."

    hide plado
    show plado at roubaringresso

    narrator "The Pierrot snatches the green ticket from Harlequin’s hand."

    a " {i}Sigh..."

    mc "{color=#a0b0c0}(Did I just walk into some kind of act? I better slip away quietly.)"

    a "Such a shame you don’t have a voice, huh, Pierrot?"


    scene cidade:
        zoom 1.8
        xalign 0.5
        yalign 0.5
    with dissolve 

    show alado:
        xalign 1.0
        yalign 1.5
        zoom 0.9
    
    show plado:
        xalign 0.0
        yalign 1.5
        zoom 0.9
    
    a "Guess you can’t say all those nasty things you’re thinking~"

    scene cidade:
        zoom 1.6
        xalign 0.5
        yalign 0.5
    with dissolve 

    show alado:
        xalign 0.8
        yalign 1.2
    
        zoom 0.8

    show plado:
        xalign 0.2
        yalign 1.2

        zoom 0.8

    a "Just wait 'til the Jester hears about this, heh!"

    narrator "You take small steps, slowly backing away. Once you’re a safe distance from their argument, you pick up the pace and head to work."

label trabalho_dia2:

    stop music fadeout 2.0
    play music "audio/musicas/cafeteria.mp3" fadein 2.0 volume 0.1

    scene cafe with dissolve

    mc "{i}Sigh..."
    mc "Made it on time, phew… Boss, I brought the… keys."
    mc "{color=#a0b0c0}(Is he talking to a cop?)"

    c "Just leave the keys on the counter, I’ll talk to you in a sec."

    mc "{color=#a0b0c0}(What happened this time? The store looks fine, doesn’t seem like it was broken into… did something happen to Carol?)"

    show chefe with dissolve

    c "Alright, was it a hassle closing the store last night?"

    mc "N-no, it was fine… what happened?"

    show chefeserio with dissolve
    hide chefe

    c "Well... Carol didn’t come home last night. Looks like she ran away."

    mc "She ran away?? She had issues with her family, yeah, but running away like that… that’s weird."
    mc "She didn’t show any signs she’d do something like this."

    c "She must have her reasons. If she shows up here, we’re supposed to notify the police."
    c "Carol’s probably not in a good state of mind."

    show chefe with dissolve
    hide chefeserio
    
    c "I’m going to start looking for a new employee, so I’ll be in the back doing interviews."
    c "Once your shift’s over, you can head home. I’ve got the store covered."

    mc "Oh, sure."
    mc "{color=#a0b0c0}(I never thought she’d do something like that. Then again, I guess we were just coworkers…)"
    mc "{color=#a0b0c0}(She never told me anything. But she was always so responsible… and said she really needed this job.)"

    scene balcaodia with dissolve
    mc "{color=#a0b0c0}(Maybe she was under a lot of stress at home.)"
    mc "{i}Sigh..."

    play sound "audio/efeitos/portaloja.mp3" volume 0.2
    pause 1.0

    mc "Good morning!{w=0.3} Ah!"

    play sound "audio/efeitos/guizo.mp3"
    show idle with dissolve
    mc "It's you again! Want something to drink, Pierrot?"

    hide idle
    play sound "audio/efeitos/guizo.mp3"
    show inclinado_e_corado with dissolve

    narrator "He nods, and points at a milkshake."

    mc "A milkshake? Isn’t it a bit cold for that? Haha."
    mc "Alright, have a seat and I’ll bring it to your table."

    narrator "He nods again and walks away from the counter."
    hide inclinado_e_corado with dissolve

    scene cafe:
        xalign 0
        yalign 0.5
        zoom 3.0
    with pushright

    show chefeserio with dissolve

    c "[mc_nome], did he buy anything?"

    mc "Yeah, a milkshake."

    c "Good. I don’t want those guys hanging around here without buying anything. Let him know we don’t allow flyering inside."

    mc "Got it!"

    hide chefeserio with dissolve

    scene balcaodia with pushleft

    show encara:
        zoom 2.0
        xalign 0.5
    with hpunch

    show olhos at tilt_loop:
        zoom 2.0
        xalign 0.5
    
    mc "{color=#a0b0c0}(Damn it, this again!?)"
    mc "W-whoa, you scared me! I thought you sat on the table or something…"
    mc "{color=#a0b0c0}(He’s really close.)"

    narrator "He grabs your arm firmly, locking eyes with you, then makes a gesture, calling you closer."

    mc "What is it…?"

    narrator "He whispers."

    hide encara
    hide olhos
    play sound "audio/efeitos/guizo.mp3"
    show sussurro with dissolve

    p "{size=25}{cps=10}Is he…{w=0.2} being mean to you,{w=0.2} [titulo_pierrot]?"

    mc "Huh? M-my boss? Haha, no, no!"
    mc "He was just giving me some reminders. He’s actually pretty nice."
    mc "{color=#a0b0c0}(I’d forgotten he can’t speak in front of others. But this is still really weird, especially with him crouching down and whispering like this…)"

    p "{size=25}Will you… come tonight?"

    mc "To the circus? Sure, I’ll be there to watch."

    p "{size=25}That makes me happy, [mc_nome]."
    p "{size=25}Will you promise to use my ticket tonight, [titulo_pierrot]?"


label promessa:

    menu:
        "I promise":
            mc "Sure, I promise."

    mc "{color=#a0b0c0}(He’s still holding my arm… Why are the claws on that glove so sharp?)"

    hide sussurro
    play sound "audio/efeitos/guizo.mp3"
    show ops:
        xalign 0.5
        zoom 1.2
    with dissolve

    narrator "He noticed you staring at the claws on his glove, let go of your arm, and made a silly face."

    mc "What’s with the tickets, anyway?"

    play sound "audio/efeitos/portaloja.mp3" volume 0.5
    pause 1.0

    hide ops
    show shh:
        xalign 0.5
        zoom 1.2
    with dissolve

    c1 "Mommy, look! A clown!"

    mc "Lucky you, huh."

    hide shh
    play sound "audio/efeitos/guizo.mp3"
    show inclinado_e_corado with dissolve

    c2 "It's true, darling. He's quite big, isn't he? But this circus isn't for children, it'll give you nightmares."
    c1 "Noo!"

    hide inclinado_e_corado

    show idle at deslizar_esquerda
    show mulher:
        xalign 0.6
    with dissolve
   
    m "Excuse me, I don't have all day! Can't you see me standing at the counter? Bring me my coffee, no sugar. Lazy one."

    mc "Well, I need to get back to work. Just a second, ma'am."

    mc "{color=#a0b0c0}(Looks like it's gonna be a long day.)"

    show expression Solid("#000000C0") as escurecer
    show milkshake:
        xalign 0.5
        yalign 0
    with dissolve

    mc "Uh, here you go... sir? Your milkshake."
    mc "{color=#a0b0c0}(What a weird combo haha, strawberry, chocolate, and coffee.)"

    narrator "The impatient woman next to you sighs loudly and checks her watch."

    hide escurecer with dissolve
    hide milkshake with dissolve
    pause 0.3

    mc "Yours is coming right up, ma'am."

    narrator "Pierrot carefully places the money in your hand along with a small chocolate bar."

    mc "Oh, is this a 'tip' for me? Thanks!"

    hide idle with dissolve
    play sound "audio/efeitos/guizo.mp3"
    show plado:
        xalign 0.0
    with dissolve

    narrator "He quickly nods and waves goodbye. As he turns around, you notice him staring at the grumpy woman before walking away."

    hide plado with slowdissolve
    show expression Solid("#0000007a") as escurecer
    with dissolve 

    mc "{color=#a0b0c0}(Aw, too bad... I was curious to see if he'd take off the mask to drink that...)"
    mc "{color=#a0b0c0}(This guy... I’ve been running into him a lot since yesterday.)"
    mc "{color=#a0b0c0}(I think he’s kinda...)"

    menu:
        
        "Weird":
            mc "{color=#a0b0c0}(Honestly? It's weird. He always seems to be around, though he doesn't feel threatening.)"

        "Cute":
            mc "{color=#a0b0c0}(Yeah, I guess that’s a good way to put it. It’s kind of cute how he always shows up and brings me little gifts.)"
        "Creepy":
            mc "{color=#a0b0c0}(He’s as tall as the door, that strange mask of his almost always has a smile on it… )"
            mc "{color=#a0b0c0}(And yeah, he does some pretty strange things sometimes.)"
            mc "{color=#a0b0c0}(I mean… it is a little creepy. Though I’m still not sure if I like that…)"

    mc "Sorry for the wait."

    hide mulher
    show mulher at pulinho:
        xalign 0.6
    with dissolve

    m "Uuuhg..."
    m "This coffee’s as awful as the service. I’m never coming back to this dump."

    mc "{color=#a0b0c0}(Is that a promise?){/color} I’m so sorry…"
    hide mulher with dissolve
    mc "{color=#a0b0c0}(Sometimes rude customers just show up… what can you do.)"
    mc "{color=#a0b0c0}(At least I got a chocolate to cheer me up.)"

label Arlequim_cafe:

    play sound "audio/efeitos/portaloja.mp3" volume 0.5
    pause 1.0

    a "Oh! So this is where you work, [titulo_arlequim]?"

    show frente with slowdissolve

    mc "{color=#a0b0c0}(He followed me too… great.)"
    mc "Good afternoon. Want something to drink?"

    a "Of course! I’ll take an iced coffee."

    mc "I’ll get it ready."

    narrator "He leans over the counter, watching you as you make the coffee."
    a "Soooo.... Are you finally gonna accept my ticket?"

    mc "No. I already have one, and I promised I’d use it."

    hide frente
    show alado with dissolve

    a "You sure? It’d be so much more fun if you used mine ♪"

    mc "Why?"

    hide alado with dissolve
    show alesilencio 

    a "{i}That’s a secret."

    mc "{color=#a0b0c0}(Ugh, these two…)"

    hide alesilencio
    show frente with dissolve 
    mc "Here’s your iced coffee."

    a "Alright, alright. In that case…"
    a "A little something for you. I’d love for you to wear it."
    a "Here, let me put it on."

    narrator "He steps closer and gently pins the pin to your shirt collar. He’s not as tall as Pierrot, but still has to lean in quite a bit to reach."

    scene broche with dissolve

    mc "Hmn?"

    narrator "You hear the claw of his glove click softly against the metal of the pin as he gives it a tap, chuckling under his breath in a low tone."

    a "{bt=2}{b}{color=#41d623}I’m going to take you from him."

    mc "...Excuse me?"

    scene balcaodia with dissolve
    show arlemaca:
        zoom 3.0
        xalign 0.5
        yalign 0.1
        
    with dissolve

    a "You’ll see ♪"

    hide arlemaca
    show frente with dissolve

    a "Anyway, here’s the payment."

    hide frente
    show normal at efeito_deslifade
    with dissolve

    a "See you tonight, [titulo_arlequim]."
    a "Make sure you don’t miss my show, alright?"

    mc "H-Hey!"

    hide normal with dissolve

    mc "{color=#a0b0c0}(Take me from him? What is this? Are they playing some kind of game with me?)"
    mc "Tch..."
    mc "{color=#a0b0c0}(I really can’t tell if they’re teasing me or trying to pull me into something else)"  ####### AQUI

label fimdo_turno:

    scene balcao with dissolve

    show chefema with dissolve

    c "Your shift’s just about over. I’ll keep the shop open for another hour."
    c "Until we hire someone new, I’ll have to cut back the hours a bit."

    mc "Got it! What happened to your arm?"

    c "This? Oh, something scratched me out back. Pretty sure it was a huge cat or something."

    mc "Hm. Be careful."

    menu:
        "Give a bandage":
            mc "Here, I’ve got a bandage."
            c "Thanks! Good thing you carry this kind of stuff around."
            mc "I’m kind of clumsy, to be honest. So I always keep one with me."
            c "That makes sense, haha!"
        "Check the wound":
            mc "Did you clean it already?"
            c "Yeah, it’s nothing serious."
            mc "Still, those are some big claws for a stray cat huh?"
            c "If you’d seen the size of that thing, you wouldn’t think it’s weird."
    
    mc "Anyway, I gotta go, don’t wanna be late. I’m heading to the circus tonight."

    c "Sounds fun. Tell me how it was later, maybe I’ll check it out sometime."

    mc "Sure! See you later!"

label circo:
    stop music fadeout 1.5
    play music "audio/musicas/circo.mp3" fadein 2.0 volume 0.1

    scene circo with slowdissolve

    mc "Uhm..."
    mc "{color=#a0b0c0}(I’m not really into crowded places... but things are pretty lively here. There’s a food fair right at the entrance of the big top.)"

    show bilheteiro with slowdissolve

    b "Hello there, visitor! May I punch your ticket?"

    mc "Sure, here it is!"

    if final_rosa == True:
        jump fimrosa

    play sound "audio/efeitos/furar.mp3"
    pause 0.5
    b "Oh, a special ticket! Be sure to keep it safe, alright? You’ll need to show it at the attractions."
    
    mc "Okay, but what’s a special ticket?"

    b "Hm? You’ve got front row seats."

    mc "Nice! Thanks."

    b "Enjoy the show!"

    hide bilheteiro with dissolve

    scene bilheteria with dissolve

    mc "{color=#a0b0c0}(So that’s how it works? The box office tickets are all yellow. I can see a few black ones too, but no pink, green, or even red ones like mine.)"

    scene circo with dissolve
    mc "{color=#a0b0c0}(Alright, let’s see what we’ve got here.)"
    mc "{color=#a0b0c0}(There’s a pink and black tent over that way, a green one, a purple one, and Pierrot’s red tent.)"
    mc "{color=#a0b0c0}(Looks like his show isn’t on yet. I can visit another one in the meantime.)"

label tendas:
    menu:
        "Pink tent":
            show bilheteiro with dissolve
            b "Oh! So sorry, you don’t have access to this area, my dear."

            mc "Ok, sorry."
            hide bilheteiro with dissolve
            jump tendas 
        "Purple tent":

            mc "The Jester. Looks like his show already happened. Maybe there’ll be another one later."
            jump tendas

        "Green tent":
            mc "{color=#a0b0c0}(Oh, it’s already started!)"

label tenda_verde:
    stop music fadeout 1.5
    play music "audio/musicas/arlequim.mp3" fadein 1.5 volume 0.1

    scene tendaverde:
        zoom 2.0
        xalign 0.5
    with dissolve
    show expression Solid("#000000C0") as escurecer
    show normal with dissolve

    a "Good evening, my dear monsters. Enjoy my show!"

    scene historia with slowdissolve

    show monstros with dissolve

    a "{i}Far from everything, where God’s eyes cannot reach, the monsters lived."
    a "{cps=10}{i}Forgotten. Hungry. Silent."
    show tenda with dissolve
    show homem at balanco_organico:
        xalign 0.4
        yalign 0.9
    with dissolve
    
    a "Until the man appeared. He raised a tent upon the dead earth and made a deal:"

    hide homem
    show homem at pulinho:
        xalign 0.4
        yalign 0.9

    pause 0.2
    hide homem
    show homem at balanco_organico:
        xalign 0.4
        yalign 0.9
    

    a "{color=#ff0000}Work for me, you hideous little creatures, and I will feed you."

    hide monstros
    show monstros at pulinho
    hide homem
    show homem:
        xalign 0.4
        yalign 0.9

    a "{color=#ffffff}How wonderful!"
    a "Thought the monsters. And so{cps=20} they obeyed."

    scene historia
    show multidao with dissolve
    show monstros with dissolve

    a "But the man brought more men. And more..."
    a "They laughed at the monsters."
    a "They applauded their pain."

    scene black with dissolve
    show homem at balanco_organico:
        zoom 3.5
        xalign 0.5
        yalign 1

    a "{color=#ff0000}What if I charged others to watch?"
    a "The crowd loved it."

    a "But the man wanted more, always more. So he began to feed them less."

    hide homem
    show homem at balanco_organico:
        zoom 4.5
        xalign 0.5
        yalign 1
    
    a "{color=#ff0000}This way they’ll be weak. Harmless."
    
    hide homem with dissolve

    show monstros2:
        xalign 0.5
        yalign 0.5
    with dissolve

    a "He laughed, while the monsters rotted in their cages, swallowed by the dark."
    a "And then they thought:"
    hide monstros2
    show monstros2:
        zoom 4.0
        xalign 0.9
        yalign 0.1
    with dissolve

    a "{color=#961ee6}What if we became human?"

    hide monstros2
    show monstros2:
        zoom 4.0
        xalign 0.5
        yalign 0.1
    with dissolve

    a "We could eat as much as we want."

    hide monstros2
    show monstros2:
        zoom 4.0
        xalign 0.2
        yalign 0.1
    with dissolve
    a "{color=#ffaf54}No one would hurt us ever again."

    scene historia with dissolve
    show expression Solid("#000000C0") as escurecer

    show monstros2:
        xalign 0.5
        yalign 0.5
    with dissolve

    a "And on a moonless night, when the sky seemed dead,"

    hide monstros2
    show monstros3:
        xalign 0.5
        yalign 0.5
    with dissolve

    show columbina:
        xalign 0.4
        yalign 0.6
    with dissolve
    
label glitch1_columbina:
    a "The monsters realized there was an angel among them!"
    
    show screen sobreposicao_texto(_("{glitch=20}{color=#e61ee6}The monsters realized a{/color}{color=#e73314} sacrifice{/color}{color=#e61ee6} would be necessary.{/glitch}"))
    hide columbina
    hide monstros3
    show glitch1 at glitch
    pause 1.0
    hide glitch1
    show monstros3:
        xalign 0.5
        yalign 0.5
    
    show columbina:
        xalign 0.4
        yalign 0.6
   
    
    a "{cps=100}The monsters realized there was an angel among them!"
    
label glitch2_columbina:

    scene black

    show columbina at deslizarsutil_dir
    with dissolve 

    
    a "{color=#e61ed5}I can feed you, grow strong, become human and build a home for us."
    show textbox:
        yalign 1.0
    show screen sobreposicao_texto2(_("{glitch=20}{b}{color=#e61ee6}Please, no!{/glitch}"))
    pause 0.9
    show screen sobreposicao_texto2(_("{glitch=20}{b}{color=#961ee6}We have no choice.{/glitch}"))
    pause 0.9
    show screen sobreposicao_texto2(_("{glitch=20}{b}{color=#41d623}She is the weakest of us.{/glitch}"))
    pause 0.9
    show screen sobreposicao_texto(_("{glitch=20}{b}{color=#ffffff}You will give us the strength to go on.{/glitch}"))
    pause 0.9

    hide textbox
    a "The angel said."

label glitch3_columbina:
    scene colum 
    show glitch_colu
    pause 0.5
    hide glitch_colu

    show screen sobreposicao_texto("{glitch=40}{b}{color=#e61ee6}PlEASE HELP ME, I DON’T WANT TO DIE.{/glitch}")

    show cfinal
    pause 0.1
    hide cfinal
    pause 0.1
    show cfinal
    pause 0.1
    hide cfinal
    pause 0.1
    show cfinal
    pause 0.3
    hide cfinal

    scene historia
    show monstros4:
        xalign 0.5
        yalign 0.8

    a "And then, as if she had never existed, she vanished with the wind."
    a "Our little miracle…"
    show screen sobreposicao_texto2("{color=#41d623}Our little {glitch=20}{color=#e61ee6}sacrifice.{/glitch}")
    pause 1.6

label final_historia:

    show homem at pulinho:
        xalign 0.5
        yalign 0.9
    with dissolve
    a "The next morning, the man returned to laugh."

    hide monstros4
    show monstros5:
        xalign 0.5
        yalign 0.8
    with dissolve

    hide homem
    show homem at tilt_glitch:
        xalign 0.5
        yalign 0.8

    a "But the monsters’ eyes had changed."
    a "They were free."
    a "They were hungry."
    scene black

    a "And that’s how the monsters became human!"

    scene historia with slowdissolve
    show humanos:
        xalign 0.5
        yalign 0.8
    
    a "Oh, and what happens next, you ask?"
    a "After that, the new humans took their home and began to travel together."
    a "Searching for a place to build it again and live happily, just as the angel wished."
    scene black with slowdissolve
    a "Thank you! Thank you little monsters!"
    
label fimda_historia:
    scene tendas1:
        zoom 1.2
    with dissolve

    mc "{color=#a0b0c0}(People actually seemed to enjoy that.)"
    mc "{color=#a0b0c0}(That story felt pretty macabre, though...)"

    show frente with dissolve
    a "I'm glad you came to see my show... I was hoping you’d be watching."

    mc "Ah... hello! Your story was... peculiar."

    hide frente
    show alado with dissolve
    a "Yeah, it’s a pretty old story from the circus. It's a tradition to tell it on certain nights."

    hide alado
    show frente at pulinho

    a "Oh!{w} I see you're wearing my gift! That makes me so excited!"

    hide frente
    show frente:
        zoom 1.5
        xalign 0.5
        yalign 0.2
    with dissolve

    mc "{color=#a0b0c0}(Oh, right... I forgot about that.)"

    hide frente
    show frente:
        zoom 2.5
        xalign 0.5
        yalign 0.2

    mc "W-What?"

    a "{i}It looks good on you. {cps=10}Almost...{w=0.2} too intimate."

    hide frente
    show frente2:
        zoom 2.5
        xalign 0.5
        yalign 0.2
    with dissolve

    a "Did you like it?{w=0.2} Or are you trying to tease me?"

    narrator "You frown in protest, but his words caught you off guard. You don’t even know how to respond." with vpunch

    show frente3:
        zoom 2.5
        xalign 0.5
        yalign 0.21
    with dissolve
    hide frente2

    narrator "He smiles, clearly amused by your confusion."

    a "Mmh… I love that!"
    a "I love seeing my green mark so close to your skin."
    a "Like a quiet, forbidden kiss."

    mc "{color=#a0b0c0}(He's way too close... I should-)"

    play sound "audio/efeitos/pegar.mp3" volume 0.5
    narrator "You take a step back, bumping into the circus tent’s cold wall."

    mc "{color=#a0b0c0}(What is wrong with this guy??)"

    play sound "audio/efeitos/pegar.mp3" volume 0.5
    show arlemaca:
        zoom 2.5
        xalign 0.5
        yalign 0.1
    with dissolve
    hide frente3
    narrator "He leans in, bracing his arms around you."
    
    a "Running away?"
    a "Scared? Or..."
    a "{cps=10}...Secretly enjoying it?"

    mc "{color=#a0b0c0}(Enjoying it? No way I... Do I?)"

    menu:
        "Yes":
            narrator "He smiles wider at your hesitation."
            hide arlemaca
            show arlemaca:
                zoom 2.55
                xalign 0.5
                yalign 0.1
            with dissolve
            
            a "No need to say a word. I can read you."
            a "Your silent screams."
            a "Red doesn’t suit you, darling."
            a "That intoxicating green... fits better ♪"

            mc "{color=#a0b0c0}(His scent... it’s good. And that voice... it's too intense.)"
            narrator "He smiles again, like he knows his poisonous words have burrowed into your mind, then slowly steps back."

            hide arlemaca
            show frente:
                zoom 1.5
                xalign 0.5
                yalign 0.2
            with dissolve
            a "I want to give you another gift."
        "No":
            narrator "He catches the subtle shift in your eyes, then backs away with a slow, almost wicked smile."
            hide arlemaca
            show frente3 with dissolve

            a "Oh, don’t take me so seriously, darling..."
            a "I was only... performing~"
            mc "{color=#a0b0c0}(Performing...? Yeah, sure.)"
            a "How about… a tiny apology?"

    hide frente
    hide frente3
    show arlemaca with dissolve
    a "What do you say?"

    mc " A candy apple?"

    a "Yeah, we call it a 'Love Apple' or 'Maçã do amor', but don’t get the wrong idea, it’s still just an apple."

    mc "Well..."

    hide arlemaca
    play sound "audio/efeitos/sacarfaca.mp3" volume 0.2
    show screen animacao
    pause 1.0
    hide screen animacao

    show screen arlequim_maca
    show tendas1:
        zoom 1.2
        xalign 1.0
    with dissolve

    pause 0.2

    show tendas2:
        zoom 1.2
        xalign 1.0
    with dissolve

    pause 0.2

    show tendaverde:
        zoom 1.2
        xalign 1.0
    with dissolve

    pause 0.5
    hide screen arlequim_maca
    scene tendaverde with dissolve
    show frente at pulinho:
        yalign 0.5
        zoom 1.5
    
    mc "What--{nw=0.5}"
    mc "What was that??"
    mc "Where... did that come from?"

    hide frente
    show alado at pulinho:
        yalign 0.3
        zoom 1.5

    a "{size=25}Hah... always so dramatic."
    a "I guess someone around here really {i}hates{/i} apples."

    mc "Does this kind of thing happen a lot around here?"

    narrator "You try to look at the knife sticking out of the candy apple, but the Harlequin in front of you quickly snatches it away and tosses the apple aside."

    hide alado
    show normal:
        xpos 500
        zoom 1.5
    with dissolve
    a "No need to worry, [titulo_arlequim]. I'm sure it was just a little joke."
    a "Looks like I’ll have to delay giving it to you."
    
    mc "{color=#a0b0c0}(A pretty dangerous joke... Are these guys actually insane?)"

    mc "Alright...{w=0.3} I should get going, the next show’s about to start."
    a "Have fun, [titulo_arlequim]. Who knows, maybe I’ll see you around."

label barracas:
    scene circo with slowdissolve

    mc "{color=#a0b0c0}(Well, weirdness aside... I’m actually getting kinda hungry. Maybe I should grab something to eat before heading to Pierrot’s tent?)"

    menu:
        "Buy some food":
            mc "Well, why not?"
            $ envenenada = True
            menu:
                "Popcorn":
                    mc "Mmm! This smells so good."
                    narrator "You scarf down your snack and quickly feel full."
                "Sweet popcorn":
                    mc "Mmm! This smells so good."
                    narrator "You scarf down your snack and quickly feel full."
                "Candy apple":
                    scene feira with dissolve

                    narrator "Before the vendor can hand you the food, someone snatches it from him, and a familiar face leans in, offering the candy apple to you."

                    play sound "audio/efeitos/guizo.mp3"
                    show pimaca:
                        xpos 500
                    with dissolve
                    mc "Funny guy. How’d you even find me in a crowd like this?"

                    hide pimaca with dissolve
                    play sound "audio/efeitos/guizo.mp3"
                    show inclinado_e_corado at pulinho
                    p "{cps=10}{size=35}..."
                    mc "Okay, okay, not really the best place for small talk, huh? I’m heading in before the show starts."

                    narrator "He smiles brightly and waves before walking away."

                    hide inclinado_e_corado with slowdissolve
                "Hot dog":
                    mc "Mmm! This smells so good."
                    narrator "You scarf down your snack and quickly feel full."

        "Forget it":
            mc "Nah, I guess I'm not that hungry, I can eat something better at home and cheaper too."

label barraca_pierrot:

    mc "{color=#a0b0c0}(I better hurry before the show starts.)"

    scene tendapi with dissolve
    pause 0.3
    show tendapi2 with slowdissolve

    stop music fadeout 2.0
    play music "audio/musicas/pierrot.mp3" fadein 2.0 volume 0.2

    mc "{color=#a0b0c0}(Oh! A theatrical performance? I was wondering what a show without speaking would be like.)"

    scene tendapi
    show pierrotapre at dramatic_pan
    with dissolve

    narrator "He shifts into a more menacing posture, his smile turning sinister. He moves in a strange, hypnotic dance as the lights change around him."
    narrator "It feels like he’s dancing with his own shadow."
    narrator "Except when he moves one way, the shadow moves the other... in a really creepy way."

    pause 0.3
    show aplauso with dissolve
    show expression Solid("#000000C0") as escurecer with dissolve
    mc "{color=#a0b0c0}(Whoa, he really changes on stage.)"

    scene palcomu with fade
    show aplauso
    pause 0.3

    scene palcomu2
    show aplauso at deslizar_esquerdapalco
    pause 0.5

    mc "A stage assistant! Even from here, you can tell how much taller he is than her."

    hide aplauso
    play sound "audio/efeitos/sacarfaca.mp3" volume 0.5

    show facaspi:
        xalign 0.1
        yalign 0.45

    mc "{color=#a0b0c0}(Knives?)"

    narrator "The woman moves slowly, stretching her arms a few times."

    hide facaspi with dissolve
    pause 0.2

    scene faca1 with hpunch

    play sound "audio/efeitos/arremesso.mp3" volume 0.5
    mc "W-woah..."

    play sound "audio/efeitos/arremesso.mp3" volume 0.5
    scene faca2 with hpunch

    narrator "You hear some people cheering for him to hit her."
    mc "{color=#a0b0c0}(It’s just acting... and some crazy people... relax.)"

    play sound "audio/efeitos/arremesso.mp3" volume 0.5
    scene faca3 with hpunch
    mc "{color=#a0b0c0}(Those knives are landing way too close to her... That's--{nw=0.6})"

    play sound "audio/efeitos/golpef.mp3" volume 0.5
    scene faca4 with hpunch
    pause 0.5

    scene mulher2 with fade
    pause 1.0
    scene black
    show mulher2 at escurece_corpo

    mc "{color=#a0b0c0}(... Terrifying!!)"
    mc "{sc=3}{color=#a0b0c0}(N-no... that wasn’t real... right? Ha... ha... just acting...){/sc}"
    mc "{sc=1}{color=#a0b0c0}(It was just a performance. Of course it was... haha...){/sc}"
    mc "{sc=3}{color=#a0b0c0}(But... the blood... the way she fell...){/sc}"
    mc "{sc=5}{color=#a0b0c0}(Damn it. I need to get out of here.){/sc}"

label circo_final:
    stop music fadeout 1.0
    play music "audio/musicas/circo.mp3" volume 0.1
    scene circo:
        yalign 1.0
        xalign 0.7
        zoom 2.0
    with dissolve

    mc "{sc=1}{color=#a0b0c0}(Air... I need air...)"
    mc "{sc=1}{color=#a0b0c0}(Haha... this is insane. Just a show... it's just a show... right?)"

    mc "{color=#a0b0c0}(I guess the creepy atmosphere of this place got to me a little.)"
    mc "{color=#a0b0c0}(I mean, the stage lights were low for a reason, right? It was just a scare, that’s all. I wasn’t expecting it.)"

    if envenenada == True:
        mc "{color=#ff69b4}(But... I feel like the atmosphere here is messing with me. My body feels warm... in a good way.)"

    narrator "You feel a heavy hand land on your shoulder."

    play sound "audio/efeitos/guizo.mp3"
    show pitenso at pulinho
    mc "!!!" with hpunch
    pause 0.2
    
    mc "A-ah! Oh, it’s you, jeez…"
    hide pitenso 
    show idle:
        zoom 1.3
        xalign 0.5
        yalign 0.5
    with dissolve

    mc "You’re awfully quiet for someone covered in bells..."


    show bravo:
        zoom 1.3
        xalign 0.5
        yalign 0.5
    with slowdissolve

    mc "W-what is it?"

    show encaraclose with dissolve
    show olhosarregalados
    play sound "audio/efeitos/guizo.mp3"
    narrator "He slowly raises his hand, hesitant, and runs the claw of his glove along the pin on your collar."

    show olhosvidrados at tilt_olhos:
        xalign 0.529
        yalign 0.33
    with dissolve

    mc "Oh, right... Your, uh… friend? He gave it to me."

    narrator "He grips your collar, leaning in closer."

    hide encaraclose
    hide olhosarregalados
    hide olhosvidrados

    play sound "audio/efeitos/guizo.mp3"
    show encaraclose:
        xalign 0.5
        zoom 1.2
    
    show olhosarregalados:
        xalign 0.5
        zoom 1.2
    
    show olhosvidrados at tilt_olhos:
        zoom 1.2
        xalign 0.529
        yalign 0.4
    with dissolve

    mc "Pierrot?"

    p "{cps=10}{size=40}..."

    show encaracloseso:
        xalign 0.5
        zoom 1.2
    with dissolve

    pause 0.2

    play sound "audio/efeitos/pegar.mp3"
    scene pin2 with dissolve

    mc "Hmn?"

    mc "Uh… thanks?"
    mc "{color=#a0b0c0}(They’re definitely not friends.)"

    scene circo:
        yalign 1.0
        xalign 0.7
        zoom 2.0
    
    play sound "audio/efeitos/guizo.mp3"
    show sussurro with dissolve

    narrator "He lowers himself, slowly getting closer to you, and leans in to whisper."

    if envenenada == True:
        mc "{color=#ff69b4}(My heart's beating faster...)"
        narrator "{sc=1}{color=#ff69b4}You feel your body slipping into euphoria. You're warm, your hands are shaking,\n and a strange joy and rush take over while your heart races wildly in your chest."
        jump envenenada

    p "Did you like my show?"

    mc "O-of course, it was… it was…"

    menu: 
        "Amazing":
            mc "Amazing! Your performance was amazing! It almost looked like two people dancing out there!"
            mc "And your magic tricks too! How did you make that woman seem so real?"
        "Scary ":
            mc "Scary! I mean, I know scaring people is kind of your whole thing, but I wasn’t ready for that hah."
            mc "That woman looked so real… I wasn’t sure if it was part of the act or…"
            mc "Heh, anyway… y-you really caught me off guard! How did you do that?"
        "Fun":
            mc "That was fun! I’ll admit it wasn’t what I expected, And that whole scene with the woman tied up? That was wild!"
            mc "How did you even do that?"
    
    play sound "audio/efeitos/guizo.mp3"
    hide sussurro
    show silencio:
        zoom 1.2
        xalign 0.5
        yalign 0.5
    with dissolve

    mc "So many secrets…"

    play sound "audio/efeitos/guizo.mp3"
    hide silencio
    show sussurro with dissolve

    p "{i}Why don’t you stay a little longer? I could show you the rest of the circus."

    mc "Actually, I should probably get going. It’s not a great idea to be wandering around alone this late."

    show sussurro2 with dissolve

    p "Shall I escort you, [titulo_pierrot]? If you’re frightened, I can ensure you reach safety."

    mc "No need, really! I’m fine, don’t worry. I wouldn’t want to bother you."

    p "May I see you again tomorrow?"

    menu:
        "Sure":
            mc "Sure, why not? Things got a lot more interesting with you around."

            hide sussurro
            hide sussurro2
            play sound "audio/efeitos/guizo.mp3"
            show piapaixonado with dissolve

            mc "W-Woah!"

            p "I shall look forward to it, [titulo_pierrot]."

            mc "Hah, see you tomorrow, Pierrot."

            p "Until tomorrow, [mc_nome], my dearest."

            jump emcasa
        "Better not":
            $ bolo = True
            mc " I… think it’s better if I don’t."
            
            hide sussurro
            hide sussurro2
            play sound "audio/efeitos/guizo.mp3"
            show chocado with dissolve

            p "B-but… why? Did I do something wrong, [titulo_pierrot]?"

            hide chocado
            play sound "audio/efeitos/guizo.mp3"
            show chocado:
                zoom 1.5
                xalign 0.5
                yalign 0.5
            with dissolve 

            mc "I’m just… not so sure about all this. Give me some time, okay?"

            p "{cps=5}{size=45}..."

            jump badend

label badend:
    
    mc "Well… good night."

    hide chocado
    show pitenso:
        zoom 1.2
        xalign 0.5
        yalign 0.5
    with dissolve

    p "Wait! … S-since I won’t get to see you tomorrow… may I give you one last gift?"

    mc "Uh, well…"

    p "You must be starving! You haven’t eaten anything all day, have you [titulo_pierrot]?"

    mc "{color=#a0b0c0}(Ugh… he’s not wrong.)"

    p "I made this earlier, just for you. Please… try it and tell me if you like it."

    show expression Solid("#000000C0") as escurecer
    show bolo:
        xalign 0.5
        yalign 0.4
    with dissolve

    mc "{color=#a0b0c0}(Aww, that’s actually kinda sweet. Well, I better eat so he’ll let me head home.)"

    hide escurecer
    hide bolo with dissolve

    hide pitenso
    play sound "audio/efeitos/guizo.mp3"
    show inclinado_e_corado with dissolve
    narrator "You eat the cake while Pierrot keeps you company."

    show screen efeito_veneno

    mc "That was really good! You’re actually great at this."

    hide inclinado_e_corado
    play sound "audio/efeitos/guizo.mp3"
    show encaraclosesorriso with dissolve
    show olhosvidrados at tilt_olhos:
        xalign 0.53
        yalign 0.31
        
    mc "Now I should just--"
    mc "{cps=10}Uhgn... ?"

    p "What is it? Are you thirsty?"

    mc "Yeah, but…"
    mc "{sc=3}{color=#ff69b4}S-something’s wrong..."
    mc "{sc=3}{color=#ff69b4}You..."

    play sound "audio/efeitos/cair.mp3"
    stop music fadeout 10.0
    scene black
    show screen desmaio with dissolve

    narrator "{sc=1}{color=#ff69b4}Your body collapses as your consciousness drifts away. You can feel someone holding \nyou tightly."
    narrator "{sc=1}{color=#ff69b4}Every sound seems distant, though you catch brief flashes of what’s happening \nbefore everything fades to black."

    p "T-That was close..."
    p "I almost... almost lost you [titulo_pierrot]."
    p "{sc=1}{color=#ffaf54}I saw it in your eyes... you were going to leave me, weren’t you?"
    p "{sc=1}{color=#ffaf54}For a second... I thought I’d have to..."

    hide screen desmaio with Dissolve(0.5) #preto
    show piscar1
    show pegueivcbad
    show olhos_bad

    show abrir_olhos zorder 40

    p "N-No... It’s all right now. Everything’s fine."
    p "You just needed... to stop fighting me."
    p "{b}M-Maybe this was all a little game of pretend?"
    p "{b}Maybe you wanted me to chase you?"
    p "Or... maybe I moved too fast."
    p "I should’ve been more patient... more gentle."
    p "I scared you, didn’t I?"

    show screen piscando
    pause 0.2
    show screen desmaio
    hide pegueivcbad
    hide olhos_bad
    show pegueivcbadb
    show olhos_bad:
        xpos 0.54  # 55% da tela na horizontal
        ypos 0.5
        anchor (0.5, 0.5)
       
    pause 0.1

    hide screen piscando
    hide screen desmaio
    show abrir_olhos
    pause 0.2
    
    p "I’ll take good care of you, I promise."
    p "{sc=1}{color=#ffaf54}Even if you try to run again..."
    p "{sc=1}{color=#ffaf54}Even if you look at me like that again..."
    p "{sc=1}{color=#ffaf54}I’ll gently remind you that you need me."
    p "{sc=1}{color=#ffaf54}With kindness, patience... or with another dose."

    show screen piscando
    pause 0.2
    show screen desmaio
    hide pegueivcbadb
    hide olhos_bad
    show faminto

    pause 0.1

    hide screen piscando
    hide screen desmaio
    show abrir_olhos
    pause 0.2

    p "{sc=3}{color=#ffaf54}Because I love you."
    p "{sc=1}{color=#ffaf54}My sweet angel..."
    p "{sc=1}{color=#ff0000}Don’t make me devour you too."

    scene black with slowdissolve
    pause 0.5
    play sound "audio/efeitos/correntes.mp3" volume 0.5
    pause 2.5

    #jump fimdejogo
    jump sequestro


label emcasa:
    stop music fadeout 1.0
    scene black with dissolve

    mc "Man, I’m exhausted..."
    scene quarto with slowdissolve

    mc "But that was fun, kinda creepy too."
    mc "I’m not even hungry anymore. I think I’ll just head straight to bed."
    pause 1.0

    scene quartoapagado:
        zoom 1.3
        xalign 1.0
        yalign 0.3
    with dissolve 

    pause 0.5

    play sound "audio/efeitos/vidro.mp3" volume 0.5
    show mao1:
        zoom 1.3
        xalign 1.0
        yalign 0.3

    pause 1.0

    show mao2:
        zoom 1.3
        xalign 1.0
        yalign 0.3

    pause 0.2

    show sombram:
        zoom 1.3
        xalign 1.0
        yalign 0.3
    with slowdissolve

    pause 1.5

    scene quartoapagado:
        zoom 1.3
        xalign 1.0
        yalign 0.3
    with dissolve 

    pause 0.2
    show pfinalquarto with dissolve
    play music "audio/musicas/drama.mp3" fadein 5.0 volume 0.1
    p """
        {cps=15}
        We can take it slow then, [titulo_pierrot]...

        {cps=15}I can be patient, I can smile at you and pretend I’m not burning inside.

        """

    show pf2 at zoom_lento
    with slowdissolve

    p """
        {cps=20}{sc=2}{color=#ffaf54}Pretend I’m not imagining you breathless, trembling beneath my touch.

        {cps=20}{sc=2}{color=#ffaf54}Just look at what you're doing to me...

        {cps=20}{sc=2}{color=#ffaf54}This love... it’s growing, twisting, taking shapes that might scare you if I showed you now.

        {cps=20}{sc=2}{color=#ffaf54}But that’s all right. I can keep it hidden, for now.

        {cps=20}{sc=2}{color=#ffaf54}That sweet demeanor... that gaze that teases me without even knowing it...

        {cps=20}{sc=2}{color=#ffaf54}As if you weren’t aware that you’re poisoning me with love in every little gesture.

        {cps=20}{sc=2}{color=#ffaf54}But that’s all right, [titulo_pierrot].... 
        
        {cps=30}{sc=2}{color=#ffaf54}Because when I have you, it won’t be gentle.

        {cps=30}{sc=2}{color=#ffaf54}I want it to be, but I know it won’t. I’ll leave my mark on you. From the inside out.

        {cps=30}{sc=2}{color=#ffaf54}Until your body knows my name better than it knows your own.

        """

    show pf3:
        zoom 1.5
        xalign 0.3
        yalign 0.5

    show olgosf3 at tilt_olhos:
        zoom 1.5
        xalign 0.3
        yalign 0.5

    p """

        {cps=30}{sc=2}{color=#ffaf54}Until your skin burns at the touch of anyone who isn’t me.

        {cps=30}{sc=2}{color=#ffaf54}You’ll cry, tremble, beg… But not from pain... Well.

        {cps=30}{sc=2}{color=#ffaf54}{i}Unless that’s what you want ♪

        {cps=30}{sc=2}{color=#ffaf54}I’ll always be there for you, hungry, yet gentle.

        {cps=30}{sc=2}{color=#ffaf54}That’s how you like it, isn’t it?

        {cps=30}{sc=2}{color=#ffaf54}But if it’s not, I can change.

        {cps=30}{sc=2}{color=#ffaf54}I can move to your rhythm, in whatever way you desire.

        {cps=30}{sc=2}{color=#ffaf54}In whatever way makes you mine.

        {cps=30}{sc=2}{color=#ffaf54}I can remake myself for you, shape myself to fit the image you hold of me.

        {cps=30}{sc=2}{color=#ffaf54}Do you want me gentle? Affectionate? Shy? Or perhaps… bold?

        {cps=30}{sc=2}{color=#ffaf54}Do you want a hunter, chasing you with relentless passion?

        {cps=30}{sc=2}{color=#ffaf54}Do you want me rough?

        {cps=30}{sc=2}{color=#ffaf54}It’s all right ♪ I’ll learn what takes your breath away.

        {cps=30}{sc=2}{color=#ffaf54}I’ll learn the intensity that makes your soul, and your body tremble for me.

        {cps=30}{sc=2}{color=#ffaf54}Because I love you, [titulo_pierrot] [mc_nome].

        """

    scene black with slowdissolve

    p "And for you... I can be everything."

    scene black
    
    pause 0.5

    jump devolta_emcasa


label envenenada:

    show screen efeito_veneno

    p "Did you like my show?"
    menu:
        "{sc=2}{color=#ff69b4}Yes":
            pass
        "{sc=2}{color=#ff69b4}Yes":
            pass
        "{sc=2}{color=#ff69b4}Yes":
            pass

    
    mc "{sc=1}That was amazing!! I can’t even explain it. At first I felt scared and unsure,\n but now everything just feels so... incredible!"

    narrator "{sc=1}{color=#ff69b4}He's still so close, whispering, keeping the conversation just between you two."

    mc "{sc=1.5}{color=#ff69b4}(My heart won’t stop racing... maybe... I actually like him?)"
    mc "{sc=2}{color=#ff69b4}(I feel kind of nervous when he gets this close.)"

    show sussurrov2
    hide sussurro

    p "Would you like me to show you the rest of the circus?"

    mc "{sc=1}{color=#ff69b4}Of course! I... I’d love to spend more time with you."

    hide sussurrov2
    show inclinado_e_corado:
        xalign 0.5
        zoom 1.5
    narrator "{sc=1}{color=#ff69b4}You take his hand. He blushes and squeezes yours firmly."

    p "I’m certain you will find this place quite delightful, [titulo_pierrot]."

    narrator "{sc=1}{color=#ff69b4}You smile, panting lightly, staring into Pierrot's grinning mask."

    mc "{sc=3}{color=#ff69b4}(I'm... feeling dizzy...)" with fade
    mc "{sc=3}{color=#ff69b4}I think... something’s wrong with me..." with fade

    play sound "audio/efeitos/cair.mp3" volume 0.5
    stop music fadeout 5.0

    scene black
    show screen desmaio with dissolve

    p "Wha-- [titulo_pierrot]??"

    narrator "{sc=1}{color=#ff69b4}Your body collapses as your consciousness drifts away. You can feel someone holding you tightly."
    narrator "{sc=1}{color=#ff69b4}Every sound seems distant, though you catch brief flashes of what’s happening \nbefore everything fades to black."

    p "{sc=1}{color=#ffaf54}What...?"
    p "Oh,{w=0.3}{cps=10} {i}I see now."
    p "{cps=20}It's all right, [mc_nome] I am here to take care of you."
    play sound "audio/efeitos/guizo.mp3"

    p "{i}Oh, [titulo_pierrot] ♪"
    p "{i}You’ve been waiting for this, haven’t you? Ah... but not nearly as much as I have."
    p "{i}It feels so {b}unbelievably{/b} good to hold you like this."
    p "{sc=3}{color=#ffaf54}Finally mine."

    hide screen desmaio with Dissolve(0.5) #preto
    show piscar1
    show pegueivc
    

    show abrir_olhos zorder 40
    
    p "{sc=1}{color=#ffaf54}The warmth of your skin… the scent of your flesh…"
    p "{sc=1}{color=#ffaf54}You have no idea what you’re doing to me right now…"
    
    show screen piscando
    pause 0.2
    show screen desmaio
    hide pegueivc
    show pegueivcb

    pause 0.1

    hide screen piscando
    hide screen desmaio
    show abrir_olhos
    pause 0.2
    p "{sc=1}{color=#ffaf54}{b}The way your breath falters… how your body yields, even in unconsciousness."
    p "{sc=1}{color=#ffaf54}{b}It's cruel of you, you know?"
    p "{sc=1}{color=#ffaf54}To be so {b}delici-- {nw=0.2}"
    p "{sc=1}{color=#ffaf54}{b}Lovely! so…{w=0.1} delicate."
    p "{sc=1}{color=#ffaf54}{b}And to leave me here,{w=0.1} on the edge of losing control."

    show screen piscando
    pause 0.2
    show screen desmaio
    show faminto

    pause 0.1

    hide screen piscando
    hide screen desmaio
    show abrir_olhos
    pause 0.2

    p "{sc=2}{color=#ffaf54}{b}I have so many thoughts, [titulo_pierrot]…"
    p "{sc=2}{color=#ffaf54}{b}So many desires…"
    p "{sc=2}{color=#ffaf54}{b}My hands ache to explore every inch of you."
    p "{sc=2}{color=#ffaf54}{b}My teeth itch at the thought of marking you. Claiming you as mine."
    p "{sc=2}{color=#ffaf54}{b}But… no. Not yet."

    show screen piscando
    pause 0.2
    show screen desmaio
    hide pegueivcb
    show faminto

    pause 0.1

    hide screen piscando
    hide screen desmaio
    show abrir_olhos
    pause 0.2

    p "{sc=2}{color=#ffaf54}{b}That wouldn’t be any fun, would it?"
    p "{sc=2}{color=#ffaf54}{b}You need to see."
    p "{sc=2}{color=#ffaf54}{b}To feel."
    p "{sc=2}{color=#ffaf54}{b}To… choose. Choose me."
    p "{sc=2}{color=#ffaf54}{b}Even though I’m completely obsessed with you right now."
    p "{sc=2}{color=#ffaf54}{b}I’ll wait."

    show screen piscando
    pause 1.0
    hide screen piscando with dissolve
    scene black with dissolve

    p "{sc=1}{color=#ffaf54}{b}For when you wake up..."
    p "{b}...I want your eyes on mine."

    pause 0.5
    play sound "audio/efeitos/correntes.mp3" volume 0.5

    pause 2.5

    #jump fimdejogo
    jump sequestro

 
label fimrosa: 

    play sound "audio/efeitos/furar.mp3" volume 0.5
    b "Oh! {w=0.2}That ticket gives you special access."
    
    b "Please, come this way."

    mc "Really? Wow, thanks!"

    scene circo at zoom_tendarosa

    pause 0.5

    scene tendarosa with dissolve

    mc "Huh? But it’s so dark in here..."

    mc "Hey{nw}"

    play sound "audio/efeitos/golpe.mp3" 
    with hpunch

    stop music fadeout 0.5
    scene black

    narrator "You feel a heavy blow before everything goes black."

    d "Take [persistent.p_objeto] to the back."

    show tendarosa at groggy_shake
    with slowdissolve

    mc "Mmhn... {color=#a0b0c0}(My head...)"
    mc "{color=#a0b0c0}(What...? I can’t move my legs... or my arms.)"
    mc "Hummm uhuunmb!!!"
    mc "{color=#a0b0c0}(My mouth is covered am I... tied up?)"

    play music "audio/musicas/drama.mp3" fadein 3.0 volume 0.1
    show tendarosaacesa
    if persistent.p_sujeito == "they":
        des "{color=#2c1ee6}Looks like they're awake. They're pretty."
    else:
        des "{color=#2c1ee6}Looks like [persistent.p_sujeito]’s awake. [persistent.p_sujeito]’s pretty."

    des "{color=#2c1ee6}Let’s begin. Anyone interested in this one?"

    show sombrastenda with dissolve
    pause 0.3

    des "{color=#ffaf54}No."
    des "{color=#41d623}Then I’m out too."
    des "{color=#ffaf54}..."
    des "{color=#961ee6}Hmm... No."
    des "{color=#e74c3c}Nope."
    des "{color=#2c1ee6}Hmm..  I think I’ll pass too."

    des "{color=#2c1ee6}Very well, then we can either relocate [persistent.p_objeto]..."

    show sombrastendaso
    des "{b}{cps=20}{color=#2c1ee6}Or devour [persistent.p_objeto]."

    stop music
    scene black

    narrator "You failed to catch the Pierrot’s attention... and met a tragic end."
    narrator "{color=#e61ecb}Ending: Missing."
    scene black

    jump fimdejogo

#label fimdejogo:
    #stop music fadeout 2.0
    #hide screen piscando
    #hide screen abrir_olhos
    #hide screen efeito_veneno with dissolve
    #scene black
    #pause 0.5

    #show text _("{size=50}{color=#ffffff}{b}Thanks for playing!\n If you'd like to see this project continue, leave a comment and rate it on the official page.") with dissolve
    #return
