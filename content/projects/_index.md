---
title: "Projects"
description: "Extracurricular Fun"
ShowToc: true
TocOpen: true  # Optional: Keep it open by default
---
I've done a bunch of miscellaneous projects in recent years. I was definitely more enthusiastic for some projects compared to others, but all of them taught me some useful lesson.

# TA'ing
- 15-210: PowerLab SML autograder. *Private to 15-210.*
- 21-259: [recitation worksheets](https://github.com/88Mangos/15-459-s)


# Hackathons
They're fun, if only to meet cool people and see interesting projects get prototyped very quickly. 

## as a participant
- [MuFFLe](https://github.com/collaborativebioinformatics/MuFFLe) at NVIDIA x CMU 2026 Federated Learning Hackathon, Most Collaborative Award
- MolSnap, St. Jude Knowledge in Data Science (KIDS) 2025 Hackathon, Most Technical Project. 
*Private to St. Jude Children's Research Hospital.*
- [MyWriter](https://github.com/C4fune/Sturgeon-Pro-Shops-Tartan-Hacks), TartanHacks 2025.
- [MSDS Summarizer](https://github.com/88Mangos/NOVA24), NOVA 2024.
- [CMU Study Group Finder](https://github.com/SwiftCoderJoe/HackCMU24), HackCMU 2024.

## as an organizer
- [AWAP26 Matchmaking Server](https://github.com/acm-cmu/awap-matchmaking-2026). 
*Private to ACM@CMU.*
- HackCMU 2025 Judge
- [CMU x IDQuantique Innovation Track](https://github.com/88Mangos/CMU-x-IDQuantique-Challenge), Future Leaders in Quantum (FLiQ) 2025. 

# Courses and Research
A summary of course final projects and research. Notably, I've omitted projects that are just part of the course.

- 15-442 Course Project: [Mangrove](https://github.com/88Mangos/mangrove), a memory-aware scheduler for optimizing DAG execution on constrained hardware.
- MolSnap Toolbox: extending MolSnap with automated literature review agents. 
*Private to St. Jude Children's Research Hospital.*
- 11-785 Course Project: [Open-Ended Self-Edits](https://github.com/cheongalc/open-ended-self-edits), experiments in self-improving LLMs via self-edits on training data
- 99-270: Summer research, synthetic data generation of chemical reaction diagrams
- 02-181 Course Project: Modifying DADA2
- 21-241 Course Project: PageRank vs. HITS Analysis

# Ideas and WIP

As I work on course projects and general software things, I think developer tools are nice projects that seem small but really increase the quality of life. I'm glad that Ron Minsky agrees (*c.f., 411 S26 guest lecture*). 

## Auto-Formatters are Great
I think some of my most enjoyable programming experiences were using Go for the first time for AWAP 26 server development - Go's very opiniated auto-formatter (which also alphabetizes your imports!!) was just great for reducing my cognitive burden.

I will say that the OCaml Jane Street profile for autoformatting was considerably more annoying, as it had this habit of squashing any unnecessary line breaks. So while I like Jane Street OCaml's heavy usage of named arguments (`~f` and `~init` for list folds for example), I really felt like writing the 411 compiler was reading just a ginormous wall of OCaml text. It doesn't help either that OCaml forces repeated `let...in...` unlike SML which has let-binding blocks `let...in...end`. Multiple declarations in a let get annoying because then it becomes like a tuple declaration, and that's annoying as hell to extend because if you have like 10 of those, you have to make sure you match up where you want to add a new declaration. And if declarations depend on each other it's even more annoying.

## Contracts are Frustrating
Another frustrating experience was writing Python contracts while I was doing my AP Research project. In general Python and ML-related libraries (PyTorch, NumPy) are so annoying because of the broadcasting rules and shape mismatches. Just way too much cognitive overhead to write some code.

## People can't name things
Write own programming language that is just the semantically meaningful counterpart of parallel CPP. For example, `transform` becomes `map`, and C++ `map` becomes `dictionary` as it should have always been. `option` should exist as a type - SML did good there.

## Other cool aspirational goals
- Contribute to LLVM somehow?
- Rewrite 411 compiler, but in C++20, 23, or 26 so I can use concepts and shit 

Anyways, onto my ideas.

# WIP

## Shelved Projects
- `Jstarb`, a job tracker in Zig. I threw in the towel because I would essentially just be replicating my Google Sheet, but much worse... and there aren't any fun systems programming things since the whole thing was going to run locally as a single-threaded application. 
- `tpp`, solely because I wanted to try out Zig instead of dealing with C++.
