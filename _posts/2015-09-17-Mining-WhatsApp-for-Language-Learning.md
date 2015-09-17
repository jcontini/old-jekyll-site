---
title: Mining WhatsApp for Language Learning
---

I recently moved to Indonesia and am slowly learning the local language, Bahasa Indonesia. I've been learning a bit from a tutor, but when I try to use the sentiences and words in conversation, my local friends tell me that the style I'm using is too formal and folks don't really talk that way in everyday language. At the same time, I realised that I mostly had no clue what was being said in the Bahasa-speaking WhatsApp groups that I've been added to.

As a fan of the pareto principle, I thought that maybe if I could learn the 20% of words that should make up about 80% of the conversation, perhaps my overall comprehension could improve a bit faster. Since my immediate use case was understanding the thousands of messages being exchanged in the Open Data Club group, I figured that would be a good corpus to use for a word frequency analysis. Here's how I did it. 

1. In WhatsApp on your phone, go into a group chat and press the menu button. Tap More > Email chat > Without Media, and email the chat to yourself.

1. Download the .txt file to your computer. In my case, this was "WhatsApp Chat with Open Data Club.txt"

1. Now we want to get rid of the dates/times/names/numbers at the beginning of each line. Open the txt file in Sublime Text, and do a regex find & replace for `(?<=\n).*?(?=: ):` to delete everything but the actual conversation content.

1. I wrote a little [Python script](/files/wordcount.py) to count all words in a text file and save the results to a CSV with the word counts. Save that to the same folder that your Whatsapp text file is in. (I used an [online word counter](http://wordcounttools.com/) before, but my WhatsApp conversation history got too large for that.)

Shout out to my friend and former colleage [@_couper](https://twitter.com/_couper) for convincing me to write this post. I've been meaning to get blogging for awhile and this seems like a good start!