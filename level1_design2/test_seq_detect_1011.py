# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug(dut):
    """Test 1 for 1011 sequence detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Sequence detector Testbench! ######')

    # intitalize input

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f'Input bit: {dut.inp_bit.value}')
    dut._log.info(f'Current state: {dut.current_state.value}')
    dut._log.info(f'Next state: {dut.next_state.value}')

    #assert dut.current_state.value == dut.SEQ_1.value, f"Sequence must be detected but is not detected {dut.current_state.value}!= {dut.SEQ_1.value}"

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f'Input bit: {dut.inp_bit.value}')
    dut._log.info(f'Current state: {dut.current_state.value}')
    dut._log.info(f'Next state: {dut.next_state.value}')
    #assert dut.current_state.value == dut.SEQ_10.value, f"Sequence must be detected but is not detected {dut.current_state.value}!= {dut.SEQ_10.value}"

    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info(f'Input bit: {dut.inp_bit.value}')
    dut._log.info(f'Current state: {dut.current_state.value}')
    dut._log.info(f'Next state: {dut.next_state.value}')
    
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f'Input bit: {dut.inp_bit.value}')
    dut._log.info(f'Current state: {dut.current_state.value}')
    dut._log.info(f'Next state: {dut.next_state.value}')


    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f'Input bit: {dut.inp_bit.value}')
    dut._log.info(f'Current state: {dut.current_state.value}')
    dut._log.info(f'Next state: {dut.next_state.value}')


    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f'Input bit: {dut.inp_bit.value}')
    dut._log.info(f'Current state: {dut.current_state.value}')
    dut._log.info(f'Next state: {dut.next_state.value}')

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f'Input bit: {dut.inp_bit.value}')
    dut._log.info(f'Current state: {dut.current_state.value}')
    dut._log.info(f'Next state: {dut.next_state.value}')
    dut._log.info(f'Output sequence 1011 detected: {dut.seq_seen.value}')
    
    assert dut.current_state.value == dut.SEQ_1011.value, f"Sequence must be detected but is not detected {dut.current_state.value}!= {dut.SEQ_1011.value}"

    
