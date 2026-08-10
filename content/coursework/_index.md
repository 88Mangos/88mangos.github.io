---
title: "Coursework"
description: "Taking and teaching courses at CMU"
ShowToc: true
TocOpen: true  # Optional: Keep it open by default
# Keep this thing hidden
draft: false
sitemap:
  disable: true
_build:
  list: never
---

*Why is this page not accessible from the home page?* Because it's just a word dump from me and I'm not tryna have random people reading shit in my writer's voice, which is not the same as my everyday voice. Plus it's lwk annoying when ppl find this shit.

**How to Read This:** from top-to-bottom, my semesters are in reverse chronological order. I will provide some context here at the top for your reading pleasure. 

I am not trying to make a course review website, I just want to document all of the cool stuff I've learned and make comments on the changing landscape of courses at CMU.

I also inject a lot of my own opinions into things, so I'll give a brief "About Me" to contextualize my takes:
> I was born and raised in Memphis, TN and up until I got into CMU, mostly worked on biology and science research stuff. I did some competitions in HS, though I sucked - I barely reached USACO Silver (embarrassed to admit it took me 2 tries) and I made the AIME twice, but on the AMC12 which is famously easier than the 10. 

> Also, I came into CMU with 18 courses worth of AP credit, which works out to 164 units of credit. I took the placement test to upgrade my AP Biology credit to replace 03-121. As such, I take very few general education courses, and when I do take them, I have been fortunate to take courses that are genuinely interesting to me.

Thus, many of my opinions will be from the context of somebody who had an OK foundation in math/CS, but is seeing a lot of the concepts for the first time. Use that to calibrate my opinions of courses. 

Before we begin, one last thing: *CMU genuinely pushes me to use 100% of my brain, but I am more than 100% smarter than I was when I came in. So when I say courses were hard, I mean they were genuinely hard for me.*

# Spring 2026 (50 units)
- 15-411: Compiler Design
- 15-442: Machine Learning Systems
- 10-301: Introduction to Machine Learning
- 73-102: Principles of Microeconomics
- 07-070: Teaching Techniques for Computer Science
- 15-210 [TA]: Parallel and Sequential Data Structures and Algorithms

Yeah so I thought I'd lower the number of units after overloading the previous semester. But I forgot to account for the fact that compilers and MLSys would end up being timesinks.

Micro was chill, but the game theory was kinda difficult and I did have to study for it. I really appreciate Prof. Serra for making the course more than just AP Micro review though. 301 wasn't terribly difficult, interesting to me, and also not too bad to study for given that (1) I had already taken IDL (11-785) and (2) self-studied parts of CS231n and CS182A for research. 07-070 was a nice little intro to TA'ing course for CS TAs that was also chill.

Onto the things I have an opinion about. 411 became AI-allowed for the first time. So Claude abuse was absolutely rampant. Joe and I weren't Claude abusers (at least, not until the last 3 days before L5 was due), and we sorta regret it. But even with all of the weirdness of this iteration of 411, I still felt like I learned a lot. I've never read/written/debugged so much code before, and a lot of things I've learned so far came full circle. Whether it was the statics/dynamics judgements from 312, writing representation invariant checkers like malloc lab (213) and contracts from 122, all the functional programming skills from 150 and OCaml, the algorithms from 210 (Tarjan DFS numbering spam), the course was just a lot of fun. Even after I spent 60 hours after spring break rewriting our entire middle end to support on-the-fly Trivial Phi Elimination before Lab LLVM. And even when we submitted L4 using *all 3 late days*, after the whole class got a one day extension. And yes, even after having to buy a Claude subscription 3 days before L5 was due because otherwise there was no way our multiplier was going to be good enough. I think it speaks to how good 411 is, that even when the course policies are confusing as hell, the value of writing a compiler with your partner is so high that it just cancels out.

MLSys was super chill for the first 9 weeks. And then the TIRx GEMM assignment hit (writing kernels for Blackwell GPUs specifically, using a DSL that the AI assistants hadn't been trained on yet) and that was evil. Though I heard that was super Claude-Code-able, but I hadn't bought Claude Code yet and was still trying to complete the assignment without coding agents (*411 L5 was the first time I'd ever used coding agents*). The course project also felt a little scuffed - since it was due after compilers, I had Claude write the code after I gave it a scaffold of the algorithms I wanted to implement. It took a few human refactors (coding agents seem to love rewriting functions that already exist because keeping things in context is hard) but it worked out. 

Anyways my favorite part was TA'ing 210. I think it's a bit too recent for me to write a reflection on, but yeah this was the highlight of my semester. Overhauling CriticalLab and writing the autograder for PowerLab was tedious but honestly pretty cool, and teaching content that I had struggled with just a semester prior was also very rewarding. TA'ing 210 made me so much smarter, both because of the other TAs, the professors, and the course content itself. 

*Am I a furry because I wore a cow costume to proctor the final? I personally don't think so...* 

## Projects I enjoyed
- 411: all the labs. Especially Lab LLVM was cool since it's like... real?
- MLSys: 
  - TIRx GEMM
  - using MPI for the first time and learning about data parallelism
- 301 HW8, building an RL agent to play Pong 

# Fall 2025 (57 units, small overload, but...)
- 15-210: Parallel and Sequential Data Structures and Algorithms
- 15-312: Foundations of Programming Langauges
- 15-259: Probability and Computing
- 11-785: Introduction to Deep Learning (PhD version)
- 85-110: Cognitive Psychology
- 21-259 [TA]: Calculus in Three Dimensions

On top of all of this, I also worked part-time for Scale AI as a Technical Advisor Intern. I signed a few NDAs so all I can say was that I worked on GenAI stuff at Scale. But this extra responsibility, on top of overloading with a grad class, the grad class was IDL, and also TA'ing for the first time - yeah I overdid it this semester. 

Every week felt like I was just trying to survive to hit the next deadline. And my Tuesdays/Thursdays were hell: wake up, teach 259 recitation, go to Cogpsych, go to 312, go to PnC, and finally be free. 10 AM to 3:30 PM, zero breaks. And on Tuesdays, add on a 9-10 AM 210 recitation. 

To be honest I have nothing great to say about some of my classes so I'll just omit (*elide*) the negativity. I guess IDL gave me a lot of experience implementing stuff in PyTorch, and gave me the chance to use PSC resources for the first time, which was cool. Onto the good parts: cogpsych was super chill but also very interesting (*note I never got to take AP Psychology, but friends who had said it cogpsych was not really useful*). 

I got B's in both PnC and 312. To be honest that 312 final is the dumbest I've ever felt - I thought I earned a 9/270 and somehow got away with a 172/270. However, the 312 content was super interesting, and though it didn't help with compilers as much as I'd hoped, learning from Bob Harper definitely expanded my brain. It definitely hurt while my brain was expanding though - had to use late days for the first time ever on the programs as proofs homework. 

PnC was the exact opposite from 312 - while I had been doing really well in 312 up until the final, I'd been doing only OK in PnC, mostly due to the hellish Tuesday/Thursday schedules giving me no time to study for the in-class quizzes, which I promptly bombed. I got a 95 on the final though so that's nice, plus the material was super helpful. 

210 was definitely my most rewarding class, though 312 and IDL took away most of my time I would've procured for it. With 251 under my belt, the randomized algorithms and probability sections weren't too bad, plus the treaps/MSTs part built on 251 and 122 knowledge so it wasn't too hard to keep up despite my lower-than-optimal time investment into the class. But my glaze for 210 is only just beginning (foreshadowing).

TA'ing for 259 was nice - I loved freestyling the recitations and holding OH to help students get their Aha! moments. In a sense I rediscovered how much I liked teaching - I'd lowkey forgotten because in all my classes at CMU thus far, I'd been the one learning and barely getting by, so being the student who had experience who could help others was rewarding. Working with a genius like Prof. O'Dorney was a good experience too.

All in all, this was my "limit testing" semester (self-report) and I definitely inted. But it's OK because honestly things worked out, and in my opinion, the highest-value classes are the ones that (1) tell you what you want to study, followed by (2) tell you what you don't want to study. 

## Projects I enjoyed
- 11-785 (IDL)
  - MyTorch: supporting MLPs, CNNs, RNNs, and other PyTorch functionality just using NumPy
  - bonus autograd engine implementation for MyTorch


# Summer 2025 (24 units)
- 99-270: Summer Undergraduate Research Apprenticeship
- 18-213: Introduction to Computer Systems

Contrary to the wisdom of Bay Area tryhards, not getting an internship freshman year is *not* the end of the world. But keeping busy is fine - I mean look what I did over winter 2024 because I was bored - so I decided I'd take 213 over the summer and do some summer research, continuing the commitment from the fall. I'd joined MAIL and as part of the onboarding, self-studied parts of CS231n (Stanford) and CS128a (UC Berkeley), and was now deemed ready for the summer research.

To be honest, I didn't think this summer was super eventful academically, but it was fun to go to Kennywood and do other things that I typically didn't have time to do during the semester - e.g., cook actual food instead of spamming the meal plan. 213 was extremely chill because it was remote and taught from the KesBoat, but I really enjoyed reading the CSAPP textbook and working through the exercises (*even if I only did them because I skipped the Zoom lectures*).

I guess SURA was great QPA padding? and 213 has a lot of cool content... but otherwise not much to add. Definitely hated the off-campus house I stayed in on Beeler during the second half of summer, and that made me realize I don't wanna be unemployed and broke.

## Projects I enjoyed
- Research:
  - write a transformer encoder/decoder from scratch in PyTorch
    - encoder for solubility prediction
    - decoder for retrosynthetic prediction of reactants from products
- 18-213:
  - cache simulator and cache optimization of matrix transpose
  - custom malloc implementation
  - writing a terminal shell

# Spring 2025 (56 units)
- 15-251: Great Theoretical Ideas in Computer Science
- 15-150: Principles of Functional Programming
- 21-266: Vector Calculus using Matrix Algebra
- 02-180: Great Ideas in Computational Biology (Part I)
- 02-181: Great Ideas in Computational Biology (Part II)
- 79-345: Roots of Rock and Roll
- 69-138: Outdoor Soccer 

This was the first year of SCS Minis and also the first time 251 introduced their Claude-powered PandaBot. Like GPTutor from Concepts, it was a really helpful tool in making me simplify my logic. My mentor TA Dhruv was also very supportive. 

After what I thought was a chill freshman fall, I decided to push myself a bit and take as many classes as vpeet would allow. To be honest it was a slug fest - 15-150 wasn't bad, but I had no prior knowledge of the material, and would watch Brandon Wu lectures instead of actually going to class. I'd also fall asleep a lot in the comp bio minis because they were right after lunch, and Hunan Express block meals are *quite* heavy.

I barely squeaked by 251 with a 90.38%, which was nice. SML was tedious, but also in retrospect it's a learning experience - plus, setting up SML/NJ locally would prove super useful for 210/312 and being a 210 TA (more foreshadowing).

Clive's 21-266 was super chill for me since I had already taken multivariable calculus in high school, and I really enjoyed his pre-lecture notes templates that I could follow along with. I also really enjoyed 02-180, learning dynamic programming and other cool genome algorithms that I would later hear about again in 210. The cool Eulerian vs. Hamiltonian paths modification motivation that Prof. Compeau gave while teaching about De Bruijn graphs was also very interesting. Part II was a bit more tedious - one of many times where I felt that a course's final project was completely unnecessary and irrelevant to the value of the course.

But beyond the technicals, this semester also had two great fun classes. Roots of Rock and Roll was extremely fun (though I often slept through it) and gave me a bit more hometown pride for Memphis (Elvis is definitely no small part of the history of Rock and Roll). The essays forced me to actually read and keep my literature skills sharp, and I enjoyed the genuinely useful feedback from the older-than-usual TAs. Outdoor soccer during the second half of the semester was fun too, though attendance-mandatory PE is kinda weird to me. It was fun playing with complete newbies and graduating seniors that used to play for the varsity team.

## Projects I enjoyed
- 02-180 and 181
  - hidden markov models
  - sequence alignment algorithms
  - Viterbi algorithm
  - Burrows-Wheeler transform
  - suffix tries
- 15-251
  - Turing Machine Simulator and Karp Reductions

# Winter 2025
- 15-459: Undergraduate Quantum Computation

CMU traumatizes you into being *extremely bored* when you're at home because the CMU CS environment upregulates your stress so high, you don't know what to do when it comes back down.

I was somewhat interested in quantum computing, and I found that Prof. O'Donnell posted all his lectures online, so I watched *all* of them in 2-3 weeks and did all the homework problems. Some of the homework problems required some AI assistance since I hadn't taken 251, but after taking 241, most of the problems were doable on my own. Prof. O'Donnell gave me permission to upload my solutions to GitHub (as well as my code for the pbit and qubit simulators), so check them out if you're interested [[Link]](https://github.com/88Mangos/15-459-s).

# Fall 2024 (52 units)
- 15-122: Principles of Imperative Computation
- 15-151: Mathematical Foundations for Computer Science
- 21-241: Matrices and Linear Transformations
- 76-102: Advanced First Year Writing
- 07-128: SCS First-Year Immigration
- 07-131: Great Practical Ideas in Computer Science
- 99-101: Core @ CMU

Freshman fall was honestly deceptively chill. I had expected to get hit by a train and drop at least a B or two in my first semester, but to me, I was lulled into a false sense of security (foreshadowing...)

That being said, I wouldn't say any of these courses were particularly *easy*. 15-122 was the first time I'd programmed in C, and the piloting of the now notorious weekly Checkins ensured that I could never really rest - if you slacked off after the programming was due, then the checkin was the day after. Slack off after the checkin, and the PP is due. Slack off after the PP is submitted, and the programming is due right after.

With Concepts (15-151), I got to be part of the GPTutor pilot during the second half of the semester. It was great for helping me simplify and formalize my proofs - I ended up getting 100s on most of my homeworks in the second of the semester, and part of that was definitely beacuse GPTutor pointed out the places where I was being too verbose or proving implications in the wrong direction.

Linear algebra (21-241) was good because it felt the most familiar - though I did not take linear algebra in high school, the format of the class made it less stressful than Concepts or 122. One weekly homework and occasional midterms provided an easy schedule to plan around. 

Advanced First Year Writing was also super fun, as Profetzel's topic of "The Good Life" and "Wonder" really made me slow down and look around at CMU. With the stress of classes and learning so many new things, it was good to be reminded to take it all in and chill out. 

## Projects I enjoyed
- 15-122:
  - C0 Virtual Machine (C0VM)
  - Huffman Encoding
  - Editor
- 21-241:
  - PageRank analysis project, implemented in Julia

It was fun to make a working text editor, even if I only did the buffer parts and not the UI. The PageRank project was fun to do with Joe, *who will be a recurring character.* 

And as an ending note, taking 07-131 was super helpful - getting a nice LaTeX template and a low-stakes formal introduction to Vim/Git helped me set up a lot of workflows that I still use, e.g.,
- local LaTeX via LaTeX Workshop extension in VSCode and MacTeX
- local git repos for all my homeworks, which serve as checkpoints (and also ways to prove my innocence if, god forbid, I get accused of an AIV)
- LaTeX macros
- using Vim for small tasks (e.g., Git commits)

# Summer 2024 (1 unit)
- 15-051: Discrete Math Primer

This is the summer leading up to freshman year, but I wanted to note this course. Several students I talked to felt like it was kind of review of material they knew, *I suspect because they did a lot more math and coding in HS*. I had no clue when injections/surjections/bijections were, and I also had very rudimentary introductions to set theory - *as in, I knew that curly braces meant something was a set.*

I completed this course while vacationing in Japan and China and honestly, I think it was extremely useful before taking Concepts (15-151). 

So begins a common motif in my opinions of CMU courses, which is that the CMU faculty who design the curriculum are much smarter than I am, and therefore I would be wise to follow the path they've set. 

## Projects I enjoyed
I made these for funsies:
- Cube Puzzle Blender Animation, because I had just taken AP 3-D Art [[Link]](https://github.com/88Mangos/Cube-Puzzle)
- Logic Parser because I was worried I had to sharpen up my coding skills [[Link]](https://github.com/88Mangos/Logic-Parser)