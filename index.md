---
title: CS 295/395 Secure Distributed Computation
layout: default
---

# UVM CS 295/395: Secure Distributed Computation (Fall 2020)

## Announcements

None yet.

## Course Description

Techniques for secure computation involving multiple distributed
parties, including applied cryptography, homomorphic encryption,
secure multiparty computation, verified computation, and
zero-knowledge proof. Applications including Bitcoin and other
blockchain systems, Ethereum and other smart contracts, encrypted
databases, and computing on encrypted data.

This is a programming-based course, with minimal theory background
required. Programming projects may include:

 - Building an encrypted database that runs queries over encrypted
   data without decrypting it
 - Building a distributed protocol that computes the average salary
   among several parties, without revealing any individual's salary
 - Building a decentralized cryptocurrency, using techniques from
   blockchain research
 - Building a decentralized smart contract system

## Learning Objectives

By the end of this course, you will be able to:

- Describe the common goals of secure computation techniques
- Define and apply the following concepts:
  - Secure multiparty computation
  - Homomorphic encryption
  - Zero-knowledge proof
  - Distributed ledger
  - Blockchain
- Build systems that compute on encrypted data
- Implement protocols for zero-knowledge proof
- Evaluate the communications cost of a distributed protocol
- Argue for the security of a distributed protocol

## Administrative

- **Lecture**: Monday, Wednesday, Friday, 9:40am - 10:30am, on MS Teams
- **Instructor**: Joe Near (jnear at uvm dot edu)
- **Office hours**: Mondays and Fridays, 3-4pm, and by appointment

## Resources

- **Lectures** will take place *synchronously* on MS Teams. If you
  have not been added to the CS 295 Team, please email me. Lectures
  will be recorded and available on MS Teams for offline viewing.
- **Course textbooks** are available online (see below)
- **Blackboard** for the course is available [here](https://bb.uvm.edu/webapps/blackboard/execute/launcher?type=Course&id=_143340_1&url=)
- **Course Github Repo** [is available here](https://github.com/jnear/cs295-secure-computation)
- **Daily exercises**
  - [Download exercises here](https://github.com/jnear/cs295-secure-computation/tree/master/exercises)
  - Turn in notebook files on Blackboard
- **Homework assignments** 
  - [Download notebooks here](https://github.com/jnear/cs295-secure-computation/tree/master/homework)
  - Turn in notebook files on Blackboard
- **Discussions** will take place on MS Teams
- **Videos** from lecture are available [here](https://web.microsoftstream.com/group/3416a83c-5358-4b6e-8747-01d9c1963f01?view=videos)

## Textbook & Other References

Please **do not** buy any books for this course. All required reference material is available online for free.

We will use the following textbooks for this course:

- [Pragmatic MPC](https://securecomputation.org/)  
  David Evans, Vladimir Kolesnikov and Mike Rosulek

- [Bitcoin and Cryptocurrency Technologies](https://bitcoinbook.cs.princeton.edu/) ([PDF available here](https://d28rh4a8wq0iu5.cloudfront.net/bitcointech/readings/princeton_bitcoin_book.pdf))  
   Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller, Steven Goldfeder 

- Zero Knowledge Proofs: An Illustrated Primer  
  Matthew Green
  - [Part 1](https://blog.cryptographyengineering.com/2014/11/27/zero-knowledge-proofs-illustrated-primer/)
  - [Part 2](https://blog.cryptographyengineering.com/2017/01/21/zero-knowledge-proofs-an-illustrated-primer-part-2/)

In addition to these, we will reference a number of academic papers
throughout the semester.

### Links and Helpful Resources

- None yet

## Policies

### Grading

Your grade for the course will be determined as follows:

- 11 homework assignments (5% each; 55% total)
- in-class exercises (25% total) (3 lowest scores will be dropped)
- final project (20%)

### Exams & Quizzes

There will be no exams for this course.
There is no final exam, and this course will conclude before the University's exam period.

### Homework Assignments and Daily In-class Exercises

This course will use Python for examples and for programming
assignments.  Students are expected to be proficient in Python
programming.  Programming assignments will be distributed and turned
in as Jupyter notebooks. [Click
here](https://jnear.github.io/cs295-secure-computation/jupyter) for
instructions on installing Jupyter Notebook.

**Assignment Submission*: Homework and in-class exercises will be
turned in via Blackboard.

To submit an assignment:

1. Complete the released Jupyter Notebook by filling in answers to all the questions
2. Submit the notebook file (the .ipynb file) as your solution on Blackboard

*Please* do not change the name of the .ipynb file. This makes the
grading process more difficult.

Please let me know if you have any questions about the submission process.

### Late Work

Late work *may* be accepted, but you *must* make arrangements with me
first. If you need to turn something in late, for any reason, please
email me *before the deadline*. Depending on the circumstances, I may
(or may not) impose a late penalty on your grade.

### Collaboration & Allowed References

Collaboration on the high-level ideas and approach on assignments is encouraged.
Copying someone else's work is not allowed.
Any collaboration, even at a high level, must be declared when you submit your assignment.
Every assignment must include a collaboration statement.
E.g., "I discussed high-level strategies for solving problem 2 and 5 with Alex."

The official references for the course are listed in the schedule below.
Copying from references other than these is not allowed.
In particular, code and proofs should not be copied from other sources,
including Stack Overflow and other public sources.

Students caught copying work are eligible for immediate failure of the course and disciplinary action by the University.
All academic integrity misconduct will be treated according to [UVM's Code of Academic Integrity](https://www.uvm.edu/policies/student/acadintegrity.pdf).

## Final Projects

The course will include a final project, completed in groups of 1-3 students.
The final project will demonstrate your mastery of the concepts covered in this course.

Click [here](https://jnear.github.io/cs295-secure-computation/projects) for more complete information.

## Schedule

Note that class will **not** be held on the following dates:

- Monday, Sep. 7 (labor day)
- Wednesday and Friday of Thanksgiving week

Important due dates:

- Homework assignments are due every *Monday* at 11:59pm.
- In-class exercises are due *the day of the class*, by 11:59pm.

| Item                                                                                                    | Due Date |
| -----------------------------------------------------------------------------------------------:        | -------- |
| [Homework 1](https://github.com/jnear/cs295-secure-computation/blob/master/homework/HW_1.ipynb)         | 9/14/20  |
| [Homework 2](https://github.com/jnear/cs295-secure-computation/blob/master/homework/HW_2.ipynb)         | 9/21/20  |
| [Homework 3](https://github.com/jnear/cs295-secure-computation/blob/master/homework/HW_3.ipynb)         | 9/28/20  |
| [Homework 4](https://github.com/jnear/cs295-secure-computation/blob/master/homework/HW_4.ipynb)         | 10/5/20  |
| Homework 5 *lite*                                                                                       | 10/14/20 |
| [Homework 6](https://github.com/jnear/cs295-secure-computation/blob/master/homework/CS295_HW_6.ipynb)   | 10/19/20 |
| [Homework 7](https://github.com/jnear/cs295-secure-computation/blob/master/homework/CS295_HW_7.ipynb)   | 10/26/20 |
| [Homework 8](https://github.com/jnear/cs295-secure-computation/blob/master/homework/CS295_HW_8.ipynb)   | 11/2/20  |
| [Homework 9](https://github.com/jnear/cs295-secure-computation/blob/master/homework/CS295_HW_9.ipynb)   | 11/9/20  |
| [Homework 10](https://github.com/jnear/cs295-secure-computation/blob/master/homework/CS295_HW_10.ipynb) | 11/16/20 |
| Homework 11                                                                                             | 12/4/20  |
| Project presentations                                                                                   | TBA      |
| Final project writeup/implementation                                                                    | TBA      |

Schedule of topics:

| Week of... | Topics                                                                               | Reference  |
| ---------: | ------------------------------------------------------------------------------------ | ---------  |
| 8/31/20    | Intro to secure computation, additive secret sharing                                 | PMPC Ch. 1 |
| 9/7/20     | Adversaries and threat models (no class Monday)                                      | PMPC Ch. 2 |
| 9/14/20    | Shamir secret sharing                                                                | PMPC Ch. 3 |
| 9/21/20    | Shamir secret sharing operations                                                     | PMPC Ch. 3 |
| 9/28/20    | Multiparty computation for arithmetic circuits: GMW protocol                         | PMPC Ch. 3 |
| 10/5/20    | *Intermission*. Real systems; garbled circuits; malicious MPC                        | PMPC Ch. 6 |
| 10/12/20   | Partially homomorphic cryptosystems: Paillier and El Gamal                           | TBA        |
| 10/19/20   | Fully homomorphic encryption                                                         | TBA        |
| 10/26/20   | Zero-knowledge proof I                                                               | PMPC Ch. 6 |
| 11/2/20    | Zero-knowledge proof II                                                              | PMPC Ch. 6 |
| 11/9/20    | Distributed ledgers and blockchains                                                  | BCT Ch. 1  |
| 11/16/20   | Bitcoin                                                                              | BCT Ch. 2  |
| 11/23/20   | Challenges of Bitcoin (no class Wednesday, Friday)                                   | BCT        |
| 11/30/20   | Blockchain applications: smart contracts, filesystems, etc                           | BCT Ch. 10 |
| 12/2/20    | Open challenges and project presentations                                            |            |

# Accommodations

In keeping with University policy, any student with a documented
disability interested in utilizing accommodations should contact SAS,
the office of Disability Services on campus. SAS works with students
and faculty in an interactive process to explore reasonable and
appropriate accommodations, which are communicated to faculty in an
accommodation letter. All students are strongly encouraged to meet
with their faculty to discuss the accommodations they plan to use in
each course. A student's accommodation letter lists those
accommodations that will not be implemented until the student meets
with their faculty to create a plan. Contact SAS: A170 Living/Learning
Center; 802-656-7753; access@uvm.edu; or www.uvm.edu/access

# Religious Holidays

Students have the right to practice the religion of their choice. Each
semester students should submit in writing to their instructors by the
end of the second full week of classes their documented religious
holiday schedule for the semester. An arrangement can then be made to
make up the missed work.

# Student Athletes

In order to be excused from classes, student athletes should submit
appropriate documentation to the Professor in advance of all
scheduling conflicts within the first two weeks of class. Those
missing class are expected to submit make-up assignments within a
reasonable time period.
