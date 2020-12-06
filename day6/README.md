# Day 6: Custom Customs

## Part One

As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration forms are
distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked `a` through `z`. All you need to do is identify the questions
for which anyone in your group answers "yes".
Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help.
For each of the people in their group, you write down the questions for which they answer "yes", one per line.
For example:
```text
abcx
abcy
abcz
```
In this group, there are 6 questions to which anyone answered "yes": `a`, `b`, `c`, `x`, `y`, and `z`.
(Duplicate answers to the same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the plane
([your puzzle input](data.txt)).
Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line.
For example:
```text
abc

a
b
c

ab
ac

a
a
a
a

b
```

This list represents answers from five groups:

1. The first group contains one person who answered "yes" to `3` questions: `a`, `b`, and `c`.
1. The second group contains three people; combined, they answered "yes" to `3` questions: `a`, `b`, and `c`.
1. The third group contains two people; combined, they answered "yes" to `3` questions: `a`, `b`, and `c`.
1. The fourth group contains four people; combined, they answered "yes" to only `1` question, `a`.
1. The last group contains one person who answered "yes" to only `1` question, `b`.
1. In this example, the sum of these counts is `3 + 3 + 3 + 1 + 1 = 11`.

For each group, count the number of questions to which anyone answered "yes".
***What is the sum of those counts?***

Your puzzle answer was `6297`.

<span style="color:yellow">The first half of this puzzle is complete! It provides one gold star: *</span>

## Part Two
As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which
everyone answered "yes"!

Using the same example as above:
```text
abc

a
b
c

ab
ac

a
a
a
a

b
```
This list represents answers from five groups:

1. In the first group, everyone (all one person) answered "yes" to `3` questions: `a`, `b`, and `c`.
1. In the second group, there is no question to which everyone answered "yes".
1. In the third group, everyone answered yes to only `1` question, `a`. Since some people did not answer "yes" to `b` or
   `c`, they don't count.
1. In the fourth group, everyone answered yes to only `1` question, `a`.
1. In the fifth group, everyone (all 1 person) answered "yes" to `1` question, `b`.
1. In this example, the sum of these counts is `3 + 0 + 1 + 1 + 1 = 6`.

For each group, count the number of questions to which everyone answered "yes".
***What is the sum of those counts?***

`3158`

That's the right answer! You are <span style="color:yellow">one gold star</span> closer to saving your vacation.