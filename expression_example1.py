from parse_tree import VariableParseTree, NumberParseTree, AssignmentParseTree, AdditionParseTree, MultiplicationParseTree, RemainderParseTree, SequentialCompositionParseTree
from list_to_string import l2s

x = VariableParseTree('x')
y = VariableParseTree('y')

two = NumberParseTree(2)
three = NumberParseTree(3)
ten = NumberParseTree(10)

assignment1 = AssignmentParseTree(x, ten)
expression1 = MultiplicationParseTree(x, two)
assignment2 = AssignmentParseTree(y, expression1)
expression2 = AdditionParseTree(x, y)
assignment3 = AssignmentParseTree(x, expression2)
expression3 = RemainderParseTree(x, three)
assignment4 = AssignmentParseTree(y, expression3)

program1 = SequentialCompositionParseTree(assignment1, assignment2)
program2 = SequentialCompositionParseTree(program1, assignment3)
program3 = SequentialCompositionParseTree(program2, assignment4)

print(program3)
print(program3.interpret({}))
print(l2s(program3.compile()))
