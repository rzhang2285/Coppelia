#!/bin/sh

ulimit -s unlimited

rm -rf obj_dir

verilator -O3 -Wall -language 1364-2001 --top-module or1200_cpu \
  +incdir+../cores/or1200 -Mdir obj_dir -cc ../cores/or1200/*.v --exe tb_cpu.cpp

make -j -C obj_dir/ -f Vor1200_cpu.mk Vor1200_cpu

extract-bc -l llvm-link obj_dir/Vor1200_cpu

klee -emit-all-errors -coi-prune=true -halt-when-fired=true --search=hardware --libc=uclibc --posix-runtime obj_dir/Vor1200_cpu.bc

