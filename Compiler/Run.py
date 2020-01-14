import Parse as parse
import _debug


def func_run():
    func = list(parse.func.keys())
    run = list(parse.run.keys())
    var = list(parse.var.values())
    tag = list(parse.var.keys())
    value = list(parse.run.values())
    for i in range(len(parse.run)):
        if run[i] in func:
            code = parse.func[run[i]].split(':')
            parameter = code[0].split(',')
            real_parameter = value[i].split(', ')
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
                                for q in range(len(parse.var)):
                                    if tag[q] in real_parameter:
                                        edit = var[q]
                                        while True:
                                            temp = 0
                                            for z in range(len(tag)):
                                                if tag[z] in edit:
                                                    edit = edit.replace(tag[z], var[z])
                                                    temp = 1
                                            if temp == 0:
                                                break
                                    print(eval(edit), end='')
                        except:
                            continue
                elif part[0] == 'in':
                    if parameter[j] in part[1]:
                        memory = "'" + input('please input for ' + real_parameter[j] + ': ') + "'"
                        parse.var[real_parameter[j]] = memory
                        var = list(parse.var.values())


if __name__ == '__main__':
    parse.parse('file.arrow')
    func_run()
