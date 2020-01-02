import os
import sys
import argparse
import ctypes

bug_no = 20 

full_signals_except_1 = [
        'top->__VlSymsp->TOP__or1200_cpu__or1200_except.__PVT__delayed1_ex_dslot', 
        'top->__VlSymsp->TOP__or1200_cpu__or1200_except.ex_dslot'
        ]
full_signals_except_2 = [
        'top->__VlSymsp->TOP__or1200_cpu__or1200_except.wb_pc'
        ]
full_signals_except_3 = [
        'top->__VlSymsp->TOP__or1200_cpu__or1200_except.__PVT__delayed_iee'
        ]
full_signals_except_4 = [
        'top->__VlSymsp->TOP__or1200_cpu__or1200_except.__PVT__delayed_tee'
        ]
full_signals_except_5 = [
        'top->__VlSymsp->TOP__or1200_cpu__or1200_except.__PVT__state', 
        'top->__VlSymsp->TOP__or1200_cpu__or1200_except.except_type'
        ]
full_signals_except_6 = [
        'top->__VlSymsp->TOP__or1200_cpu__or1200_except.__PVT__ex_freeze_prev'
        ]
full_signals_except_7 = [
        'top->__VlSymsp->TOP__or1200_cpu__or1200_except.__PVT__trace_trap'
        ]
full_signals_sprs = [
        'top->__VlSymsp->TOP__or1200_cpu__or1200_sprs.__PVT__sr_reg_bit_eph_select'
        ]
full_signals_mult_mac_1 = [
        'top->__VlSymsp->TOP__or1200_cpu.__PVT__or1200_mult_mac__DOT__mul_stall_count'
        ]
full_signals_mult_mac_2 = [
        'top->__VlSymsp->TOP__or1200_cpu.__PVT__or1200_mult_mac__DOT__div_free', 
        'top->__VlSymsp->TOP__or1200_cpu.__PVT__or1200_mult_mac__DOT__div_cntr', 
        'top->__VlSymsp->TOP__or1200_cpu.__PVT__or1200_mult_mac__DOT__div_quot_r'
        ]
full_signals_genpc_1 = [
        'top->__VlSymsp->TOP__or1200_cpu.__PVT__or1200_genpc__DOT__wait_lsu'
        ]
full_signals_genpc_2 = [
        'top->__VlSymsp->TOP__or1200_cpu.__PVT__or1200_genpc__DOT__pcreg_select'
        ]
full_signals_freeze_1 = [
        'top->__VlSymsp->TOP__or1200_cpu.__PVT__or1200_freeze__DOT__multicycle_cnt'
        ]
full_signals_freeze_2 = [
        'top->__VlSymsp->TOP__or1200_cpu.__PVT__or1200_freeze__DOT__waiting_on'
        ]
full_signals_ctrl = [
        'top->__VlSymsp->TOP__or1200_cpu__or1200_ctrl.__PVT__sp_return_counter'
        ]
full_signals_operandmuxes_1 = [
        'top->__VlSymsp->TOP__or1200_cpu.__PVT__or1200_operandmuxes__DOT__saved_a'
        ]
full_signals_operandmuxes_2 = [
        'top->__VlSymsp->TOP__or1200_cpu.__PVT__or1200_operandmuxes__DOT__saved_b'
        ]
full_signals_register = [
        'top->__VlSymsp->TOP__or1200_cpu__or1200_rf__rf_a.__PVT__mem[16]', 
        'top->__VlSymsp->TOP__or1200_cpu__or1200_rf__rf_b.__PVT__mem[17]' 
        ]

full_fsm = [full_signals_except_1, full_signals_except_2, full_signals_except_3, 
        full_signals_except_4, full_signals_except_5, full_signals_except_6, 
        full_signals_except_7, full_signals_sprs, full_signals_mult_mac_1, 
        full_signals_mult_mac_2, full_signals_genpc_1, full_signals_genpc_2, 
        full_signals_freeze_1, full_signals_freeze_2, full_signals_ctrl, 
        full_signals_operandmuxes_1, full_signals_operandmuxes_2, 
        full_signals_register]

signals_except_1 = ['delayed1_ex_dslot', 'ex_dslot']
signals_except_2 = ['wb_pc']
signals_except_3 = ['delayed_iee']
signals_except_4 = ['delayed_tee']
signals_except_5 = ['state', 'except_type']
signals_except_6 = ['ex_freeze_prev'] 
signals_except_7 = ['trace_trap']
signals_sprs = ['sr_reg_bit_eph_select']
signals_mult_mac_1 = ['mul_stall_count']
signals_mult_mac_2 = ['div_free', 'div_cntr', 'div_quot_r']
signals_genpc_1 = ['wait_lsu']
signals_genpc_2 = ['pcreg_select']
signals_freeze_1 = ['multicycle_cnt']
signals_freeze_2 = ['waiting_on']
signals_ctrl = ['sp_return_counter'] 
signals_operandmuxes_1 = ['saved_a']
signals_operandmuxes_2 = ['saved_b']
signals_register = ['r1', 'r2']

 
fsm = [signals_except_1, signals_except_2, signals_except_3, 
        signals_except_4, signals_except_5, signals_except_6, 
        signals_except_7, signals_sprs, signals_mult_mac_1, 
        signals_mult_mac_2, signals_genpc_1, signals_genpc_2, 
        signals_freeze_1, signals_freeze_2, signals_ctrl, 
        signals_operandmuxes_1, signals_operandmuxes_2, signals_register]

range_fsm_end = [
        '& (delayed1_ex_dslot <= 1) & (ex_dslot)); \n', 
        '); \n', # wb_pc
        '); \n', # delayed_iee
        '); \n', # delayed_tee
        '& (state <= 7) & (except_type <= 15)); \n',
        '& (ex_freeze_prev <= 1)); \n', 
        '& (trace_trap <= 1)); \n',
        '& (sr_reg_bit_eph_select <= 1)); \n',
        '& (mul_stall_count <= 3)); \n', 
        '& (div_free <= 1) & (div_cntr <= 63)); \n',
        '& (wait_lsu <= 1)); \n', 
        '& (pcreg_select <= 1)); \n',
        '& (multicycle_cnt <= 7)); \n', 
        '& (waiting_on <= 3)); \n',
        '& (sp_return_counter <= 50)); \n', 
        '& (saved_a <= 1)); \n',
        '& (saved_b <= 1)); \n',
        '); \n' # r1
        ]

range_fsm_middle = [
        '& (delayed1_ex_dslot <= 1) & (ex_dslot) \n', 
        '', # wb_pc
        '', # delayed_iee
        '', # delayed_tee
        '& (state <= 7) & (except_type <= 15) \n',
        '& (ex_freeze_prev <= 1) \n', 
        '& (trace_trap <= 1) \n',
        '& (sr_reg_bit_eph_select <= 1) \n',
        '& (mul_stall_count <= 3) \n', 
        '& (div_free <= 1) & (div_cntr <= 63) \n',
        '& (wait_lsu <= 1) \n', 
        '& (pcreg_select <= 1) \n',
        '& (multicycle_cnt <= 7) \n', 
        '& (waiting_on <= 3) \n',
        '& (sp_return_counter <= 50) \n', 
        '& (saved_a <= 1) \n',
        '& (saved_b <= 1) \n',
        '' # r1
        ]


def gentb(fsm_no, last_cycle, assert_list):
    tbfile = "tb_cpu.cpp"
    testbench = open(tbfile, 'w')

    testbench.write('#include "obj_dir/Vor1200_cpu.h"\n')
    testbench.write('#include "obj_dir/Vor1200_cpu__Syms.h"\n')
    testbench.write('#include "verilated.h"\n')
    testbench.write('#include <klee/klee.h>\n')
    testbench.write('#include "../include/constraints.h"\n')

    testbench.write('int main(int argc, char **argv) {\n')
    testbench.write('   Vor1200_cpu* top = new Vor1200_cpu;\n')
    testbench.write('   int clk, rst;\n')
    testbench.write('\n')

    testbench.write('   rst = 1; \n')
    testbench.write('   top->rst = rst; \n')
    testbench.write('   clk = 1; \n')
    testbench.write('   clk = !clk; \n')
    testbench.write('   top->clk = clk; \n')
    testbench.write('   top->eval(); \n')
    testbench.write('   clk = !clk; \n')
    testbench.write('   top->clk = clk; \n')
    testbench.write('   top->eval(); \n')
    testbench.write('   clk = !clk; \n')
    testbench.write('   top->clk = clk; \n')
    testbench.write('   top->eval(); \n')
    testbench.write('   clk = !clk; \n')
    testbench.write('   top->clk = clk; \n')
    testbench.write('   top->eval(); \n')


    testbench.write('unsigned int icpu_dat_i, icpu_ack_i, icpu_rty_i, icpu_err_i;\n')
    testbench.write('unsigned int icpu_adr_i, icpu_tag_i, dcpu_dat_i, dcpu_ack_i;\n')
    testbench.write('unsigned int dcpu_rty_i, dcpu_err_i, dcpu_tag_i, boot_adr_sel_i;\n')
    testbench.write('unsigned int mtspr_dc_done, sig_int, sig_tick;\n')
    testbench.write('\n')

    testbench.write('unsigned int delayed1_ex_dslot, ex_dslot, wb_pc, delayed_iee;\n')
    testbench.write('unsigned int delayed_tee, state, except_type, ex_freeze_prev;\n')
    testbench.write('unsigned int trace_trap, sr_reg_bit_eph_select, mul_stall_count, wait_lsu;\n')
    testbench.write('unsigned int pcreg_select, multicycle_cnt, div_free, div_cntr;\n')
    testbench.write('unsigned int div_quot_r, waiting_on, saved_a, saved_b, sp_return_counter;\n')
    testbench.write('unsigned int r1, r2;\n')
    testbench.write('\n')

    testbench.write('klee_make_symbolic(&icpu_dat_i, sizeof(icpu_dat_i), "icpu_dat_i");\n')
    testbench.write('klee_make_symbolic(&icpu_ack_i, sizeof(icpu_ack_i), "icpu_ack_i");\n')
    testbench.write('klee_make_symbolic(&icpu_rty_i, sizeof(icpu_rty_i), "icpu_rty_i");\n')
#    testbench.write('klee_make_symbolic(&icpu_err_i, sizeof(icpu_err_i), "icpu_err_i");\n')
    testbench.write('klee_make_symbolic(&icpu_adr_i, sizeof(icpu_adr_i), "icpu_adr_i");\n')
    testbench.write('klee_make_symbolic(&icpu_tag_i, sizeof(icpu_tag_i), "icpu_tag_i");\n')
    testbench.write('klee_make_symbolic(&dcpu_dat_i, sizeof(dcpu_dat_i), "dcpu_dat_i");\n')
    testbench.write('klee_make_symbolic(&dcpu_ack_i, sizeof(dcpu_ack_i), "dcpu_ack_i");\n')
    testbench.write('klee_make_symbolic(&dcpu_rty_i, sizeof(dcpu_rty_i), "dcpu_rty_i");\n')
#    testbench.write('klee_make_symbolic(&dcpu_err_i, sizeof(dcpu_err_i), "dcpu_err_i");\n')
    testbench.write('klee_make_symbolic(&dcpu_tag_i, sizeof(dcpu_tag_i), "dcpu_tag_i");\n')
    testbench.write('klee_make_symbolic(&boot_adr_sel_i, sizeof(boot_adr_sel_i), "boot_adr_sel_i");\n')
    testbench.write('klee_make_symbolic(&mtspr_dc_done, sizeof(mtspr_dc_done), "mtspr_dc_done");\n')
    testbench.write('klee_make_symbolic(&sig_int, sizeof(sig_int), "sig_int");\n')
    testbench.write('klee_make_symbolic(&sig_tick, sizeof(sig_tick), "sig_tick");\n')
    testbench.write('klee_make_symbolic(&r1, sizeof(r1), "r1");\n')
    testbench.write('klee_make_symbolic(&r2, sizeof(r2), "r2");\n')

    mk_list = []
    for a in assert_list[::2]:
        for m in fsm:
            if a in m:
                ind = fsm.index(m)
                mk_list.append(ind)

    for i in fsm_no:
        if (i != fsm_no[-1]):
            for s in fsm[int(i)]:
                testbench.write('klee_make_symbolic(&'+s+', sizeof('+s+'), "'+s+'");\n')
    for m in mk_list:
	if (m != mk_list[-1]):
	    for s in fsm[m]:
                testbench.write('klee_make_symbolic(&'+s+', sizeof('+s+'), "'+s+'");\n')
    testbench.write('\n')

    testbench.write('or1k_constraints(icpu_dat_i);\n');

    testbench.write('klee_assume((icpu_ack_i <= 1) & (icpu_rty_i <= 1) & \n')
    testbench.write('(icpu_tag_i <= 7) & \n')
    testbench.write('(dcpu_ack_i <= 1) & (dcpu_rty_i <= 1) & \n')
    testbench.write('(dcpu_tag_i <= 7) & \n')
    testbench.write('(boot_adr_sel_i <= 1) & (mtspr_dc_done <= 1) & \n')
    if fsm_no or mk_list:
        testbench.write('(sig_int <= 1) & (sig_tick <= 1)\n')
    else:
        testbench.write('(sig_int <= 1) & (sig_tick <= 1));\n')
  
    already_end = 0
    for i in fsm_no:
        if (i == fsm_no[-1]):
            testbench.write(range_fsm_end[int(i)])
            already_end = 1
        else:
            testbench.write(range_fsm_middle[int(i)])
    for m in mk_list:
        if (m == mk_list[-1]):
            if (already_end == 0):
                already_end = 1
	    testbench.write(");")
        else:
            testbench.write(range_fsm_middle[int(m)])
    testbench.write('\n')

    testbench.write('top->icpu_dat_i = icpu_dat_i;\n')
    testbench.write('top->icpu_ack_i = icpu_ack_i;\n')
    testbench.write('top->icpu_rty_i = icpu_rty_i;\n')
    testbench.write('top->icpu_err_i = 0;\n')
    testbench.write('top->icpu_adr_i = icpu_adr_i;\n')
    testbench.write('top->icpu_tag_i = icpu_tag_i;\n')
    testbench.write('top->dcpu_dat_i = dcpu_dat_i;\n')
    testbench.write('top->dcpu_ack_i = dcpu_ack_i;\n')
    testbench.write('top->dcpu_rty_i = dcpu_rty_i;\n')
    testbench.write('top->dcpu_err_i = 0;\n')
    testbench.write('top->dcpu_tag_i = dcpu_tag_i;\n')
    testbench.write('top->boot_adr_sel_i = boot_adr_sel_i;\n')
    testbench.write('top->mtspr_dc_done = mtspr_dc_done;\n')
    testbench.write('top->sig_int = sig_int;\n')
    testbench.write('top->sig_tick = sig_tick;\n')

    testbench.write('top->du_stall = 0;\n')
    testbench.write('top->du_addr = 0;\n')
    testbench.write('top->du_dat_du = 0;\n')
    testbench.write('top->du_read = 0;\n')
    testbench.write('top->du_write = 0;\n')
    testbench.write('top->du_dsr = 0;\n')
    testbench.write('top->du_dmr1 = 0;\n')
    testbench.write('top->du_hwbkpt = 0;\n')
    testbench.write('top->du_hwbkpt_ls_r = 0;\n')
    testbench.write('top->du_flush_pipe = 0;\n')
    testbench.write('top->spr_dat_pic = 0;\n')
    testbench.write('top->spr_dat_tt = 0;\n')
    testbench.write('top->spr_dat_pm = 0;\n')
    testbench.write('top->spr_dat_dmmu = 0;\n')
    testbench.write('top->spr_dat_immu = 0;\n')
    testbench.write('top->spr_dat_du = 0;\n')
    testbench.write('\n')

    for i in fsm_no:
        for sfull, s in zip(full_fsm[int(i)], fsm[int(i)]):
            testbench.write(sfull+' = '+s+';\n')
    for m in mk_list:
        for sfull, s in zip(full_fsm[m], fsm[m]):
            testbench.write(sfull+' = '+s+';\n')
    testbench.write('\n')




    testbench.write('   rst = 0;\n')
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

    
    if (last_cycle == 1):
        testbench.write('   clk = !clk;\n')
        testbench.write('   top->clk = clk;\n')
        testbench.write('   top->eval();\n')
        testbench.write('\n')
    
        testbench.write('   clk = !clk;\n')
        testbench.write('   top->clk = clk;\n')
        testbench.write('   top->eval();\n')
        testbench.write('\n')

        if (bug_no == 20):
            #=== b06 ===#
            testbench.write('if (((top->__VlSymsp->TOP__or1200_cpu__or1200_ctrl.ex_insn & 4292870144) >> 21 == 1826) && \n')
            testbench.write('   (top->__VlSymsp->TOP__or1200_cpu.__PVT__operand_a > top->__VlSymsp->TOP__or1200_cpu.__PVT__operand_b) && \n')
            testbench.write('   (((top->__VlSymsp->TOP__or1200_cpu__or1200_sprs.__PVT__to_sr >> 9) & 1) != 1)) \n')
            testbench.write('   klee_assert(0);\n')
            testbench.write('\n')
        elif (bug_no == 21):
            #=== b07 ===#
            testbench.write('if (((top->__VlSymsp->TOP__or1200_cpu__or1200_ctrl.ex_insn & 4292870144) >> 21 == 1829) && \n')
            testbench.write('(top->__VlSymsp->TOP__or1200_cpu.__PVT__operand_a <= top->__VlSymsp->TOP__or1200_cpu.__PVT__operand_b) && \n')
            testbench.write('(((top->__VlSymsp->TOP__or1200_cpu__or1200_sprs.__PVT__to_sr >> 9) & 1) == 0)) \n')
            testbench.write('klee_assert(0); \n')
    else:
        print assert_list
        if ((len(assert_list) == 2) and (assert_list[0] == "r1")):
            testbench.write('   clk = !clk;\n')
            testbench.write('   top->clk = clk;\n')
            testbench.write('   top->eval();\n')
            testbench.write('\n')
            if (int(assert_list[1]) < 0):
                assert_list[1] = ctypes.c_uint32(int(assert_list[1])).value

            testbench.write('   clk = !clk;\n')
            testbench.write('   top->clk = clk;\n')
            testbench.write('   top->eval();\n')
            testbench.write('\n')
            testbench.write('   if ((top->__VlSymsp->TOP__or1200_cpu__or1200_rf.__PVT__rf_addrw == 16) && \n')
            testbench.write('   (top->__VlSymsp->TOP__or1200_cpu__or1200_rf.__PVT__rf_dataw == '+str(assert_list[1])+')) \n')
            testbench.write('   klee_assert(0); \n')
            testbench.write('\n')
        else:
            first = 1
            for s in assert_list[::2]:
                for m in fsm:
                    for v in m:
                        if s == v:
                            ind_0 = assert_list.index(s)
                            ind_1 = m.index(v)
                            ind_2 = fsm.index(m)
                            print full_fsm[ind_2][ind_1], assert_list[ind_0+1]
                            if (int(assert_list[ind_0+1]) < 0):
                                assert_list[ind_0+1] = ctypes.c_uint32(int(assert_list[ind_0+1])).value
                            if first == 1:
                                if (len(assert_list)==2):
                                    testbench.write('if ('+full_fsm[ind_2][ind_1]+' == '+str(assert_list[ind_0+1])+' \n')
                                else:
                                    testbench.write('if (('+full_fsm[ind_2][ind_1]+' == '+str(assert_list[ind_0+1])+') \n')
                                first = 0
                            else:
                                testbench.write(' && ('+full_fsm[ind_2][ind_1]+' == '+str(assert_list[ind_0+1])+') \n')
            if first == 0:
                testbench.write(')\n')
            testbench.write('klee_assert(0);\n')
            testbench.write('\n')

    testbench.write('   delete top;\n')
    testbench.write('   exit(0);\n')
    testbench.write('}\n')

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--fsmno", nargs='*', default=())
parser.add_argument("-l", "--lastcycle", type=int, default=0)
parser.add_argument("-a", "--assertlist", nargs='*', default=())
args = parser.parse_args()
gentb(args.fsmno, args.lastcycle, args.assertlist)

