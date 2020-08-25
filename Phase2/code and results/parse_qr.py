from ply import yacc
from lex import Lexer

class Parser:

    tokens = Lexer().tokens

    def __init__(self):
        pass

    def p_program(self, p):
        """program : declist MAIN LRB RRB block"""
        print("program : declist MAIN LRB RRB block")#dghighan mesle fili ke gozashtin

    def p_decli_version1(self,p):
        """declist : dec"""
        print("declist : dec ")  # type1
    def p_decli_version2(self,p):
        """declist : declist dec"""
        print("declist : declist ")  # type2

    def p_decli_version3(self,p):
        """declist : empty"""
        print("declist : empty ")  # type3



    def p_decversion1(self, p):
        """dec : vardec """
        print("""dec : vardec """)
    def p_decversion2(self, p):
        """dec : funcdec """
        print("""dec : funcdec """)




    def p_type1(self, p):
        """type : INTEGER"""

        print("""type : INTEGERNUMBER""")
    def p_type2(self, p):
        """type :  FLOAT"""
        print("""type :  FLOAT""")


    def p_type3(self, p):
        """type :  BOOLEAN"""
        print("""type : BOOLEAN""")




    def p_iddec_version1(self, p):
        """iddec : ID"""
        print("""iddec : ID""")

    def p_iddec1_version2(self, p):
        """iddec :  ID LSB exp RSB"""
        print("""ID LSB exp RSB""")
    def p_iddec1_version3(self, p):
        """iddec :  ID ASSIGN exp"""
        print("""iddec :  ID ASSIGN exp""")




    def p_idlist_version1(self, p):
        """idlist : iddec"""
        print("""idlist : iddec""")
    def p_idlist_version2(self, p):
        """idlist :  idlist COMMA iddec"""
        print("""idlist :  idlist COMMA iddec""")




    def p_vardec(self, p):
        """vardec : type idlist SEMICOLON"""
        print("""vardec : type idlist SEMICOLON""")#semicolen ham dashterror




    def p_funcdec_vesrion1(self, p):
        """funcdec : type ID LRB paramdecs RRB block"""
        print("""funcdec : type ID LRB paramdecs RRB block""")


    def p_funcdec_version2(self, p):
        """funcdec :  VOID ID LRB paramdecs RRB block"""
        print("""funcdec :  VOID ID LRB paramdecs RRB block""")





    def p_paramdecs_vesrion1(self, p):
        """paramdecs : paramdecslist"""
        print("""paramdecs : paramdecslist""")
    def p_paramdecs_version2(self, p):
        """paramdecs : empty"""
        print("""paramdecs :  empty""")




    def p_paramdecslist_vesrion1(self, p):
        """paramdecslist : paramdec"""
        print("""paramdecslist : paramdec""")

    def p_paramdecslist_vesrion2(self, p):
        """paramdecslist : paramdecslist COMMA paramdec"""
        print("""paramdecslist : paramdecslist COMMA paramdec""")




    def p_paramdec_vesrion1(self, p):
        """paramdec : type ID"""
        print("""paramdec : type ID""")
    def p_paramdec_version2(self, p):
        """paramdec : type ID LSB RSB"""
        print("""paramdec : type ID LSB RSB""")




    def p_varlist_version1(self, p):
        """varlist : vardec"""
        print("""varlist : vardec""")

    def p_varlist_version2(self, p):
        """varlist :  varlist vardec"""
        print("""varlist :  varlist vardec """)


    def p_varlist_version3(self, p):
        """varlist : empty"""
        print("""varlist : empty""")




    def p_block(self, p):
        """block : LCB varlist stmtlist RCB"""
        print("block : LCB varlist stmtlist RCB")




    def p_stmtlist_version1(self, p):
        """stmtlist : stmt"""
        print("""stmtlist : stmt""")

    def p_stmtlist_version2(self, p):
        """stmtlist : stmtlist stmt"""
        print("""stmtlist : stmtlist stmt""")


    def p_stmtlist_version3(self, p):
        """stmtlist :  empty"""
        print("""stmtlist : empty""")





    def p_lvalue_version1(self, p):
        """lvalue : ID"""
        print("""lvalue : ID""")

    def p_lvalue_version2(self, p):
        """lvalue : ID LSB exp RSB"""
        print("""lvalue : ID LSB exp RSB""")




    def p_stmt_version1(self, p):
        """stmt : matched_stmt"""
        print("""stmt : matched_stmt""")#shyd mohemtrin bakhsh taghsim kedn be match va unmached bshe

    def p_stmt_version2(self, p):
        """stmt : unmatched_stmt"""
        print("""stmt : unmatched_stmt""")




    def p_stmt_matched_version1(self, p):
        """matched_stmt : IF LRB exp RRB matched_stmt elseiflist ELSE matched_stmt %prec IF_D"""
        print("""matched_stmt : IF LRB exp RRB matched_stmt elseiflist ELSE matched_stmt""")#if ghbol nmird


    def p_stmt_matched_version2(self, p):
        """matched_stmt : everythingthatcanhappen"""
        print("""matched_stmt : everythingthatcanhappen(other)""")




    def p_stmt_unmatched_version1(self, p):
        """unmatched_stmt : IF LRB exp RRB matched_stmt elseiflist %prec IF_D"""
        print(
            """unmatched_stmt : IF LRB exp RRB stmt elseiflist""")
    def p_stmt_unmatched_version2(self, p):
        """unmatched_stmt : IF LRB exp RRB matched_stmt elseiflist ELSE unmatched_stmt %prec IF_D"""
        print(
            """unmatched_stmt :  IF LRB exp RRB matched_stmt elseiflist ELSE unmatched_stmt""")





    def p_stmt_others_version1(self, p):
        """everythingthatcanhappen : RETURN exp SEMICOLON"""
        print("""everythingthatcanhappen : RETURN exp SEMICOLON""")

    def p_stmt_others_version2(self, p):
        """everythingthatcanhappen : exp SEMICOLON"""
        print("""everythingthatcanhappen : exp SEMICOLON""")


    def p_stmt_others_version3(self, p):
        """everythingthatcanhappen : block"""
        print(
            """everythingthatcanhappen : block""")


    def p_stmt_others_version4(self, p):
        """everythingthatcanhappen : WHILE LRB exp RRB stmt"""
        print(""" WHILE LRB exp RRB stmt""")


    def p_stmt_others_version5(self, p):
        """everythingthatcanhappen : FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt"""
        print("""everythingthatcanhappen : FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt""")


    def p_stmt_others_version6(self, p):
        """everythingthatcanhappen : PRINT LRB ID RRB SEMICOLON"""
        print("""everythingthatcanhappen : PRINT LRB ID RRB SEMICOLON""")




    def p_elseiflist_version1(self, p):
        """elseiflist : ELIF LRB exp RRB stmt"""
        print("""elseiflist : ELIF LRB exp RRB stmt""")
    def p_elseiflist_version2(self, p):
        """elseiflist : elseiflist ELIF LRB exp RRB stmt"""
        print("""elseiflist : elseiflist ELIF LRB exp RRB stmt""")

    def p_elseiflist_version3(self, p):
        """elseiflist : empty"""
        print("""elseiflist : empty""")





    def p_exp_version1(self, p):
        """exp : lvalue ASSIGN exp"""
        print("""exp : lvalue ASSIGN exp""")


    def p_exp_version2(self, p):
        """exp : exp operator exp %prec OP"""
        print("""exp : exp operator exp""")


    def p_exp_version3(self, p):
        """exp : exp relop exp %prec RELOP"""
        print("""exp : exp relop exp""")


    def p_exp_version5(self, p):
        """exp : const"""
        print("""exp : const""")


    def p_exp_version6(self, p):
        """exp : lvalue"""
        print("""exp : lvalue """)


    def p_exp_version7(self, p):
        """exp : ID LRB explist RRB"""
        print("""exp : ID LRB explist RRB""")

    def p_exp_version8(self, p):
        """exp : LRB exp RRB"""
        print("""exp : LRB exp RRB""")


    def p_exp_version9(self, p):
        """exp : ID LRB RRB"""
        print("""exp : ID LRB RRB""")
    def p_exp_version10(self, p):
        """exp : SUB exp %prec UMINUS"""
        print("""exp : SUB exp""")

    def p_exp_version11(self, p):
        """exp : NOT exp"""
        print("""exp : NOT exp""")







    def p_operator_version1(self, p):
        """operator : OR"""
        print("""operator : OR""")
    def p_operator_version2(self, p):
        """operator : AND"""
        print("""operator : AND""")
    def p_operator_version3(self, p):
        """operator : SUM"""
        print("""operator : SUM""")

    def p_operator_version4(self, p):
        """operator : SUB"""
        print("""operator : SUB""")

    # def p_operator_version5(self, p):
    #     """operator : MUL"""
    #     print("""operator : MUL""")
    def p_operator_version6(self, p):
        """operator : MUL"""
        print("""operator : MUL""")
    def p_operator_version7(self, p):
        """operator : DIV"""
        print("""operator : DIV""")


    def p_operator_version8(self, p):
        """operator : MOD"""
        print("""operator : MOD""")


    def p_const_version1(self, p):
        """const : INTEGERNUMBER"""
        print("""const : INTEGERNUMBER""")

    def p_const_version2(self, p):
        """const : FLOATNUMBER"""
        print("""const : FLOATNUMBER""")


    def p_const_version3(self, p):
        """const : TRUE"""
        print("""const : TRUE""")

    def p_const_version4(self, p):
        """const : FALSE"""
        print("""const : FALSE""")

    def p_relop_version1(self, p):
        """relop : GT"""
        print("""relop : GT""")


    def p_relop_version2(self, p):
        """relop : LT"""
        print("""relop : LT""")

    def p_relop_version3(self, p):
        """relop : NE"""
        print("""relop : NE""")
    def p_relop_version4(self, p):
        """relop : EQ"""
        print("""relop : EQ""")

    def p_relop_version5(self, p):
        """relop : LE"""
        print("""relop : LE""")
    def p_relop_version6(self, p):
        """relop : GE"""
        print("""relop : GE""")

    def p_explist_version1(self, p):
        """explist : exp"""
        print("""explist : exp""")

    def p_explist_version2(self, p):
        """explist : explist COMMA exp"""
        print("""explist: explist COMMA exp""")

    def p_empty(self, p):
        """empty : %prec EMPTY"""
        pass

    precedence = (
        ('nonassoc', 'EMPTY'),#olaviate bala akhrin olaviuat
        ('nonassoc', 'IF_D'),
        ('nonassoc', 'ELIF'),
        ('nonassoc', 'ELSE'),
        ('nonassoc', 'RELOP'),
        ('nonassoc', 'OP'),
        ('left', 'COMMA'),
        ('right', 'ASSIGN'),
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'EQ', 'NE'),
        ('left', 'GT', 'LT', 'GE', 'LE'),
        ('left', 'SUM', 'SUB'),
        ('left', 'MUL', 'DIV', 'MOD'),
        ('right', 'NOT'),
        ('right', 'UMINUS')
    )

    def p_error(self, p):
        print(p.value)
        raise Exception('ParsingError: invalid grammar at ', p)

    def build(self, **kwargs):
        """build the parser"""
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
