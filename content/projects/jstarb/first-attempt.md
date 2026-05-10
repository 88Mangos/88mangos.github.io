---
title: "First Attempt"
description: "Running into a wall"
date: 2026-05-09
ShowToc: true
TocOpen: true  # Optional: Keep it open by default
---
After finishing the Ziglings tutorial today, I figured I'd get coding. I started by fleshing out my Event and Entry structs, and I had a general idea inspired by 210's STSeqs and blockchain ledgers. 

# Initial Struct Definitions for Entries and Events
We take inspiration from 15-210 SML Library's Single-Threaded Sequences (STSeq), which are views of a sequence derived from a history. A user should only use the "most-recent" version of an STSeq; doing otherwise violates the promised cost bounds, as that would require re-creating the most recent version from the history.

> Also technically lends from **event-based databases**. Entries contain a ledger which is just a list of events. Events have their own subvariants, but more importantly, Entries also store their own views, which are updated and materialized based on the ledger.

Similarly, the entire job tracker focuses on tracking an individual `Entry`, each containing a "ledger" of `Event`s. It is therefore possible to query everything we'd ever want to know about an `Entry` from the ledger, but we want to cache the information into a "view" for better cache locality and higher performance.

## Example Query 
To answer the question

> When did I apply to be a 15-210 TA?

The naive approach is is to find the entry for the 15-210 TA job opening, then iterate through the ledger in chronological order until we find the `Event` that says `Applied`. However, if we cache the `applied_at` time for each job opening, we needn't perform this search every time, and we also improve cache locality since it'll be stored in the struct, and not in some evil linked list. 

*Granted, this is a terrible example, because the `Event` of applying to a job opening is likely one of the first elements in the ledger, and therefore unlikely to take more than one or two linked-list pointer jumps. But we're not trying to be practical here are we? If we were, I'd just stick with my Google Sheet.*

## Future Ideas
For now, I'll store everything locally in a JSON-serialized format. But eventually (*after taking 15-445, Database Systems*) I'd like to try to write my own database engine in Zig. I think it'd be cool. So we'll see.

> **Interesting Idea for the Future:** custom Zig DB for Jstarb.

# [Future] Handling Location Data
The core issue with handling locations is that there are technically infinitely many. I mean let's be honest, most tech jobs are in NYC or SF. But it would be annoying to input that each time - what if I type in "NYC" one time, but then "New York City, NY" another time?

We could use fuzzy matching, but that seems a little stupid because these are fixed cities that are knowable, and a little overkill since any fuzziness comes from user error, not variability between different locations.

We could use tries to do some funny string algorithm things, but this is definitely not the first concern of mine - though it will serve as an interesting extension.

> **Interesting Idea for the Future:** fuzzy entry to autocompletion via weighted tries

# Defining the Features I Want

## What I Want

1. I track both job applications and resume buckets/event registrations related to my career search. Ideally I'd like entries to fall into one of these categories, with some extensibility in the future in case there's some other wacky way to do career events. For example, I might add coffee chats and then related notes to that chat.

2. For job applications, there are position titles, locations, fields (e.g., Finance, Big Tech, startup, etc.), potentially supplementary materials (which are currently nicely embedded as Google docs tiles in Google sheets), as well as a status field that can be anywhere from submitted -> OA -> OA done -> interviewing and more. Due to the various differences between different interview processes, that becomes a very difficult thing to specify.

I'd also like a date of when I found something (optional), when I applied to something, and if there are interviews/OAs, dates on which I did those. Ideally these auto-update, i.e., once I click something to mark them as completed, the completion date/time metadata is stored automatically. I might also want to store the link t the application for reference later, in case I want to send the link to a friend.

3. Like I said, I also need to be able to make my visualizations. Currently, I have table columns telling me which week (e.g., week 15) of what year each thing was applied to, as well as a relative date column that can then be used to compute whether something occurred in the past week or not.



Designing a SQL schema to do all of these things seems difficult. But writing my own database engine also seems difficult. 

## Workflows I Want
I'm also thinking about how I want to interface with this tool. Honestly I would've been perfectly fine with Notion if it didn't make me pay for charts, and I would've been fine with sheets if making charts were a little less tedious. I envision the following workflows:

1. I see a job posting I am interested in and should apply to later. I open up this tool and enter it in as a job application, put the link in, and flag it for later. Ideally the app has a docket telling me what I have TO-DO (which may also include reachouts or upcoming coffee chats)

2. I apply to a job. Then I can do the same thing as above except I also mark it as applied to and that default sets the state to submitted.

3. I receive an OA for a job. Then I can mark that down and set the state to OA pending completion.

4. I complete an OA for a job. Then I can mark that down and again step the state.

If there are several OAs, I'd want a nice way to track that. A producer/consumer pattern is weird because sometimes I might receive several OAs for one job, or one OA for several roles in the same company. Thinking of the data structure there is a bit annoying.

5. I receive an interview. Then I again mark that down and step the state to interviewing, and optinally mark down the scheduled time of the interview.

6. I complete an interview round. I mark that down. Again the state shouldn't be a pure DFA state machine - we need to have some memory of how many interviews we've seen thus far.

Plus interviews can be split into behavioral or technical or general. And I'd like to have a place to put my interview prep notes, which can be GDoc links for now.

7. If I haven't updated a job in 6 months, I can assume I was ghosted. If I get a rejection email, I can mark it as rejected. If I get an offer, I can mark it as such too. There are also instances where a job may seem to ghost me but then eventually reject me. In that case I can just update to rejected after the state was ghosted.

8. And of course there's the visualization workflows, which could be a nice dashboard but this is probably going to come last.

## Charts I want
Existing ones are
1. number of jobs applied to overall, sorted by accepted/rejected/ghosted, should exclude resume buckets and events

2. the number of applications in the past 7 days, which can then become the bigger line chart for the weekly number of applications since I began applying to jobs 

3. hopefully some number of stats for average number of interviews, time between interviews, length of job process time (with and without the places that ghost me), though these won't be able to be done retroactively, so these stats aren't super important.

# Hitting a wall, on [archive/actions-attempt-1](https://github.com/88Mangos/jstarb/releases/tag/archive%2Factions-attempt-1)

Unfortunately, my initial struct definitions had way too many layers of nested variant types. I initially tried to treat Zig development the same way I treated OCaml development for 411 - abuse algebraic data types and records to enforce correctness via the type system. 

But as I found out in 411 while writing `verifyCFG`, and now while writing Zig code, contracts may be the more idiomatic way to enforce correctness. Mangling the types through layers of nested unions and weird access patterns
1. destroys cache locality, hurting my goal of writing high performance code
2. is also just cumbersome as HELL to read. I mean look at this snippet from `src/back/data.zig`:
```zig
// data, with corresp. Entry fields to update, using 15210 as a placeholder time
    type: union(enum) {
        job_opening: enum {
            BeginTracking
            // Entry.job_opening.state.pending = LookingAt
            ,
            Applied
            // Entry.job_opening.state.submitted.{}
            ,
            OAReceived
            // Entry.job_opening.state.oa.status = Received
            // Entry.job_opening.state.oa.due = 15210
            // Entry.job_opening.state.oa.notes = "Pre-OA yap"
            ,
            OADone
            // Entry.job_opening.state.oa.status = Complete
            // Entry.job_opening.state.oa.notes = "Post-OA yap"
            ,
            InterviewReceived
            // Entry.job_opening.state.interview.people = [], add if known
            // Entry.job_opening.state.interview.location = null, add if known
            // Entry.job_opening.state.interview.scheduled = null, add if known
            // Entry.job_opening.state.interview.complete = false
            // Entry.job_opening.state.interview.notes = "Pre-interview yap"
            // Entry.job_opening.state.interview.type = Behavioral | Technical | General
            ,
            InterviewScheduled
            // Entry.job_opening.state.interview.people = [add people here]
            // Entry.job_opening.state.interview.location = "probably remote"
            // Entry.job_opening.state.interview.scheduled = 15210
            // Entry.job_opening.state.interview.notes = "More pre-interview yap"
            ,
            InterviewReScheduled,
            InterviewDone
            // Entry.job_opening.state.interview.complete = true
            // Entry.job_opening.state.interview.notes = "Post-interview yap"
            ,
            OfferReceived
            // Entry.job_opening.state.offer = Received
            ,
            OfferAccepted
            // Entry.job_opening.state.offer = Accepted
            ,
            OfferRejected
            // Entry.job_opening.state.offer = Rejected
            ,
            Rejected
            // Entry.job_opening.state.noOffer = Rejected
            ,
            Withdrawn
            // Entry.job_opening.state.pending = Withdrawn
            ,
        },
```
Holy stupid number of dots. This might be a greenting test (iykyk). 

After consulting my favorite brainstorming tool, Big G, I realized that flattening things out was both better for cache locality, and probably easier for me as a programmer to write.

# The Silver Lining
I was able to really specify the actions I wanted to take, translating the workflows from english to pseudocode. And now I have a much better idea of how I want to write the actions code. 