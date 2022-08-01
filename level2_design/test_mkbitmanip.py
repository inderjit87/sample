# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock


from model_mkbitmanip import *

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 

# Test 1
@cocotb.test()
def run_test_1(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Test 1 to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    print(f'SRC1 value in binary: {dut.mav_putvalue_src1.value}')
    print(f'SRC1 value in hex: {hex(dut.mav_putvalue_src1.value)}')
    print(f'SRC2 value in binary: {dut.mav_putvalue_src2.value}')
    print(f'SRC2 value in hex: {hex(dut.mav_putvalue_src2.value)}')
    print(f'SRC3 value in binary: {dut.mav_putvalue_src3.value}')
    print(f'SRC3 value in hex: {hex(dut.mav_putvalue_src3.value)}')
    print(f'Instruction value in binary: {dut.mav_putvalue_instr.value}')
    print(f'Instruction value in hex: {hex(dut.mav_putvalue_instr.value)}')
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message


    
    
# Test 2   
@cocotb.test()
def run_test_2(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1


    ######### CTB : Test 2 to expose the bug #############
    # input transaction

    for i in range(10):

        A = random.randint(0, 4294967295)
        B = random.randint(0, 4294967295)
        C = 0x0
        mav_putvalue_src1 = A
        mav_putvalue_src2 = B
        mav_putvalue_src3 = C
       # mav_putvalue_src1 = 0b00000000000000001010101010100000
       # mav_putvalue_src2 = 0b00000000000000000000000000000011
       # mav_putvalue_src3 = 0x0
     
    mav_putvalue_instr = 0b01000000000000000111000000110011

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    print(f'SRC1 value in binary: {dut.mav_putvalue_src1.value}')
    print(f'SRC1 value in hex: {hex(dut.mav_putvalue_src1.value)}')
    print(f'SRC2 value in binary: {dut.mav_putvalue_src2.value}')
    print(f'SRC2 value in hex: {hex(dut.mav_putvalue_src2.value)}')
    print(f'SRC3 value in binary: {dut.mav_putvalue_src3.value}')
    print(f'SRC3 value in hex: {hex(dut.mav_putvalue_src3.value)}')
    print(f'Instruction value in binary: {dut.mav_putvalue_instr.value}')
    print(f'Instruction value in hex: {hex(dut.mav_putvalue_instr.value)}')
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message


# Test 3   
@cocotb.test()
def run_test_3(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1


    ######### CTB : Test 3 to expose the bug #############
    # input transaction

    mav_putvalue_src1 = 0b00000000000000001010101010100000
    mav_putvalue_src2 = 0b00000000000000000000000000000011
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0b01000000000000000111000000110011

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    print(f'SRC1 value in binary: {dut.mav_putvalue_src1.value}')
    print(f'SRC1 value in hex: {hex(dut.mav_putvalue_src1.value)}')
    print(f'SRC2 value in binary: {dut.mav_putvalue_src2.value}')
    print(f'SRC2 value in hex: {hex(dut.mav_putvalue_src2.value)}')
    print(f'SRC3 value in binary: {dut.mav_putvalue_src3.value}')
    print(f'SRC3 value in hex: {hex(dut.mav_putvalue_src3.value)}')
    print(f'Instruction value in binary: {dut.mav_putvalue_instr.value}')
    print(f'Instruction value in hex: {hex(dut.mav_putvalue_instr.value)}')
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message


# Test 4
@cocotb.test()
def run_test_4(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1


    ######### CTB : Test 4 to expose the bug #############
    # input transaction

    mav_putvalue_src1 = 0x0
    mav_putvalue_src2 = 0x3
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0b01000000000000000111000000110011

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    print(f'SRC1 value in binary: {dut.mav_putvalue_src1.value}')
    print(f'SRC1 value in hex: {hex(dut.mav_putvalue_src1.value)}')
    print(f'SRC2 value in binary: {dut.mav_putvalue_src2.value}')
    print(f'SRC2 value in hex: {hex(dut.mav_putvalue_src2.value)}')
    print(f'SRC3 value in binary: {dut.mav_putvalue_src3.value}')
    print(f'SRC3 value in hex: {hex(dut.mav_putvalue_src3.value)}')
    print(f'Instruction value in binary: {dut.mav_putvalue_instr.value}')
    print(f'Instruction value in hex: {hex(dut.mav_putvalue_instr.value)}')
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

# Test 5
@cocotb.test()
def run_test_5(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1


  ######### CTB : Test 5 to expose the bug #############
    # input transaction

    mav_putvalue_src1 = 0x0
    mav_putvalue_src2 = 0x33
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x40007033

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    print(f'SRC1 value in binary: {dut.mav_putvalue_src1.value}')
    print(f'SRC1 value in hex: {hex(dut.mav_putvalue_src1.value)}')
    print(f'SRC2 value in binary: {dut.mav_putvalue_src2.value}')
    print(f'SRC2 value in hex: {hex(dut.mav_putvalue_src2.value)}')
    print(f'SRC3 value in binary: {dut.mav_putvalue_src3.value}')
    print(f'SRC3 value in hex: {hex(dut.mav_putvalue_src3.value)}')
    print(f'Instruction value in binary: {dut.mav_putvalue_instr.value}')
    print(f'Instruction value in hex: {hex(dut.mav_putvalue_instr.value)}')
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

 
# Test 6
@cocotb.test()
def run_test_6(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1


  ######### CTB : Test 6 to expose the bug #############
    # input transaction

    mav_putvalue_src1 = 0x0
    mav_putvalue_src2 = 0x6033
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x40006033

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    print(f'SRC1 value in binary: {dut.mav_putvalue_src1.value}')
    print(f'SRC1 value in hex: {hex(dut.mav_putvalue_src1.value)}')
    print(f'SRC2 value in binary: {dut.mav_putvalue_src2.value}')
    print(f'SRC2 value in hex: {hex(dut.mav_putvalue_src2.value)}')
    print(f'SRC3 value in binary: {dut.mav_putvalue_src3.value}')
    print(f'SRC3 value in hex: {hex(dut.mav_putvalue_src3.value)}')
    print(f'Instruction value in binary: {dut.mav_putvalue_instr.value}')
    print(f'Instruction value in hex: {hex(dut.mav_putvalue_instr.value)}')
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

# Test 7
@cocotb.test()
def run_test_7(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1


  ######### CTB : Test 7 to expose the bug #############
    # input transaction

    mav_putvalue_src1 = 0x2033
    mav_putvalue_src2 = 0x2000
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x40004033

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    print(f'SRC1 value in binary: {dut.mav_putvalue_src1.value}')
    print(f'SRC1 value in hex: {hex(dut.mav_putvalue_src1.value)}')
    print(f'SRC2 value in binary: {dut.mav_putvalue_src2.value}')
    print(f'SRC2 value in hex: {hex(dut.mav_putvalue_src2.value)}')
    print(f'SRC3 value in binary: {dut.mav_putvalue_src3.value}')
    print(f'SRC3 value in hex: {hex(dut.mav_putvalue_src3.value)}')
    print(f'Instruction value in binary: {dut.mav_putvalue_instr.value}')
    print(f'Instruction value in hex: {hex(dut.mav_putvalue_instr.value)}')
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message


# Test 8
@cocotb.test()
def run_test_8(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1


  ######### CTB : Test 8 to expose the bug #############
    # input transaction

    mav_putvalue_src1 = 0x0533
    mav_putvalue_src2 = 0x0500
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x20001033

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    print(f'SRC1 value in binary: {dut.mav_putvalue_src1.value}')
    print(f'SRC1 value in hex: {hex(dut.mav_putvalue_src1.value)}')
    print(f'SRC2 value in binary: {dut.mav_putvalue_src2.value}')
    print(f'SRC2 value in hex: {hex(dut.mav_putvalue_src2.value)}')
    print(f'SRC3 value in binary: {dut.mav_putvalue_src3.value}')
    print(f'SRC3 value in hex: {hex(dut.mav_putvalue_src3.value)}')
    print(f'Instruction value in binary: {dut.mav_putvalue_instr.value}')
    print(f'Instruction value in hex: {hex(dut.mav_putvalue_instr.value)}')
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message


# Test 9
@cocotb.test()
def run_test_9(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1


  ######### CTB : Test 9 to expose the bug #############
    # input transaction

    mav_putvalue_src1 = 0x0033
    mav_putvalue_src2 = 0x5000
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x20005033

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    print(f'SRC1 value in binary: {dut.mav_putvalue_src1.value}')
    print(f'SRC1 value in hex: {hex(dut.mav_putvalue_src1.value)}')
    print(f'SRC2 value in binary: {dut.mav_putvalue_src2.value}')
    print(f'SRC2 value in hex: {hex(dut.mav_putvalue_src2.value)}')
    print(f'SRC3 value in binary: {dut.mav_putvalue_src3.value}')
    print(f'SRC3 value in hex: {hex(dut.mav_putvalue_src3.value)}')
    print(f'Instruction value in binary: {dut.mav_putvalue_instr.value}')
    print(f'Instruction value in hex: {hex(dut.mav_putvalue_instr.value)}')
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message
