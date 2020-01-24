import _debug

var = {}
func = {
    'print': 'string,string2,string3,string4,string5,string6,string7,string8,string8,string_l:out string=>out string2=>out string3=>out string4=>out string5=>out string6=>out string7=>out string8=>out string_l',
    'input': 'string:in string'}
run = {}
if_statement = {}

errorCode = 0


def error(message):
    print("syntax error :", message)


def func_run(run_key, run_value):
    func_key = list(func.keys())
    var_value = list(var.values())
    var_key = list(var.keys())
    if_value = list(if_statement.values())
    if_key = list(if_statement.keys())

    for i in range(len(if_statement)):
        for q in range(len(var)):
            if var_key[q] in if_key[i]:
                edit = var_value[q]
                while True:
                    temp = 0
                    for z in range(len(var_key)):
                        if var_key[z] in edit:
                            edit = edit.replace(var_key[z], var_value[z])
                            temp = 1
                    if temp == 0:
                        break
                if _debug.debug:
                    print(edit)
                print(eval(edit), end='')

    if run_key in func_key:
        code = func[run_key].split(':')
        parameter = code[0].split(',')
        real_parameter = run_value.split(', ')
        if _debug.debug:
            print(real_parameter)
            print(parameter)
        fpart = code[1].split('=>')
        for j in range(len(fpart)):
            part = fpart[j].split(' ')
            if part[0] == 'out':
                if parameter[j] in part[1]:
                    try:
                        if real_parameter[j][0] == "'" and real_parameter[j][len(real_parameter[j]) - 1] == "'":
                            print(real_parameter[j][1:-1], end=' ')
                        else:
                            for q in range(len(var)):
                                if _debug.debug:
                                    print(var_key[q], var_key[q] in real_parameter)
                                if var_key[q] in real_parameter:
                                    while True:
                                        edit = var_value[q]
                                        temp = 0
                                        for z in range(len(var_key)):
                                            if var_key[z] in edit:
                                                edit = edit.replace(var_key[z], var_value[z])
                                                temp = 1
                                        if temp == 0:
                                            break
                                    print(eval(edit), end='')
                                    break
                                else:
                                    print(eval(var_value[j]), end='')
                    except:
                        continue
            elif part[0] == 'in':
                if parameter[j] in part[1]:
                    memory = "'" + input('please input for ' + real_parameter[j] + ': ') + "'"
                    var[real_parameter[j]] = memory
                    var_value = list(var.values())
                    var_key = list(var.keys())


def parse(location_file):
    error_code = 0

    with open(location_file, 'r') as f:
        while True:
            word = f.readline()
            if not word: break

            if _debug.debug:
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
                            var[word[i - 1]] = string
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
                        elif word[i] == '/-/':
                            break
                        elif word[i] == 'run':
                            try:
                                string = word[i + 2]

                                for j in range(i + 3, len(word)):
                                    string = string + ' ' + word[j]
                            except:
                                string = ''
                            run[word[i + 1]] = string
                            break
                        elif i != 0:
                            if error_code == 0:
                                error('E0: invalid token')
                                error_code = 1
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
                        func_run(word[i+1], string)
                        break
                    elif word[i] == 'if':
                        string = word[i + 1]

                        for j in range(i + 2, len(word)):
                            string = string + ' ' + word[j]

                        parameter = string.split(' => ')
                        if_statement[parameter[0]] = parameter[1]
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
        if _debug.debug:
            print('var:', var)
            print('func:', func)
            print('run:', run)
            print('if:', if_statement)


if __name__ == '__main__':
    location = input('enter location: ')
    parse(location)
    print('\nparse finished.')
