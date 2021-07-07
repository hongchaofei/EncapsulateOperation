
class Variable(object):

    AutoVariableNum = 0

    def __init__(self, name=None, owner=None, op_code=None):
        super(Variable, self).__init__()
        self.owner = owner
        self.value = None
        if not name:
            self.name = 'autoname' + str(Variable.AutoVariableNum)
            Variable.AutoVariableNum += 1
        else:
            self.name = name


        self.op_code = op_code





    def __add__(self, other):
        res = Variable(op_code=('add', self, other))
        return res

    def __sub__(self, other):
        res = Variable(op_code=('sub', self, other))
        return res
