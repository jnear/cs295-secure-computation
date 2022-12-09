# Exam 2 Topic List

## Partially Homomorphic Encryption

- Basic operations
- Homomorphism and limitations
- Paillier cryptosystem (additive homomorphism)
- ElGamal cryptosystem (multiplicative homomorphism)

## Fully Homomorphic Encryption

- Basic operations
- Homomorphisms (both additive and multiplicative)
- Limitations (noise compounds with operations, especially multiplication)
- Parameters (tradeoff between ciphertext size and noise capacity)

## Zero Knowledge Proofs

- Definition and framework
- Structure (commit; challenge; response; check)
- Parameter setting (making it unlikely the prover can cheat)
- MPC-in-the-head for ZK on circuits
- Fiat-Shamir transform for non-interactivity

## Blockchains and Hash Structures

- Blockchain: linked list with hash pointers
- Merkle tree: binary tree with hash pointers
- Hash pointers detect tampering with low storage cost

## Bitcoin

- Blockchain holding transactions
- Validity
  - Hash pointers are correct
  - Each transaction output is used for at most one transaction input
  - Each input is signed with public key attached to corresponding output
- Mining: proof of work
  - Miners race to find a new block that hashes to value below "difficulty level"
  - Try new random "nonce" in block to modify hash
  - Harder difficulty level = need to try more nonces to find a "good" block
  - When new block found, broadcast to others
  - Others "accept" block by building on it
  - Others validate new blocks they receive

## Blockchain Topics

- Proof of stake
  - Peercoin: special "coinstake" transactions make mining less difficult; staking coins resets their "age"
  - Ethereum: staking coins (~$20k) allows you to become a validator and get rewards; if you misbehave as a validator, you lose your stake
- FileCoin: mining = storing other people's files on your HD
- Smart Contracts
  - Smart contract is a program stored on the blockchain
  - Transactions can invoke parts of the program to send and receive money
  - Major challenge: bugs (e.g. DAO)
  - No take-backs!
- NFTs
  - Just currencies you can't split (non-fungible)
  - Implemented in Ethereum as smart contracts that tell you their owner and allow sales
  - No connection to actual assets in the real world
- Anonymity: ZCoin
  - Many people put coins into a pool
  - Transaction spends a coin from the pool by proving (in ZK) that it hasn't been spent before
  - Breaks links between inputs & outputs
- Off-chain transactions
  - Idea: maintain a "bar tab" with another party, put many transactions on it
  - At some point, "settle" the tab with one on-chain transaction that transfers the balance
  - ZK rollup: settlement includes a zero-knowledge proof that the settlement is correct wrt the bar tab
    - Anyone can check validity, requires no trust in the other party
  - Lightning network: settlement doesn't include a proof; if it's wrong, other party can "dispute" and take your money
    - *You* need to check validity, requires watching the blockchain closely

## Misc Topics

- Secure aggregation: lightweight MPC protocols for federated machine learning (basically high-dimensional summation)
- Holistic privacy
  - Input privacy: protocol is secure wrt ideal functionality
  - Ouput privacy: ideal functionality doesn't leak too much about inputs
  - Becoming more common: combine crypto (input privacy) with differential privacy (output privacy)
- Secure enclaves / trusted execution environments (TEEs)
  - Special CPUs with built-in private keys
  - Act as a trusted third party; much faster than crypto
  - But: many bugs have been found
