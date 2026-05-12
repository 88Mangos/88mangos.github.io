---
title: "Throwing in the Towel"
description: "Ran into a very familiar wall"
date: 2026-05-12
ShowToc: true
TocOpen: true  # Optional: Keep it open by default
---

After trying to wrestle with the requirements, I realize that my spreadsheet already does what it needs. Furthermore, so far it's felt like a whole headache trying to write out the types - there's not much fun systems things to do once that's all figured out. The application itself would be single-threaded, so there's no need for Zig's concurrency features, and it feels like it would take forever to get to the rendering part and writing a Zig frontend. 

So with that, I'll sunset this project and not sink too much time into it. It did force me to think a lot, which is good, but I think the Google Sheet approach is (1) more familiar to me, and (2) the perfect amount of good enough for what I need.