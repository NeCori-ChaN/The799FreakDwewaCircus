default mc_nome = ""

default mesa1_concluida = False
default mesa2_concluida = False
default mesa3_concluida = False

default panfleto_1 = True
default panfleto_2 = True
default panfleto_3 = True
default panfleto_4 = True

default faca = False
default curativo = False

default ingresso_rosa = False

default envenenada = False

default final_rosa = False

default conversap = False
default oi_arlequim_played = False
default convite_aceito = False
default bolo = False
default pierrot_ficanoquarto = False
default arlequim_ficanoquarto = False

default marca_arlequim = False
default toquegentil = False
default mordida_negada = False
default jes_sombras_played = False

default espelhos_usados = {
    "a": False,
    "b": False,
    "c": False,
    "d": False,
    "h": False,
    "j": False,
    "p": False,
}

default espelhos_finalizados = False
default visitas_espelhoh = 0

default visita_azul = False
default visita_ciano = False
default visita_roxa = False
default visitas_preta = 0

default olhos_fechados_paraela = False
default floremcasa = False
default fala_noespelhododoc = False
default naoseguir = False

default persistent.unlocked_scenes = {
    "cena_01": False,
    "cena_02": False,
    
}



default nomes_especiais = {
    "neko": _("Hey, looks like we share the same name. Well, I guess that’s kind of common... anyway, good luck!"),
    "pierrot": _("You want to use my name, [titulo_pierrot]? But I like yours much more. Please, let me call you by your sweet name."),
    "harlequin": _("Are you in love with me? That’s why you want to use my name? Heh, better stick to yours."),
    "arlequim": _("Are you in love with me? That’s why you want to use my name? Heh, better stick to yours."),
    "bilheteiro": _("You and I both know that’s not your name. Follow the rules, do it properly."),
    "ticket taker": _("You and I both know that’s not your name. Follow the rules, do it properly."),
    "tickettaker": _("You and I both know that’s not your name. Follow the rules, do it properly... and write it correctly."),
    "jester": _("There’s only one Jester. We’re not having this conversation again, right? Good."),
    "doctor": _("Hah, that was a good one, but it won’t work. Use your own name sweetie."),
    "doutor": _("Hah, that was a good one, but it won’t work. Use your own name sweetie."),
}

default personagens = {
    "neko": n,        # p é o Character definido para Neko
    "pierrot": p,     # p é o Character definido para Pierrot
    "harlequin": a,
    "arlequim": a,
    "bilheteiro": b,
    "ticket taker": b,
    "tickettaker": b,
    "jester": j,
    "doctor": doc,
    "doutor": doc,
}


transform mexe_olhos:
    linear 1.0 xoffset 3 yoffset 1
    linear 1.0 xoffset -4 yoffset -1
    repeat


screen input_box():
    
    frame:
        xalign 0.5
        yalign 0.7
        xsize 380
        ysize 55
        has vbox

        input:
            default ""
            value VariableInputValue("mc_nome")
            length 20
            xalign 0.5
            xoffset 20  # Desloca o texto 20px para a direita
            # Adiciona a ação do Enter para confirmar
            
    textbutton "Ok":
        xalign 0.62
        yalign 0.7
        ysize 55
        xsize 55

        action Return()
        style "botao_ok"
        keysym('K_RETURN', 'K_KP_ENTER')

style botao_ok:
    color "#ee130c"
    bold True
    background "black"
    hover_background "#11c1e0d3"
    hover_color "#f8b117"
    padding (5, 10)


screen pratos:

    imagebutton:
        xalign 0.2
        yalign 0.62

        auto "images/objetos/prato_%s.png"
        action Jump("tutorial")
        activate_sound "audio/efeitos/prato.mp3"

screen mesas:

    imagebutton:
        xalign 0.604
        yalign 0.745

        auto "images/objetos/mesa1_%s.png"
        action [Hide("mesas"), Jump("mesa1")]
        activate_sound "audio/efeitos/pegar.mp3"
        sensitive not mesa1_concluida

    imagebutton:
        xalign 0.64
        yalign 0.857

        auto "images/objetos/mesa2_%s.png"
        action [Hide("mesas"), Jump("mesa2")]
        activate_sound "audio/efeitos/pegar.mp3"
        sensitive not mesa2_concluida

    imagebutton:
        xalign 0.72
        yalign 1.031

        auto "images/objetos/mesa3_%s.png"
        action [Hide("mesas"), Jump("mesa3")]
        activate_sound "audio/efeitos/pegar.mp3"
        sensitive not mesa3_concluida

transform zoom_mesa1:

    xalign 0.7
    yalign 0.5
    zoom 1.0
    linear 0.8 zoom 1.5

transform zoom_mesa2:

    xalign 0.7
    yalign 0.8
    zoom 1.0
    linear 0.8 zoom 1.5

transform zoom_mesa3:

    xalign 0.7
    yalign 1.0
    zoom 1.0
    linear 0.8 zoom 1.5

screen panfletos:

    if panfleto_1:
        imagebutton:
            auto "images/objetos/p1_%s.png"
            xpos 0
            ypos 820
            action SetVariable("panfleto_1", False)
            activate_sound "audio/efeitos/panfleto.mp3"

    if panfleto_2:
        imagebutton:
            auto "images/objetos/p2_%s.png"
            xpos 990
            ypos 950
            action SetVariable("panfleto_2", False)
            activate_sound "audio/efeitos/panfleto.mp3"

    if panfleto_3:
        imagebutton:
            auto "images/objetos/p3_%s.png"
            xpos 1100
            ypos 810
            action SetVariable("panfleto_3", False)
            activate_sound "audio/efeitos/panfleto.mp3"

    if panfleto_4:
        imagebutton:
            auto "images/objetos/p4_%s.png"
            xpos 1050
            ypos 720
            action SetVariable("panfleto_4", False)
            activate_sound "audio/efeitos/panfleto.mp3"

    # Verificação automática
    if not panfleto_1 and not panfleto_2 and not panfleto_3 and not panfleto_4:
        timer 0.5 action [Hide("panfletos"), Jump("cliente_suspeito")]

screen ingresso_rosa():
    zorder 10
    add "ingresso_rosa" xpos 600 ypos 90
    
image paranoia:
    "images/objetos/paranoia1.png" with dissolve
    pause 0.5
    "images/objetos/paranoia2.png" with dissolve
    pause 0.5
    "images/objetos/paranoia3.png" with dissolve
    pause 0.5
    "images/objetos/paranoia2.png" with dissolve
    pause 0.5
    repeat

#transform tilt_glitch:
    # Pequenos movimentos imprevisíveis
    linear 0.03 xoffset 4 yoffset -2
    linear 0.02 xoffset -6 yoffset 3
    linear 0.04 xoffset 2 yoffset -1
    linear 0.03 xoffset -3 yoffset 1
    linear 0.02 xoffset 1 yoffset 0
    linear 0.04 xoffset 0 yoffset 0
    
    # Pausa — parece que estabilizou
    pause 0.6
    
    # Tilt forte repentino com deslocamento
    linear 0.03 xoffset 30 yoffset -15
    linear 0.03 xoffset -30 yoffset 15
    linear 0.03 xoffset 0 yoffset 0

    # Opcional: repetir para efeito contínuo
    repeat

transform tilt_glitch:
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    linear 0.05 xoffset 3
    linear 0.05 xoffset -3
    linear 0.05 xoffset 0
    repeat

transform zoom_luzes:

    xalign 0.2
    yalign 0.5
    zoom 1.0
    linear 0.5 zoom 2.0

transform zoom_sangue:
    
    zoom 1.0
    linear 0.7 zoom 1.5 yalign 0.2

transform pulinho:
    xalign 0.5
    yoffset 0
    linear 0.1 yoffset -20
    linear 0.1 yoffset 0

screen ingresso_vermelho():
    zorder 10
    add "ingresso_vermelho" xpos 600 ypos 20

screen ingresso_vermelhofurado():
    zorder 10
    add "ingresso_vermelhofurado" xpos 600 ypos 20

image magica:
    "images/pierrot/1.png"
    pause 0.2
    "images/pierrot/2.png"
    pause 0.1
    "images/pierrot/3.png"
    pause 0.1
    "images/pierrot/4.png"
    pause 0.1
    "images/pierrot/5.png"
    pause 0.1
    "images/pierrot/6.png"
    pause 0.3
    "images/pierrot/7.png" with dissolve

transform susto:
    xalign 0.5
    ypos -500
    zoom 2.5
    linear 0.3 zoom 1.0 yalign 0.5

image tv:
    "images/objetos/t1.png"
    pause 0.5
    "images/objetos/t2.png"
    pause 0.5
    "images/objetos/t3.png"
    pause 0.5
    repeat

image estatica:
    "images/objetos/e1.png"
    pause 0.1
    "images/objetos/e2.png"
    pause 0.1
    "images/objetos/e3.png"
    pause 0.1
    repeat

image piscar:
    "images/objetos/piscar1.png" with slowdissolve
    pause 0.5
    "images/objetos/piscar2.png"
    pause 0.2
    "images/objetos/piscar3.png"
    pause 0.2
    "images/objetos/piscar2.png"
    pause 0.2
    "images/objetos/piscar1.png"
    pause 0.2
    
transform zoomlento:
    zoom 2.0
    xalign 0.5
    pause 2
    linear 10.0 zoom 2.5

transform zoomrapido:
    xalign 0.5
    linear 0.1 zoom 5

transform deslizar_direita:
    xalign 0.5
    linear 0.5 xalign 1.0

screen ingresso_verde():
    zorder 10
    add "ingresso_verde" xpos 600 ypos 90

transform roubaringresso:
    xalign 0.0
    linear 0.4 xalign 0.5
    pause 0.8
    linear 2.5 xalign 0.0

transform tilt_loop:
    linear 0.3 xoffset 2
    linear 0.8 xoffset -1
    repeat

transform deslizar_esquerda:
    xalign 0.5
    easeout 2 xpos 480

transform efeito_deslifade:
    xalign 0.5
    easeout 1 xalign 0.55

transform balanco_organico:

    easein 0.3 yoffset -3 rotate -3
    easeout 0.3 yoffset 3 rotate 3
    easein 0.2 yoffset 0 rotate 0
    repeat

transform deslizarsutil_dir:
    zoom 4.0
    xalign 0.2
    yalign 1
    linear 8.0 xalign 0.8

# Um screen leve para sobrepor texto por cima da caixa de diálogo
screen sobreposicao_texto(msg):
    on "show" action Play("sound", "audio/efeitos/glitch.mp3")
    add "gui/textbox.png":
        yalign 1.0 
    #text msg color "#ff0000" size 28 xalign 0.3 yalign 0.85 outlines [(2, "#000")]  # vermelho com sombra
    text msg size 28 xalign 0.3 yalign 0.85
    timer 2.0 action Hide("sobreposicao_texto")  # some depois de 2 segundos
    

screen sobreposicao_texto2(msg):
    on "show" action Play("sound", "audio/efeitos/glitch.mp3")
    zorder 50
    add "gui/textbox.png":
        yalign 1.0 
    text msg size 30 xalign 0.3 yalign 0.85
    timer 0.9 action Hide("sobreposicao_texto2")  # some depois de 2 segundos

transform glitch:
    xalign 0.5
    yalign 0.5
    xoffset -10
    pause 0.05
    xoffset 10
    pause 0.05
    xoffset -7
    pause 0.04
    xoffset 7
    pause 0.04
    xoffset 0

image glitch_colu:
    "images/glitch/c1.png"
    pause 0.1
    "images/glitch/c2.png"
    pause 0.1
    "images/glitch/c3.png"
    pause 0.1
    "images/glitch/c4.png"
    pause 0.1
    "images/glitch/c5.png"
    pause 0.1

image facas:
    "images/arlequim/1.png"
    pause 0.09
    "images/arlequim/2.png"
    pause 0.01
    "images/arlequim/3.png"
    pause 0.01
    "images/arlequim/4.png"
    pause 0.01
    "images/arlequim/alemaca2.png" with dissolve

screen animacao:
    zorder 10
    add "facas"

screen arlequim_maca:
    zorder 10
    add "images/arlequim/alemaca2.png" xpos -400

transform dramatic_pan():
    zoom 4.0
    xalign 0.4 yalign 0.35
    linear 2.0 xalign 0.42
    pause 0.3
    
    # Fade-out antes de inverter
    linear 0.3 alpha 0.0
    zoom 3.0
    xzoom -1.0
    yalign 0.2
    xalign 1.0
    linear 0.5 alpha 1.0

    linear 2.0 xalign 0.9
    pause 0.3

    # Fade-out antes de voltar ao normal
    linear 0.3 alpha 0.0
    xzoom 1.0
    zoom 3.0
    xalign 0.3
    yalign 0.8
    linear 0.3 alpha 1.0

    easeout 2.5 xalign 0.7

    linear 0.3 alpha 0.0
    zoom 1.0

transform deslizar_esquerdapalco:
    xalign 0.5
    easein 3.5 xpos 350

transform escurece_corpo:
    linear 2.0 alpha 0.1  # ou 0.0 se quiser apagar completamente
 
transform tilt_olhos:
    linear 0.2 xoffset 2
    linear 0.1 xoffset -3
    linear 0.3 xoffset 3
    linear 0.5 xoffset -1
    repeat

transform veneno_pulsante:
    alpha 0.0
    block:
        linear 3.0 alpha 0.2
        linear 3.0 alpha 0.05
        linear 3.0 alpha 0.3
        linear 3.0 alpha 0.1
        linear 3.0 alpha 0.4
        linear 3.0 alpha 0.2
        linear 3.0 alpha 0.5
        linear 3.0 alpha 0.3
        # adicione mais ciclos se quiser
        repeat

screen efeito_veneno():
    zorder 100  # ou qualquer valor bem alto para garantir

    add "images/veneno.png" at veneno_pulsante

screen piscando():
    zorder 99

    add "piscar" 

image abrir_olhos:
    "images/objetos/piscar3.png" with dissolve
    pause 0.5
    "images/objetos/piscar2.png"
    pause 0.2
    "images/objetos/piscar1.png"

screen desmaio:
    #zorder 80
    add "images/preto.png"

image olhos_bad:
    "images/objetos/olhobad1.png"
    pause 0.2
    "images/objetos/olhobad2.png"
    pause 0.2
    "images/objetos/olhobad3.png"
    pause 0.2
    "images/objetos/olhobad2.png"
    pause 0.2
    repeat

transform zoom_lento:
    
    linear 20.0 zoom 1.5 xalign 0.3 yalign 0.5

transform zoom_tendarosa:
    linear 1.0 zoom 1.5 xalign 0.0 yalign 1.0

transform groggy_shake:
    linear 0.1 xoffset -5 yoffset -5
    linear 0.5 xoffset 5 yoffset 5
    linear 1.1 xoffset -3 yoffset 3
    linear 0.4 xoffset 0 yoffset 0
    repeat

transform zoomlento2:
    zoom 2.5
    xalign 0.5
    linear 10.0 zoom 2.8

transform zoomrapido2:
    xalign 0.5
    easein 0.4 zoom 1.5

transform tilt_olhosv:
    linear 0.2 yoffset 2
    linear 0.1 yoffset -3
    linear 0.3 yoffset 3
    linear 0.5 yoffset -1
    repeat

image arle_surpreso:
    "images/arlequim/asur1.png"
    pause 0.2
    "images/arlequim/asur2.png"
    pause 0.2
    "images/arlequim/asur4.png"
    pause 0.2
    
transform zoomrapido3:
    xalign 1.0
    yalign 0.5
    easein 0.5 zoom 1.5

transform correndo(t=1.0):  # t é o tempo base da animação
    # Zoom em paralelo aos movimentos
    parallel:
        align(0.5, 0.5)
        ease 0.8 zoom 1.5  # zoom para dentro
    # Movimento vertical
    parallel:
        ease t/2 yoffset -15
        block:
            ease t yoffset +15
            ease t yoffset -15
            repeat
    # Movimento horizontal
    parallel:
        ease t xoffset -15
        block:
            ease t*2 xoffset +15
            ease t*2 xoffset -15
            repeat

transform zoomrapido4:
    xalign 0.5
    easein 0.4 zoom 1.8

transform deslizarsutil_dir2:
    
    xpos -100
    yalign 1
    easein 7.0 xalign 500

transform deslizar_bil:
    zoom 1.2
    xalign 0.7
    yalign 0.5
    easein 2 xalign 0.2

transform fade_in_olho:
    alpha 0.0
    linear 2.0 alpha 1.0

screen oi_arlequim():
    if not oi_arlequim_played:
        add Movie(play="images/oi.webm", channel="movie_bg", loop=False)
        timer 3.0 action [SetVariable("oi_arlequim_played", True), Hide("oi_arlequim")]
    
image arlecapat:
    "images/arlequim/arlecapa1.png" with dissolve
    pause 0.5 
    "images/arlequim/arlecapa2.png"with dissolve
    pause 0.5 
    "images/arlequim/arlecapa3.png" with dissolve
    pause 0.5 
    
image sanguinho:
    "images/objetos/san1.png" with dissolve
    pause 0.2
    "images/objetos/san2.png" with dissolve
    pause 0.2
    "images/objetos/san3.png" with dissolve
    pause 0.2
    "images/objetos/san4.png" with dissolve
    pause 0.2

transform olhospulse:
    xalign 0.5
    yalign 0.5
    linear 0.7 xzoom 1.01 yzoom 1.0
    linear 0.7 xzoom 1.0 yzoom 1.0
    linear 0.7 yalign 0.53
    repeat

transform zoom_centro:
    xalign 0.5
    yalign 0.5
    zoom 1.0
    linear 2.5 zoom 1.5 yalign 1.0

transform olhos_pulsando:
    anchor (0.5, 0.5)  # centraliza o ponto de zoom
    xalign 0.5
    yalign 0.5
    zoom 1.0
    linear 1.0 zoom 1.01
    linear 1.0 zoom 1.0
    repeat

image pp:
    "images/pierrot/pp1.png" with dissolve
    pause 4.0
    "images/pierrot/pp2.png" with dissolve
    pause 4.0
    repeat

image coracoes:
    "images/objetos/c1.png"
    pause 0.2
    "images/objetos/c2.png"
    pause 0.2
    "images/objetos/c3.png"
    pause 0.2
    "images/objetos/c4.png"
    pause 0.2
    "images/objetos/c5.png"
    pause 0.2
    repeat

image olho_abraco:
    "images/objetos/o1.png"
    pause 0.2
    "images/objetos/o2.png"
    pause 1.0
    "images/objetos/o1.png"
    pause 0.2
    "images/objetos/o2.png"
    pause 0.5

image luzes_doc:
    "images/objetos/l1.png"
    pause 0.1
    "images/objetos/l2.png"
    pause 0.1
    "images/objetos/l3.png"
    pause 0.1
    "images/objetos/l4.png"
    pause 0.05
    "images/objetos/l5.png"
    pause 0.05
    "images/objetos/l6.png"
    pause 0.05
    "images/objetos/l7.png"
    pause 0.05
    "images/objetos/l8.png"
    pause 0.05
    "images/objetos/l9.png"
    pause 0.05

screen contract_screen():
    modal True  # evita clicar em coisas atrás da tela

    # Ao clicar em qualquer lugar, fecha a screen
    key "mouseup_1" action Return()
    add "contrato"
    
    frame:
        xalign 0.5
        yalign 0.61
        xsize 640
        ysize 400
        background None
        
        vbox:
            spacing 10

            frame:
                background None
                xalign 0.5
                text _("{size=30}{color=#000000}{b}Contract{/b}") xalign 0.5 

            frame:
                background None
                xalign 0.5
                text _("{size=21}{color=#000000}{b}Individual consultation.") xalign 0.5

            # TEXTO NORMAL ALINHADO À ESQUERDA
            text _(
            
                "{size=19}{color=#000000}"
                "Feeling sick? Hallucinating things that don’t exist? Hearing\nvoices calling from the circus’s dark tents?\n"
                "Maybe it’s time you visit the Doctor.\n"
            ) xalign 0.2

            text _(
                "{size=18}{color=#000000}"
                "• Entering the tent is entirely your responsibility.\n"
                "• Once inside, only the Doctor decides when the consultation ends.\n"
                "• We aren’t liable for any injuries during this attraction.\n"
                "{/size}"
            )

            # LINHA FINAL CENTRALIZADA
            text _("{b}{color=#000000}Obey the Doctor and you’ll be fine.{/b}") xalign 0.5

transform zoom_meio:
    xalign 0.5
    yalign 0.3
    zoom 1.0
    linear 1.2 zoom 1.5

transform olho_dodr(d_in=1.5, hold=0.8, d_out=1.0):
    alpha 0.0                      
    linear d_in alpha 1.0          
    pause hold                     
    linear d_out alpha 0.0         

image doc_animacao:
    "images/doutor/doca1.png"
    pause 0.3
    "images/doutor/doca2.png"
    pause 0.3
    "images/doutor/doca3.png"
    pause 0.3
    repeat

init python:
    style.choice_button = Style(style.default)
    style.choice_button.size = 40
    style.choice_button.padding = (20, 10)
    style.choice_button.background = "gui/choice_idle_background.png"
    style.choice_button.hover_background = "gui/choice_hover_background.png"
    style.choice_button.font = "DejaVuSans.ttf"
    style.choice_button.color = "#ffffff"
    style.choice_button.hover_color = "#ff53c6"   # cor quando hover (rosa)

default no_button_text = "No"
default yes_button_text = "Yes"

screen doutor_escolhas:
    vbox:
        spacing 20
        align (0.5, 0.35)

        textbutton yes_button_text action Return("yes") style "choice_button":
            hovered SetVariable("yes_button_text", "{color=#e61ee6}Yes")
            unhovered SetVariable("yes_button_text", "Yes")

        textbutton no_button_text action Return("no") style "choice_button":
            hovered SetVariable("no_button_text", "{color=#e61ee6}Yes")
            unhovered SetVariable("no_button_text", "No")
            
            
image jesa:
    "images/jester/je2.png"
    pause 0.2
    "images/jester/je3.png"
    pause 0.3
    "images/jester/je2.png"
    pause 0.2
    "images/jester/je3.png"
    pause 0.3
    "images/jester/je2.png"
    pause 0.2
    
    
image glitchroxo:
    "images/glitch/g1.png"
    pause 0.2
    "images/glitch/g2.png"
    pause 0.3
    "images/glitch/g3.png"
    pause 0.1
    "images/glitch/g4.png"
    pause 0.2
    "images/glitch/g5.png"
    pause 0.5
    
transform zoom_peça:
    zoom 2.5
    xalign 0.3
    yalign 0.35
    linear 20.0 xalign 0.6

screen sobreposicao_texto3(msg):
    on "show" action Play("sound", "audio/efeitos/glitch.mp3")
    add "gui/textbox.png":
        yalign 1.0 
    
    text msg size 28 xalign 0.3 yalign 0.85
    timer 3.0 action Hide("sobreposicao_texto3")

image monglitch:
    "images/glitch/mmgore1.png"
    pause 0.1
    "images/glitch/mmgore2.png"
    pause 0.2
    "images/glitch/mmgore3.png"
    pause 0.1
    "images/glitch/mmgore1.png"
    pause 0.2

image devorar:
    "images/glitch/md0.png" with dissolve
    pause 0.2
    "images/glitch/md1.png" 
    pause 0.1
    "images/glitch/md2.png"
    pause 0.1
    "images/glitch/md3.png"
    pause 0.2
    "images/glitch/md4.png"
    pause 0.05

transform mordidamz:
    zoom 1.5
    xalign 0.5
    yalign 0.5
    easein 0.25 zoom 2.0 yalign 0.6

screen jes_sombras():
    if not jes_sombras_played:
        add Movie(play="images/jester/jestersombras.webm", channel="movie_bg", loop=False)
        timer 3.0 action [SetVariable("jes_sombras_played", True), Hide("jes_sombras")]

transform fadeolhojes:
    alpha 0.0
    linear 1.5 alpha 1.0  # sobe a opacidade em 1.5s
    linear 1.5 alpha 0.0  # desce a opacidade em 1.5s

image mordidam:
    "images/glitch/boca.png"
    pause 0.1
    "images/glitch/boca2.png" 
    pause 0.1
    "images/glitch/boca3.png"
    pause 0.1
    "images/glitch/boca4.png"
    pause 0.1

screen labirinto_espelhos:

    if not espelhos_usados["p"]:
        imagebutton:
            ypos -200
            auto "images/objetos/espelhop_%s.png"
            action [SetDict(espelhos_usados, "p", True), Jump("espelhop")]
    else:
        imagebutton:
            ypos -200
            idle "images/objetos/espelhop_idle.png"
            insensitive "images/objetos/espelhop_queb.png"
            action None
        #activate_sound "audio/efeitos/prato.mp3"

    if not espelhos_usados["j"]:
        imagebutton:
            xalign 0.2
            yalign 0.1

            auto "images/objetos/espelhoj_%s.png"
            action [SetDict(espelhos_usados, "j", True), Jump("espelhoj")]
    else:
        imagebutton:
            xalign 0.2
            yalign 0.1
            idle "images/objetos/espelhoj_idle.png"
            insensitive "images/objetos/espelhoj_inse.png"
            action None


    if not espelhos_usados["b"]:
        imagebutton:
            xalign 0.32
            yalign 0.3
        
            auto "images/objetos/espelhob_%s.png"
            action [SetDict(espelhos_usados, "b", True), Jump("espelhob")]
    else:
        imagebutton:
            xalign 0.32
            yalign 0.3
        
            idle "images/objetos/espelhob_idle.png"
            insensitive "images/objetos/espelhob_inse.png"
            action None

    if not espelhos_usados["a"]:
        imagebutton:
            xalign 1.0
            yalign 0.3
        
            auto "images/objetos/espelhoa_%s.png"
            action [SetDict(espelhos_usados, "a", True), Jump("espelhoa")]
    else:
        imagebutton:
            xalign 1.0
            yalign 0.3
        
            idle "images/objetos/espelhoa_idle.png"
            insensitive "images/objetos/espelhoa_inse.png"
            action None

    if not espelhos_usados["d"]:
        imagebutton:
            xalign 0.81
            yalign 0.1
        
            auto "images/objetos/espelhod_%s.png"
            action [SetDict(espelhos_usados, "d", True), Jump("espelhod")]
    else:
        imagebutton:
            xalign 0.81
            yalign 0.1
        
            idle "images/objetos/espelhod_idle.png"
            insensitive "images/objetos/espelhod_inse.png"
            action None


    imagebutton:
        xalign 0.7
        yalign 0.3
    
        idle "images/objetos/espelhoh_idle.png"
        action [
        SetVariable("visitas_espelhoh", visitas_espelhoh + 1),
        If(visitas_espelhoh >= 2,
            Jump("insistente"),
            Jump("espelhoh")
        )
    ]

    imagebutton:
        xalign 0.519
        ypos -20
    
        auto "images/objetos/espelhoc_%s.png"
        action Jump("espelhoc")

label labirinto_loop:
    scene labirinto
    call screen labirinto_espelhos
    $ renpy.pause(0.5, hard=True)
    #return

init python:
    import random

transform voz_eco1:
    alpha 0.0
    zoom 0.8
    linear 0.5 alpha 1.0 zoom 3.0
    pause 0.3
    linear 0.4 alpha 0.0


init python:
    import random, time

    palavras_vozes = [
        _("Freaks"),
        _("Abominations"),
        _("GET OUT"),
        _("MONSTERS"),
        _("They’re too tall"),
        _("HAHAHAHAHA"),
        _("Those eyes aren’t normal"),
        _("That smile isn’t normal"),
        _("Disgusting"),
        _("Horrible"),
        _("Get out of our town"),
        _("HAHAHAHAHA"),
        _("FREAKS")
    ]

    vozes_ativas = []

    def _spawn_glitch():
        # para tradução
        palavra_original = random.choice(palavras_vozes)

        palavra_formatada = "%(text)s"

        palavra = renpy.substitute(
            palavra_formatada % {"text": palavra_original}
        )

        x = random.uniform(0.05, 0.95)
        y = random.uniform(0.05, 0.9)
        size = random.uniform(0.9, 1.3)
        dur = random.uniform(0.25, 0.6)
        rot = random.uniform(-18, 18)
        jitter = random.uniform(-0.02, 0.02)

        item = {
            "text": palavra,
            "x": x,
            "y": y,
            "size": size,
            "dur": dur,
            "rot": rot,
            "jitter": jitter,
            "start": time.time()
        }
        vozes_ativas.append(item)

    def _tick_cleanup():
        now = time.time()
        vozes_ativas[:] = [v for v in vozes_ativas if now - v["start"] < v["dur"]]


transform voz_glitch(x, y, size, dur, rot, jitter):
    xpos x
    ypos y
    zoom size
    rotate rot
    alpha 0.0

    linear 0.04 alpha 1.0

    linear 0.02 xpos x + jitter ypos y - jitter
    linear 0.02 xpos x - jitter ypos y + jitter

    linear 0.02 xpos x + jitter*0.8 ypos y - jitter*0.8
    linear 0.02 xpos x - jitter*0.8 ypos y + jitter*0.8

    linear 0.02 xpos x + jitter*0.5 ypos y - jitter*1.5
    linear 0.02 xpos x - jitter*0.5 ypos y + jitter*1.5

    pause max(0.0, dur - 0.24)

    linear 0.06 alpha 0.0


screen vozes_glitch(spawn_min=0.05, spawn_max=0.35):

    timer 0.06 repeat True action Function(_maybe_spawn, spawn_min, spawn_max)
    timer 0.08 repeat True action Function(_tick_cleanup)

    for v in vozes_ativas:
        text v["text"]:
            at voz_glitch(v["x"], v["y"], v["size"], v["dur"], v["rot"], v["jitter"])
            size int(52 * v["size"])
            color "#fa0202"
            outlines [(2, "#00000088", 0, 0)]
            bold True


init python:
    def _maybe_spawn(min_t, max_t):
        if random.random() < 0.22:
            _spawn_glitch()


image fogonoparquinho:
    "images/objetos/reflexoh1.png" with dissolve
    pause 0.7
    "images/objetos/reflexoh2.png" with dissolve
    pause 0.7
    "images/objetos/reflexoh3.png" with dissolve
    pause 0.7
    "images/objetos/reflexoh2.png" with dissolve
    pause 0.7
    repeat

image misterioso:
    "images/objetos/h1.png" with dissolve
    pause 0.5
    "images/objetos/h2.png"
    pause 0.3
    "images/objetos/h1.png"
    pause 0.3
    "images/objetos/h2.png"
    pause 0.3
    repeat

transform olhospulse2:
    xalign 0.5
    yalign 0.5
    linear 0.7 xzoom 1.0 yzoom 1.0
    linear 0.7 xzoom 1.05 yzoom 1.0
    linear 0.7 yalign 0.53
    repeat

screen maoc:
    zorder 30
    
    add "images/objetos/maotrasc.png" at descer
    add "gui/textbox.png" at descer: 
        yalign 1.0
    add "images/objetos/maofrentec.png" at descer
 

transform descer:
    xalign 0.5
    yalign 1.0
    pause 0.2

    linear 0.15 ypos 1.5

transform zoomcolu:
    linear 0.2 zoom 2.0 xalign 0.0

image riscos:
    "images/objetos/risco1.png"
    pause 0.1
    "images/objetos/risco2.png"
    pause 0.1
    "images/objetos/risco3.png"
    pause 0.1
    repeat

transform deslizar_hmns:
    xalign 0.7
    yalign 0.5

    easein 0.5 xalign 0.8

image sanguefeito:
    "images/objetos/sanguefeito1.png"
    pause 0.1
    "images/objetos/sanguefeito2.png"
    pause 0.1
    "images/objetos/sanguefeito3.png"
    pause 0.1

transform zoom_saidadoespelho:
    xalign 0.5
    yalign 0.3
    linear 0.5 zoom 1.5 xalign 0.9

transform pulinho2:
    
    yoffset 0
    linear 0.1 yoffset -20
    linear 0.1 yoffset 0

transform movimento_vindodir:
    xpos 1200
    ypos -300
    linear 0.3 ypos -400
    easeout 0.3 xalign 1.2 yalign -1.9

transform movimento_vindoesq:
    xpos -500
    ypos -300
    linear 0.3 ypos -400
    easeout 0.3 xalign -0.2 yalign -1.9

transform movimento_voltandodir:
    xalign 1.2
    yalign -1.9
    easeout 0.3 yalign -1.5
    linear 0.1 yalign -2.5
    easein 0.4 xalign 1.8  yalign -5.0

transform movimento_voltandoesq:
    xalign -0.2
    yalign -1.9
    easeout 0.3 yalign -1.5
    linear 0.1 yalign -2.5
    easein 0.4 xalign -0.8 yalign -5.0

transform movimento_vindodir2:
    xalign 1.8
    yalign -5.0
    linear 0.3 yalign -6.0
    easeout 0.3 xalign 1.2 yalign -1.9
    pause 0.2
    easeout 0.3 xalign 1.8 yalign -5.0

transform rejeitado_esquerda:
    xalign -0.8
    yalign -5.0
    linear 0.3 yalign -6.0
    easeout 0.3 xalign -0.2 yalign -1.9
    pause 0.2
    easein 0.3 xalign -2.0
    pause 0.1
    easeout 0.3 xalign -0.8 yalign -5.0

transform escolhido_tutorial:
    linear 0.1 xalign 0.5

transform movimento_vindoesq2:
    xalign -0.8
    yalign -5.0
    linear 0.3 yalign -6.0
    easeout 0.3 xalign -0.2 yalign -1.9
    pause 0.2
    easeout 0.3 xalign -0.8 yalign -5.0

transform rejeitado_direita:
    xalign 1.8
    yalign -5.0
    linear 0.3 yalign -6.0
    easeout 0.3 xalign 1.2 yalign -1.9
    pause 0.2
    easein 0.3 xalign 3.0
    pause 0.1
    easeout 0.3 xalign 1.8 yalign -5.0

transform fimtutorial:
    yalign -5.0
    easein 3.0 yalign -15.0

label nome_columbinad1:
    show black with dissolve 
    pause 0.4
    
    show glitch_columsangue zorder 10:
        alpha 0.8
    pause 0.2
    show c6 at glitch_dela
    
    show text _("{glitch=50}{size=100}{b}{color=#e61ee6}We’re not the same") zorder 11
    pause 0.5
    hide c6
    show text _("{glitch=20}{size=100}{b}{color=#e61ee6}You and I") zorder 11
    pause 1.0
    show glitchroxo at glitch_dela
    pause 1.0
    show text _("{glitch=20}{size=100}{b}{color=#e61ee6}I didn’t want to") zorder 11
    hide glitchroxo
    pause 1.0
    show devorar at glitch_dela
    pause 1.0
    show text _("{glitch=20}{size=100}{b}{color=#e61ee6}But our fate was cursed") zorder 11
    hide devorar
    pause 1.0
    show monglitch at glitch_dela:
        zoom 2.0
        xalign 1.0
        yalign 0.2
    pause 0.3
    hide monglitch
    show text _("{glitch=20}{size=100}{b}{color=#e61ee6}I should have listened to him") zorder 11
    pause 1.0
    show g5 at glitch_dela:
        zoom 4.0
        xalign 0.5
        yalign 0.0
    pause 1.0
    
    show text _("{glitch=20}{size=100}{b}{color=#e61ee6}It was my fault") zorder 11
    hide g5
    pause 1.0
    show text _("{glitch=20}{size=100}{b}{color=#e61ee6}Now they are broken") zorder 11
    pause 1.8
    scene black
    jump nomes

label nome_columbinad2:
    show preto with dissolve  
    pause 0.4
    
    show glitch_columsangue zorder 10:
        alpha 0.8
    pause 0.2
    show c6 at glitch_dela zorder 5
    
    show text _("{glitch=50}{size=100}{b}{color=#e61ee6}We’re not the same") zorder 11
    pause 0.5
    hide c6
    show text _("{glitch=20}{size=100}{b}{color=#e61ee6}You and I") zorder 11
    pause 1.0
    show glitchroxo at glitch_dela zorder 5
    pause 1.0
    show text _("{glitch=20}{size=100}{b}{color=#e61ee6}I didn’t want to") zorder 11
    hide glitchroxo
    pause 1.0
    show devorar at glitch_dela zorder 5
    pause 1.0
    show text _("{glitch=20}{size=100}{b}{color=#e61ee6}But our fate was cursed") zorder 11
    hide devorar
    pause 1.0
    show monglitch at glitch_dela zorder 5:
        zoom 2.0
        xalign 1.0
        yalign 0.2
    pause 0.3
    hide monglitch
    show text _("{glitch=20}{size=100}{b}{color=#e61ee6}I should have listened to him") zorder 11
    show g5 at glitch_dela zorder 5:
        zoom 4.0
        xalign 0.5
        yalign 0.0
    pause 1.0
    
    show text _("{glitch=20}{size=100}{b}{color=#e61ee6}It was my fault") zorder 11
    hide g5
    pause 1.0
    show text _("{glitch=20}{size=100}{b}{color=#e61ee6}Now they are broken") zorder 11
    pause 1.5
    hide glitch_columsangue
    hide preto
    hide text
    jump nomedenovo

image glitch_columsangue:
    "images/objetos/glitchn1.png"
    pause 0.3
    "images/objetos/glitchn2.png"
    pause 0.2
    "images/objetos/glitchn3.png"
    pause 0.2
    "images/objetos/glitchn2.png"
    pause 0.2
    repeat

transform glitch_dela:
    xoffset 0
    yoffset 0
    linear 0.03 xoffset -5 yoffset 5
    linear 0.03 xoffset 5 yoffset -5
    linear 0.03 xoffset -3 yoffset 3
    repeat

image reflexojester:
    "images/objetos/reflexoj3.png" with dissolve
    pause 0.5
    "images/objetos/reflexoj2.png" with dissolve
    pause 0.5
    repeat

transform olhobilmaupos:
    xalign 0.525
    ypos -8

image icones_nekobueno:
    "images/objetos/icones1.png"
    pause 0.5
    "images/objetos/icones2.png"
    pause 0.5
    repeat


screen site_oficial():

    frame:
        background "#000000C0"
        xalign 0.5
        yalign 0.3
        xsize 1800
        ysize 500
        padding (20, 20)

        vbox:
            spacing 10
            xalign 0.5
            yalign 0.2

            text _("Support the Official Release") size 70 color "#cc0606" bold True xalign 0.5
            text _("This game is available only through its official website:") size 30 color "#ffffff" xalign 0.5
            text "⭐ {a=https://garula.itch.io/the-freak-circus}https://garula.itch.io/the-freak-circus{/a} ⭐" size 30 color "#ffaf54" xalign 0.5
            text _("If you found it elsewhere, it was shared {b}without permission.") size 30 color "#ffffff" xalign 0.5 yoffset 20
            text _("Please support the official release so future updates,\n stories, and events can keep coming to life.") size 30 color "#ffffff" xalign 0.5
            text _("{b}Thank you for respecting the work behind The Freak Circus.") size 30 color "#ffaf54" xalign 0.5 yoffset 20

    add "icones_nekobueno" xalign 0.5 yalign 0.9
