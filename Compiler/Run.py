import Parse as parse


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
            real_parameter = value[i]

            fpart = code[1].split('=>')
            for j in range(len(fpart)):
                part = fpart[j].split(' ')
                for k in range(len(func)):
                    if part[0] == 'out':
                        for p in range(len(parameter)):
                            if part[1] == parameter[p]:
                                if real_parameter[0] == "'" and real_parameter[len(real_parameter) - 1] == "'":
                                    print(real_parameter[1:-1])
                                else:
                                    for q in range(len(parse.var)):
                                        try:
                                            if tag[q] == real_parameter:
                                                print(eval(var[q]))


if __name__ == '__main__':
    parse.parse('file.arrow')
    func_run()