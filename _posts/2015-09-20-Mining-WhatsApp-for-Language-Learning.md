---
title: Mining WhatsApp for Language Learning
---

I recently moved to Indonesia and am slowly learning the local language, Bahasa Indonesia. I've been learning a bit from a tutor, but when I try to use the sentences and words in conversation, my local friends tell me that the style I'm using is too formal and not how people naturally talk. I also noticed a lot of slang/informal words in Bahasa-speaking WhatsApp groups I've been added to.

As a fan of the Pareto principle, I thought that maybe if I could learn the 20% of words that make up 80%-ish of the conversation, perhaps my overall comprehension could improve a bit faster. Since my immediate use case was understanding the thousands of messages being exchanged in the Open Data Club WhatsApp group, I figured that would be a good corpus to use for a word frequency analysis. Here's how I did it.

1. In WhatsApp on your phone, go into a group chat and press the menu button. Tap More > Email chat > Without Media, and email the chat to yourself.

1. Download the .txt file to your computer. In my case, this was "WhatsApp Chat with Open Data Club.txt". I renamed it to WhatsApp.txt for simplicity.

1. Save [this little Python script](/files/wordcount.py) I threw together to the same folder that your WhatsApp text file is in. This filters out the metadata (names, phone numbers, dates), counts all the words, and saves them to a CSV.

1. Open up a terminal in that folder and type `python wordcount.py WhatsApp.txt`, where WhatsApp.txt is the name of the text file with the conversation. Within a few seconds, you should see 'output.csv' created in that same folder. That's your list! By default, this exports a CSV with the count of all words. If you want to limit to the top 100 words, you can do that by `python wordcount.py WhatsApp.txt 100`.

1. To bulk translate the words, I opened the csv in Google Docs and added a 'Translation' column that uses the =GOOGLETRANSLATE formula to bulk translate every word. This is maybe only about 95% accurate, but it's a great start to review with a native speaker.

If anyone has suggestions for improving the code/process, please [submit a pull request](https://github.com/jcontini/jcontini.github.io/pulls) or let me know in the comments! 

![Translating words in Google Sheets](/images/posts/translate.gif)

Shout out to my friend and former colleage [@_couper](https://twitter.com/_couper) for convincing me to write this post. I've been meaning to get blogging for awhile and this seems like a good start!