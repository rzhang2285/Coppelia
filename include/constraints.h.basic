#ifndef __CONSTRAINTS_H_
#define __CONSTRAINTS_H_

#define opcode_mask  4227858432
#define opcode_offset (32-6)
#define nop_op_mask 50331648
#define nop_op_offset (32-8)
#define movhi_op_mask 65536
#define movhi_op_offset (32-16)
#define sys_op_mask 67043328
#define sys_op_offset (32-16)
#define lv_op_mask 255
#define lv_op_offset 0
#define lvcust_op_mask 240
#define lvcust_op_offset (32-28)
#define shift_op_mask 192
#define shift_op_offset (32-26)
#define sf_op_mask 65011712
#define sf_op_offset (32-11)
#define mac_op_mask 3
#define mac_op_offset 0
#define lf_op_mask 255
#define lf_op_offset 0
#define lfcust_op_mask 240
#define lfcust_op_offset 4
#define arith1_op_mask 768
#define arith1_op_offset 8
#define arith2_op_mask 192
#define arith2_op_offset 6
#define arith3_op_mask 15
#define arith3_op_offset 0
#define usf_op_mask 65011712
#define usf_op_offset (32-11)
void or1k_constraints(int insn) {
  klee_assume(
      // l.j N (00 0x0  NNNNN NNNNN NNNN NNNN NNNN NNNN)
      ((insn & opcode_mask) >> opcode_offset == 0) | 
      // l.jal N (00 0x1  NNNNN NNNNN NNNN NNNN NNNN NNNN)
      ((insn & opcode_mask) >> opcode_offset == 1) | 
      // l.bnf N (00 0x3  NNNNN NNNNN NNNN NNNN NNNN NNNN)
      ((insn & opcode_mask) >> opcode_offset == 3) |
      // l.bf N (00 0x4  NNNNN NNNNN NNNN NNNN NNNN NNNN)
      ((insn & opcode_mask) >> opcode_offset == 4) | 
      // l.nop K (00 0x5  01--- ----- KKKK KKKK KKKK KKKK)
      (((insn & opcode_mask) >> opcode_offset == 5) & 
       ((insn & nop_op_mask) >> nop_op_offset == 1)) | 
      // l.movhi rD, K (00 0x6  DDDDD ----0 KKKK KKKK KKKK KKKK)
      (((insn & opcode_mask) >> opcode_offset == 6) & 
       ((insn & movhi_op_mask) >> movhi_op_offset == 0)) | 
      // l.macrc rD (00 0x6  DDDDD ----1 0000 0000 0000 0000)
      (((insn & opcode_mask) >> opcode_offset == 6) & 
       ((insn & movhi_op_mask) >> movhi_op_offset == 1)) | 
      // l.sys K (00 0x8  00000 00000 KKKK KKKK KKKK KKKK)
      (((insn & opcode_mask) >> opcode_offset == 8) & 
       ((insn & sys_op_mask) >> sys_op_offset == 0)) |
      // l.trap K (00 0x8  01000 00000 KKKK KKKK KKKK KKKK)
      (((insn & opcode_mask) >> opcode_offset == 8) & 
       ((insn & sys_op_mask) >> sys_op_offset == 256)) | 
      // l.msync (00 0x8  10000 00000 0000 0000 0000 0000)
      (((insn & opcode_mask) >> opcode_offset == 8) & 
       ((insn & sys_op_mask) >> sys_op_offset == 512)) | 
      // l.psync (00 0x8  10100 00000 0000 0000 0000 0000)
      (((insn & opcode_mask) >> opcode_offset == 8) & 
       ((insn & sys_op_mask) >> sys_op_offset == 640)) |
      // l.csync (00 0x8  11000 00000 0000 0000 0000 0000)
      (((insn & opcode_mask) >> opcode_offset == 8) & 
       ((insn & sys_op_mask) >> sys_op_offset == 768)) | 
      // l.rfe (00 0x9  ----- ----- ---- ---- ---- ----)
      ((insn & opcode_mask) >> opcode_offset == 9) | 
/*      
      // lv.all_eq.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x1 0x0)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 16)) | 
      // lv.all_eq.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x1 0x1)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 17)) | 
      // lv.all_ge.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x1 0x2)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 18)) | 
      // lv.all_ge.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x1 0x3)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 19)) | 
      // lv.all_gt.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x1 0x4)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 20)) | 
      // lv.all_gt.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x1 0x5)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 21)) | 
      // lv.all_le.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x1 0x6)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 22)) | 
      // lv.all_le.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x1 0x7)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 23)) | 
      // lv.all_lt.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x1 0x8)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 24)) | 
      // lv.all_lt.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x1 0x9)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 25)) | 
      // lv.all_ne.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x1 0xA)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 26)) | 
      // lv.all_ne.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x1 0xB)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 27)) | 
      // lv.any_eq.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x2 0x0)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 32)) | 
      // lv.any_eq.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x2 0x1)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 33)) | 
      // lv.any_ge.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x2 0x2)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 34)) | 
      // lv.any_ge.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x2 0x3)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 35)) | 
      // lv.any_gt.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x2 0x4) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 36)) | 
      // lv.any_gt.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x2 0x5) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 37)) | 
      // lv.any_le.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x2 0x6)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 38)) | 
      // lv.any_le.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x2 0x7)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 39)) | 
      // lv.any_lt.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x2 0x8)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 40)) | 
      // lv.any_lt.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x2 0x9) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 41)) | 
      // lv.any_ne.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x2 0xA)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 42)) | 
      // lv.any_ne.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x2 0xB) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 43)) | 
      // lv.add.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x3 0x0) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 48)) | 
      // lv.add.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x3 0x1)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 49)) | 
      // lv.adds.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x3 0x2)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 50)) | 
      // lv.adds.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x3 0x3)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 51)) | 
      // lv.addu.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x3 0x4)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 52)) | 
      // lv.addu.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x3 0x5) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 53)) | 
      // lv.addus.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x3 0x6)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 54)) | 
      // lv.addus.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x3 0x7) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 55)) | 
      // lv.and rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x3 0x8) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 56)) | 
      // lv.avg.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x3 0x9)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 57)) | 
      // lv.avg.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x3 0xA)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 58)) | 
      // lv.cmp_eq.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x4 0x0)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 64)) | 
      // lv.cmp_eq.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x4 0x1)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 65)) | 
      // lv.cmp_ge.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x4 0x2)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 66)) | 
      // lv.cmp_ge.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x4 0x3)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 67)) | 
      // lv.cmp_gt.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x4 0x4)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 68)) | 
      // lv.cmp_gt.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x4 0x5)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 69)) | 
      // lv.cmp_le.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x4 0x6) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 70)) | 
      // lv.cmp_le.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x4 0x7)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 71)) | 
      // lv.cmp_lt.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x4 0x8) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 72)) | 
      // lv.cmp_lt.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x4 0x9)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 73)) | 
      // lv.cmp_ne.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x4 0xA) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 74)) | 
      // lv.cmp_ne.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x4 0xB) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 75)) | 
      // lv.madds.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x5 0x4)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 84)) | 
      // lv.max.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x5 0x5)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 85)) | 
      // lv.max.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x5 0x6)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 86)) | 
      // lv.merge.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x5 0x7) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 87)) | 
      // lv.merge.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x5 0x8)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 88)) | 
      // lv.min.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x5 0x9) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 89)) | 
      // lv.min.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x5 0xA) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 90)) | 
      // lv.msubs.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x5 0xB) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 91)) | 
      // lv.muls.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x5 0xC)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 92)) | 
      // lv.nand rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x5 0xC)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 93)) | 
      // lv.nor rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x5 0xE) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 94)) | 
      // lv.or rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x5 0xF)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 95)) | 
      // lv.pack.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x6 0x0)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 96)) | 
      // lv.pack.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x6 0x1)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 97)) | 
      // lv.packs.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x6 0x2)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 98)) | 
      // lv.packs.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x6 0x3)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 99)) | 
      // lv.packus.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x6 0x4)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 100)) | 
      // lv.packus.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x6 0x5)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 101)) | 
      // lv.perm.n rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x6 0x6)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 102)) | 
      // lv.rl.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x6 0x7) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 103)) | 
      // lv.rl.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x6 0x8) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 104)) | 
      // lv.sll.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x6 0x9) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 105)) | 
      // lv.sll.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x6 0xA) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 106)) | 
      // lv.sll rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x6 0xB) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 107)) | 
      // lv.srl.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x6 0xC)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 108)) | 
      // lv.srl.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x6 0xD)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 109)) | 
      // lv.sra.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x6 0xE)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 110)) | 
      // lv.sra.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x6 0xF)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 111)) | 
      // lv.srl rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x7 0x0)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 112)) | 
      // lv.sub.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x7 0x1)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 113)) | 
      // lv.sub.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x7 0x2)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 114)) | 
      // lv.subs.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x7 0x3)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 115)) | 
      // lv.subs.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x7 0x4)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 116)) | 
      // lv.subu.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x7 0x5)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 117)) | 
      // lv.subu.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x7 0x6)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 118)) | 
      // lv.subus.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x7 0x7)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 119)) | 
      // lv.subus.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x7 0x8)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 120)) | 
      // lv.unpack.b rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x7 0x9)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 121)) | 
      // lv.unpack.h rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x7 0xA)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 122)) | 
      // lv.xor rD, rA, rB (00 0xA  DDDDD AAAAA BBBB B--- 0x7 0xB) 
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lv_op_mask) >> lv_op_offset == 123)) | 
      // lv.cust1 (00 0xA  ----- ----- ---- ---- 0xC ----)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lvcust_op_mask) >> lvcust_op_offset == 12)) | 
      // lv.cust2 (00 0xA  ----- ----- ---- ---- 0xD ----)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lvcust_op_mask) >> lvcust_op_offset == 13)) | 
      // lv.cust3 (00 0xA  ----- ----- ---- ---- 0xE ----)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lvcust_op_mask) >> lvcust_op_offset == 14)) | 
      // lv.cust4 (00 0xA  ----- ----- ---- ---- 0xF ----)
      (((insn & opcode_mask) >> opcode_offset == 10) & 
       ((insn & lvcust_op_mask) >> lvcust_op_offset == 15)) |
*/      
      // l.jr rB (01 0x1  ----- ----- BBBB B--- ---- ----)
      ((insn & opcode_mask) >> opcode_offset == 17) | 
      // l.jalr rB (01 0x2  ----- ----- BBBB B--- ---- ----) 
      ((insn & opcode_mask) >> opcode_offset == 18) | 
      // l.maci rA, I (01 0x3  ----- AAAAA IIII IIII IIII IIII) 
      ((insn & opcode_mask) >> opcode_offset == 19) | 
      // l.lwa rD, I(rA) (01 0xB  DDDDD AAAAA IIII IIII IIII IIII)
      ((insn & opcode_mask) >> opcode_offset == 27) | 
/*
      // l.cust1 (01 0xC  ----- ----- ---- ---- ---- ----)
      ((insn & opcode_mask) >> opcode_offset == 28) | 
      // l.cust2 (01 0xD  ----- ----- ---- ---- ---- ----)
      ((insn & opcode_mask) >> opcode_offset == 29) | 
      // l.cust3 (01 0xE  ----- ----- ---- ---- ---- ----)
      ((insn & opcode_mask) >> opcode_offset == 30) | 
      // l.cust4 (01 0xF  ----- ----- ---- ---- ---- ----)
      ((insn & opcode_mask) >> opcode_offset == 31) |
*/
      // l.ld rD, I(rA) (10 0x0  DDDDD AAAAA IIII IIII IIII IIII)
      ((insn & opcode_mask) >> opcode_offset == 32) | 
      // l.lwz rD, I(rA) (10 0x1  DDDDD AAAAA IIII IIII IIII IIII)
      ((insn & opcode_mask) >> opcode_offset == 33) | 
      // l.lws rD, I(rA) (10 0x2  DDDDD AAAAA IIII IIII IIII IIII)
      ((insn & opcode_mask) >> opcode_offset == 34) | 
      // l.lbz rD, I(rA) (10 0x3  DDDDD AAAAA IIII IIII IIII IIII)
      ((insn & opcode_mask) >> opcode_offset == 35) | 
      // l.lbs rD, I(rA) (10 0x4  DDDDD AAAAA IIII IIII IIII IIII)
      ((insn & opcode_mask) >> opcode_offset == 36) | 
      // l.lhz rD, I(rA) (10 0x5  DDDDD AAAAA IIII IIII IIII IIII)
      ((insn & opcode_mask) >> opcode_offset == 37) | 
      // l.lhs rD, I(rA) (10 0x6  DDDDD AAAAA IIII IIII IIII IIII) 
      ((insn & opcode_mask) >> opcode_offset == 38) | 
      // l.addi rD, rA, I (10 0x7  DDDDD AAAAA IIII IIII IIII IIII)
      ((insn & opcode_mask) >> opcode_offset == 39) | 
      // l.addic rD, rA, I (10 0x8  DDDDD AAAAA IIII IIII IIII IIII) 
      ((insn & opcode_mask) >> opcode_offset == 40) |  
      // l.andi rD, rA, K (10 0x9  DDDDD AAAAA KKKK KKKK KKKK KKKK)
      ((insn & opcode_mask) >> opcode_offset == 41) | 
      // l.ori rD, rA, K (10 0xA  DDDDD AAAAA KKKK KKKK KKKK KKKK) 
      ((insn & opcode_mask) >> opcode_offset == 42) | 
      // l.xori rD, rA, I (10 0xB  DDDDD AAAAA IIII IIII IIII IIII) 
      ((insn & opcode_mask) >> opcode_offset == 43) | 
      // l.muli rD, rA, I (10 0xC  DDDDD AAAAA IIII IIII IIII IIII) 
      ((insn & opcode_mask) >> opcode_offset == 44) | 
      // l.mfspr rD, rA, K (10 0xD  DDDDD AAAAA KKKK KKKK KKKK KKKK) 
      ((insn & opcode_mask) >> opcode_offset == 45) | 
      // l.slli rD, rA, L (10 0xE  DDDDD AAAAA ---- ---- 00LL LLLL) 
      (((insn & opcode_mask) >> opcode_offset == 46) & 
       ((insn & shift_op_mask) >> shift_op_offset == 0)) |
      // l.srli rD, rA, L (10 0xE  DDDDD AAAAA ---- ---- 01LL LLLL) 
      (((insn & opcode_mask) >> opcode_offset == 46) & 
       ((insn & shift_op_mask) >> shift_op_offset == 1)) | 
      // l.srai rD, rA, L (10 0xE  DDDDD AAAAA ---- ---- 10LL LLLL) 
      (((insn & opcode_mask) >> opcode_offset == 46) & 
       ((insn & shift_op_mask) >> shift_op_offset == 2)) | 
      // l.rori rD, rA, L (10 0xE  DDDDD AAAAA ---- ---- 11LL LLLL) 
      (((insn & opcode_mask) >> opcode_offset == 46) & 
       ((insn & shift_op_mask) >> shift_op_offset == 3)) | 
      // l.sfeqi rA, I (10 0xF  00000 AAAAA IIII IIII IIII IIII) 
      (((insn & opcode_mask) >> opcode_offset == 47) & 
       ((insn & sf_op_mask) >> sf_op_offset == 0)) |
      // l.sfnei rA, I (10 0xF  00001 AAAAA IIII IIII IIII IIII) 
      (((insn & opcode_mask) >> opcode_offset == 47) & 
       ((insn & sf_op_mask) >> sf_op_offset == 1)) | 
      // l.sfgtui rA, I (10 0xF  00010 AAAAA IIII IIII IIII IIII)
      (((insn & opcode_mask) >> opcode_offset == 47) & 
       ((insn & sf_op_mask) >> sf_op_offset == 2)) | 
      // l.sfgeui rA, I (10 0xF  00011 AAAAA IIII IIII IIII IIII) 
      (((insn & opcode_mask) >> opcode_offset == 47) & 
       ((insn & sf_op_mask) >> sf_op_offset == 3)) | 
      // l.sfltui rA, I (10 0xF  00100 AAAAA IIII IIII IIII IIII) 
      (((insn & opcode_mask) >> opcode_offset == 47) & 
       ((insn & sf_op_mask) >> sf_op_offset == 4)) | 
      // l.sfleui rA, I (10 0xF  00101 AAAAA IIII IIII IIII IIII) 
      (((insn & opcode_mask) >> opcode_offset == 47) & 
       ((insn & sf_op_mask) >> sf_op_offset == 5)) | 
      // l.sfgtsi rA, I (10 0xF  01010 AAAAA IIII IIII IIII IIII) 
      (((insn & opcode_mask) >> opcode_offset == 47) & 
       ((insn & sf_op_mask) >> sf_op_offset == 10)) | 
      // l.sfgesi rA, I (10 0xF  01011 AAAAA IIII IIII IIII IIII) 
      (((insn & opcode_mask) >> opcode_offset == 47) & 
       ((insn & sf_op_mask) >> sf_op_offset == 11)) | 
      // l.sfltsi rA, I (10 0xF  01100 AAAAA IIII IIII IIII IIII)
      (((insn & opcode_mask) >> opcode_offset == 47) & 
       ((insn & sf_op_mask) >> sf_op_offset == 12)) | 
      // l.sflesi rA, I (10 0xF  01101 AAAAA IIII IIII IIII IIII) 
      (((insn & opcode_mask) >> opcode_offset == 47) & 
       ((insn & sf_op_mask) >> sf_op_offset == 13)) | 
      // l.mtspr rA, rB, K (11 0x0  KKKKK AAAAA BBBB BKKK KKKK KKKK) 
      ((insn & opcode_mask) >> opcode_offset == 48) | 
      // l.mac rA, rB (11 0x1  ----- AAAAA BBBB B--- ---- 0x1)
      (((insn & opcode_mask) >> opcode_offset == 49) & 
       ((insn & mac_op_mask) >> mac_op_offset == 1)) | 
      // l.msb rA, rB (11 0x1  ----- AAAAA BBBB B--- ---- 0x2) 
      (((insn & opcode_mask) >> opcode_offset == 49) & 
       ((insn & mac_op_mask) >> mac_op_offset == 2)) | 
/*
      // lf.add.s rD, rA, rB (11 0x2  DDDDD AAAAA BBBB B--- 0x0 0x0)
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 0)) |
      // lf.sub.s rD, rA, rB (11 0x2  DDDDD AAAAA BBBB B--- 0x0 0x1) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 1)) | 
      // lf.mul.s rD, rA, rB (11 0x2  DDDDD AAAAA BBBB B--- 0x0 0x2) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 2)) | 
      // lf.div.s rD, rA, rB (11 0x2  DDDDD AAAAA BBBB B--- 0x0 0x3) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 3)) | 
      // lf.itof.s rD, rA (11 0x2  DDDDD AAAAA 0000 0--- 0x0 0x4) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 4)) | 
      // lf.ftoi.s rD, rA (11 0x2  DDDDD AAAAA 0000 0--- 0x0 0x5) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 5)) |
      // lf.rem.s rD, rA, rB (11 0x2  DDDDD AAAAA BBBB B--- 0x0 0x6) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 6)) |
      // lf.madd.s rD, rA, rB (11 0x2  DDDDD AAAAA BBBB B--- 0x0 0x7) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 7)) | 
      // lf.sfeq.s rA, rB (11 0x2  ----- AAAAA BBBB B--- 0x0 0x8) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 8)) | 
      // lf.sfne.s rA, rB (11 0x2  ----- AAAAA BBBB B--- 0x0 0x9) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 9)) | 
      // lf.sfgt.s rA, rB (11 0x2  ----- AAAAA BBBB B--- 0x0 0xA) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 10)) | 
      // lf.sfge.s rA, rB (11 0x2  ----- AAAAA BBBB B--- 0x0 0xB) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 11)) | 
      // lf.sflt.s rA, rB (11 0x2  ----- AAAAA BBBB B--- 0x0 0xC) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 12)) | 
      // lf.sfle.s rA, rB (11 0x2  ----- AAAAA BBBB B--- 0x0 0xD) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 13)) | 
      // lf.cust1.s rA, rB (11 0x2  ----- AAAAA BBBB B--- 0xD ----)
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lfcust_op_mask) >> lfcust_op_offset == 13)) | 
      // lf.add.d rD, rA, rB (11 0x2  DDDDD AAAAA BBBB B--- 0x1 0x0) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 16)) | 
      // lf.sub.d rD, rA, rB (11 0x2  DDDDD AAAAA BBBB B--- 0x1 0x1) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 17)) | 
      // lf.mul.d rD, rA, rB (11 0x2  DDDDD AAAAA BBBB B--- 0x1 0x2) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 18)) | 
      // lf.div.d rD, rA, rB (11 0x2  DDDDD AAAAA BBBB B--- 0x1 0x3) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 19)) | 
      // lf.itof.d rD, rA (11 0x2  DDDDD AAAAA 0000 0--- 0x1 0x4) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 20)) | 
      // lf.ftoi.d rD, rA (11 0x2  DDDDD AAAAA 0000 0--- 0x1 0x5) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 21)) | 
      // lf.rem.d rD, rA, rB (11 0x2  DDDDD AAAAA BBBB B--- 0x1 0x6) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 22)) | 
      // lf.madd.d rD, rA, rB (11 0x2  DDDDD AAAAA BBBB B--- 0x1 0x7) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 23)) | 
      // lf.sfeq.d rA, rB (11 0x2  ----- AAAAA BBBB B--- 0x1 0x8) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 24)) | 
      // lf.sfne.d rA, rB (11 0x2  ----- AAAAA BBBB B--- 0x1 0x9)
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 25)) | 
      // lf.sfgt.d rA, rB (11 0x2  ----- AAAAA BBBB B--- 0x1 0xA) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 26)) | 
      // lf.sfge.d rA, rB (11 0x2  ----- AAAAA BBBB B--- 0x1 0xB) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 27)) | 
      // lf.sflt.d rA, rB (11 0x2  ----- AAAAA BBBB B--- 0x1 0xC) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 28)) | 
      // lf.sfle.d rA, rB (11 0x2  ----- AAAAA BBBB B--- 0x1 0xD) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lf_op_mask) >> lf_op_offset == 29)) | 
      // lf.cust1.d rA, rB (11 0x2  ----- AAAAA BBBB B--- 0xE ----) 
      (((insn & opcode_mask) >> opcode_offset == 50) & 
       ((insn & lfcust_op_mask) >> lfcust_op_offset == 14)) |
*/
      // l.swa I(rA), rB (11 0x3  IIIII AAAAA BBBB BIII IIII IIII) 
      ((insn & opcode_mask) >> opcode_offset == 51) | 
      // l.sd I(rA), rB (11 0x4  IIIII AAAAA BBBB BIII IIII IIII) 
      ((insn & opcode_mask) >> opcode_offset == 52) | 
      // l.sw I(rA), rB (11 0x5  IIIII AAAAA BBBB BIII IIII IIII) 
      ((insn & opcode_mask) >> opcode_offset == 53) | 
      // l.sb I(rA), rB (11 0x6  IIIII AAAAA BBBB BIII IIII IIII) 
      ((insn & opcode_mask) >> opcode_offset == 54) | 
      // l.sh I(rA), rB (11 0x7  IIIII AAAAA BBBB BIII IIII IIII) 
      ((insn & opcode_mask) >> opcode_offset == 55) | 
      // l.add rD, rA, rB (11 0x8  DDDDD AAAAA BBBB B-00 ---- 0x0) 
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 0) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 0)) | 
      // l.addc rD, rA, rB (11 0x8  DDDDD AAAAA BBBB B-00 ---- 0x1) 
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 0) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 1)) | 
      // l.sub rD, rA, rB (11 0x8  DDDDD AAAAA BBBB B-00 ---- 0x2) 
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 0) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 2)) | 
      // l.and rD, rA, rB (11 0x8  DDDDD AAAAA BBBB B-00 ---- 0x3) 
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 0) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 3)) | 
      // l.or rD, rA, rB (11 0x8  DDDDD AAAAA BBBB B-00 ---- 0x4) 
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 0) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 4)) | 
      // l.xor rD, rA, rB (11 0x8  DDDDD AAAAA BBBB B-00 ---- 0x5)
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 0) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 5)) | 
      // l.mul rD, rA, rB (11 0x8  DDDDD AAAAA BBBB B-11 ---- 0x6) 
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 3) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 6)) | 
      // l.sll rD, rA, rB (11 0x8  DDDDD AAAAA BBBB B-00 00-- 0x8) 
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 0) & 
       ((insn & arith2_op_mask) >> arith2_op_offset == 0) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 8)) | 
      // l.srl rD, rA, rB (11 0x8  DDDDD AAAAA BBBB B-00 01-- 0x8) 
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 0) & 
       ((insn & arith2_op_mask) >> arith2_op_offset == 1) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 8)) | 
      // l.sra rD, rA, rB (11 0x8  DDDDD AAAAA BBBB B-00 10-- 0x8) 
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 0) & 
       ((insn & arith2_op_mask) >> arith2_op_offset == 2) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 8)) | 
      // l.ror rD, rA, rB (11 0x8  DDDDD AAAAA BBBB B-00 11-- 0x8) 
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 0) & 
       ((insn & arith2_op_mask) >> arith2_op_offset == 3) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 8)) | 
      // l.div rD, rA, rB (11 0x8  DDDDD AAAAA BBBB B-11 ---- 0x9) 
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 3) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 9)) | 
      // l.divu rD, rA, rB (11 0x8  DDDDD AAAAA BBBB B-11 ---- 0xA) 
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 3) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 10)) | 
      // l.mulu rD, rA, rB (11 0x8  DDDDD AAAAA BBBB B-11 ---- 0xB) 
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 3) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 11)) | 
      // l.extbs rD, rA (11 0x8  DDDDD AAAAA ---- --00 01-- 0xC) 
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 0) & 
       ((insn & arith2_op_mask) >> arith2_op_offset == 1) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 12)) | 
      // l.exths rD, rA (11 0x8  DDDDD AAAAA ---- --00 00-- 0xC) 
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 0) & 
       ((insn & arith2_op_mask) >> arith2_op_offset == 0) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 12)) | 
      // l.extws rD, rA (11 0x8  DDDDD AAAAA ---- --00 00-- 0xD) 
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 0) & 
       ((insn & arith2_op_mask) >> arith2_op_offset == 0) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 13)) | 
      // l.extbz rD, rA (11 0x8  DDDDD AAAAA ---- --00 11-- 0xC) 
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 0) & 
       ((insn & arith2_op_mask) >> arith2_op_offset == 3) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 12)) | 
      // l.extbz rD, rA (11 0x8  DDDDD AAAAA ---- --00 10-- 0xC) 
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 0) & 
       ((insn & arith2_op_mask) >> arith2_op_offset == 2) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 12)) | 
      // l.extwz rD, rA (11 0x8  DDDDD AAAAA ---- --00 01-- 0xD) 
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 0) & 
       ((insn & arith2_op_mask) >> arith2_op_offset == 1) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 13)) | 
      // l.cmov rD, rA, rB (11 0x8  DDDDD AAAAA BBBB B-00 ---- 0xE) 
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 0) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 14)) | 
      // l.ff1 rD, rA (11 0x8  DDDDD AAAAA ---- --00 ---- 0xF) 
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 0) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 15)) | 
      // l.fl1 rD, rA (11 0x8  DDDDD AAAAA ---- --01 ---- 0xF) 
      (((insn & opcode_mask) >> opcode_offset == 56) & 
       ((insn & arith1_op_mask) >> arith1_op_offset == 1) & 
       ((insn & arith3_op_mask) >> arith3_op_offset == 15)) | 
      // l.sfeq rA, rB (11 0x9  00000 AAAAA BBBB B--- ---- ----) 
      (((insn & opcode_mask) >> opcode_offset == 57) & 
       ((insn & usf_op_mask) >> usf_op_offset == 0)) | 
      // l.sfne rA, rB (11 0x9  00001 AAAAA BBBB B--- ---- ----) 
      (((insn & opcode_mask) >> opcode_offset == 57) & 
       ((insn & usf_op_mask) >> usf_op_offset == 1)) | 
      // l.sfgtu rA, rB (11 0x9  00010 AAAAA BBBB B--- ---- ----) 
      (((insn & opcode_mask) >> opcode_offset == 57) & 
       ((insn & usf_op_mask) >> usf_op_offset == 2)) | 
      // l.sfgeu rA, rB (11 0x9  00011 AAAAA BBBB B--- ---- ----) 
      (((insn & opcode_mask) >> opcode_offset == 57) & 
       ((insn & usf_op_mask) >> usf_op_offset == 3)) | 
      // l.sfltu rA, rB (11 0x9  00100 AAAAA BBBB B--- ---- ----)
      (((insn & opcode_mask) >> opcode_offset == 57) & 
       ((insn & usf_op_mask) >> usf_op_offset == 4)) | 
      // l.sfleu rA, rB (11 0x9  00101 AAAAA BBBB B--- ---- ----)
      (((insn & opcode_mask) >> opcode_offset == 57) & 
       ((insn & usf_op_mask) >> usf_op_offset == 5)) | 
      // l.sfgts rA, rB (11 0x9  01010 AAAAA BBBB B--- ---- ----)
      (((insn & opcode_mask) >> opcode_offset == 57) & 
       ((insn & usf_op_mask) >> usf_op_offset == 10)) | 
      // l.sfges rA, rB (11 0x9  01011 AAAAA BBBB B--- ---- ----)
      (((insn & opcode_mask) >> opcode_offset == 57) & 
       ((insn & usf_op_mask) >> usf_op_offset == 11)) |
      // l.sflts rA, rB (11 0x9  01100 AAAAA BBBB B--- ---- ----) 
      (((insn & opcode_mask) >> opcode_offset == 57) & 
       ((insn & usf_op_mask) >> usf_op_offset == 12)) | 
      // l.sfles rA, rB (11 0x9  01101 AAAAA BBBB B--- ---- ----) 
      (((insn & opcode_mask) >> opcode_offset == 57) & 
       ((insn & usf_op_mask) >> usf_op_offset == 13)) 
/*
      // l.cust5 (11 0xC  DDDDD AAAAA BBBB BLLL LLLK KKKK)
      ((insn & opcode_mask) >> opcode_offset == 60) | 
      // l.cust6 (11 0xD  ----- ----- ---- ---- ---- ----) 
      ((insn & opcode_mask) >> opcode_offset == 61) | 
      // l.cust7 (11 0xE  ----- ----- ---- ---- ---- ----) 
      ((insn & opcode_mask) >> opcode_offset == 62) | 
      // l.cust8 (11 0xF  ----- ----- ---- ---- ---- ----) 
      ((insn & opcode_mask) >> opcode_offset == 63)
*/
);
  return;
}

#endif /* __CONSTRAINTS_H_ */
