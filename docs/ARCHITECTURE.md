# Architecture & Controls

[Back to project](../README.md)

## Design

The 4-bit datapath uses four registers (`R1`–`R4`), two operand-selection multiplexers, a custom ALU, a destination decoder, and a write-data multiplexer.

![Main datapath](../assets/datapath-overview.png)

### Signal flow

1. The source multiplexers select the two register operands.
2. The ALU processes the operands using the selected `OPR` code.
3. The write-data multiplexer selects manual data or the ALU result.
4. The destination decoder selects the register to be updated on the clock edge.

## Controls

| Signal | Width | Function |
| :--- | :---: | :--- |
| `Manual_IN` | 4 | 4-bit manual data input |
| `LOAD` | 1 | Select manual input or ALU write-back |
| `SEL_A` | 2 | Select operand A register |
| `SEL_B` | 2 | Select operand B register |
| `SEL_D` | 2 | Select destination register |
| `OPR` | 2 | Choose ALU operation |
| `RST` | 1 | Reset registers |
| Clock | 1 | Update the enabled register |
| `ZERO` | 1 | Zero-result status LED |

## ALU

![ALU schematic](../assets/alu-subcircuit.png)

| `OPR` | Function |
| :---: | :--- |
| `00` | Addition |
| `01` | Subtraction |
| `10` | Bitwise AND |
| `11` | Bitwise OR |

The result is 4 bits wide. The zero flag is computed from the output bits:

```text
ZF = NOT (result[3] OR result[2] OR result[1] OR result[0])
```

## Using the datapath

1. Open the circuit in Logisim-evolution and select `main`.
2. Choose a register using `SEL_D`, enter a value with `Manual_IN`, and select the manual input path using `LOAD`.
3. Pulse the clock to store the value. Repeat to initialize another register.
4. Set `SEL_A` and `SEL_B` to select the two operands.
5. Set the desired `OPR` code and observe the output.
6. Switch `LOAD` to the ALU output path, select a destination register, and pulse the clock to store the result.

[Example test cases](VERIFICATION.md)
