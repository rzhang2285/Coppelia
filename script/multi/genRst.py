import os
import sys
import argparse

signals_except_1 = [
        'top->__VlSymsp->TOP__or1200_cpu__or1200_except.__PVT__delayed1_ex_dslot', 
        'top->__VlSymsp->TOP__or1200_cpu__or1200_except.ex_dslot'
        ]
signals_except_2 = [
        'top->__VlSymsp->TOP__or1200_cpu__or1200_except.wb_pc'
        ]
signals_except_3 = [
        'top->__VlSymsp->TOP__or1200_cpu__or1200_except.__PVT__delayed_iee'
        ]
signals_except_4 = [
        'top->__VlSymsp->TOP__or1200_cpu__or1200_except.__PVT__delayed_tee'
        ]
signals_except_5 = [
        'top->__VlSymsp->TOP__or1200_cpu__or1200_except.__PVT__state', 
        'top->__VlSymsp->TOP__or1200_cpu__or1200_except.except_type'
        ]
signals_except_6 = [
        'top->__VlSymsp->TOP__or1200_cpu__or1200_except.__PVT__ex_freeze_prev'
        ]
signals_except_7 = [
        'top->__VlSymsp->TOP__or1200_cpu__or1200_except.__PVT__trace_trap'
        ]
signals_sprs = [
        'top->__VlSymsp->TOP__or1200_cpu__or1200_sprs.__PVT__sr_reg_bit_eph_select'
        ]
signals_mult_mac_1 = [
        'top->__VlSymsp->TOP__or1200_cpu.__PVT__or1200_mult_mac__DOT__mul_stall_count'
        ]
signals_mult_mac_2 = [
        'top->__VlSymsp->TOP__or1200_cpu.__PVT__or1200_mult_mac__DOT__div_free', 
        'top->__VlSymsp->TOP__or1200_cpu.__PVT__or1200_mult_mac__DOT__div_cntr', 
        'top->__VlSymsp->TOP__or1200_cpu.__PVT__or1200_mult_mac__DOT__div_quot_r'
        ]
signals_genpc_1 = [
        'top->__VlSymsp->TOP__or1200_cpu.__PVT__or1200_genpc__DOT__wait_lsu'
        ]
signals_genpc_2 = [
        'top->__VlSymsp->TOP__or1200_cpu.__PVT__or1200_genpc__DOT__pcreg_select'
        ]
signals_freeze_1 = [
        'top->__VlSymsp->TOP__or1200_cpu.__PVT__or1200_freeze__DOT__multicycle_cnt'
        ]
signals_freeze_2 = [
        'top->__VlSymsp->TOP__or1200_cpu.__PVT__or1200_freeze__DOT__waiting_on'
        ]
signals_ctrl = [
        'top->__VlSymsp->TOP__or1200_cpu__or1200_ctrl.__PVT__sp_return_counter'
        ]
signals_operandmuxes_1 = [
        'top->__VlSymsp->TOP__or1200_cpu.__PVT__or1200_operandmuxes__DOT__saved_a'
        ]
signals_operandmuxes_2 = [
        'top->__VlSymsp->TOP__or1200_cpu.__PVT__or1200_operandmuxes__DOT__saved_b'
        ]
signals_register = [
        'top->__VlSymsp->TOP__or1200_cpu__or1200_rf__rf_a.__PVT__mem[16]',
        'top->__VlSymsp->TOP__or1200_cpu__or1200_rf__rf_b.__PVT__mem[17]'
        ]

fsm = [signals_except_1, signals_except_2, signals_except_3, 
        signals_except_4, signals_except_5, signals_except_6, 
        signals_except_7, signals_sprs, signals_mult_mac_1, 
        signals_mult_mac_2, signals_genpc_1, signals_genpc_2, 
        signals_freeze_1, signals_freeze_2, signals_ctrl, 
        signals_operandmuxes_1, signals_operandmuxes_2, 
        signals_register]

sim_signals_except_1 = ['delayed1_ex_dslot', 'ex_dslot']
sim_signals_except_2 = ['wb_pc']
sim_signals_except_3 = ['delayed_iee']
sim_signals_except_4 = ['delayed_tee']
sim_signals_except_5 = ['state', 'except_type']
sim_signals_except_6 = ['ex_freeze_prev']
sim_signals_except_7 = ['trace_trap']
sim_signals_sprs = ['sr_reg_bit_eph_select']
sim_signals_mult_mac_1 = ['mul_stall_count']
sim_signals_mult_mac_2 = ['div_free', 'div_cntr', 'div_quot_r']
sim_signals_genpc_1 = ['wait_lsu']
sim_signals_genpc_2 = ['pcreg_select']
sim_signals_freeze_1 = ['multicycle_cnt']
sim_signals_freeze_2 = ['waiting_on']
sim_signals_ctrl = ['sp_return_counter']
sim_signals_operandmuxes_1 = ['saved_a']
sim_signals_operandmuxes_2 = ['saved_b']
sim_signals_register = ['r1', 'r2']

sim_fsm = [sim_signals_except_1, sim_signals_except_2, sim_signals_except_3,
        sim_signals_except_4, sim_signals_except_5, sim_signals_except_6,
        sim_signals_except_7, sim_signals_sprs, sim_signals_mult_mac_1,
        sim_signals_mult_mac_2, sim_signals_genpc_1, sim_signals_genpc_2,
        sim_signals_freeze_1, sim_signals_freeze_2, sim_signals_ctrl,
        sim_signals_operandmuxes_1, sim_signals_operandmuxes_2, sim_signals_register]

def genrst(fsm_no, last_cycle, assert_list):
    rstfile = 'tb_reset.cpp';
    lstfile = 'lstValues.txt';

    testbench = open(rstfile, 'w')
    lastfile = open(lstfile, 'w')

    testbench.write('#include "obj_dir/Vor1200_cpu.h"\n')
    testbench.write('#include "obj_dir/Vor1200_cpu__Syms.h"\n')
    testbench.write('#include "verilated.h"\n')
    testbench.write('#include <iostream>\n')
    testbench.write('#include <typeinfo>\n')

    testbench.write('int main(int argc, char **argv) {\n')
    testbench.write('   Vor1200_cpu* top = new Vor1200_cpu;\n')
    testbench.write('   int clk, rst;\n')
    testbench.write('\n')

    testbench.write('   rst = 1;\n')
    testbench.write('   clk = 1;\n')
    testbench.write('   top->rst = rst;\n')
    testbench.write('\n')

    testbench.write('   clk = !clk;\n')
    testbench.write('   top->clk = clk;\n')
    testbench.write('   top->eval();\n')
    testbench.write('\n')

    testbench.write('   clk = !clk;\n')
    testbench.write('   top->clk = clk;\n')
    testbench.write('   top->eval();\n')
    testbench.write('\n')
    
    testbench.write('   clk = !clk;\n')
    testbench.write('   top->clk = clk;\n')
    testbench.write('   top->eval();\n')
    testbench.write('\n')
    
    testbench.write('   clk = !clk;\n')
    testbench.write('   top->clk = clk;\n')
    testbench.write('   top->eval();\n')
    testbench.write('\n')

    mk_list = []
    for a in assert_list[::2]:
        for m in sim_fsm:
            if a in m:
                ind = sim_fsm.index(m)
                mk_list.append(ind)

    for i in fsm_no:
        for s in fsm[int(i)]:
            testbench.write('   std::cout << (int)'+s+' << " ";\n') 
            lastfile.write('-1 ')
    for m in mk_list:
        for s in sim_fsm[int(m)]:
            ind_1 = sim_fsm[int(m)].index(s)
            testbench.write('   std::cout << (int)'+fsm[int(m)][ind_1]+' << " ";\n')
            if s in assert_list:
                ind_2 = assert_list.index(s)
                lastfile.write(str(assert_list[ind_2+1])+' ')
            else:
                lastfile.write('-1 ')

    
        
    testbench.write('\n')
    lastfile.write('\n')

    testbench.write('   delete top;\n')
    testbench.write('   exit(0);\n')
    testbench.write('}\n')

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--fsmno", nargs='*', default=())
parser.add_argument("-l", "--lastcycle", type=int, default=0)
parser.add_argument("-a", "--assertlist", nargs='*', default=())
args = parser.parse_args()
genrst(args.fsmno, args.lastcycle, args.assertlist)

