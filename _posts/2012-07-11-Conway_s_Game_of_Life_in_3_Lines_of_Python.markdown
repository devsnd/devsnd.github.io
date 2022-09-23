---
layout: post
title:  "Conway’s Game of Life in 3 Lines of Python"
date:   2012-07-11 16:06:57 +0000
categories: ['Programming', 'Python', 'Useless']
legacy_permalink: http://fomori.org/blog/?p=413
---


Conway’s Game of Life in 3 Lines of Python
==========================================

[![](/assets/2012-07-11-Conway_s_Game_of_Life_in_3_Lines_of_Python/200px-Game_of_life_block_with_border.svg_.png "200px-Game_of_life_block_with_border.svg")](/assets/2012-07-11-Conway_s_Game_of_Life_in_3_Lines_of_Python/200px-Game_of_life_block_with_border.svg_.png)I recently saw a video of an implementation of [Conway’s game of life written in APL](http://www.youtube.com/watch?v=a9xAKttWgP4) which was done in just one line. And because I couldn’t sleep last night, I implemented it in python as short as I possibly could.

So here it is:

```
def evolution(life,s=size,next=0):
    for j,i,nb in map(lambda j:(j,j+s+1,bin(life&((7|5<>((life>>i)&1))&1))<
```

There’s a little write-up and the source after the break.

It isn’t exactly readable nor pretty, but it works. Unfortunately there are several caveats I didn’t get around: The function expects a number as input *life*, whereas the binary representation of that number is a two dimensional array with 1 representing a live cell and 0 a dead cell. Also the function expects those numbers to be padded with zeros on the outside. The third problem is, that it currently only works for arrays of the size n².

So to create a game, one first has to find the number that represents the initial status and its size. Thats easy:

```
size = 5
life = int('''
00000
00100
00100
00100
00000'''.replace('n',''),2)
```

It seems to work reasonably well for small fields but I guess that the way python handles really large numbers is the reason for a sudden performance hit for a field with the size of around 20.

On the code:
============

I used a few tricks to reduce the number of lines, without calculating things multiple times. For example, I am using a bit mask to find out which neighbors are alive:

```
life&((7|5<
```

7 in binary is 111, 5 is 101 and 7 is again 111. I then shifted the bits so that the mask would align to the size of the field. Then I perform a bitwise logical-and with the mask shifted by *j* which is my array index. This gives me a number that has as many ones in binary representation as *j* has neighbors. So to count the neighbors I convert the number using to a binary representation and count how many times the character ’1′ is inside that string:  

*bin(5)* gives *’0b101′* which means 2 neighbors, so I count count them like this: *bin(7)[2:].count(’1′)*

You can have a [look at the source code and play around with it (game-of-life-3liner.zip)](http://fomori.org/blog/wp-content/uploads/2012/07/game-of-life-3liner.zip). There are two other figures inside the code to try out.

  

	