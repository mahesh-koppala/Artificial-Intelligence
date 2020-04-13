

import sys
from logical_expression import *



def tt_entails(knowledge_base, statement, negation, symbolslist):
    kb_symbols = []
    s_variables = []
    model = symbolslist.copy();
    get_symbols(knowledge_base, kb_symbols)
    get_symbols(statement, s_variables)
    kb_symbols = list(set(kb_symbols))
    s_variables = list(set(s_variables))
    kb_symbols.extend(s_variables)
    symbols = list(set(kb_symbols))
    for sym_key in model.keys():
        try:
            symbols.remove(sym_key)
        except Exception:
            pass
    check_true_false(knowledge_base, statement, symbolslist, negation, symbols, model)


def main(argv):
    if len(argv) != 4:
        print('Usage: %s [wumpus-rules-file] [additional-knowledge-file] [input_file]' % argv[0])
        sys.exit(0)

    
    try:
        input_file = open(argv[1], 'rb')
    except:
        print('failed to open file %s' % argv[1])
        sys.exit(0)
    symlist = {}
    
    print '\nLoading wumpus rules...'
    knowledge_base = logical_expression()
    knowledge_base.connective = ['and']
    for line in input_file:
        
        if line[0] == '#' or line == '\r\n' or line == '\n' or line == '\r':
            continue
        counter = [0]  
        subexpression = read_expression(line.rstrip('\r\n'), counter)
        if subexpression.connective[0] == '':
            symlist[subexpression.symbol[0]] = True
        if subexpression.connective[0].lower() == 'not':
            if subexpression.subexpressions[0].symbol \
                    and subexpression.subexpressions[0].connective[0] == '':
                symlist[subexpression.subexpressions[0].symbol[0]] = False
        knowledge_base.subexpressions.append(subexpression)
    input_file.close()

    
    try:
        input_file = open(argv[2], 'rb')
    except:
        print('failed to open file %s' % argv[2])
        sys.exit(0)

    
    print 'Loading additional knowledge...'
    for line in input_file:
        
        if line[0] == '#' or line == '\r\n' or line == '\n' or line == '\r':
            continue
        counter = [0]  
        subexpression = read_expression(line.rstrip('\r\n'), counter)
        if subexpression.connective[0] == '':
            symlist[subexpression.symbol[0]] = True
        if subexpression.connective[0].lower() == 'not':
            if subexpression.subexpressions[0].connective[0] == '':
                symlist[subexpression.subexpressions[0].symbol[0]] = False
        knowledge_base.subexpressions.append(subexpression)
    input_file.close()

    
    if not valid_expression(knowledge_base):
        sys.exit('invalid knowledge base')

    
    print_expression(knowledge_base, '\n')

    
    try:
        input_file = open(argv[3], 'rb')
    except:
        print('failed to open file %s' % argv[3])
        sys.exit(0)
    print 'Loading statement...'
    statement = input_file.readline().rstrip('\r\n')
    input_file.close()
    negation = '(not ' + statement + ')'

    
    statement = read_expression(statement)
    counter = [0]
    negation = read_expression(negation, counter)
    if not valid_expression(statement):
        sys.exit('invalid statement')

    
    print '\nChecking statement:',
    print_expression(statement, '')
    print

    
    tt_entails(knowledge_base, statement, negation, symlist)

    sys.exit(1)


if __name__ == '__main__':
    main(sys.argv)
