# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test0_basic_mux(dut):
    """Test 0 for mux"""

    Inp0 = 1
    SEL = 0
    
    # input driving 
    dut.sel.value = SEL
    dut.inp0.value = Inp0
    #dut.inp13.value = Inp13
     
    await Timer(2, units='ns')
        
    # cocotb.log.info('##### CTB: Develop your test here ########')
    
    assert dut.out.value == Inp0, f"Muliplexer has selected wrong input: {dut.sel.value} != 0"

    cocotb.log.info('##### CTB: Test 0 #####')


@cocotb.test()
async def test1_basic_mux(dut):
    """Test 1 for mux"""

    Inp1 = 1
    SEL = 1
    
    # input driving 
    dut.sel.value = SEL
    dut.inp1.value = Inp1
     
    await Timer(2, units='ns')
        
    # cocotb.log.info('##### CTB: Develop your test here ########')
    
    assert dut.out.value == Inp1, f"Muliplexer has selected wrong input: {dut.sel.value} != 1"

    cocotb.log.info('##### CTB: Test 1 #####')


@cocotb.test()
async def test2_basic_mux(dut):
    """Test 2 for mux"""

    Inp2 = 1
    SEL = 2
    
    # input driving 
    dut.sel.value = SEL
    dut.inp2.value = Inp2
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp2, f"Muliplexer has selected wrong input: {dut.sel.value} != 2"

    cocotb.log.info('##### CTB: Test 2 #####')

@cocotb.test()
async def test3_basic_mux(dut):
    """Test 3 for mux"""

    Inp3 = 1
    SEL = 3
    
    # input driving 
    dut.sel.value = SEL
    dut.inp3.value = Inp3
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp3, f"Muliplexer has selected wrong input: {dut.sel.value} != 3"

    cocotb.log.info('##### CTB: Test 3 #####')

@cocotb.test()
async def test4_basic_mux(dut):
    """Test 4 for mux"""

    Inp4 = 1
    SEL = 4
    
    # input driving 
    dut.sel.value = SEL
    dut.inp4.value = Inp4
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp4, f"Muliplexer has selected wrong input: {dut.sel.value} != 4"

    cocotb.log.info('##### CTB: Test 4 #####')

@cocotb.test()
async def test5_basic_mux(dut):
    """Test 5 for mux"""

    Inp5 = 1
    SEL = 5
    
    # input driving 
    dut.sel.value = SEL
    dut.inp5.value = Inp5
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp5, f"Muliplexer has selected wrong input: {dut.sel.value} != 5"

    cocotb.log.info('##### CTB: Test 5 #####')

@cocotb.test()
async def test6_basic_mux(dut):
    """Test 6 for mux"""

    Inp6 = 1
    SEL = 6
    
    # input driving 
    dut.sel.value = SEL
    dut.inp6.value = Inp6
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp6, f"Muliplexer has selected wrong input: {dut.sel.value} != 6"

    cocotb.log.info('##### CTB: Test 6 #####')


@cocotb.test()
async def test7_basic_mux(dut):
    """Test 7 for mux"""

    Inp7 = 1
    SEL = 7
    
    # input driving 
    dut.sel.value = SEL
    dut.inp7.value = Inp7
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp7, f"Muliplexer has selected wrong input: {dut.sel.value} != 7"

    cocotb.log.info('##### CTB: Test 7 #####')

    
@cocotb.test()
async def test8_basic_mux(dut):
    """Test 8 for mux"""

    Inp8 = 1
    SEL = 8
    
    # input driving 
    dut.sel.value = SEL
    dut.inp8.value = Inp8
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp8, f"Muliplexer has selected wrong input: {dut.sel.value} != 8"

    cocotb.log.info('##### CTB: Test 8 #####')

@cocotb.test()
async def test9_basic_mux(dut):
    """Test 8 for mux"""

    Inp9 = 1
    SEL = 9
    
    # input driving 
    dut.sel.value = SEL
    dut.inp9.value = Inp9
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp9, f"Muliplexer has selected wrong input: {dut.sel.value} != 9"

    cocotb.log.info('##### CTB: Test 9 #####')


@cocotb.test()
async def test10_basic_mux(dut):
    """Test 10 for mux"""

    Inp10 = 1
    SEL = 10
    
    # input driving 
    dut.sel.value = SEL
    dut.inp10.value = Inp10
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp10, f"Muliplexer has selected wrong input: {dut.sel.value} != 10"

    cocotb.log.info('##### CTB: Test 10 #####')


@cocotb.test()
async def test11_basic_mux(dut):
    """Test 11 for mux"""

    Inp11 = 1
    SEL = 11
    
    # input driving 
    dut.sel.value = SEL
    dut.inp11.value = Inp11
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp11, f"Muliplexer has selected wrong input: {dut.sel.value} != 11"

    cocotb.log.info('##### CTB: Test 11 #####')


@cocotb.test()
async def test12_basic_mux(dut):
    """Test 12 for mux"""

    Inp12 = 1
    SEL = 12
    
    # input driving 
    dut.sel.value = SEL
    dut.inp12.value = Inp12
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp12, f"Muliplexer output is incorrect: {dut.sel.value} != 12"

    cocotb.log.info('##### CTB: Test 12 #####')


@cocotb.test()
async def test13_basic_mux(dut):
    """Test 13 for mux"""

    Inp13 = 1
    SEL = 13
    
    # input driving 
    dut.sel.value = SEL
    dut.inp13.value = Inp13
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp13, f"Muliplexer output is incorrect: {dut.sel.value} != 13"

    cocotb.log.info('##### CTB: Test 13 #####')


@cocotb.test()
async def test14_basic_mux(dut):
    """Test 14 for mux"""

    Inp14 = 1
    SEL = 14
    
    # input driving 
    dut.sel.value = SEL
    dut.inp14.value = Inp14
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp14, f"Muliplexer output is incorrect: {dut.sel.value} != 14"

    cocotb.log.info('##### CTB: Test 14 #####')


@cocotb.test()
async def test15_basic_mux(dut):
    """Test 15 for mux"""

    Inp15 = 1
    SEL = 15
    
    # input driving 
    dut.sel.value = SEL
    dut.inp15.value = Inp15
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp15, f"Muliplexer output is incorrect: {dut.sel.value} != 15"

    cocotb.log.info('##### CTB: Test 15 #####')


@cocotb.test()
async def test16_basic_mux(dut):
    """Test 16 for mux"""

    Inp16 = 1
    SEL = 16
    
    # input driving 
    dut.sel.value = SEL
    dut.inp16.value = Inp16
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp16, f"Muliplexer output is incorrect: {dut.sel.value} != 16"

    cocotb.log.info('##### CTB: Test 16 #####')


@cocotb.test()
async def test17_basic_mux(dut):
    """Test 17 for mux"""

    Inp17 = 1
    SEL = 17
    
    # input driving 
    dut.sel.value = SEL
    dut.inp17.value = Inp17
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp17, f"Muliplexer output is incorrect: {dut.sel.value} != 17"

    cocotb.log.info('##### CTB: Test 17 #####')

@cocotb.test()
async def test18_basic_mux(dut):
    """Test 18 for mux"""

    Inp18 = 1
    SEL = 18
    
    # input driving 
    dut.sel.value = SEL
    dut.inp18.value = Inp18
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp18, f"Muliplexer output is incorrect: {dut.sel.value} != 18"

    cocotb.log.info('##### CTB: Test 18 #####')


@cocotb.test()
async def test19_basic_mux(dut):
    """Test 19 for mux"""

    Inp19 = 1
    SEL = 19
    
    # input driving 
    dut.sel.value = SEL
    dut.inp19.value = Inp19
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp19, f"Muliplexer output is incorrect: {dut.sel.value} != 19"

    cocotb.log.info('##### CTB: Test 19 #####')


@cocotb.test()
async def test20_basic_mux(dut):
    """Test 20 for mux"""

    Inp20 = 1
    SEL = 20
    
    # input driving 
    dut.sel.value = SEL
    dut.inp20.value = Inp20
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp20, f"Muliplexer output is incorrect: {dut.sel.value} != 20"

    cocotb.log.info('##### CTB: Test 20 #####')

@cocotb.test()
async def test21_basic_mux(dut):
    """Test 21 for mux"""

    Inp21 = 1
    SEL = 21
    
    # input driving 
    dut.sel.value = SEL
    dut.inp21.value = Inp21
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp21, f"Muliplexer output is incorrect: {dut.sel.value} != 21"

    cocotb.log.info('##### CTB: Test 21 #####')


@cocotb.test()
async def test22_basic_mux(dut):
    """Test 22 for mux"""

    Inp22 = 1
    SEL = 22
    
    # input driving 
    dut.sel.value = SEL
    dut.inp22.value = Inp22
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp22, f"Muliplexer output is incorrect: {dut.sel.value} != 22"

    cocotb.log.info('##### CTB: Test 22 #####')



@cocotb.test()
async def test23_basic_mux(dut):
    """Test 23 for mux"""

    Inp23 = 1
    SEL = 23
    
    # input driving 
    dut.sel.value = SEL
    dut.inp23.value = Inp23
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp23, f"Muliplexer output is incorrect: {dut.sel.value} != 23"

    cocotb.log.info('##### CTB: Test 23 #####')


@cocotb.test()
async def test24_basic_mux(dut):
    """Test 24 for mux"""

    Inp24 = 1
    SEL = 24
    
    # input driving 
    dut.sel.value = SEL
    dut.inp24.value = Inp24
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp24, f"Muliplexer output is incorrect: {dut.sel.value} != 24"

    cocotb.log.info('##### CTB: Test 24 #####')


@cocotb.test()
async def test25_basic_mux(dut):
    """Test 25 for mux"""

    Inp25 = 1
    SEL = 25
    
    # input driving 
    dut.sel.value = SEL
    dut.inp25.value = Inp25
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp25, f"Muliplexer output is incorrect: {dut.sel.value} != 25"

    cocotb.log.info('##### CTB: Test 25 #####')


@cocotb.test()
async def test26_basic_mux(dut):
    """Test 26 for mux"""

    Inp26 = 1
    SEL = 26
    
    # input driving 
    dut.sel.value = SEL
    dut.inp26.value = Inp26
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp26, f"Muliplexer output is incorrect: {dut.sel.value} != 26"

    cocotb.log.info('##### CTB: Test 26 #####')

@cocotb.test()
async def test27_basic_mux(dut):
    """Test 27 for mux"""

    Inp27 = 1
    SEL = 27
    
    # input driving 
    dut.sel.value = SEL
    dut.inp27.value = Inp27
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp27, f"Muliplexer output is incorrect: {dut.sel.value} != 27"

    cocotb.log.info('##### CTB: Test 27 #####')


@cocotb.test()
async def test28_basic_mux(dut):
    """Test 28 for mux"""

    Inp28 = 1
    SEL = 28
    
    # input driving 
    dut.sel.value = SEL
    dut.inp28.value = Inp28
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp28, f"Muliplexer output is incorrect: {dut.sel.value} != 28"

    cocotb.log.info('##### CTB: Test 28 #####')



@cocotb.test()
async def test29_basic_mux(dut):
    """Test 29 for mux"""

    Inp29 = 1
    SEL = 29
    
    # input driving 
    dut.sel.value = SEL
    dut.inp29.value = Inp29
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp29, f"Muliplexer output is incorrect: {dut.sel.value} != 29"

    cocotb.log.info('##### CTB: Test 29 #####')



@cocotb.test()
async def test30_basic_mux(dut):
    """Test 30 for mux"""

    Inp30 = 1
    SEL = 30
    
    # input driving 
    dut.sel.value = SEL
    dut.inp30.value = Inp30
     
    await Timer(2, units='ns')
        
    assert dut.out.value == Inp30, f"Muliplexer output is incorrect: {dut.sel.value} != 30"

    cocotb.log.info('##### CTB: Test 30 #####')