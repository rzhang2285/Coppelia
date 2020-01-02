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
);
  return;
}

#endif /* __CONSTRAINTS_H_ */
