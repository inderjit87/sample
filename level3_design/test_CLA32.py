# Cocotb Testbench for 32 bit CLA adder
import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_CLA32_Basic(dut):
    """Test for 32 bit CLA adder which calculates a ='bd999; b='d98999"""

    # input driving 
    A = 429
    B = 429
    dut.a.value = A
    dut.b.value = B

    cocotb.log.info('A|B||cout|sum')

    await Timer(2, units='ns')
    
    assert dut.sum.value == A + B, "Adder result is incorrect: {A} + {B} != {SUM}".format(
    A=int(dut.a.value) , B=int(dut.b.value), SUM=int(dut.sum.value))


@cocotb.test()
async def test_CLA32_randomise(dut):
    """Test for adding two random numbers multiple times"""

    for i in range(5):

        A = random.randint(0, 4294967295)
        B = random.randint(0, 4294967295)
        
        A = 0b1100100011001010
        B = 0b1100100011001010
        dut.a.value = A
        dut.b.value = B

        await Timer(2, units='ns')
        
        dut._log.info(f'A={A:05} B={B:05} model={A+B:05} DUT={int(dut.sum.value):05}')
        assert dut.sum.value == A + B , "Randomised test failed with: {A} + {B} != {SUM}".format(
        A=dut.a.value, B=dut.b.value, SUM=dut.sum.value)
        
    


