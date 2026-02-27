
default player_pronouns = None

default persistent.pronome = _("neutro")
default persistent.p_genero_pt = "neutro"


# Pronomes em português:
default persistent.p_sujeito_pt = "ele"
default persistent.p_objeto_pt = "ele"
default persistent.p_possessivo_pt = "dele"


# Pronomes sujeito, objeto e possessivo
default persistent.p_sujeito = _("they")
default persistent.p_objeto = _("them")
default persistent.p_possessivo = _("theirs")

#Lembrete referência ao gênero como string
default persistent.p_genero = "neutro"  # "feminino", "masculino" e "neutro"

#Pierrot
default titulo_pierrot = _("my dear")
define titulos_pierrot = {
    "feminino": _("my lady"),
    "masculino": _("my lord"),
    "neutro": _("my dear")
}

#Arlequim

default titulo_arlequim = _("dear one")
define titulos_arlequim = {
    "feminino": _("ma'am"),
    "masculino": _("sir"),
    "neutro": _("dear one")
}

# dicionario traduzido

define titulos_pierrot_traduzido = {
    "feminino": _("milady"),
    "masculino": _("milorde"),
    "neutro": _("meu bem")
}

define titulos_arlequim_traduzido = {
    "feminino": _("madame"),
    "masculino": _("lorde"),
    "neutro": _("meu bem")
}

define artigos_portugues = {
    "feminino": "a",
    "masculino": "o",
    "neutro": "e"
}


#JP
define titulos_pierrot_JP = {
    "feminino": _("マイレディ"),
    "masculino": _("マイロード"),
    "neutro": _("マイディアー")
}

define titulos_arlequim_JP = {
    "feminino": _("マダム"),
    "masculino": _("サー"),
    "neutro": _("親愛なる君")
}



label escolha_pronomes:

    menu:
        "He / Him":
            $ persistent.p_sujeito = _("he")
            $ persistent.p_objeto = _("him")
            $ persistent.p_possessivo = _("his")
            #pt
            $ persistent.p_sujeito_pt = "ele"
            $ persistent.p_objeto_pt = "ele"
            $ persistent.p_possessivo_pt = "dele"

            # chinês
            $ persistent.p_sujeito_cn = "他"
            $ persistent.p_objeto_cn = "他"
            $ persistent.p_possessivo_cn = "他的"

            #JP
            $ persistent.p_sujeito_jp = "彼"
            $ persistent.p_objeto_jp = "彼"
            $ persistent.p_possessivo_jp = "彼の"
            $ persistent.p_eu_jp = "僕"

            $ persistent.p_genero = _("masculino")
            $ persistent.p_genero_pt = "masculino"
            $ player_pronouns = "he"
            
        "She / Her":
            $ persistent.p_sujeito = _("she")
            $ persistent.p_objeto = _("her")
            $ persistent.p_possessivo = _("hers")
            #pt
            $ persistent.p_sujeito_pt = "ela"
            $ persistent.p_objeto_pt = "ela"
            $ persistent.p_possessivo_pt = "dela"

            # chinês
            $ persistent.p_sujeito_cn = "她"
            $ persistent.p_objeto_cn = "她"
            $ persistent.p_possessivo_cn = "她的"

            #JP
            $ persistent.p_sujeito_jp = "彼女"
            $ persistent.p_objeto_jp = "彼女"
            $ persistent.p_possessivo_jp = "彼女の"
            $ persistent.p_eu_jp = "私"

            $ persistent.p_genero = _("feminino")
            $ persistent.p_genero_pt = "feminino"
            $ player_pronouns = "she"
            
        "They / Them":
            $ persistent.p_sujeito = _("they")
            $ persistent.p_objeto = _("them")
            $ persistent.p_possessivo = _("theirs")
            #pt
            $ persistent.p_sujeito_pt = "elu"
            $ persistent.p_possessivo_pt = "delu"

            # chinês
            $ persistent.p_sujeito_cn = "TA"
            $ persistent.p_objeto_cn = "TA"
            $ persistent.p_possessivo_cn = "TA的"

            #JP
            $ persistent.p_sujeito_jp = "この人"
            $ persistent.p_objeto_jp = "あの人"
            $ persistent.p_possessivo_jp = "あの人の"
            $ persistent.p_eu_jp = "自分"
            
            $ persistent.p_genero = _("neutro")
            $ persistent.p_genero_pt = "neutro"
            $ player_pronouns = "they"

    $ titulo_pierrot = titulos_pierrot[persistent.p_genero]
    $ titulo_arlequim = titulos_arlequim[persistent.p_genero]      

    return
