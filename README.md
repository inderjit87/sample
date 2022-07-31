# challenges-inderjit303
challenges-inderjit303 created by GitHub Classroom

# Level 1 Design 1 (Mux Design Verification)

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Gitpod id is included in the screenshot shown below*

![l1d1_image1](https://user-images.githubusercontent.com/99788755/182015934-d71a6af6-e681-4be8-ba86-7d8c379be922.png)


## Verification Environment (Level 1 Design 1)

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux module here) which takes in 5-bit select input *sel*, 1-bit inputs *inp0* to *inp30* and it gives 1-bit output *out*.

A cocotb Testbench is created for each individual inputs *inpo* to *inp30*. 
In each cocotb test, the inputs are first assigned values and then are driven as follows:

```
 Inp0 = 1
 SEL = 0
```

```
 # input driving 
 dut.sel.value = SEL
 dut.inp0.value = Inp0
```

31 such cocotb tests are created for testing all states of input and monitoring output.

![l1d1_image2](https://user-images.githubusercontent.com/99788755/182016224-2026ce7f-2b9e-481f-89b3-f7a1867a0fb3.png)

The assert statement is used for comparing the multiplexer's output to the expected value and the cocotb log command display's the user typed message as shown below: 

![l1d1_image3](https://user-images.githubusercontent.com/99788755/182016740-c253fc77-eacc-4a3e-9b22-b8d92ad93266.png)


The following error's are observed:

**Error 1**
```
test12_basic_mux failed
Traceback (most recent call last):
File "/workspace/challenges-inderjit303/level1_design1/test_mux.py", line 236, in test12_basic_mux
assert dut.out.value == Inp12, f"Muliplexer output is incorrect: {dut.sel.value} != 12"
AssertionError: Muliplexer output is incorrect: 01100 != 12
```

**Error 2**
```
test30_basic_mux failed
Traceback (most recent call last):
File "/workspace/challenges-inderjit303/level1_design1/test_mux.py", line 560, in test30_basic_mux
assert dut.out.value == Inp30, f"Muliplexer output is incorrect: {dut.sel.value} != 30"
AssertionError: Muliplexer output is incorrect: 11110 != 30
```

## Test Scenario **(Level 1 Design 1)**
Cocotb tests are created for testing all states of input and monitoring outputs purposes. This makes sure that all the inputs are compared with expected output and DUT output. 

The following cases reveals incorrect outputs for 2 such inputs cases: 

Case 1: 
- Test inputs: Inp12 = 1 and SEL = 12
- Expected Output: out = 12
- Observed Output in the DUT dut.out.value != Inp12 != 12

Case 2: 
- Test inputs: Inp12 = 1 and SEL = 30
- Expected Output: out = 30
- Observed Output in the DUT dut.out.value != Inp30 != 30

Output mismatches for the above inputs proving that there is a **design bug in Level 1 Design 1**

![l1d1_image4](https://user-images.githubusercontent.com/99788755/182018143-9dd1cbe3-3dd1-4b98-9517-734b1242c366.png)


## Design Bug (Level 1 Design 1)
Based on the above test input and analysing the design, two bugs in the code were detected as discussed below: 

```
5'b01101: out = inp12;     ====> BUG 1
5'b01101: out = inp13;
5'b01110: out = inp14;            
```

For the mux design, the logic should be '5'b01100: out = inp12' instead of '5'b01101: out = inp12' as in the design code.

```
5'b11100: out = inp28;
5'b11101: out = inp29;
default: out = 0;          ====> BUG 2
```

For the mux design, the logic should be '5'b11110: out = inp30' instead of 'default: out = 0' as in the design code.


## Design Fix (Level 1 Design 1)
Updating the verilog design code and re-running the test makes the test pass.

![l1d1_image6](https://user-images.githubusercontent.com/99788755/182022235-bd16f2d3-8efd-462f-9e0b-120b8c50d833.png)

The updated design is updated in the folder 'fixed_level1_design1'

## Verification Strategy (Level 1 Design 1)
As explained in test scenarios above, bug free verilog code is updated in folder named 'fixed_level1_design1'
The following bugs were detected and corrected.

Case 1: 
- Test inputs: Inp12 = 1 and SEL = 12
- Expected Output: out = 12
- Observed Output in the DUT dut.out.value = Inp12 = 12

Case 2: 
- Test inputs: Inp12 = 1 and SEL = 30
- Expected Output: out = 30
- Observed Output in the DUT dut.out.value = Inp30 = 30

Output matches for the above inputs proving that **Level 1 Design 1 is bug free**

![l1d1_image5](https://user-images.githubusercontent.com/99788755/182021868-8bf24130-1865-4fdd-a2f5-2fca44ae3207.png)

## Is the verification complete for Level 1 Design 1 ?   
The bugs present in original verilog code were detected using cocotb testbench verification on level1_design1 MUX code. 
The bugs were located in code and updated bug-free. The same Cocotb test which detected the bugs, now with modified changes in the code, passes without committing any errors.
Hence, the verification of Mux Level 1 Design 1 is complete. 

# 

# Level 1 Design 2 (Sequence Detector Verification)

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Gitpod id is included in the screenshot shown below*

![l1d2_image1](https://user-images.githubusercontent.com/99788755/182026222-2b934776-da3e-4fab-a0e0-0ae27012771a.png)


## Verification Environment (Level 1 Design 2)

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives input sequence of bits to the Design Under Test (seq_detect_1011 module here) which takes in 1-bit input *clk*, *reset*, *inp_bit* and it gives 1-bit output *seq_seen*.

A cocotb Testbench is created to detect the input sequence pattern 1011. Sequence detector accepts input *inp_bit* a string a bits either 0 or 1. The output *seq_seen* goes high when the target sequence *1011* has been detected with overlap sequence. 

In cocotb testbench, the inputs are first assigned values and then are driven as follows:

![l1d2_image3](https://user-images.githubusercontent.com/99788755/182026472-14d29353-abd1-407a-bf04-392bdb521470.png)

Next, a 10us period clock is created on port clk and clock is started with reset. Cocotb tests are created for the input sequence *1101111*

![l1d2_image2](https://user-images.githubusercontent.com/99788755/182026315-cc3e90d8-3b41-4d84-a3c9-d01812fd9aaa.png)


The assert statement is used for comparing the current state value to the expected sequence 1011 and the cocotb log command display's the user typed message as shown below:

![l1d2_image4](https://user-images.githubusercontent.com/99788755/182026399-0140428f-a820-4503-8587-a7aa8324d9f4.png)


The following error's are observed:

**Error 1**
```
test12_basic_mux failed
Traceback (most recent call last):
File "/workspace/challenges-inderjit303/level1_design1/test_mux.py", line 236, in test12_basic_mux
assert dut.out.value == Inp12, f"Muliplexer output is incorrect: {dut.sel.value} != 12"
AssertionError: Muliplexer output is incorrect: 01100 != 12
```

**Error 2**
```
test30_basic_mux failed
Traceback (most recent call last):
File "/workspace/challenges-inderjit303/level1_design1/test_mux.py", line 560, in test30_basic_mux
assert dut.out.value == Inp30, f"Muliplexer output is incorrect: {dut.sel.value} != 30"
AssertionError: Muliplexer output is incorrect: 11110 != 30
```

## Test Scenario **(Level 1 Design 2)**
Cocotb tests are created for testing all states of input and monitoring outputs purposes. This makes sure that all the inputs are compared with expected output and DUT output. 

![l1d2_image6](https://user-images.githubusercontent.com/99788755/182026718-6ac98353-878a-428b-8665-33856b524d75.png)


The following cases reveals incorrect outputs for 2 such inputs cases: 

Case 1: 
- Test inputs: Inp12 = 1 and SEL = 12
- Expected Output: out = 12
- Observed Output in the DUT dut.out.value != Inp12 != 12

Case 2: 
- Test inputs: Inp12 = 1 and SEL = 30
- Expected Output: out = 30
- Observed Output in the DUT dut.out.value != Inp30 != 30

Output mismatches for the above inputs proving that there is a **design bug in Level 1 Design 1**

![l1d2_image5](https://user-images.githubusercontent.com/99788755/182026652-191b1c45-40bd-4cbc-8d2e-4272d4ee6758.png)


## Design Bug (Level 1 Design 2)
Based on the above test input and analysing the design, two bugs in the code were detected as discussed below: 

```
5'b01101: out = inp12;     ====> BUG 1
5'b01101: out = inp13;
5'b01110: out = inp14;            
```

For the mux design, the logic should be '5'b01100: out = inp12' instead of '5'b01101: out = inp12' as in the design code.

```
5'b11100: out = inp28;
5'b11101: out = inp29;
default: out = 0;          ====> BUG 2
```

For the mux design, the logic should be '5'b11110: out = inp30' instead of 'default: out = 0' as in the design code.


## Design Fix (Level 1 Design 2)
Updating the verilog design code and re-running the test makes the test pass.

![l1d2_image7](https://user-images.githubusercontent.com/99788755/182026727-cd48515e-366c-4ccc-b2cb-34490df96dd9.png)


The updated design is updated in the folder 'fixed_level1_design1'

## Verification Strategy (Level 1 Design 2)
As explained in test scenarios above, bug free verilog code is updated in folder named 'fixed_level1_design1'
The following bugs were detected and corrected.

Case 1: 
- Test inputs: Inp12 = 1 and SEL = 12
- Expected Output: out = 12
- Observed Output in the DUT dut.out.value = Inp12 = 12

Case 2: 
- Test inputs: Inp12 = 1 and SEL = 30
- Expected Output: out = 30
- Observed Output in the DUT dut.out.value = Inp30 = 30

Output matches for the above inputs proving that **Level 1 Design 2 is bug free**

![l1d2_image8](https://user-images.githubusercontent.com/99788755/182026698-6d8e7a17-a4c0-4ee2-9fd7-3765f61d81de.png)


## Is the verification complete ?   (Level 1 Design 2)
Yes, the bugs were detected using cocotb testbench verification on level1_design1 MUX code. 
The bugs were located in code and eliminated.
Hence, the verification of Mux Level 1 Design 1 completed by Pass DUT test. 

