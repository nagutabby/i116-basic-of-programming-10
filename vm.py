from stack import EmptyStack
from list_to_string import l2s
from custom_exception import VMError, DivisionByZeroException
from cname import CName

class VM():
    def __init__(self, cl) -> None:
        self.clist = cl
        self.stk = EmptyStack()
        self.environment: dict = {}
    def str(self) -> str:
        return f'stack: {self.stk}, command list: {l2s(self.clist)}, environment: {self.environment}'

    def run(self):
        for com in self.clist:
            if com.cname == CName.PUSH:
                self.stk = self.stk.push(com.num)
            elif com.cname == CName.MONE:
                if self.stk.is_empty():
                    raise VMError('stk is empty for mone')
                x = self.stk.top()
                self.stk = self.stk.pop().push(-1 * x)
            elif com.cname == CName.MUL:
                if self.stk.is_empty_or_one():
                    raise VMError('stk consists of 1 or 0 element for mul')
                y = self.stk.top()
                x = self.stk.pop().top()
                self.stk = self.stk.pop().pop().push(x * y)
            elif com.cname == CName.DIV:
                if self.stk.is_empty_or_one():
                    raise VMError('stk consists of 1 or 0 element for div')
                y = self.stk.top()
                x = self.stk.pop().top()
                if y == 0:
                    raise DivisionByZeroException('division by zero in VM')
                self.stk = self.stk.pop().pop().push(x / y)
            elif com.cname == CName.REM:
                if self.stk.is_empty_or_one():
                    raise VMError('stk consists of 1 or 0 element for rem')
                y = self.stk.top()
                x = self.stk.pop().top()
                if y == 0:
                    raise DivisionByZeroException('division by zero in VM')
                self.stk = self.stk.pop().pop().push(x % y)
            elif com.cname == CName.ADD:
                if self.stk.is_empty_or_one():
                    raise VMError('stk consists of 1 or 0 element for add')
                y = self.stk.top()
                x = self.stk.pop().top()
                self.stk = self.stk.pop().pop().push(x + y)
            elif com.cname == CName.SUB:
                if self.stk.is_empty_or_one():
                    raise VMError('stk consists of 1 or 0 element for sub')
                y = self.stk.top()
                x = self.stk.pop().top()
                self.stk = self.stk.pop().pop().push(x - y)
            elif com.cname == CName.EQ:
                if self.stk.is_empty_or_one():
                    raise VMError('stk consists of 1 or 0 element for eq')
                y = self.stk.top()
                x = self.stk.pop().top()
                if x == y:
                    self.stk = self.stk.pop().pop().push(1)
                else:
                    self.stk = self.stk.pop().pop().push(0)
            elif com.cname == CName.NEQ:
                if self.stk.is_empty_or_one():
                    raise VMError('stk consists of 1 or 0 element for neq')
                y = self.stk.top()
                x = self.stk.pop().top()
                if x == y:
                    self.stk = self.stk.pop().pop().push(0)
                else:
                    self.stk = self.stk.pop().pop().push(1)
            elif com.cname == CName.LT:
                if self.stk.is_empty_or_one():
                    raise VMError('stk consists of 1 or 0 element for lt')
                y = self.stk.top()
                x = self.stk.pop().top()
                if x < y:
                    self.stk = self.stk.pop().pop().push(1)
                else:
                    self.stk = self.stk.pop().pop().push(0)
            elif com.cname == CName.GT:
                if self.stk.is_empty_or_one():
                    raise VMError('stk consists of 1 or 0 element for gt')
                y = self.stk.top()
                x = self.stk.pop().top()
                if x > y:
                    self.stk = self.stk.pop().pop().push(1)
                else:
                    self.stk = self.stk.pop().pop().push(0)
            elif com.cname == CName.AND:
                if self.stk.is_empty_or_one():
                    raise VMError('stk consists of 1 or 0 element for and')
                y = self.stk.top()
                x = self.stk.pop().top()
                if x == 0 or y == 0:
                    self.stk = self.stk.pop().pop().push(0)
                else:
                    self.stk = self.stk.pop().pop().push(1)
            elif com.cname == CName.OR:
                if self.stk.is_empty_or_one():
                    raise VMError('stk consists of 1 or 0 element for or')
                y = self.stk.top()
                x = self.stk.pop().top()
                if x == 0 and y == 0:
                    self.stk = self.stk.pop().pop().push(0)
                else:
                    self.stk = self.stk.pop().pop().push(1)
            elif com.cname == CName.LOAD:
                try:
                    x = self.environment[com.name]
                except KeyError:
                    raise UndefinedVar('undefined variable')
                self.stk = self.stk.push(x)
            elif com.cname == CName.STORE:
                if self.stk.is_empty():
                    raise VMError('stk is empty for store')
                self.environment[com.name] = self.stk.top()
                self.stk = self.stk.pop()
            else:
                raise VMError("An invalid command was met!")
        if self.stk.is_empty():
            raise VMError('stk is empty when vm terminates!')
        return self.environment
