---
title: "Learning Zig via Ziglings"
description: "Learning a cool programming language"
date: 2026-05-08
updated: 2026-05-09
status: completed (115 exercises)
ShowToc: true
TocOpen: true  # Optional: Keep it open by default
---

I've been curious about Zig for awhile, and I started learning via [Ziglings](https://codeberg.org/ziglings/exercises/#ziglings). To be honest, after taking 312 and 411 (and programming in C many times for other classes) I really like Zig so far. I'll write down tips for myself as well as curiosities and criticisms from the lens of taking 312 with Bob Harper. *I am by no means a PL expert I just have opinions.*

# Things I like about Zig 

## It's `Go`-esque
It's got the nice `defer` behavior from Golang, extended with `errdefer`, and it's better than `Go` because it gets rid of stupid `null` - but not really, instead making the `NONE` for the optional type have value `null`. Which is chill, though I prefer SML's `NONE` or OCaml's `None`.

## Sum Types 
I also really like the tagged unions (i.e., sum types). Exercise `57_unions3` was nice to see, though I did have a gripe.

## OOP-ish?
I think it's cool that structs can have associated methods and basically act as objects. Though I don't think they're technically OOP.

### Google AI Search Summary, "are zig structs technically objects":


*Yes, Zig structs are technically data-oriented objects because they are composite types that hold named data fields and can contain methods, behaving as namespaces, data containers, or "classes". However, they differ from conventional Object-Oriented (OO) objects because they are value types, not reference types, and do not inherently include inheritance or polymorphism.*

**Key Characteristics of Zig Structs**

*Data + Methods: Structs can contain fields (data) and functions (methods).*

*Instantiation: Similar to objects in OO languages, a struct is instantiated to be used (e.g., var my_obj = MyStruct{};).*

*File-level Structs: Every @imported Zig file is implicitly a struct, allowing you to treat files as objects/namespaces.Value Types: Structs are generally copied by value, not by reference, which is distinct from many OOP languages where objects are manipulated via pointers.*

*No Implicit Runtime: They do not have built-in garbage collection, runtime polymorhpism, or inheritance, making them more similar to C structs with added methods.*

*In summary, they are "objects" in the sense that they act as containers for data and behavior, but they are not "objects" in the context of traditional class-based, runtime-heavy OOP.*

## Testing inside the file
Comptime was cool, but as someone who had to write the PowerLab autograder in SML, this in-file testing framework seems absolutely amazing. No need for a `Tests` module to be imported, which is a functor that takes in the student's submission for the module for the associated lab - everything is now in one place. 

Thus far, given my 411 and 312 experience, it seems like: 
1. it would be very intuitive to write a compiler for Zig, as the explicit blocks as expressions and other rules seem very neat (hence why they have a grammar specification that is only 580 lines long)
2. the creator (using the benefit of hindsight) has axed all the stupidity of existing languages (null pointers and the like)
3. been very intentional about the design choices. So far I have very few gripes (*granted, I am by no means a reputable authority on programming language ergonomics*) and that's surprising to me considering I've almost always had a complaint about a language I've used.

# Gripes I have 

## Where is `make clean` equivalent?
Often in Makefiles, you'll define a `make clean`. Zig's build system seems great thus far (tbh Ziglings may not be the best place to really see it shine), but I feel like there's got to be a way to clear cached Zig builds. Granted, I only ran into this while doing `046_optionals2` when I wanted to comment/uncomment the line that leads to a null dereference, and the actual issue was that Ziglings uses a .txt file to track the last exercise you completed (probably to avoid re-running the ones you've done). But still I feel like there should be a `make clean` equivalent for
```sh
rm -rf zig-cache zig-out
# Why can't we just have 
#   zig build clean 
# be a shortcut for this?
```

## `void` is actually `unit`
Why is the `void` type actually `unit` (from SML)? It's a zero-bit type with one value, which is `{}`. Are we serious. It's not truly `void`, it's `unit`. But this is a small gripe tbh.

*Technically the void type in Zig does not follow the 15-312 type-theoretic void type, which has no values (nullary case). The void type in Zig is in fact, the unit type, and thus has one value `{}`.*

### Google AI Search Summary, "are zig void values units?":

*Yes, in Zig, void values are considered units.*

*Zero-Bit Type: The void type is a zero-bit type, meaning it requires zero bytes of memory to store.*

*One Possible Value: Despite having no size, it has exactly one possible value: {}.*

*Canonical Form: The value is represented by the literal {}, which is the canonical form and recommended over other syntax.*

*While void indicates the absence of useful information (like a return value), in Zig’s type system, it is still a type with a valid, single value (a unit type), rather than being truly "nothing".*

## Why can't I inline explicate enums for tagged unions?
Why can't I do this?
```zig
const Insect = union(enum { flowers_visited, still_alive }) {
    flowers_visited: u16,
    still_alive: bool,
};
```

For now, you either have to independently declare the enum
```zig
const InsectStat = enum { flowers_visited, still_alive };

const Insect = union(InsectStat) {
    flowers_visited: u16,
    still_alive: bool,
};
```

Or have the enum be inferred 

```zig
const Insect = union(enum) {
    flowers_visited: u16,
    still_alive: bool,
};
```