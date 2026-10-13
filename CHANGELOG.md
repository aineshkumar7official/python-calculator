# Changelog

## [2.0.0] - 2026-09-10
### Added
- Full expressions with order of operations (PEMDAS) and parentheses, using the shunting-yard algorithm
- Trigonometry: `sin`, `cos`, `tan` (degrees)
### Changed
- Rewrote the parser: v1 handled one operator type per line; v2 handles any mix
### Removed
- Modulus `%` (planned to return)

## [1.0.0] - 2026-09-08
### Added
- Single-operation calculator: `+`, `-`, `*`, `/`, `^`, `%`, `sqrt`, `log`
- Division-by-zero, negative square root, and non-positive log errors
- Continuous input loop with quit words
