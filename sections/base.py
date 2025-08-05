class Section:
    """A Section on the tape"""

    def __init__(self, title: str, *args, **kwargs):
        self.title = title

    def reset(self):
        p.set_with_default()

    def print_title(self):
        p.set_with_default(
            bold=True,
            underline=True,
            )
        p.textln(self.title)
        p.set_with_default()

    def print_bulleted_list(self, items: list, bullet: str = "-"):
        for i in items:
            p.textln(f"{bullet} {i}")

    def string(self, s: str):
        p.text(s)

    def print(self):
        self.title()

class ImageSection(Section):
    pass

class Ticket(Section):
    pass





        
