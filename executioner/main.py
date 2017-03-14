import sys
class Executioner(object):
    def __init__(self, obj):
        self.obj = obj
        self.build()
    
    def build(self):
        del sys.argv[0]
        for arg in sys.argv:
            command = getattr(self.obj, arg, 'nope')
            if command is not 'nope':
                sys.argv.remove(arg)
                param = getattr(self.obj, arg + '_param')
                if(param == 'string'):
                    command(sys.argv[0])
                    del sys.argv[0]
                elif(param == 'int'):
                    command(int(sys.argv[0]))
                    del sys.argv[0]
                elif(param == 'float'):
                    command(float(sys.argv[0]))
                    del sys.argv[0]
                elif(param.find('list:') != -1):
                    list_type = param.split(':')[1]
                    list_params = self.build_list(list_type)
                    command(list_params)
    
    def build_list(self, list_type):
        list_of_params = []
        for multi in range(len(sys.argv)):
            arg_l = sys.argv[0]
            if(getattr(self.obj, arg_l, 'nonexist') is not 'nonexist'):
                return list_of_params
            if(list_type == 'string'): list_of_params.append(arg_l)
            elif(list_type == 'int'): list_of_params.append(int(arg_l))
            elif(list_type == 'float'): list_of_params.append(float(arg_l))
            del sys.argv[0]
        return list_of_params
    
        
