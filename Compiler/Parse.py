import _debug
var = {}
func = {'print': 'string,string2,string3,string4,string5,string6,string7,string8,string8,string_l:out string=>out string2=>out string3=>out string4=>out string5=>out string6=>out string7=>out string8=>out string_l', 'input': 'string:in string'}
run = {}
errorCode = 0


def error(message):
    print("syntax error :", message)


def parse(location):
    error_code = 0
    with open(location, 'r') as f:
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
