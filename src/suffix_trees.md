# Suffix Trees

A *suffix* is a non-empty substring at the end of a string of charaters.

For example, for the word `HORSE`, it has the following suffixes:
* E
* SE
* RSE
* ORSE
* HORSE  (yes it includes the full string)

A *suffix array* is an array which contains the sorted indices of all suffixes
for a word.

For example, the suffix array for the word `CAMEL` is:
```
suffixes = [camel, amel, mel, el, l]
sorted = [amel, camel, el, l, mel]
original_indexes = suffix_array = [1, 0, 3, 4, 2]
```

The suffix array provides a space efficient alternative to a *suffix tree*,
which itself is a compressed version of a *trie*.

Suffix arrays can do everything suffix trees can, with some additional
information such as a Longest Common Prefix (LCP) array.

### Longest Common Prefix Array

A *longest common prefix array* is an array where each index stores how many
characters two sorted suffixes have in common with each other.

For example, take ths string:  `ABABBAB`

| Sorted Index | LCP Value | Suffix |
|:--:|:--:|:--:|
| 5 | 0 | AB |
| 0 | 2 | ABABBAB |
| 2 | 2 | ABBAB |
| 6 | 0 | B |
| 4 | 1 | BAB |
| 1 | 3 | BABBAB |
| 3 | 1 | BBAB |

The LCP value compares the suffix with the one immediately preceding it.  For
example, BABBAB is compared against the one before, BAB, and it shares the
first three characters with it, therefore it has an LCP value of 3.

### Finding Unique Substrings

The problem of finding/counting all the unique substrings of a string is a
commonplace problem in computer science.

The naive algorithm generates all substrings and places them in a set resulting
in a \\(O(N^2)\\) algorithm.

A better approach is to use the LCP array.  This provides a quick and space
efficient solution.

The best approach is to use the "Rabin-Karp algorithm with bloom filters" (sp),
which is not discussed here.

The number of unique substrings is:

\\(\dfrac{n (n + 1)}{2} - \sum _ {i=1}^{n} LCP[i]\\)

### Finding the longest common substring

Suppose the question is something like:  Given s1, s2, s3, s4 and some k value,
find the length of the longest common substring between any combination of k
strings of them.

1. Concatenate all strings using unique sentinel values that are
   lexicographically less than the letters of each string.  Such as #, $, %, &
2. Build the suffix array and LCP array.  This can be done in linear time.
3. Use a sliding window technique against the LCP to find windows where k
   different strings are represented.  The minimum LCP within the window is the
   current LCS.  Important note: You skip the value of the first LCP element in
   the window.
4. Greedily scan the LCP array and update some LCS variable.

### Longest repeated substring

The longest repeated substring is yet another problem in computer science we
can solve efficiently using hte information stored in the LCP array.

Brute force method requires \\(O(N^2)\\) time and lots of space.  Using the
information inside the LCP array saves you time and space.

Basically we just need to construct the LCP and take the largest LCP value.
