---
title: "Second Attempt"
description: "Running into a wall, again"
date: 2026-05-11
ShowToc: true
TocOpen: true  # Optional: Keep it open by default
---
I tried to make another rewrite, and I made it farther this time. But the issue I ran into was when writing updates: it is extremely cumbersome to handle updates, and figure out how the ledger should work.

More specifically, I got stuck when trying to implement logic to reschedule an interview. Rescheduling an interview means overwriting the existing data - which is fine, but this means our data is ephemeral, i.e., I'll never be able to query the old times again, which may not be useful in the case of an interview, but might be useful in general (e.g., in case I reneg an offer). So that led me to write an `Item` struct, so `Entry` contains `Item` and an `Update` may sometimes be linked to an `Item`. This is way too many layers of nesting, and additionally, since an `Item` can be modified, then we'd need to maintain ledgers for the `Item`, leading to lots of nesting of arrays.

That's not very performant. So I turned to the ol' pal Gemini [[Link]](https://gemini.google.com/share/611c501eb056) and it ended up telling me to treat my data as a relational database... which sucks because I was hoping to avoid watching the 15-445 lectures before doing this project. Oh well. So I'll begin watching the DB systems videos I guess. 