# Final Project Information (Fall 2022)

## Schedule & Requirements

### Requirements

The goal of the final project is for you to build a complete system that accomplishes a realistic task with strong security guarantees. Final projects will be completed in groups of 1-3. The deliverables for the project will be as follows:

- A *project proposal* of 1 paragraph, describing:
  - Who is in your group
  - What problem you're trying to solve
  - A brief description of the approach you plan to use (e.g. what data; what algorithms)
- A *project writeup* of 1-3 pages, containing:
  - A problem statement
  - A technical description of your solution, with emphasis on anything that makes your solution unique; your description should be sufficient to enable the reader to *reproduce your implementation*
  - A description of the results - if you've evaluated your implementation on real data, describe how well it works
- A *project presentation video* of about 5 minutes
  - Your presentation should include slides or a demo
  - All group members should present some part of the project
  - Your presentation should cover the same material as your writeup, and be understandable to anyone who has taken this class (i.e. related work that was not covered in class should be explained in your presentation)
- Your *implementation*, in whatever form you choose
  - You can use any language or libraries you prefer, but a Python notebook will make grading easier

### Schedule & Grading

The final project is worth 10% of your final grade. The schedule for final project deliverables, and the contribution of each one to the grade you receive for the final project, are as follows:

| Deliverable                | Due Date                      | Grade Percent | Turn In    |
| ---------------------:     | ----------------------------- | ------------- | ---------- |
| Project Proposal           | 11/18/22 by 11:59pm           | 10%           | Blackboard |
| Project Presentation Video | 12/12/22 by 11:59pm           | 30%           | Blackboard |
| Implementation             | 12/12/22 at 11:59pm           | 40%           | Blackboard |
| Project Writeup            | 12/12/22 at 11:59pm           | 20%           | Blackboard |


### Graduate Students

Graduate students (and undergraduates taking the course for graduate credit) will be expected to develop a more ambitious final project (a more sophisticated algorithm or approach; a larger or more challenging dataset; or a more detailed analysis of experimental results).

## Project Ideas

You're welcome to work on any project interesting to you, as long as it's related to the concepts we have covered in class. My suggestion would be to implement one of the techniques we discussed in class, but did not implement in an exercise or homework assignment. Suggested examples include:

- Yao's garbled circuits protocol
- MPC protocol for calculating variance without revealing the mean
- Circuit for calculating variance without revealing the mean (with BGW or FHE)
- Bootstrapping circuit for FHE (very challenging)
- Implementation of non-interactive ZK protocol for graph coloring
- Circuits to check validity of electronic votes (see the voting protocol from our homework)
- Implementation of one of the case studies from Homework 6
- Cryptocurrency implementation (validation of blockchain; validation of transactions; coin-based transactions)
- Simulation of distributed cryptocurrency system (broadcasting transactions; mining; broadcasting new blocks)

