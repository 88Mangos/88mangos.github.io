---
title: "PyStubs"
description: "Python Libraries Dummy Placeholders for Local Development"
date: 2026-04-06
updated: 2026-05-08
status: shelved
ShowToc: true
TocOpen: true  # Optional: Keep it open by default
---
<!-- 2026/04/06 12:19 AM -->

[Similar Project?](https://github.com/ModOrganizer2/pystubs-generation)

Rust/C++ Project: parsing python files and writing the .pyi placeholders with good documentation, can hook into local LLMs to generate good docstrings, but essentially you just parse for every namespace Tx.cuda.blahblahblah and make the appropriate files. Very simple agentic thing surely, also verifiable. Inspired by setting up the typings folder for mlsys assignment tirx gemm

In essence, I was developing my CUDA kernels locally on my mac (and thus couldn't install the actual libraries that required CUDA), and this might be a common workflow for ML development - so some sort of agentic pipeline that scrapes the PyPI distribution for the CUDA-reliant packages, and creates stubs using .pyi files and mirrors the same directory structure as the real package. That way it's somewhat easy to debug locally, and typechecking + linters (Ruff) don't get super angry at you. 

Just in general better for developer experience.