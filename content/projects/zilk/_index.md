---
title: "Zilk"
description: "Another Project IDea"
date: 2026-05-12
ShowToc: true
TocOpen: true  # Optional: Keep it open by default
---
After sadly shelving `jstarb`, I leaned a little more into 210 material (I also recently watched [danderson's talk on lazy ranges at CppCon 2025](https://www.youtube.com/watch?v=gLOH5md4gok)) and I thought it might be cool to implement these things in Zig. I was really surprised to see zig had a native `@reduce` built-in... so I figure they care about parallel execution somewhat. Though the builtin reduce is for SIMD instructions (instruction-level parallelism), not thread-level parallelism.
