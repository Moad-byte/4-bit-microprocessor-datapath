# Test Cases

[Back to project](../README.md) · [Architecture and controls](ARCHITECTURE.md)

The following examples illustrate the datapath's arithmetic, logic, register selection, and write-back behavior.

## Arithmetic and logic

| Operand A | Operand B | `OPR` | Function | 4-bit result | `ZF` |
| :---: | :---: | :---: | :--- | :---: | :---: |
| `5` | `3` | `00` | ADD | `8` | `0` |
| `4` | `4` | `01` | SUB | `0` | `1` |
| `C` | `A` | `10` | AND | `8` | `0` |
| `C` | `A` | `11` | OR | `E` | `0` |
| `F` | `1` | `00` | ADD | `0` | `1` |

*Values use hexadecimal notation.*

### Addition: 5 + 3 = 8

![Addition result](../assets/addition-test.png)

### Subtraction: 4 - 4 = 0

![Zero flag example](../assets/zero-flag-test.png)

## Register and control checks

- **Register loading:** Set a manual 4-bit value, choose the destination with `SEL_D`, and pulse the clock.
- **Operand selection:** Change `SEL_A` and `SEL_B` and observe the selected register values at the ALU inputs.
- **Write-back:** Select the ALU result through `LOAD` and store it in the target register.
- **Reset:** Activate `RST` and observe the register values return to their reset state.
- **Zero flag:** Observe the zero LED when the ALU result is `0000`.
