

init python:
    class GlitchText(renpy.Displayable,str):
        def __init__(self, child, amount, **kwargs):
            super(GlitchText, self).__init__(**kwargs)
            if isinstance(child, (str, unicode)):
                self.child = Text(child)
            else:
                self.child = child
            self.amount = amount

        #def __new__(cls, child, amount, **kwargs):
            #if isinstance(child, (str, unicode)):
                #return str.__new__(cls, child)

        def render(self, width, height, st, at):
            child_render = renpy.render(self.child, width, height, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            y = 0
            while y < self.height:
                glitch_occurs = renpy.random.random() * 100 < self.amount
                if glitch_occurs:
                    curr_height = renpy.random.randint(-10,10)
                else:
                    curr_height = renpy.random.randint(0,10)
                curr_offset = renpy.random.randint(-10,10)
                curr_surface = child_render.subsurface((0,y,self.width,curr_height))
                if glitch_occurs:
                    render.subpixel_blit(curr_surface, (curr_offset, y))
                else:
                    render.subpixel_blit(curr_surface, (0, y))
                if curr_height > 0:
                    y += curr_height
                else:
                    y -= curr_height
            renpy.redraw(self, 0.1) #renpy.redraw(self,0)
            return render

    # Argument is the percertage of the time it'll apply a random offset to a randomly sized slice.
    # offset_percent: (Float between 0.0-100.0) Percentage chance a random block of the render will be offset.
    # 0 will cause it to never occur. 100 will cause an offset on every line.
    # Example: {glitch=59.94}Text{/glitch}
    def glitch_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            argument = 10.0
        else:
            argument = float(argument)
        my_style = DispTextStyle()
        text_combined = ""
        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:
                text_combined += text
            elif kind == renpy.TEXT_TAG:
                # Mantém as tags internas (como {color}, {b}, etc.)
                text_combined += "{" + text + "}"
            elif kind == renpy.TEXT_TAG_WITH_ARGUMENT:
                tagname, arg = text.split("=", 1)
                text_combined += "{" + tagname + "=" + arg + "}"
            else:
                new_list.append((kind, text))  # Preserve outros tipos

        char_disp = GlitchText(my_style.apply_style(text_combined), argument)
        new_list.insert(0, (renpy.TEXT_DISPLAYABLE, char_disp))
        return new_list

    config.custom_text_tags["glitch"] = glitch_tag
