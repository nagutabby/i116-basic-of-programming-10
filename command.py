from cname import CName

class Command():
    def __init__(self, cname, x) -> None:
        self.cname = cname
        if cname == CName.PUSH:
            self.num = x
        elif cname == CName.LOAD:
            self.name = x
        elif cname == CName.STORE:
            self.name = x
    def __str__(self) -> str:
        if self.cname == CName.PUSH:
            return f'{self.cname}({self.num})'
        elif self.cname == CName.LOAD:
            return f'{self.cname}({self.name})'
        elif self.cname == CName.STORE:
            return f'{self.cname}({self.name})'
        else:
            return str(self.cname)

