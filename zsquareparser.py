# Muhammad Zeshan
# Muhammad Zeeshan Arif

import enum
import sys

class Tokens(enum.Enum):
    ADD = "Addition Operator"
    SUB = "Subtraction Operator"
    MUL = "Multiplication Operator"
    DIV = "Division Operator"
    MOD = "Modolus Operator"
    ASSM = "Assignment Operator"
    AASSM = "Addition Assignment Operator(Compound)"
    SASSM = "Subtraction Assignment Operator(Compound)"
    MASSM = "Multiplication Assignment Operator(Compound)"
    DASSM = "Division Assignment Operator(Compound)"
    MODASSM = "Modulus Assignment Operator(Compound)"
    UNADD = "Uniary Addition Operator"
    UNSUB = "Uniary Subtraction Operator"
    EQ = "Equal Comparison Operator"
    NEQ = "Not Equal Comparison Operator"
    LT = "Less Than Comaprison Operator"
    GT = "Greater Than Comparison Operator"
    LEQ = "Less Than or Equal To Comparison Operator"
    GEQ = "Greator Than or Equal To Comparison Operator"
    AND = "Logical and Operator"
    OR = "Logical or Operator"
    NOT = "Logical not Operator"
    SCOLON = "Semicolon"
    COLON = "Colon"
    STER = "Statement Termination Operator"
    COMMA = "Comma"
    OPENBRAC = "Open Bracket"
    CLOSEBRAC = "Close Bracket"
    OPENCUR = "Open Curley Bracket"
    CLOSECUR = "Close Curley Bracket"
    OPENSQR = "Open Square Bracket"
    CLOSESQR = "Close Square Bracket"
    EOF = "End of File"
    ID = "Identifier"
    INTCON = "Integer Constant"
    DECCON = "Decimal Constant"
    STRCON = "String Constant"
    CHARCON = "Character Constant"
    COM = "Comment"
    BOOL_KEY = "boolean_keyword"
    INT_KEY = "integer_keyword"
    DEC_KEY = "decimal_keyword"
    CHAR_KEY = "char_keyword"
    TEXT_KEY = "text_keyword"
    PUT_KEY = "put_keyword"
    GET_KEY = "get_keyword"
    CHECKIF_KEY = "checkif_keyword"
    ELIF_KEY = "elif_keyword"
    ELSE_KEY = "else_keyword"
    LOOP_KEY = "loop_keyword"
    UNTIL_KEY = "until_keyword"
    REP_KEY = "repeat_keyword"
    FUN_KEY = "function_keyword"
    VOID_KEY = "void_keyword"
    NEW_KEY = "new_keyword"
    THROW_KEY = "throw_keyword"
    FUNC_NAME = "function_name"
    ERR = "Invalid Token"
    EOFILE = "EndOfFile"

    
def getChar():
    if getChar.index == len(content):
        return -1
    c = content[getChar.index]
    getChar.index += 1
    return c
getChar.index = 0

def validToken(ch):
    if ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == '%' or ch == '=' or ch == ':' or ch == '[' or ch == ']' or ch == '{' or ch == '}' or ch == '(' or ch == ')' or ch == '<' or ch == '>' or ch == ',' or ch == '\n' or ch == ' ':
        return True
    return False
  
#nextToken
def nextToken():
    ch = getChar()
    if ch == -1:
        return Tokens.EOFILE.value, "eof"
    elif ch == ';':
        return Tokens.SCOLON.value, ch
    elif ch == ':':
        return Tokens.COLON.value, ch
    elif ch == '.':
        if nextToken.checkDot == True:
            nextToken.checkDot = False
            return Tokens.STER.value, ch
        else:
            word = ch
            ch = getChar()
            if ch != -1 and ch.isdigit():
                isValid = True
                while True:
                    word += ch
                    ch = getChar()
                    if ch == -1:
                        break
                    elif ch.isdigit():
                        pass
                    elif ch == '.':
                        checkDot = True
                        isValid = True
                        break
                    elif not validToken(ch):
                        isValid = False
                    elif ch == '!':
                        if getChar() == '=':
                            getChar.index -= 1
                            break
                        else:
                            getChar.index -= 1
                            isValid = False
                    elif ch == '.':
                        if getChar().isdigit():
                            getChar.index -= 1
                            isValid = False
                        else:
                            getChar.index -= 1
                            break
                    else:
                        break
                getChar.index -= 1
                if isValid == False:
                    return Tokens.ERR.value, word
                else:
                    scan.checkDot = True
                    return Tokens.DECCON.value, word
            else:
                return Tokens.STER.value, word
    elif ch == ',':
        return Tokens.COMMA.value, ch
    elif ch == '(':
        return Tokens.OPENBRAC.value, ch
    elif ch == ')':
        return Tokens.CLOSEBRAC.value, ch
    elif ch == '{':
        return Tokens.OPENCUR.value, ch
    elif ch == '}':
        return Tokens.CLOSECUR.value, ch
    elif ch == '[':
        return Tokens.OPENSQR.value, ch
    elif ch == ']':
        return Tokens.CLOSESQR.value, ch
    elif ch == '=':
        word = ch
        ch = getChar()
        if ch == '=':
            word += ch
            return Tokens.EQ.value, word
        else:
            getChar.index -= 1
            return Tokens.ASSM.value, word
    elif ch == '+':
        word = ch
        ch = getChar()
        if ch == '=':
            word += ch
            return Tokens.AASSM.value, word
        elif ch == '+':
            word += ch
            return Tokens.UNADD.value, word
        else:
            getChar.index -= 1
            return Tokens.ADD.value, word
    elif ch == '-':
        word = ch
        ch = getChar()
        if ch == '=':
            word += ch
            return Tokens.SASSM.value, word
        elif ch == '-':
            word += ch
            return Tokens.UNSUB.value, word
        else:
            getChar.index -= 1
            return Tokens.SUB.value, word
    elif ch == '*':
        word = ch
        ch = getChar()
        if ch == '=':
            word += ch
            return Tokens.MASSM.value, word
        else:
            getChar.index -= 1
            return Tokens.MUL.value, word
    elif ch == '/':
        word = ch
        ch = getChar()
        if ch == '=':
            word += ch
            return Tokens.DASSM.value, word
        else:
            getChar.index -= 1
            return Tokens.DIV.value, word
    elif ch == '%':
        word = ch
        ch = getChar()
        if ch == '=':
            word += ch
            return Tokens.MODASSM.value, word
        else:
            getChar.index -= 1
            return Tokens.MOD.value, word
    elif ch == '<':
        word = ch
        ch = getChar()
        if ch == '=':
            word += ch
            return Tokens.LEQ.value, word
        else:
            getChar.index -= 1
            return Tokens.LT.value, word
    elif ch == '>':
        word = ch
        ch = getChar()
        if ch == '=':
            word += ch
            return Tokens.GEQ.value, word
        else:
            getChar.index -= 1
            return Tokens.GT.value, word
    elif ch == '!':
        word = ch
        ch = getChar()
        if ch == '=':
            word += ch
            return Tokens.NEQ.value, word
        else:
            getChar.index -= 1
            return Tokens.ERR.value, word
    elif ch == '\\':
        word = ch
        ch = getChar()
        if ch == '*':
            while True:
                word += ch
                ch = getChar()
                if ch == -1:
                    return Tokens.ERR.value, "Error! EOF while incomment"
                elif ch == '*':
                    ch = getChar()
                    if ch == '\\':
                        word += ch
                        return Tokens.COM.value, word
        else:
            return Tokens.ERR.value, word
    elif ch == '"':
        word = ch
        while True:
            ch = getChar()
            if ch != -1:
                word += ch
            if ch == -1:
                return Tokens.ERR.value, word
            elif ch == '"':
                return Tokens.STRCON.value, word
    elif ch == "'":
        word = ch
        ch =getChar()
        word += ch
        ch1 = getChar()
        if ch1 == "'":
            word += ch1
            return Tokens.CHARCON.value, word
        else:
            getChar.index -= 1
            while True:
                ch = getChar()
                if ch == -1:
                    break
                word += ch
                if ch == "'":
                    word += ch
                    break
            return Tokens.ERR.value, word
    elif str(ch).isdigit():
        decimal = False
        isValid = True
        count = 0
        word = ch
        while True:
            ch = getChar()
            if ch == -1:
                break
            word += ch
            if ch == '.':
                if count == 1 and isValid == True:
                    nextToken.checkDot = True
                    break
                if isValid == False:
                    getChar.index -= 1
                    break
                count += 1
                ch = getChar()
                word += ch
                if ch == '.':
                    isValid = False
                if ch == -1:
                    ch = '.'
                    break
                if ch.isdigit():
                    if decimal == True:
                        isValid = False
                    decimal = True
                elif not validToken(ch):
                    isValid = False
                else:
                    getChar.index -= 1
                    break
            elif not ch.isdigit():
                if not validToken(ch):
                    isValid = False
                else:
                    getChar.index -= 1
                    break
        if word[-1] == '.':
            getChar.index -= 1
            word = word[:-1]
            nextToken.checkDot = True
        if isValid == False:
            word = word[:-1]
            return Tokens.ERR.value, word
        elif decimal == True:
            nextToken.checkDot = True
            return Tokens.DECCON.value, word
        else:
            word = word[:-1]
            return Tokens.INTCON.value, word
    elif str(ch).isupper():
        word = ch
        while True:
            ch = getChar()
            if ch != -1:
                word += ch
            if validToken(ch) or ch == '.' or ch == -1:
                getChar.index -= 1
                break
            elif ch == '!':
                if getChar() == '=':
                    getChar.index -= 1
                    break
                else:
                    getChar.index -= 1
        getChar.index -= 1
        word = word[:-1]
        return Tokens.ERR.value, word
    elif str(ch).islower():
        word = ch
        while True:
            ch = getChar()
            if validToken(ch) or ch == '.' or ch == ' ' or ch == -1 or ch == '\n':
                break
            elif ch == '!':
                if getChar() == '=':
                    getChar.index -= 1
                    break
                else:
                    getChar.index -= 1
            word += ch
        keysList = list(keywords.keys())
        if keysList.count(word) > 0:
            getChar.index -= 1
            return keywords[word], word
        elif word == 'and':
            getChar.index -= 1
            return Tokens.AND.value, word
        elif word == 'or':
            getChar.index -= 1
            return Tokens.OR.value, word
        elif word == 'not':
            getChar.index -= 1
            return Tokens.NOT.value, word
        elif ch == '(':
            getChar.index -= 1
            return Tokens.FUNC_NAME.value, word
        else:
            word = word[:-1]
            getChar.index -= 1
            return Tokens.ERR.value, word
    elif ch == '$':
        isValid = True
        word = ch
        while True:
            ch = getChar()
            if ch == -1:
                break
            if ch.isdigit() or ch.isalpha() or ch == '_':
                pass
            elif validToken(ch) or ch == '.' or ch == ' ' or ch == '\n':
                getChar.index -= 1
                break
            elif ch == '!':
                if getChar() == '=':
                    getChar.index -= 2
                    break
                else:
                    getChar.index -= 1
                    isValid = False
            else:
                isValid = False
            word += ch
        if isValid == True:
            return Tokens.ID.value, word
        else:
            return Tokens.ERR.value, word
    elif ch == ' ':
        return nextToken()
    elif ch == '\n':
        return nextToken()
    elif ch == '\t':
        return nextToken()
    else:
        word = ch
        while True:
            ch = getChar()
            if ch != -1:
                word += ch
            if validToken(ch) or ch == '.' or ch == -1:
                break
        return Tokens.ERR.value, word

nextToken.checkDot = False


#Parser
def checkEOF():
    global token
    global lexeme
    if token == Tokens.EOFILE.value:
        sys.exit("Parsing Completed!!!")

def checkOtherOptions():
    global token
    global lexeme
    checkEOF()
    if token == Tokens.COM.value:
        token, lexeme = nextToken()
        checkEOF()
        checkOtherOptions()
    elif token == Tokens.ERR.value:
        print(token,lexeme)
        token, lexeme = nextToken()
        checkEOF()
        checkOtherOptions()
    

def BLOCK():
    global token
    global lexeme
    if lexeme == "{":
        token, lexeme = nextToken()
        checkOtherOptions()
        STATEMENTS()
        if lexeme == "}":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error! } expected")
    else:
        STATEMENT()

def STATEMENTS():
    global token
    global lexeme
    if lexeme == ".":
        token, lexeme = nextToken()
        checkOtherOptions()
    else:
        STATEMENT()
        
def STATEMENT():
    global token
    global lexeme
    if lexeme == "boolean" or lexeme == "integer" or lexeme == "decimal" or lexeme == "char" or lexeme == "text" or lexeme == ",":
        DECLARATION()
        STATEMENTprime()
    elif token == Tokens.ID.value or token == Tokens.INTCON.value or token == Tokens.DECCON.value or token == Tokens.STRCON.value or token == Tokens.CHARCON.value:
        EXPRESSION()
        STATEMENTprime()
    elif lexeme == "checkif":
        CONDITIONAL_STATEMENT()
        STATEMENTprime()
    elif lexeme == "loop":
        FOR_LOOP()
        STATEMENTprime()
    elif lexeme == "until":
        WHILE_LOOP()
        STATEMENTprime()
    elif lexeme == "repeat":
        DO_WHILE_LOOP()
        STATEMENTprime()
    else:
        print("Unexpected Token")
        token, lexeme = nextToken()
        checkOtherOptions()
        
def STATEMENTprime():
    global token
    global lexeme
    if lexeme == ".":
        token, lexeme = nextToken()
        checkOtherOptions()
    elif lexeme == "}":
        pass
    else:
        STATEMENT()
        STATEMENTprime()

def DECLARATION():
    global token
    global lexeme
    if lexeme == ",":
        token, lexeme = nextToken()
        checkOtherOptions()
        EXPRESSION()
    else:
        DATATYPE()
        DECLARATIONprime()
        
def DECLARATIONprime():
    global token
    global lexeme
    if lexeme == ":":
        token, lexeme = nextToken()
        checkOtherOptions()
        EXPRESSION()
    elif lexeme != '[':
        print("Error, unexpected token. : expected")
    else:
        if lexeme == "[":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. [ expected")
        DECLARATIONdoubleprime()

def DECLARATIONdoubleprime():
    global token
    global lexeme
    if lexeme == "]":
        token, lexeme = nextToken()
        checkOtherOptions()
        if lexeme == ":":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. : expected")
        EXPRESSION()
    elif lexeme == ",":
        token, lexeme = nextToken()
        checkOtherOptions()
        if lexeme == "]":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. ] expected")
        if lexeme == ":":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. : expected")
        EXPRESSION()
    else:
        EXPRESSION()
        DECLARATIONtripleprime()
        
def DECLARATIONtripleprime():
    global token
    global lexeme
    if lexeme == "]":
        token, lexeme = nextToken()
        checkOtherOptions()
        if lexeme == ":":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. : expected")
        EXPRESSION()
    else:
        if lexeme == ",":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. , expected")
        EXPRESSION()
        if lexeme == "]":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. ] expected")
        if lexeme == ":":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. : expected")
        EXPRESSION()

def EXPRESSION():
    global token
    global lexeme
    if token == Tokens.ID.value or token == Tokens.INTCON.value or token == Tokens.DECCON.value or token == Tokens.STRCON.value or token == Tokens.CHARCON.value:
        token, lexeme = nextToken()
        checkOtherOptions()
        EXPRESSIONprime()
    elif lexeme == ")":
        pass
    else:
        print("Error, unexpected token. constant or identifer expected")

def EXPRESSIONprime():
    global token
    global lexeme
    if lexeme == ",":
        token, lexeme = nextToken()
        checkOtherOptions()
    elif lexeme == "+" or lexeme == "-" or lexeme == "*" or lexeme == "/" or lexeme == "=" or lexeme == "new" or lexeme == "!=" or lexeme == "<" or lexeme == ">" or lexeme == "<=" or lexeme == ">=" or lexeme == "==" or lexeme == "++" or lexeme == "--" or lexeme == ":" or lexeme == "." or lexeme == "and" or lexeme == "or" or lexeme == "not":
        OP()
        EXPRESSION()
        EXPRESSIONprime()
    elif lexeme == ")":
        pass
    elif lexeme == ".":
        token, lexeme = nextToken()
        checkOtherOptions()
    else:
        pass
       # print("Error, unexpected token. dot expected")
def OP():
    global token
    global lexeme
    if lexeme == "+" or lexeme == "-" or lexeme == "*" or lexeme == "/" or lexeme == "=" or lexeme == "new" or lexeme == "!=" or lexeme == "<" or lexeme == ">" or lexeme == "<=" or lexeme == ">=" or lexeme == "==" or lexeme == "++" or lexeme == "--" or lexeme == ":" or lexeme == "." or lexeme == "and" or lexeme == "or" or lexeme == "not":
        token, lexeme = nextToken()
        checkOtherOptions()
    else:
        EXPRESSION()
    
def DATATYPE():
    global token
    global lexeme
    if lexeme == "boolean" or lexeme == "integer" or lexeme == "decimal" or lexeme == "char" or lexeme == "text":
        token, lexeme = nextToken()
        checkOtherOptions()
    else:
        print("Error, unexpected token. Datatype expected")

def CONDITIONAL_STATEMENT():
    global token
    global lexeme
    if lexeme == "checkif":
        token, lexeme = nextToken()
        checkOtherOptions()
        if lexeme == "(":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. ( expected")
        EXPRESSION()
        if lexeme == ")":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. ) expected")
        BLOCK()
        CONDITIONAL_STAREMENTprime()
    else:
        print("Error, unexpected token. checkif keyword expected")

def CONDITIONAL_STAREMENTprime():
    global token
    global lexeme
    if lexeme == "else":
        token, lexeme = nextToken()
        checkOtherOptions()
        BLOCK()
        
def FOR_LOOP():
    global token
    global lexeme
    if lexeme == "loop":
        token, lexeme = nextToken()
        checkOtherOptions()
        if lexeme == "(":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. ( expected")
        STATEMENT()
        if lexeme == ".":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. dot expected")
        STATEMENT()
        if lexeme == ".":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. dot expected")
        STATEMENT()
        if lexeme == ")":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. ) expected")
        BLOCK()
    else:
        print("Error, unexpected token. loop keyword expected")
        
def WHILE_LOOP():
    global token
    global lexeme
    if lexeme == "until":
        token, lexeme = nextToken()
        checkOtherOptions()
        if lexeme == "(":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. ( expected")
        STATEMENT()
        if lexeme == ")":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. ) expected")
        BLOCK()
    else:
        print("Error, unexpected token. until keyword expected")

def DO_WHILE_LOOP():
    global token
    global lexeme
    if lexeme == "repeat":
        token, lexeme = nextToken()
        checkOtherOptions()
        BLOCK()
        if lexeme == "until":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. until keyword expected")
        if lexeme == "(":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. ( expected")
        STATEMENT()
        if lexeme == ")":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. ) expected")
    else:
        print("Error, unexpected token. repeat keyword expected")

def FUNCTION():
    global token
    global lexeme
    if lexeme == "function":
        token, lexeme = nextToken()
        checkOtherOptions()
        if token == Tokens.FUNC_NAME.value:
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. function name expected")
        if lexeme == "(":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. ( expected")
        PARAMETER()
        if lexeme == ")":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. ) expected")
        if lexeme == ":":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. : expected")
        FUNCTIONprime()
    else:
        print("Error, unexpected token. function keyword expected")

def FUNCTIONprime():
    global token
    global lexeme
    if lexeme == "void":
        token, lexeme = nextToken()
        checkOtherOptions()
        if lexeme == "{":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. { expected")
        STATEMENTS()
        if lexeme == "}":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. } expected")
    else:
        DATATYPE()
        if lexeme == "{":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. { expected")
        STATEMENTS()
        if lexeme == "throw":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. throw keyword expected")
        EXPRESSION()
        if lexeme == "}":
            token, lexeme = nextToken()
            checkOtherOptions()
        else:
            print("Error, unexpected token. } expected")

def PARAMETER():
    global token
    global lexeme
    if lexeme == ")":
        pass
    else:
        DECLARATION()
        PARAMETERprime()

def PARAMETERprime():
    global token
    global lexeme
    if lexeme == ",":
        token, lexeme = nextToken()
        checkOtherOptions()
        PARAMETER()
        
def PARSER():
    global token
    global lexeme
    while True:
        if lexeme == "function":
            FUNCTION()
        else:
            BLOCK()
    print("Parsing completed!!!!")

    
    
keywords = {"boolean":Tokens.BOOL_KEY.value, "integer": Tokens.INT_KEY.value, "decimal": Tokens.DEC_KEY.value, "char":Tokens.CHAR_KEY.value, "text":Tokens.TEXT_KEY.value, "put":Tokens.PUT_KEY.value, "get":Tokens.GET_KEY.value, "checkif":Tokens.CHECKIF_KEY.value, "elif":Tokens.ELIF_KEY.value, "else": Tokens.ELSE_KEY.value, "loop":Tokens.LOOP_KEY.value, "until":Tokens.UNTIL_KEY.value, "repeat":Tokens.REP_KEY.value, "function": Tokens.FUN_KEY.value, "void":Tokens.VOID_KEY.value, "new":Tokens.NEW_KEY.value, "throw":Tokens.THROW_KEY.value, "and":Tokens.AND.value, "or":Tokens.OR.value, "not":Tokens.NOT.value}
file = open("file.txt", 'r')
content = file.read()
token, lexeme = nextToken()
try:
    checkOtherOptions()
    PARSER()
except SystemExit as e:
    print(e)
except:
    raise

