---
title: "Tpp"
description: "Tiny Cpp Build System"
date: 2026-05-07
updated: 2026-05-08
status: shelved
ShowToc: true
TocOpen: true  # Optional: Keep it open by default
---

Inspired by using OCaml's dune for 411, I really like the unqualified subdirs option. It means I can write code and structure directories in a way that is semantically meaningful to a human, but the compiler can just ignore it.

I also remember the immense pain of setting up C++ for Mangrove (15-442 project). Wouldn't it be nice to have a dune-esque simple build system for C++, just so we can start writing some code?

Basically, starting from an entrypoint `main.cpp`, just create a DAG by regex scanning for include headers and then checking for files that match that pattern (unfortunately C++ doesn't really have unqualified subdirs, so this doesn't quite hit the dune equivalence). 

Compilation would then just be traversing this dag and compiling things. But I don't think this project is super cool as it is, so it's shelved for now.