---
title: CS 295/395 Secure Distributed Computation
layout: default
---

# UVM CS 295/395: Secure Distributed Computation (Fall 2022)

  * [Course Description](#course-description)
  * [Administrative](#administrative)
  * [Resources](#resources)
  * [Textbook & Other References](#textbook---other-references)
  * [Policies](#policies)
    + [Grading](#grading)
    + [Exams & Quizzes](#exams---quizzes)
    + [Homework Assignments and In-class Exercises](#homework-assignments-and-in-class-exercises)
    + [Late Work](#late-work)
    + [Collaboration & Allowed References](#collaboration--allowed-references)
  * [Final Projects](#final-projects)
  * [CS Student Research Day & Extra Credit](#cs-student-research-day--extra-credit)
  * [Schedule](#schedule)

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

- **Lecture**: Monday, Wednesday, Friday, 10:50am-11:40am in Marsh Life Science 105
- **Instructor**: Joe Near (jnear at uvm dot edu)
- **Office hours**: 
  - **Joe Near** (instructor): Mondays and Fridays, 9:30am-10:30am, and by appointment; Innovation Hall E458 (or MS Teams)

## Resources

- **Course textbooks** are available online (see below)
- **Blackboard** for the course is available [here](https://bb.uvm.edu/webapps/blackboard/execute/launcher?type=Course&id=_173067_1)
- **Course Github Repo** [is available here](https://github.com/jnear/cs295-secure-computation)
- **Weekly exercises**
  - [Download exercises here](https://github.com/jnear/cs295-secure-computation/tree/master/exercises)
  - Turn in notebook files on Blackboard
- **Homework assignments** 
  - [Download notebooks here](https://github.com/jnear/cs295-secure-computation/tree/master/homework)
  - Turn in notebook files on Blackboard
- **Discussions** will take place on MS Teams
- **Review Sheets** for exams:
  - [Exam 1](https://github.com/jnear/cs295-secure-computation/tree/master/resources/review-exam1.md)

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

A very cool [podcast recently appeared on Unexplainable](https://megaphone.link/VMP1399619625) about cryptography, including interviews with Whit Diffie, Martin Hellman, and Rafael Pass.

## Policies

### Grading

Your grade for the course will be determined as follows:

- 10 homework assignments (5% each; 50% total)
- in-class weekly exercises (20% total)
- midterm exam (10%)
- final exam (10%)
- final project (10%)

Your final grade will be determined by summing the total number of
points awarded and calculating the percentage of the total possible
points. This percentage is translated into a letter grade as follows:

#### Undergraduate Students

| Percent | Letter Grade |
| ------: | ------------ |
| 98-100  | A+           |
| 93-97   | A            |
| 90-92   | A-           |
| 87-89   | B+           |
| 83-86   | B            |
| 80-82   | B-           |
| 77-79   | C+           |
| 73-76   | C            |
| 70-72   | C-           |
| 67-69   | D+           |
| 63-66   | D            |
| 60-62   | D-           |
| <60     | F            |

#### Graduate Students

| Percent | Letter Grade |
| ------: | ------------ |
| 98-100  | A+           |
| 93-97   | A            |
| 90-92   | A-           |
| 87-89   | B+           |
| 83-86   | B            |
| 80-82   | B-           |
| 77-79   | C+           |
| 73-76   | C            |
| 70-72   | C-           |
| <70     | F            |

### Exams & Quizzes

There will be two exams: a midterm and a final. You will be allowed one page of notes for each exam. See the schedule below for the dates.

### Homework Assignments and In-class Exercises

This course will use Python for examples and for programming
assignments.  Students are expected to be proficient in Python
programming.  Programming assignments will be distributed and turned
in as Jupyter notebooks. [Click
here](https://jnear.github.io/cs211-data-privacy/jupyter) for
instructions on installing Jupyter Notebook.

**Assignment Submission**: Homework and in-class exercises will be
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
Any collaboration, even at a high level, must be declared when you submit your assignment, in a note at the top of the assignment.
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

## CS Student Research Day & Extra Credit

We will **not hold class** on **Friday, September 23**. I encourage you
to attend [CS Student Research
Day](https://www.uvm.edu/~jonaolap/csrd/2022.html) and learn about
the awesome research being done by CS students at UVM!

- If you attend **two full sessions** of talks (~4 talks), **take
  brief notes on the talks you hear**, and **send the notes to me via
  email by 11:59pm on September 23**, I will give **1% extra credit to
  your final grade in the course**

## Schedule

Note that class will **not** be held on the following dates:

- Monday, September 5 (Labor Day)
- Friday, September 23 (please attend [CS Student Research Day](https://www.uvm.edu/~jonaolap/csrd/2022.html))
- Friday, October 14 (Fall Recess)
- November 21-25 (Thanksgiving)

Important due dates:

- Homework assignments are due every *Monday* at 11:59pm.
- In-class weekly exercises are due every *Friday*, by 11:59pm.

Exam dates:

- Midterm exam: Wednesday, October 12, during class (Marsh Life Science 105)
- Final exam: December 12, 10:30am - 11:30am (Marsh Life Science 105)

Homework dates:

| Item                                                                                                    | Due Date |
| -----------------------------------------------------------------------------------------:              | -------- |
| [Homework 1](https://github.com/jnear/cs295-secure-computation/blob/master/homework/CS295_HW_1.ipynb)   | 9/12/22  |
| [Homework 2](https://github.com/jnear/cs295-secure-computation/blob/master/homework/CS295_HW_2.ipynb)   | 9/19/22  |
| [Homework 3](https://github.com/jnear/cs295-secure-computation/blob/master/homework/CS295_HW_3.ipynb)   | 9/26/22  |
| [Homework 4](https://github.com/jnear/cs295-secure-computation/blob/master/homework/CS295_HW_4.ipynb)   | 10/3/22  |
| [Homework 5](https://github.com/jnear/cs295-secure-computation/blob/master/homework/CS295_HW_5.ipynb)   | 10/17/22 |
| [Homework 6](https://github.com/jnear/cs295-secure-computation/blob/master/homework/CS295_HW_6.ipynb)   | 10/24/22 |
| [Homework 7](https://github.com/jnear/cs295-secure-computation/blob/master/homework/CS295_HW_7.ipynb)   | 10/31/22 |
| [Homework 8](https://github.com/jnear/cs295-secure-computation/blob/master/homework/CS295_HW_8.ipynb)   | 11/7/22  |
| [Homework 9](https://github.com/jnear/cs295-secure-computation/blob/master/homework/CS295_HW_9.ipynb)   | 11/14/22 |
| [Homework 10](https://github.com/jnear/cs295-secure-computation/blob/master/homework/CS295_HW_10.ipynb) | 12/5/22  |
| Project proposals                                                                                       | 11/18/22 |
| Final project writeup/video/implementation                                                              | 12/12/22 |

Schedule of topics:

| Week of... | Topics                                                                               | Reference  |
| ---------: | ------------------------------------------------------------------------------------ | ---------  |
| 8/29/22    | Intro to secure computation, additive secret sharing (no exercise)                   | PMPC Ch. 1 |
| 9/5/22     | Adversaries and threat models (no class Monday)                                      | PMPC Ch. 2 |
| 9/12/22    | Shamir secret sharing                                                                | PMPC Ch. 3 |
| 9/19/22    | Shamir secret sharing operations; MPC for arithmetic circuits (no class Friday)      | PMPC Ch. 3 |
| 9/26/22    | Circuits; MPC protocols for circuits                                                 | PMPC Ch. 3 |
| 10/3/22    | GMW protocol; garbled circuits protocol; malicious MPC                               | PMPC Ch. 6 |
| 10/10/22   | *Intermission*. Review (exam Wednesday; no class Friday; no exercise)                | None       |
| 10/17/22   | Partially homomorphic cryptosystems: Paillier and El Gamal                           | TBA        |
| 10/24/22   | Fully homomorphic encryption                                                         | TBA        |
| 10/31/22   | Zero-knowledge proof                                                                 | PMPC Ch. 6 |
| 11/7/22    | Distributed ledgers and blockchains                                                  | BCT Ch. 1  |
| 11/14/22   | Bitcoin & its challenges                                                             | BCT Ch. 2  |
| 11/21/22   | No class (Thanksgiving)                                                              | BCT        |
| 11/28/22   | Blockchain applications: smart contracts, filesystems, etc                           | BCT Ch. 10 |
| 12/5/22    | Open challenges; review                                                              |            |

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
