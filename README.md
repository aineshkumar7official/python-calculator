# Python CLI Calculator

A command-line calculator built in Python for COP 2510 at USF. Version 2 evaluates full expressions with order of operations using the shunting-yard algorithm.

## How to run

```bash
python calculator.py
```

Type an expression and press Enter. Type `quit`, `exit`, `done`, or `stop` to leave.

## Examples

```
> 2 + 3 * 4
14.0
> (2 + 3) * 4
20.0
> sqrt16 + log100
6.0
> sin30
0.5
> 5 / 0
Error: Division by zero is not allowed.
```

## Features (v2.0)

- Addition `+`, subtraction `-`, multiplication `*`, division `/`, exponents `^`
- Order of operations (PEMDAS) and parentheses
- Square root `sqrt`, base-10 logarithm `log`
- Sine `sin`, cosine `cos`, tangent `tan` (input in degrees)
- Clear error messages for division by zero, invalid square roots and logs, and mismatched parentheses
- Results rounded to 2 decimal places

## How it works

The input is split into numbers and operators. Numbers go on one stack, operators on another. When an incoming operator has lower or equal priority than the one on top of the stack, the top operator is evaluated first. This is the shunting-yard algorithm, and it's what makes `2 + 3 * 4` return 14 instead of 20.

## Known limitations

- Negative numbers (`-5 + 3`) aren't supported yet
- Modulus `%` was supported in v1 but not yet in v2
- Chained exponents evaluate left to right (`2^3^2` returns 64, not 512)

## Version history

See [CHANGELOG.md](CHANGELOG.md). Earlier versions are kept in [`versions/`](versions/).
