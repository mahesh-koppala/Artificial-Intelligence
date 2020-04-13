

import sys
from copy import copy



class logical_expression:
    

    
    def __init__(self):
        self.symbol = ['']
        self.connective = ['']
        self.subexpressions = []


def print_expression(expression, separator):
    
    if expression == 0 or expression == None or expression == '':
        print '\nINVALID\n'

    elif expression.symbol[0]:  
        sys.stdout.write('%s' % expression.symbol[0])

    else:  
        sys.stdout.write('(%s' % expression.connective[0])
        for subexpression in expression.subexpressions:
            sys.stdout.write(' ')
            print_expression(subexpression, '')
            sys.stdout.write('%s' % separator)
        sys.stdout.write(')')


def read_expression(input_string, counter=[0]):
    

    result = logical_expression()
    length = len(input_string)
    while True:
        if counter[0] >= length:
            break

        if input_string[counter[0]] == ' ':  
            counter[0] += 1
            continue

        elif input_string[counter[0]] == '(':  
            counter[0] += 1
            read_word(input_string, counter, result.connective)
            read_subexpressions(input_string, counter, result.subexpressions)
            break

        else:  
            read_word(input_string, counter, result.symbol)
            break
    return result


def read_subexpressions(input_string, counter, subexpressions):
    
    length = len(input_string)
    while True:
        if counter[0] >= length:
            print '\nUnexpected end of input.\n'
            return 0

        if input_string[counter[0]] == ' ':  
            counter[0] += 1
            continue

        if input_string[counter[0]] == ')':  
            counter[0] += 1
            return 1

        else:
            expression = read_expression(input_string, counter)
            subexpressions.append(expression)


def read_word(input_string, counter, target):
    
    word = ''
    while True:
        if counter[0] >= len(input_string):
            break

        if input_string[counter[0]].isalnum() or input_string[counter[0]] == '_':
            target[0] += input_string[counter[0]]
            counter[0] += 1

        elif input_string[counter[0]] == ')' or input_string[counter[0]] == ' ':
            break

        else:
            print('Unexpected character %s.' % input_string[counter[0]])
            sys.exit(1)


def valid_expression(expression):
    
    if expression.symbol[0]:
        return valid_symbol(expression.symbol[0])

    if expression.connective[0].lower() == 'if' or expression.connective[0].lower() == 'iff':
        if len(expression.subexpressions) != 2:
            print('Error: connective "%s" with %d arguments.' %
                  (expression.connective[0], len(expression.subexpressions)))
            return 0

    elif expression.connective[0].lower() == 'not':
        if len(expression.subexpressions) != 1:
            print('Error: connective "%s" with %d arguments.' %
                  (expression.connective[0], len(expression.subexpressions)))
            return 0

    elif expression.connective[0].lower() != 'and' and \
            expression.connective[0].lower() != 'or' and \
            expression.connective[0].lower() != 'xor':
        print('Error: unknown connective %s.' % expression.connective[0])
        return 0

    for subexpression in expression.subexpressions:
        if not valid_expression(subexpression):
            return 0
    return 1


def valid_symbol(symbol):
    
    if not symbol:
        return 0

    for s in symbol:
        if not s.isalnum() and s != '_':
            return 0
    return 1



def check_true_false(knowledge_base, statement, symbolslist, negation, symbols, model):
    try:
        output_file = open('result.txt', 'w')
    except:
        print('failed to create output file')
    statement_true = tt_check_all(knowledge_base, statement, symbols, model)
    statement_false = tt_check_all(knowledge_base, negation, symbols, model)
    if statement_true == True and statement_false == False:
        output_file.write('definitely true')
        print 'definitely true'
    elif statement_true == False and statement_false == True:
        output_file.write('definitely false')
        print 'definitely false'
    elif statement_true == False and statement_false == False:
        output_file.write('possibly true, possibly false')
        print 'possibly true, possibly false'
    elif statement_true == True and statement_false == True:
        output_file.write('both true and false')
        print 'both true and false'
    else:
        output_file.write('Error')
    print
    output_file.close()



def get_symbols(expression, symbols):
    if expression.symbol[0]:
        symbols.append(expression.symbol[0])
    for subexpression in expression.subexpressions:
        get_symbols(subexpression, symbols)


def expand_model(model, sym_key, value):
    model[sym_key] = value
    return model



def tt_check_all(kb, alpha, symbols, model):
    if not symbols:
        if pl_true(kb, model):
            return pl_true(alpha, model)
        else:
            return True
    p = symbols[0]
    rest = symbols[1:]
    return tt_check_all(kb, alpha, rest, expand_model(model, p, True)) \
           and tt_check_all(kb, alpha, rest, expand_model(model, p, False))



def pl_true(expression, model):
    if expression.connective[0].lower() == 'and':
        tru_value = True
        for i, subexpression in enumerate(expression.subexpressions):
            if (i == 0):
                tru_value = pl_true(subexpression, model)
                continue;
            tru_value = tru_value and pl_true(subexpression, model)
        return tru_value
    elif expression.connective[0].lower() == 'or':
        tru_value = True
        for i, subexpression in enumerate(expression.subexpressions):
            if (i == 0):
                tru_value = pl_true(subexpression, model)
                continue;
            tru_value = tru_value or pl_true(subexpression, model)
        return tru_value
    elif expression.connective[0].lower() == 'not':
        tru_value = not pl_true(expression.subexpressions[0], model)
        return tru_value
    elif expression.connective[0].lower() == 'xor':
        tru_value = True
        for i, subexpression in enumerate(expression.subexpressions):
            if (i == 0):
                tru_value = pl_true(subexpression, model)
                continue;
            tru_value = tru_value ^ pl_true(subexpression, model)
        return tru_value
    elif expression.connective[0].lower() == 'if':
        exp1 = pl_true(expression.subexpressions[0], model)
        exp2 = pl_true(expression.subexpressions[1], model)
        return ((not exp1) or exp2)
    elif expression.connective[0].lower() == 'iff':
        exp1 = pl_true(expression.subexpressions[0], model)
        exp2 = pl_true(expression.subexpressions[1], model)
        return ((not exp1) or exp2) and ((not exp2) or exp1)
    return model[expression.symbol[0]]

