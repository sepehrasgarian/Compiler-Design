from ply import lex

reserved = {
    'while': 'WHILE',
    'if': 'IF',
    'main': 'MAIN',
    'print': 'PRINT',
    'else':'ELSE',
     'elif':'ELIF',
    'for':'FOR',
    'void':'VOID',
'true':'TRUE','false':'FALSE','return':'RETURN','int':'INTEGER','float':'FLOAT','Error':'ERROR','bool':'BOOLEAN'




}

class Lexer:

    tokens = [
        #'FOR',
        'AND','OR','NOT','ASSIGN','MOD','COMMA',
        #'WHILE',
        'LRB',
        'RRB',
        'LCB','LSB',
        'RCB','RSB',
        'SUM',
        'SUB',
        'MUL',
        'DIV',
        'LT','LE','EQ','NE',
        'GT','GE',
        'SEMICOLON',
        'ID','INTEGERNUMBER','FLOATNUMBER',
        'ERRORID','ERRORFLOAT'#ERROR ID AND FLOAT
        #'VOID','TRUE','FALSE','RETURN'
    ]
    # COLONS
    tokens += reserved.values()
    #print(reserved)


    #t_MAIN = r'main'
    t_SEMICOLON = r'\;'
    t_COMMA=r'\,'
    # BRACKETS
    t_LRB = r'\('
    t_RRB = r'\)'
    t_LCB = r'\{'
    t_RCB = r'\}'
    # OPERATOR
    t_SUM = r'\+'
    t_SUB = r'\-'
    t_MUL = r'\*'
    t_DIV = r'\/'
    t_MOD='%'
    t_LT = r'\<'
    t_LE=r'\<='
    t_EQ=r'\=='
    t_NE=r'\!='
    t_LSB=r'\['
    t_RSB=r'\]'


    t_GT = r'\>'
    t_GE=r'\>='
    t_AND=r'\&&'
    t_OR=  r'\|\|'#moshkel
    t_NOT=r'!'
    t_ASSIGN=r'\='

    # KW
    def t_ERRORID(self, t):
        r'([0-9]+[a-zA-Z_][a-zA-Z_0-9]*)'#if id start with number that should return error
        t.type='ERROR'
        print('ERROR id can not have number at first of it :))')
        return t
    def t_ERRORFLOAT(self,t):
        r' ([\d]*(\.[\d]*){2,})'
        t.type = 'ERROR'
        print("error float point:"+str(t.value))
        return t


    def t_ERROR(self, t):
        r'([\%\/\-\*\+][\s]*[\%\/\-\*\+][\%\/\-\*\+ ]*)'   #In the order of document  % / - * +

        t.type = 'ERROR'
        print("error :"+str(t.value))
        return t

    def t_FLOATNUMBER(self, t):
            r'\d+\.\d+'  #two digit number

            before, after = str(t.value).split('.')
            #print(str(len(before))+"      sqsqs")
            if len(before)>=10:
                t.type = 'ERROR'
                txt = "Error: " + "\t" + t.value + "\t" + " greater or equal to 10"
                print(txt)
                return t
            else :
                t.value = float(t.value)
                return t
    def t_INTEGERNUMBER(self, t):
        r'[0-9]+'
        p=int(t.value)
        t.value = int(t.value)


        #print(str(l)+"  len")
        if p>999999999:
            t.type = 'ERROR'
            txt = "Error: " + "\t" + str(t.value) + "\t" + " greater or equal to 10"
            print(txt)
            return t
        else:
            #print("moafgh")

            return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
    def t_ID(self,t):
        r'[a-zA-Z\x80-\xff_][a-zA-Z0-9\x80-\xff_]*'
        if t.value in reserved:
            t.type = reserved[t.value]
        return t


    t_ignore = '\n \v \t\r\f'

    def t_error(self, t):
        raise Exception('Error at', t.value)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer

    def errorwq(self):
        print("salam")