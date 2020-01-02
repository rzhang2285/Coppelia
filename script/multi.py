#!/usr/bin/env python

import os
import sys
import glob

#starting_fsm_nos = '0 1 2 3 4 5 6 7 8 9 11 12 13 -1'
#starting_fsm_nos = '0 1 2 3 4 -1'
#starting_fsm_nos = '-1'
#starting_fsm_nos = '5 6 7 8 9 -1'
#starting_fsm_nos = '11 12 13 14 -1'
starting_fsm_nos = '11 12 13 -1'

input_no = 15
regONLY = 0

def convertAssertList(assertlist):
    astr = ''
    for a in assertlist:
        astr = astr + a[0] + ' ' + str(a[1]) + ' '
    print astr
    return astr


def getResetValues():
    with open("rstValues.txt") as f:
        content = f.readlines()
        c = content[0]
        line = c.replace("\n", "")
        parts = line.split(" ")
        return parts

def getNotReset(count):
    notResetList = []
    with open("testcases.csv") as f:
        content = f.readlines()
        for c in content:
            line = c.replace("\n", "")
            parts = line.split(",")
            if (c == content[0]):
                nameList = parts
            if (parts[0] == 'test'+str(count)):
                rstValues = getResetValues()
                for i in range(len(parts)):
                    if (i >= input_no):
			print "i: ", i
			print "parts[i]: ", parts[i]
                        if (int(parts[i]) != int(rstValues[i-input_no])):
                            notResetList.append([nameList[i], int(parts[i])])
    print "notResetList: ", notResetList
    return notResetList



# prepare for klee
os.system('ulimit -s unlimited')

# clean directory 
os.system('rm -rf obj_dir')
os.system('rm -rf resultfiles')
os.system('rm *.txt')



# generate tb_reset.cpp
os.system('python multi/genRst.py -f '+starting_fsm_nos+' -l 1')

# generate reset state values
os.system('verilator -O3 -Wall -language 1364-2001 --top-module or1200_cpu +incdir+../cores/or1200 -Mdir obj_dir -cc ../cores/or1200/*.v --exe tb_reset.cpp')
os.system('make -j -C obj_dir/ -f Vor1200_cpu.mk Vor1200_cpu')
os.system('obj_dir/Vor1200_cpu > rstValues.txt')

# generate testbench
os.system('python multi/genTestBench.py -f '+starting_fsm_nos+' -l 1')

# clean directory 
os.system('rm -rf obj_dir')



# run last cycle
os.system('cp ../include/constraints.h.sfONLY  ../include/constraints.h')
os.system('verilator -O3 -Wall -language 1364-2001 --top-module or1200_cpu +incdir+../cores/or1200 -Mdir obj_dir -cc ../cores/or1200/*.v --exe tb_cpu.cpp')
os.system('make -j -C obj_dir/ -f Vor1200_cpu.mk Vor1200_cpu')
os.system('extract-bc -l llvm-link obj_dir/Vor1200_cpu')
os.system('klee -coi-prune=false -fast-validation=true --search=hardware -halt-when-fired=true -emit-all-errors -max-memory=100000000 --libc=uclibc --posix-runtime obj_dir/Vor1200_cpu.bc')


os.system('cp ../include/constraints.h.basic  ../include/constraints.h')
count = 1
errfiles = glob.glob(os.path.join('obj_dir/klee-last', '*.err'))
errfiles.sort();
errfile = errfiles[-1]
print errfile
os.system('mkdir resultfiles')


while 1:
    errfiles = glob.glob(os.path.join('obj_dir/klee-last', '*.err'))
    if errfiles:
        errfiles.sort()
        errfile = errfiles[-1]
        pcfile = errfile.replace('assert.err', 'pc')
        ktestfile = errfile.replace('assert.err', 'ktest')
        print ktestfile
        os.system('cp '+ktestfile+' resultfiles/test'+str(count)+'.ktest')
        os.system('cp '+pcfile+' resultfiles/test'+str(count)+'.pc')
        os.system('cp '+errfile+' resultfiles/test'+str(count)+'.assert.err')
        os.system('mkdir currfiles')
        os.system('cp '+ktestfile+' currfiles/test'+str(count)+'.ktest')
        os.system('cp '+pcfile+' currfiles/test'+str(count)+'.pc')
        os.system('cp '+errfile+' currfiles/test'+str(count)+'.assert.err')
        os.system('./multi/ktest2cvs.py currfiles')
        os.system('rm -r currfiles')
   
    assertList = getNotReset(count)
    print assertList
    assert_arg = convertAssertList(assertList)
    if (len(assertList) == 1 and assertList[0][0] == "r1"):
        regONLY = 1
    count += 1
    if (len(assertList) == 0):
	# clean up temporary files
	os.system("mv instructions.txt resultfiles")
	os.system("rm -rf obj_dir")
	os.system("rm *.cpp")
	os.system("rm *.csv")
	os.system("rm *.txt")
	print "Done... (See resultfiles/instructions.txt for the results.)"
        quit()
   

    # generate reset file
    os.system('python multi/genRst.py -l 0 -a '+assert_arg)
    os.system('verilator -O3 -Wall -language 1364-2001 --top-module or1200_cpu +incdir+../cores/or1200 -Mdir obj_dir -cc ../cores/or1200/*.v --exe tb_reset.cpp')
    os.system('make -j -C obj_dir/ -f Vor1200_cpu.mk Vor1200_cpu')
    os.system('obj_dir/Vor1200_cpu > rstValues.txt')

    os.system('python multi/genTestBench.py -l 0 -a '+assert_arg)
    if (regONLY == 1):
        os.system('cp ../include/constraints.h.movhiANDori ../include/constraints.h')
    os.system('rm -rf obj_dir')
    os.system('verilator -O3 -Wall -language 1364-2001 --top-module or1200_cpu +incdir+../cores/or1200 -Mdir obj_dir -cc ../cores/or1200/*.v --exe tb_cpu.cpp')
    os.system('make -j -C obj_dir/ -f Vor1200_cpu.mk Vor1200_cpu')
    os.system('extract-bc -l llvm-link obj_dir/Vor1200_cpu')
    os.system('klee -fast-validation=true --search=hardware -halt-when-fired=true -emit-all-errors -max-memory=100000000 --libc=uclibc --posix-runtime obj_dir/Vor1200_cpu.bc')

