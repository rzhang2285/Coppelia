from opcodes import Opcodes
from operands import Operands
from masks import Masks

opcode_mask = 0b11111100000000000000000000000000

def calOperands(insnhex, opcode, decode, pc):
    for oprname in Operands[decode[0]]:
        if (oprname == "(" or oprname == ")"):
            decode.append(oprname)
            continue
        elif (oprname == "I" or oprname == "K"):
            if ((oprname+"1") in Masks[opcode]):
                binmask = bin(Masks[opcode][oprname+"1"])
                opr1 = int(bin((insnhex & Masks[opcode][oprname+"1"]) >> (len(binmask)-len(binmask.rstrip('0')))), 2) 
                binmask = bin(Masks[opcode][oprname+"2"])
                opr2 = bin((insnhex & Masks[opcode][oprname+"2"]) >> (len(binmask)-len(binmask.rstrip('0'))))
                offset = len(opr2)
                opr2 = int(opr2, 2)
                opr = hex((opr1 << offset) + opr2)
            else: 
                binmask = bin(Masks[opcode][oprname])
                opr = hex((insnhex & Masks[opcode][oprname]) >> (len(binmask)-len(binmask.rstrip('0'))))
        elif (oprname == "N"):
            binmask = bin(Masks[opcode][oprname])
            opr = hex((((insnhex & Masks[opcode][oprname]) >> (len(binmask)-len(binmask.rstrip('0')))) << 2) + pc)
        else:
            binmask = bin(Masks[opcode][oprname])
            opr = hex((insnhex & Masks[opcode][oprname]) >> (len(binmask)-len(binmask.rstrip('0'))))
        if (oprname == "rD" or oprname == "rA" or oprname == "rB"):
            reg = "r"+str(int(opr,16))
            decode.append(reg)
        else:
            decode.append(opr)
    return decode

def disassemble(insn, pc=0):
    binopcode = bin(opcode_mask)
    insnhex = int(insn, 16)
    opcode = hex((insnhex & opcode_mask) >> (len(binopcode)-len(binopcode.rstrip('0'))))
    decode = []
    try: 
        a = Opcodes[opcode]
    except:
        decode.append("unknown")
        return decode
    if "op" in Masks[opcode]:
        binopcode = bin(Masks[opcode]["op"])
        op = hex((insnhex & Masks[opcode]["op"]) >> (len(binopcode)-len(binopcode.rstrip('0'))))
        try:
            a = Opcodes[opcode][op]
        except:
            decode.append("unknown")
            return decode
        if not isinstance(Opcodes[opcode][op], dict):
            decode.append(Opcodes[opcode][op])
            decode = calOperands(insnhex, opcode, decode, pc)
            return decode        
        if "op1" in Masks[opcode]:
            binopcode = bin(Masks[opcode]["op1"])
            op1 = hex((insnhex & Masks[opcode]["op1"]) >> (len(binopcode) - len(binopcode.rstrip('0'))))
            try:
                a = Opcodes[opcode][op][op1]
            except:
                decode.append("unknown")
                return decode
            if not isinstance(Opcodes[opcode][op][op1], dict):
                decode.append(Opcodes[opcode][op][op1])
                decode = calOperands(insnhex, opcode, decode, pc)
                return decode
            if "op2" in Masks[opcode]:
                binopcode = bin(Masks[opcode]["op2"])
                op2 = hex((insnhex & Masks[opcode]["op2"]) >> (len(binopcode) - len(binopcode.rstrip('0'))))
                decode.append(Opcodes[opcode][op][op1][op2])
                decode = calOperands(insnhex, opcode, decode, pc)
                return decode
            else:
                decode.append("unknown")
                return decode
        else:
            decode.append(Opcodes[opcode][op])
            decode = calOperands(insnhex, opcode, decode, pc)
            return decode
    else:
        decode.append(Opcodes[opcode]["0x0"])
        decode = calOperands(insnhex, opcode, decode, pc)
        return decode

#print disassemble("c0002811")
#print disassemble("d7e25ff4")
#print disassemble("9c60000c")
#print disassemble("e0a62803")

# pc = 0x228
# print disassemble("24000000", pc)
# print disassemble("2800007A", pc)
# print disassemble("21000000", pc)
# print disassemble("280000C0", pc)
# print disassemble("E0000088", pc)
# print disassemble("D4000804", pc)
# print disassemble("1B200000", pc)
# print disassemble("15000000", pc)
# print disassemble("00000ae7", pc)
# print disassemble("4090842", pc)
# print disassemble("ac000000")
# print disassemble("e0631806")
# print disassemble("e8000000")
