import sys

var = {}
func = {
    'print': 'string,string2,string3,string4,string5,string6,string7,string8,string8,string_l:run out string=>run out string2=>run out string3=>run out string4=>run out string5=>run out string6=>run out string7=>run out string8=>run out string_l',
    'input': 'string:run in string',
    'input_int': 'string:run in_int string'
}
run = {}
if_statement = {}

error_code = 0
var_value = list(var.values())
var_key = list(var.keys())
if_privious = 0
debug = False
ver = ''


def error(message):
    print("syntax error :", message)


def func_run_line(run_key, run_value):
    global var_value
    global var_key
    func_key = list(func.keys())

    if run_key in func_key:
        code = func[run_key].split(':')
        parameter = code[0].split(',')
        real_parameter = run_value.split(', ')
        if debug:
            print(real_parameter)
            print(parameter)
        fpart = code[1].split('=>')
        for j in range(len(fpart)):
            part = fpart[j].split(' ')
            if part[0] == 'run':
                if part[1] == 'out':
                    if parameter[j] in part[2]:
                        try:
                            if real_parameter[j][0] == "'" and real_parameter[j][len(real_parameter[j]) - 1] == "'":
                                print(real_parameter[j][1:-1], end=' ')
                            else:
                                edit = real_parameter[j]
                                for a in range(len(var)):
                                    if var_key[a] in edit:
                                        edit = edit.replace(var_key[a], var_value[a])
                                try:
                                    edit = eval(edit)
                                except:
                                    edit = edit
                                print(edit, end=' ')
                        except:
                            continue
                elif part[1] == 'in':
                    if parameter[j] in part[2]:
                        memory = "'" + input('please input for ' + real_parameter[j] + ': ') + "'"
                        var[real_parameter[j]] = memory
                        var_value = list(var.values())
                        var_key = list(var.keys())
                elif part[1] == 'in_int':
                    if parameter[j] in part[2]:
                        while True:
                            try:
                                memory = int(input('please input for ' + real_parameter[j] + ': '))
                                memory = str(memory)
                                break
                            except:
                                error('hey! it is not int!')
                        var[real_parameter[j]] = memory
                        var_value = list(var.values())
                        var_key = list(var.keys())


def parse_line(word):
    global var_value
    global var_key
    global error_code
    global if_privious

    if debug:
        print('var:', var)
        print('func:', func)
        print('run:', run)
        print('if:', if_statement)
    word = word.split(' ')
    for i in range(len(word)):
        if '\n' in word[i]:
            word[i] = word[i][:-1]
    for i in range(len(word)):
        try:
            if word[i] == '=':
                if word[0] != 'function':
                    string = word[i + 1]
                    for j in range(i + 2, len(word) - 1):
                        if word[j] == '+':
                            string = string + '+' + word[j + 1]
                        if word[j] == '-':
                            string = string + '-' + word[j + 1]
                        if word[j] == '*':
                            string = string + '*' + word[j + 1]
                        if word[j] == '/':
                            string = string + '/' + word[j + 1]
                        try:
                            for v in range(len(var_key)):
                                for k in range(len(var_key)):
                                    string = string.replace(var_key[k], var_value[k])
                                    if debug:
                                        print('var = ', string)
                            var[word[i - 1]] = string
                        except:
                            var[word[i - 1]] = string
                    var[word[i - 1]] = string
                    var_value = list(var.values())
                    var_key = list(var.keys())
                    break
            elif word[i] == 'function':
                if i == 0 and word[i + 2] == '=' and word[i + 3] == '{' and word[len(word) - 1] == '}':
                    string = word[4]
                    for j in range(5, len(word) - 1):
                        if word[j - 1] == '=>':
                            string = string + '=>' + word[j]
                        else:
                            string = string + ' ' + word[j]
                    func[word[i + 1]] = string
                    break
                else:
                    error('E1: word connected')
                    error_code = 1
                    break
            elif word[i] == '#':
                break
            elif word[i] == 'run':
                try:
                    string = word[i + 2]
                    for j in range(i + 3, len(word)):
                        string = string + ' ' + word[j]
                except:
                    string = ''
                run[word[i + 1]] = string
                func_run_line(word[i + 1], string)
                break
            elif word[i] == 'if':
                index = word.index('<=')
                try:
                    for q in range(index):
                        for a in range(len(var_key)):
                            for b in range(len(var_key)):
                                word[q] = word[q].replace(var_key[b], var_value[b])
                except:
                    error('if statue error')
                string = word[i + 1]

                for j in range(i + 2, len(word)):
                    string = string + ' ' + word[j]
                parameter = string.split(' <= ')
                if_string = parameter[1]
                for b in range(2, len(parameter)):
                    if_string = if_string + '<=' + parameter[b]
                if_statement[eval(parameter[0])] = if_string
                if_run(eval(parameter[0]), if_string, 1)
                if_privious = eval(parameter[0])
                break
            elif word[i] == 'elsif':
                if not if_privious:
                    index = word.index('<=')
                    try:
                        for q in range(index):
                            for a in range(len(var_key)):
                                for b in range(len(var_key)):
                                    word[q] = word[q].replace(var_key[b], var_value[b])
                    except:
                        error('if statue error')
                    string = word[i + 1]

                    for j in range(i + 2, len(word)):
                        string = string + ' ' + word[j]

                    parameter = string.split(' <= ')
                    if_string = parameter[1]
                    for b in range(2, len(parameter)):
                        if_string = if_string + '<=' + parameter[b]
                    if_statement[eval(parameter[0])] = if_string
                    if_run(eval(parameter[0]), if_string, 1)
                    if_privious = eval(parameter[0])
                break
            elif word[i] == 'else':
                if not if_privious:
                    string = word[i + 1]

                    for j in range(i + 2, len(word)):
                        string = string + ' ' + word[j]

                    parameter = string.split(' <= ')
                    if_string = parameter[0]
                    for b in range(1, len(parameter)):
                        if_string = if_string + '<=' + parameter[b]
                    if_run(True, if_string, 1)
                    if_privious = 0
                break
            elif word[i] == 'for':
                for_var = word[i + 1]
                if word[i + 2] == 'time':
                    for_time = word[i + 3]

                    if word[i + 4] == '<=':
                        for k in range(int(for_time)):
                            string = word[i + 5]
                            for j in range(i + 6, len(word)):
                                string = string + ' ' + word[j]
                            parameter = string.split(' <= ')
                            var[for_var] = str(k)
                            var_key = list(var.keys())
                            var_value = list(var.values())
                            for_run(parameter)
                del var[for_var]
                var_key = list(var.keys())
                var_value = list(var.values())
                break
            elif i != 0:
                if error_code == 0:
                    error('E0: invalid token')
                    error_code = 1
                    break
        except:
            if error_code == 0:
                error('runtime error')
                error_code = 1
                break
    if error_code == 1:
        exit('build failed')


def if_run(if_key, string, mode):
    global var_key
    global var_value

    if mode == 0:
        print_index = 0
        if if_key:
            string = string.split('=>')
            for i in range(len(string)):
                var_key = list(var.keys())
                var_value = list(var.values())
                temp = string[i].split(' ')
                for j in range(len(temp)):
                    for v in range(len(var_key)):
                        for k in range(len(var_key)):
                            if 'print' is temp[j]:
                                print_index = j + 1
                            elif print_index <= j:
                                if temp[j] in var_key:
                                    for a in range(len(var_key)):
                                        if temp[j] is var_key[a]:
                                            temp[j] = var_value[a]
                string[i] = temp[0]
                for j in range(1, len(temp)):
                    string[i] = string[i] + ' ' + temp[j]
                parse_line(string[i])
                print_index = 0
    else:
        print_index = 0
        if if_key:
            string = string.split('<=')
            for i in range(len(string)):
                var_key = list(var.keys())
                var_value = list(var.values())
                temp = string[i].split(' ')
                for j in range(len(temp)):
                    for v in range(len(var_key)):
                        for k in range(len(var_key)):
                            if 'print' is temp[j]:
                                print_index = j + 1
                            elif print_index <= j:
                                if temp[j] in var_key:
                                    for a in range(len(var_key)):
                                        if temp[j] is var_key[a]:
                                            temp[j] = var_value[a]
                string[i] = temp[0]
                for j in range(1, len(temp)):
                    string[i] = string[i] + ' ' + temp[j]
                parse_line(string[i])
                print_index = 0


def for_run(string):
    global var_key
    global var_value

    print_index = 0
    for i in range(len(string)):
        var_key = list(var.keys())
        var_value = list(var.values())
        temp = string[i].split(' ')
        for j in range(len(temp)):
            for v in range(len(var_key)):
                for k in range(len(var_key)):
                    if 'print' is temp[j]:
                        print_index = j + 1
                    elif print_index <= j:
                        if temp[j] in var_key:
                            for a in range(len(var_key)):
                                if temp[j] is var_key[a]:
                                    temp[j] = var_value[a]
                                    break
        string[i] = temp[0]
        for j in range(1, len(temp)):
            string[i] = string[i] + ' ' + temp[j]
        parse_line(string[i])
        print_index = 0


def func_run(run_key, run_value):
    global var_value
    global var_key
    func_key = list(func.keys())

    if run_key in func_key:
        code = func[run_key].split(':')
        parameter = code[0].split(',')
        real_parameter = run_value.split(', ')
        if debug:
            print(real_parameter)
            print(parameter)
        fpart = code[1].split('=>')
        for j in range(len(fpart)):
            part = fpart[j].split(' ')
            if part[0] == 'run':
                if part[1] == 'out':
                    if parameter[j] in part[2]:
                        try:
                            if real_parameter[j][0] == "'" and real_parameter[j][len(real_parameter[j]) - 1] == "'":
                                print(real_parameter[j][1:-1], end=' ')
                            else:
                                edit = real_parameter[j]
                                for a in range(len(var)):
                                    if var_key[a] in edit:
                                        edit = edit.replace(var_key[a], var_value[a])
                                edit = eval(edit)
                                print(edit, end=' ')
                        except:
                            continue
                elif part[1] == 'in':
                    if parameter[j] in part[2]:
                        memory = "'" + input('please input for ' + real_parameter[j] + ': ') + "'"
                        var[real_parameter[j]] = memory
                        var_value = list(var.values())
                        var_key = list(var.keys())
                elif part[1] == 'in_int':
                    if parameter[j] in part[2]:
                        while True:
                            try:
                                memory = int(input('please input for ' + real_parameter[j] + ': '))
                                memory = str(memory)
                                break
                            except:
                                error('hey! it is not int!')
                        var[real_parameter[j]] = memory
                        var_value = list(var.values())
                        var_key = list(var.keys())


def parse(location_file):
    global var_value
    global var_key
    global error_code
    global if_privious
    with open(location_file, 'r') as f:
        while True:
            word = f.readline()
            if not word: break

            if debug:
                print(word, end='')

            word = word.split(' ')
            for i in range(len(word)):
                if '\n' in word[i]:
                    word[i] = word[i][:-1]
            for i in range(len(word)):
                try:
                    if word[i] == '=':
                        if word[0] != 'function':
                            string = word[i + 1]
                            for j in range(i + 2, len(word) - 1):
                                if word[j] == '+':
                                    string = string + '+' + word[j + 1]
                                if word[j] == '-':
                                    string = string + '-' + word[j + 1]
                                if word[j] == '*':
                                    string = string + '*' + word[j + 1]
                                if word[j] == '/':
                                    string = string + '/' + word[j + 1]
                            try:
                                for v in range(len(var_key)):
                                    for k in range(len(var_key)):
                                        string = string.replace(var_key[k], var_value[k])
                                        if debug:
                                            print('var = ', string)
                                var[word[i - 1]] = string
                            except:
                                var[word[i - 1]] = string
                        var_value = list(var.values())
                        var_key = list(var.keys())
                        break
                    elif word[i] == 'function':
                        if i == 0 and word[i + 2] == '=' and word[i + 3] == '{' and word[len(word) - 1] == '}':
                            string = word[4]
                            for j in range(5, len(word) - 1):
                                if word[j - 1] == '=>':
                                    string = string + word[j]
                                else:
                                    string = string + ' ' + word[j]
                            func[word[i + 1]] = string
                            break
                        else:
                            error('E1: word connected')
                            error_code = 1
                            break
                    elif word[i] == '#':
                        break
                    elif word[i] == 'run':
                        try:
                            string = word[i + 2]

                            for j in range(i + 3, len(word)):
                                string = string + ' ' + word[j]
                        except:
                            string = ''
                        run[word[i + 1]] = string
                        func_run(word[i + 1], string)
                        break
                    elif word[i] == 'if':
                        index = word.index('=>')
                        try:
                            for q in range(index):
                                for a in range(len(var_key)):
                                    for b in range(len(var_key)):
                                        word[q] = word[q].replace(var_key[b], var_value[b])
                        except:
                            error('if statue error')
                        string = word[i + 1]

                        for j in range(i + 2, len(word)):
                            string = string + ' ' + word[j]
                        parameter = string.split(' => ')
                        if_string = parameter[1]
                        for b in range(2, len(parameter)):
                            if_string = if_string + '=>' + parameter[b]
                        if_statement[eval(parameter[0])] = if_string
                        if_run(eval(parameter[0]), if_string, 0)
                        if_privious = eval(parameter[0])
                        break
                    elif word[i] == 'elsif':
                        if not if_privious:
                            index = word.index('=>')
                            try:
                                for q in range(index):
                                    for a in range(len(var_key)):
                                        for b in range(len(var_key)):
                                            word[q] = word[q].replace(var_key[b], var_value[b])
                            except:
                                error('if statue error')
                            string = word[i + 1]

                            for j in range(i + 2, len(word)):
                                string = string + ' ' + word[j]

                            parameter = string.split(' => ')
                            if_string = parameter[1]
                            for b in range(2, len(parameter)):
                                if_string = if_string + '=>' + parameter[b]
                            if_statement[eval(parameter[0])] = if_string
                            if_run(eval(parameter[0]), if_string, 0)
                            if_privious = eval(parameter[0])
                        break
                    elif word[i] == 'else':
                        if not if_privious:
                            string = word[i + 1]

                            for j in range(i + 2, len(word)):
                                string = string + ' ' + word[j]

                            parameter = string.split(' => ')
                            if_string = parameter[0]
                            for b in range(1, len(parameter)):
                                if_string = if_string + '=>' + parameter[b]
                            if_run(True, if_string, 0)
                            if_privious = 0
                        break
                    elif word[i] == 'for':
                        for_var = word[i + 1]
                        if word[i + 2] == 'time':
                            for_time = word[i + 3]

                            if word[i + 4] == '=>':
                                for k in range(int(for_time)):
                                    string = word[i + 5]
                                    for j in range(i + 6, len(word)):
                                        string = string + ' ' + word[j]
                                    parameter = string.split(' => ')
                                    var[for_var] = str(k)
                                    var_key = list(var.keys())
                                    var_value = list(var.values())
                                    for_run(parameter)
                        del var[for_var]
                        var_key = list(var.keys())
                        var_value = list(var.values())
                        break
                    elif i != 0:
                        if error_code == 0:
                            error('E0: invalid token')
                            error_code = 1
                            break
                except:
                    if error_code == 0:
                        error('runtime error')
                        error_code = 1
                        break

    if error_code == 1:
        exit('build failed')
    else:
        if debug:
            print('var:', var)
            print('func:', func)
            print('run:', run)
            print('if:', if_statement)


def main():
    location = input('file path: ')
    parse(location)


if __name__ == '__main__':
    try:
        if sys.argv[1] == 'debug_mode':
            print('welcome to debuging mode!')
            debug = True
        elif sys.argv[1] == 'import_debug':
            print('__init__ mode : on')
            print('welcome to debuging mode!')
            import __init__
            debug = __init__.debug
            ver = __init__.ver
            print('ver :', ver)
    except:
        debug = False
    main()
    print('\nfinished.')
