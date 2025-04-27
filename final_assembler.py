import os
import sys
import argparse
from random import randint
import numpy as np
import math

def ADD(instr):
    opcode=1
    funct=0x00
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    rs=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rs,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5

def ADDU(instr):
    opcode=1
    funct=0x02
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    rs=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rs,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5

def SUB(instr):
    opcode=1
    funct=0x01
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    rs=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rs,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5

def SUBU(instr):
    opcode=1
    funct=0x04
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    rs=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rs,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5

def AND(instr):
    opcode=1
    funct=0x08
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    rs=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rs,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5

def NOT(instr):
    opcode=1
    funct=0x0c
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    rs=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rs,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5

def OR(instr):
    opcode=1
    funct=0x0a
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    rs=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rs,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5

def XOR(instr):
    opcode=1
    funct=0x0d
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    rs=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rs,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5

def MADD(instr):
    opcode=1
    funct=0x06
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    rs=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rs,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5

def MADDU(instr):
    opcode=1
    funct=0x07
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    rs=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rs,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5

def MUL(instr):
    opcode=1
    funct=0x27
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    rs=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rs,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5

def ADDI(instr):
    opcode=2
    funct=0x04
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    immi=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(immi,10)
    instr_val_4 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4

def ADDIU(instr):
    opcode=2
    funct=0x05
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    immi=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(immi,10)
    instr_val_4 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4

def ANDI(instr):
    opcode=2
    funct=0x09
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    immi=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(immi,10)
    instr_val_4 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4

def ORI(instr):
    opcode=2
    funct=0x0b
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    immi=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(immi,10)
    instr_val_4 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4

def XORI(instr):
    opcode=2
    funct=0x0e
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    immi=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(immi,10)
    instr_val_4 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4

def SLL(instr):
    opcode=2
    funct=0x0f
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    shamt=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(shamt,10)
    instr_val_4 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4

def SRA(instr):
    opcode=2
    funct=0x12
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    shamt=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(shamt,10)
    instr_val_4 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4

def SRL(instr):
    opcode=2
    funct=0x10
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    shamt=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(shamt,10)
    instr_val_4 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4

def SLA(instr):
    opcode=2
    funct=0x11
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    shamt=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(shamt,10)
    instr_val_4 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4

def LW(instr):
    opcode=3
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    offset=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(offset,16)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3

def SW(instr):
    opcode=4
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    offset=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(offset,16)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3

def LUI(instr):
    opcode=5
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    imm=int(str_list[2])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(0,5)
    instr_val_3 =np.binary_repr(imm,16)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3

def SGT(instr):
    opcode=10
    funct=0x13
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    rs=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rs,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5

def SLT(instr):
    opcode=10
    funct=0x14
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    rs=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rs,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5

def SEQ(instr):
    opcode=10
    funct=0x15
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    rs=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rs,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5

def SGTU(instr):
    opcode=10
    funct=0x16
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    rs=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rs,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5

def SLTU(instr):
    opcode=10
    funct=0x17
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    rs=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(rs,5)
    instr_val_4 =np.binary_repr(0,5)
    instr_val_5 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4+instr_val_5

def BEQ(instr):
    opcode=6
    funct=0x15
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    label=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(label,10)
    instr_val_4 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4

def BNE(instr):
    opcode=6
    funct=0x15
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    label=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(label,10)
    instr_val_4 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4

def BGT(instr):
    opcode=6
    funct=0x13
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    label=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(label,10)
    instr_val_4 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4

def BLE(instr):
    opcode=6
    funct=0x14
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    label=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rd,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(label,10)
    instr_val_4 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4

def BGTE(instr):
    opcode=6
    funct=0x14
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    label=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rt,5)
    instr_val_2 =np.binary_repr(rd,5)
    instr_val_3 =np.binary_repr(label,10)
    instr_val_4 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4

def BLEQ(instr):
    opcode=6
    funct=0x13
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    label=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rt,5)
    instr_val_2 =np.binary_repr(rd,5)
    instr_val_3 =np.binary_repr(label,10)
    instr_val_4 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4

def BLEU(instr):
    opcode=6
    funct=0x17
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    label=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rt,5)
    instr_val_2 =np.binary_repr(rd,5)
    instr_val_3 =np.binary_repr(label,10)
    instr_val_4 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4

def BGTU(instr):
    opcode=6
    funct=0x16
    instr=instr.strip()
    str_list=instr.split(',')
    rd=int(str_list[1])
    rt=int(str_list[2])
    label=int(str_list[3])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(rt,5)
    instr_val_2 =np.binary_repr(rd,5)
    instr_val_3 =np.binary_repr(label,10)
    instr_val_4 =np.binary_repr(funct,6)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3+instr_val_4

def JUMP(instr):
    opcode=7
    instr=instr.strip()
    str_list=instr.split(',')
    target=int(str_list[1])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(target,26)
    return instr_val_0+instr_val_1

def JAL(instr):
    opcode=9
    instr=instr.strip()
    str_list=instr.split(',')
    target=int(str_list[1])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(target,26)
    return instr_val_0+instr_val_1

def JR(instr):
    opcode=8
    instr=instr.strip()
    str_list=instr.split(',')
    rt=int(str_list[1])
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(0,5)
    instr_val_2 =np.binary_repr(rt,5)
    instr_val_3 =np.binary_repr(0,16)
    return instr_val_0+instr_val_1+instr_val_2+instr_val_3

def FINISH(instr):
    opcode=0x3f
    instr_val_0 =np.binary_repr(opcode,6)
    instr_val_1 =np.binary_repr(0,26)
    return instr_val_0+instr_val_1

file_a=open("machine_code.txt","w")
file_b=open("assembly.txt")

Instrs=file_b.readlines()

for instrs in Instrs:
    if(instrs[0:3]=="ADD" and instrs[0:4]!="ADDI"):
        ret_instr=ADD(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="ADDU"):
        ret_instr=ADDU(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="SUB"):
        ret_instr=SUB(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="SUBU"):
        ret_instr=SUBU(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="AND" and instrs[0:4]!="ANDI"):
        ret_instr=AND(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="NOT"):
        ret_instr=NOT(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:2]=="OR" and instrs[0:3]!="ORI"):
        ret_instr=OR(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="XOR" and instrs[0:4]!="XORI"):
        ret_instr=XOR(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="MADD"):
        ret_instr=MADD(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:5]=="MADDU"):
        ret_instr=MADDU(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="MUL"):
        ret_instr=MUL(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="ADDI"):
        ret_instr=ADDI(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:5]=="ADDIU"):
        ret_instr=ADDIU(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="ANDI"):
        ret_instr=ANDI(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="ORI"):
        ret_instr=ORI(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="XORI"):
        ret_instr=XORI(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="SLL"):
        ret_instr=SLL(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="SRA"):
        ret_instr=SRA(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="SRL"):
        ret_instr=SRL(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="SLA"):
        ret_instr=SLA(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:2]=="LW"):
        ret_instr=LW(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:2]=="SW"):
        ret_instr=SW(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="LUI"):
        ret_instr=LUI(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="SGT"):
        ret_instr=SGT(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="SGTU"):
        ret_instr=SGTU(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="SLT"):
        ret_instr=SLT(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="SLTU"):
        ret_instr=SLTU(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="SEQ"):
        ret_instr=SEQ(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="BEQ"):
        ret_instr=BEQ(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="BNE"):
        ret_instr=BNE(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="BGT"):
        ret_instr=BGT(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="BGTU"):
        ret_instr=BGTU(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="BLE"):
        ret_instr=BLE(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="BLEU"):
        ret_instr=BLEU(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="BGTE"):
        ret_instr=BGTE(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="BLEQ"):
        ret_instr=BLEQ(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:4]=="JUMP"):
        ret_instr=JUMP(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:3]=="JAL"):
        ret_instr=JAL(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:2]=="JR"):
        ret_instr=JR(instrs)
        file_a.write(ret_instr +','+'\n')
    elif(instrs[0:6]=="FINISH"):
        ret_instr=FINISH(instrs)
        file_a.write(ret_instr +','+'\n')
    else:
        print(instrs[0:14])
        print("danger danger undefined instruction!!!!")
        
file_a.close()
file_b.close()