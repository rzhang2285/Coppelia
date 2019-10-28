# Coppelia
## Description
This is the repository for the Coppelia tool described in our [MICRO '18](https://cs.unc.edu/~rzhang/files/MICRO2018.pdf) paper.

## Publication
* Rui Zhang, Calvin Deutschbein, Peng Huang, and Cynthia Sturton. 
End-to-End Automated Exploit Generation for Validating the Security of Processor Designs. 
In Proceedings of *the 51st IEEE/ACM International Symposium on Microarchitecture*, MICRO '18.

## Download
```
git clone https://github.com/rzhang2285/Coppelia
cd Coppelia
git submodule update --init --recursive
```

## Installation
### Klee
Please refer to website: [http://klee.github.io/releases/docs/v1.3.0/build-llvm34/](http://klee.github.io/releases/docs/v1.3.0/build-llvm34/) about 
how to build KLEE.

### Verilator
```
git clone http://git.veripool.org/git/verilator
git checkout verilator_3_900
cd verilator
autoconf
./configure
make
sudo make install
```
For additional information, please refer to website: [http://www.veripool.org/projects/verilator/wiki/Installing](http://www.veripool.org/projects/verilator/wiki/Installing).

Update the Makefile with your own `KLEE_ROOT` and `KLEE_INCLUDE`:

```
vim verilator/verilated.mk
KLEE_ROOT = (use your own klee_root)
KLEE_INCLUDE = (use your own klee_include)
```

Update Verilator's Makefile with Klee and WLLVM:

```
mv /usr/local/share/verilator/include/verilated.mk /usr/local/share/verilator/include/verilated.mk.bak
cp verilator/verilated.mk /usr/local/share/verilator/include
```

