
class Variable(object):

    AutoVariableNum = 0

    def __init__(self, name=None, owner=None, op_code=None):
        super(Variable, self).__init__()
        self.owner = owner
        self.backend_variable_dict = None
        if not name:
            self.name = '[tmpVar]' + str(Variable.AutoVariableNum)
            Variable.AutoVariableNum += 1
        else:
            self.name = name

        self.op_code = op_code
        self.update_var = None



    def update(self, other):
        assert isinstance(other, Variable)
        self.value = other.value


    def __add__(self, other):
        assert isinstance(other, Variable)
        # 如果是float的constant数据应该也要支持
        return Variable(op_code=('add', self, other))

    def __sub__(self, other):
        assert isinstance(other, Variable)
        return Variable(op_code=('sub', self, other))

    def __mul__(self, other):
        assert isinstance(other, Variable)
        return Variable(op_code=('mul', self, other))

    def __truediv__(self, other):
        assert isinstance(other, Variable)
        return Variable(op_code=('div', self, other))

