# Exam 1 Topic List

## Models of Secure Computation

- Outsourced computation
- Multiparty computation

## Finite Fields

- Definition
- Operations (+, *, multiplicative inverse)
- Why do we need them (randomness)
- Why does the characteristic need to be prime (multiplicative inverse)

## Defining Security

- Trusted third party
- Ideal functionality
- Real/Ideal paradigm
  - Anything you can learn from the protocol, you can also learn from the ideal functionality
- Proof of security by constructing a simulator
  - Constructive proof of the above

## Additive Secret Sharing

- Definition
- Security property
- Additive homomorphism
- No multiplicative homomorphism

## Shamir Secret Sharing

- Definition (including parameters `t` and `n`)
- Security property
- Reconstruction via interpolation
- Additive homomorphism
- (Limited) multiplicative homomorphism

## Specific-Purpose Protocols

- Summation (via secret sharing)
- Degree reduction (for Shamir secret sharing)
- Oblivious transfer (OT)

## Circuit-Based MPC Protocols

- Circuit definitions
  - Binary circuits
  - Arithmetic circuits
  - Strengths and weaknesses of each
- BGW protocol (arithmetic circuits, `n` parties; Shamir secret sharing + degree reduction)
- GMW protocol (binary circuits, 2 parties; additive secret sharing + OT)
- Strengths and weaknesses of each
