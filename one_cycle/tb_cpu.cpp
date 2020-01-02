#include "obj_dir/Vor1200_cpu.h"
#include "obj_dir/Vor1200_cpu__Syms.h"
#include "verilated.h"
#include <stdlib.h>
#include <klee/klee.h>
#include "../include/constraints.h"

int main(int argc, char **argv) {
  Vor1200_cpu* top = new Vor1200_cpu;
  int clk, rst;

  unsigned int icpu_dat_i, icpu_ack_i, icpu_rty_i, icpu_err_i, icpu_adr_i, icpu_tag_i;
  /* commented out debug unit signals */
//  unsigned int du_stall, du_addr, du_dat_du, du_read, du_write, du_dsr;
//  unsigned int du_dmr1, du_hwbkpt, du_hwbkpt_ls_r, du_flush_pipe;
  unsigned int dcpu_dat_i, dcpu_ack_i, dcpu_rty_i, dcpu_err_i, dcpu_tag_i;
  unsigned int boot_adr_sel_i;
  unsigned int spr_dat_pic, spr_dat_tt, spr_dat_pm, spr_dat_dmmu, spr_dat_immu, spr_dat_du;
  unsigned int mtspr_dc_done, sig_int, sig_tick;

  klee_make_symbolic(&icpu_dat_i, sizeof(icpu_dat_i), "icpu_dat_i");
  klee_make_symbolic(&icpu_ack_i, sizeof(icpu_ack_i), "icpu_ack_i");
  klee_make_symbolic(&icpu_rty_i, sizeof(icpu_rty_i), "icpu_rty_i");
  klee_make_symbolic(&icpu_err_i, sizeof(icpu_err_i), "icpu_err_i");
  klee_make_symbolic(&icpu_adr_i, sizeof(icpu_adr_i), "icpu_adr_i");
  klee_make_symbolic(&icpu_tag_i, sizeof(icpu_tag_i), "icpu_tag_i");

  /* commented out debug unit signals */
//  klee_make_symbolic(&du_stall, sizeof(du_stall), "du_stall");
//  klee_make_symbolic(&du_addr, sizeof(du_addr), "du_addr");
//  klee_make_symbolic(&du_dat_du, sizeof(du_dat_du), "du_dat_du");
//  klee_make_symbolic(&du_read, sizeof(du_read), "du_read");
//  klee_make_symbolic(&du_write, sizeof(du_write), "du_write");
//  klee_make_symbolic(&du_dsr, sizeof(du_dsr), "du_dsr");
  
//  klee_make_symbolic(&du_dmr1, sizeof(du_dmr1), "du_dmr1");
//  klee_make_symbolic(&du_hwbkpt, sizeof(du_hwbkpt), "du_hwbkpt");
//  klee_make_symbolic(&du_hwbkpt_ls_r, sizeof(du_hwbkpt_ls_r), "du_hwbkpt_ls_r");
//  klee_make_symbolic(&du_flush_pipe, sizeof(du_flush_pipe), "du_flush_pipe");

  klee_make_symbolic(&dcpu_dat_i, sizeof(dcpu_dat_i), "dcpu_dat_i");
  klee_make_symbolic(&dcpu_ack_i, sizeof(dcpu_ack_i), "dcpu_ack_i");
  klee_make_symbolic(&dcpu_rty_i, sizeof(dcpu_rty_i), "dcpu_rty_i");
  klee_make_symbolic(&dcpu_err_i, sizeof(dcpu_err_i), "dcpu_err_i");
  klee_make_symbolic(&dcpu_tag_i, sizeof(dcpu_tag_i), "dcpu_tag_i");

  klee_make_symbolic(&boot_adr_sel_i, sizeof(boot_adr_sel_i), "boot_adr_sel_i");

  klee_make_symbolic(&spr_dat_pic, sizeof(spr_dat_pic), "spr_dat_pic");
  klee_make_symbolic(&spr_dat_tt, sizeof(spr_dat_tt), "spr_dat_tt");
  klee_make_symbolic(&spr_dat_pm, sizeof(spr_dat_pm), "spr_dat_pm");
  klee_make_symbolic(&spr_dat_dmmu, sizeof(spr_dat_dmmu), "spr_dat_dmmu");
  klee_make_symbolic(&spr_dat_immu, sizeof(spr_dat_immu), "spr_dat_immu");
  klee_make_symbolic(&spr_dat_du, sizeof(spr_dat_du), "spr_dat_du");
  
  klee_make_symbolic(&mtspr_dc_done, sizeof(mtspr_dc_done), "mtspr_dc_done");
  klee_make_symbolic(&sig_int, sizeof(sig_int), "sig_int");
  klee_make_symbolic(&sig_tick, sizeof(sig_tick), "sig_tick");

  or1k_constraints(icpu_dat_i);

  top->icpu_dat_i = icpu_dat_i;
  top->icpu_ack_i = icpu_ack_i;
  top->icpu_rty_i = icpu_rty_i;
  top->icpu_err_i = icpu_err_i;
  top->icpu_adr_i = icpu_adr_i;
  top->icpu_tag_i = icpu_tag_i;

  /* commented out debug unit signals */
//  top->du_stall = du_stall;
//  top->du_addr = du_addr;
//  top->du_dat_du = du_dat_du;
//  top->du_read = du_read;
//  top->du_write = du_write;
//  top->du_dsr = du_dsr;
//  top->du_dmr1 = du_dmr1;
//  top->du_hwbkpt = du_hwbkpt;
//  top->du_hwbkpt_ls_r = du_hwbkpt_ls_r;
//  top->du_flush_pipe = du_flush_pipe;

  top->du_stall = 0;
  top->du_addr = 0;
  top->du_dat_du = 0;
  top->du_read = 0;
  top->du_write = 0;
  top->du_dsr = 0;
  top->du_dmr1 = 0;
  top->du_hwbkpt = 0;
  top->du_hwbkpt_ls_r = 0;
  top->du_flush_pipe = 0;

  top->dcpu_dat_i = dcpu_dat_i;
  top->dcpu_ack_i = dcpu_ack_i;
  top->dcpu_rty_i = dcpu_rty_i;
  top->dcpu_err_i = dcpu_err_i;
  top->dcpu_tag_i = dcpu_tag_i;

  top->spr_dat_pic = spr_dat_pic;
  top->spr_dat_tt = spr_dat_tt;
  top->spr_dat_pm = spr_dat_pm;
  top->spr_dat_dmmu = spr_dat_dmmu;
  top->spr_dat_immu = spr_dat_immu;
  top->spr_dat_du = spr_dat_du;
  

  top->mtspr_dc_done = mtspr_dc_done;
  top->sig_int = sig_int;
  top->sig_tick = sig_tick;

  rst = 0;
  clk = 1;
  top->rst = rst;

  // Cycle 1
  clk = !clk;
  top->clk = clk;
  top->eval();

  clk = !clk;
  top->clk = clk;
  top->eval();
  
  // Cycle 2
  clk = !clk;
  top->clk = clk;
  top->eval();

  clk = !clk;
  top->clk = clk;
  top->eval();


  if ((top->__VlSymsp->TOP__or1200_cpu__or1200_rf.__PVT__rf_we == 1) && 
      (top->__VlSymsp->TOP__or1200_cpu__or1200_rf.__PVT__rf_addrw == 0) && 
      (top->__VlSymsp->TOP__or1200_cpu__or1200_rf.__PVT__rf_dataw != 0)) 
    klee_assert(0);



  delete top;
  exit(0);
}
