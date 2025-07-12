---
title: "Type Safe Generic Data Structures in C" 
date: 2025-07-12
author: ["Tyler Yang, Daniel Hooper"]
description: "Article posted to YCombinator News that I found interesting" 
summary: "Writing generic data structures in C while maintaining type safety." 
cover:
    image: "thumbnail.png"
    alt: "Type Safe Generic Data Structure in C"
    relative: true
editPost:
    URL: "https://danielchasehooper.com/posts/typechecked-generic-c-data-structures/"
    Text: "Original Post"
---

##### Preamble
Over this summer, I had my new advisor for sophomore year and beyond assigned to me. Shout out to Richard Pattis for pointing out that
```
"If an incoming freshman reads 5 articles per day, they will have read almost 7,500 articles by the time they graduate."
```

I am not an incoming freshman, but I will read some interesting articles and jot down my thoughts. This is hopefully the first of many blog posts that serve as personal notes for me.

---

#### Level 1: void* (15-122)
[15-122, void* Lecture Notes](https://www.cs.cmu.edu/~15122/handouts/slides/review/12-voidstar.pdf)

In 122, we learned how to use `void*` and general `key_compare` functions to implement generic hash dictionaries. Stuff like `entry_key` returned abstract `key` datatypes from `entry` datatypes, and these were made to be fully general.

I quite liked this part of 15-122 (I think the check-in on hash dictionaries was the only time I aced a checkin, despite Iliano calling me silly while I was taking it...), but Daniel Hooper makes some interesting counterarguments as to what CMU's intro CS course teaches

1. it's not type safe. In Level 3, Daniel Hopper solves this issue by using macros to enforce type safety.
    ```C
    #define List(type) union { \
        ListNode *head; \
        type *payload; \
    }

    List(Foo) foo_list = {0};
    List(int) int_list = {0};
    ``` 
    Then used macros that wrap around the `list_prepend` and `list_alloc_front` functions. The ternary code didn't make sense to me at first, so I think his "old technique" was more intuitive:
    ```C
    // from original article
    // Note: I added a leading underscore to the 
    // function name since only the macro should call it
    void _list_prepend(ListNode **head, 
                    void *data, 
                    size_t data_size);
    #define list_prepend(list, item) \
    /* cast function type */ \
    ((void (*)(ListNode **, \
               __typeof__((list)->payload), \ 
               /* ^^ tyler's comment: 
                * get type of payload field 
                * which can then be used in the union
                * type to enforce the safety of 
                * type *payload.
                */
               size_t))_list_prepend)  \
               /* call function */ \
               (&((list)->head), item, sizeof(*(list)->payload)) 
    ```
    This is a bit unholy, but basically the macro lets the function get the type of the payload for the input list (the node you are prepending to), and when you call `_list_prepend`, the compiler will check that the data you seek to add for the new prepended node (i.e., `item`) has the same type.
    ```C
    // from original article
    // Note: leading underscore add to the 
    // function name since only the macro should call it
    void _list_prepend(ListNode **head, 
                    void *data, 
                    size_t data_size);

    #define list_prepend(list, item) \
        _list_prepend(&((list)->head), \
                      (1 ? (item) : (list)->payload), \
                      /* ^^ tyler's comment:
                       * ternary statements must have
                       * same type in both branches
                       * (like 15-150's SML case and
                       * pattern-matching) so this part
                       * of the macro enforces type checking.
                       */
                      sizeof(*(list)->payload)) 
                  
    List(Foo) *foo_list = NULL;
    Bar bar = {5, 6};
    list_prepend(&foo_list, &bar); // error!
    ```
    Another thing that reminded me of 15-150 was this code below, which uses a `front` that reminded me of lazy evaluation
    ```C
    // from original article
    #define list_alloc_front(list) \
        (__typeof__((list)->payload))_list_alloc_front(&(list)->head, sizeof(*(list)->payload))
        
    void *_list_alloc_front(ListNode **head) {...}
    ```
    Uses that same `__typeof__` trick from the first method. Neat!

#### Back to the drawbacks of `void*`...

2. having the linked list's `node` allocation and `data` allocation is redundant (in that we have to allocate twice instead of just once)
3. the data pointer uses an unnecessary amount of memory (8 bytes for a pointer). 
4. while traversing the list, there will be a compulsory/cold miss in the cache (getting the next node and getting the data). I recently learned what cache misses were in 18-213, so hopefully the example traversal below makes sense:
  ```C
  /* v copied from original article v */
  typedef struct ListNode ListNode;
  struct ListNode {
      ListNode *next;
      void *data;
  };

  void list_prepend(ListNode **head, void *data) {
    ListNode *node = malloc(sizeof(*node));
      node->data = data; 
      node->next = *head;
      *head = node;
    }
  /* ^ copied from original article ^ */

  // initialize some data
  int *number = malloc(sizeof(int));
  *number = 8;

  ListNode *head = NULL;
  list_prepend(&head, (void *)number); 
  // now head is a length 1 singly-linked-list

  // make og a reference to head
  ListNode *og = head; 
  
  // now head points somewhere else, 
  // og still points to old head
  list_prepend(&head, (void *)number); 
  // now we have a length 2 singly-linked list

  /* Heap view, very abstract and randomly chosen addresses
   * We will ignore alignment specifics
   * ASSUME 1 line is 8 bytes (so addr goes up by 8 each line)
   *  .
   *  .
   *  addr | value | 
   *  -----|-------|
   *  0x00 |       |
   *  0x08 | 0xf0  | <- og points here, og->next = NULL
   *  0x10 | 0xe0  | <- og->data == number
   *  0x18 |       |
   *  0x20 |       |
   *  0x28 |       |
   *  0x30 |       |
   *  .
   *  .
   *  .
   *  0xe0 | 0x8   | <- number == 0xe0, *number == 8
   *  0xe8 |       |
   *  0xf0 | 0x08  | <- head points here, head->next == og (0x8)
   *  0xf8 | 0xe0  | <- head->data == number
   */
  
  ListNode *curr = head;
  while (curr->next != NULL) {
    // compulsory cache miss,
    // need to load curr == head == 0xf0 into cache,
    // then access the next field

    // second compulsory cache miss, 
    // need to load curr->data = 0xe0
    int value = *((int *)curr->data);
    curr = curr->next; 

    // caveat: if 0xf0 and 0xe0 were in the same cache line,
    // there would only be one compulsory miss. 
  }
  ```
---

#### Level 2: Flexbile Array Member (18-213)
In 18-213's malloclab, the block struct uses a zero-length array. The initial comment mentions how
```
"The similar standard-C feature of "flexible array members" won't work here because those are not allowed to be members of a union"
```
because we needed to union our block payloads with a different type to support explicit free lists. That's where I first heard about flexible array members.

Daniel Hopper explains how this method of using flexible array members, i.e. `char data[]`, keeps the `data` allocation with the `ListNode` allocation. Just allocate the size of the next pointer, then manually add the desired size to the argument for `malloc`.

This is safer and avoids the cache miss issue that `void*` had, but unfortunately, we now have to pass the desired allocation size to `list_prepend`, so the code is a bit more verbose.

---

#### My Conclusions
This blog post from Daniel Hopper is quite clever, and could definitely prove useful for implementing anything that involves generic data structures in C. Though I enjoy using Python due to its extreme freedom (any variable can be whatever type I want, so willy-nilly), I enjoy the type safety from languages like C. 

I have been writing 15-122/18-213-style contracts in my Python code for my machine learning research, and I think it would be quite nice if I could work in a language that has the flexibility/genericity of Python but the safety of C. So this type of code could be a step in that direction!

--- 

Closing Note: I consulted Claude to make sure my analysis of the type checking macros made sense, as well as to check for typos in my cache miss example code.