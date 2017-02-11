---
title: Mining WhatsApp for Language Learning
---

I recently moved to Indonesia and am slowly learning the local language, Bahasa Indonesia. I've been learning a bit from a tutor, but when I try to use the sentences and words in conversation, my local friends tell me that the style I'm using is too formal and not how people naturally talk. I also noticed a lot of slang/informal words in Bahasa-speaking WhatsApp groups I've been added to.

I thought that if I could learn the 20% of words that make up 80%-ish of the conversation, perhaps my overall comprehension could improve a bit faster. So I put together a python script to create a CSV export of most common words and explain how to use it here. If you're on a Mac, you already have Python. If you have Windows, you might need to [install Python](https://www.python.org/downloads/windows/) first.

1. In WhatsApp on your phone, go into a group chat and press the menu button. Tap More > Email chat > Without Media, and email the chat to yourself.

1. Download the .txt file to your computer. In my case, this was "WhatsApp Chat with Open Data Club.txt". I renamed it to WhatsApp.txt for simplicity.

1. Download [this Python script](https://raw.githubusercontent.com/jcontini/whatsapp-tools/master/wordcount.py) and save it in the same folder as your WhatsApp chat.

1. Open up a terminal in that folder and type `python wordcount.py WhatsApp.txt`, where WhatsApp.txt is the name of the text file with the conversation. Within a few seconds, you should see 'wa-word-count.csv' created in that same folder. That's your list!

1. To bulk translate the words, I opened the csv in Google Docs and added a 'Translation' column that uses the `=GOOGLETRANSLATE` formula to bulk translate every word. This is maybe only about 95% accurate, but it's a great start to review with a native speaker.

![Translating words in Google Sheets](/images/posts/translate.gif)

By default, this exports a CSV with the count of all words. If you want to limit to the top 100 words, you can do that by `python wordcount.py WhatsApp.txt 100`.

If anyone has suggestions for improving the code/process, please [submit a pull request](https://github.com/jcontini/whatsapp-tools/pulls) or let me know in the comments! 

Thanks to my friend and former colleague [@_couper](https://twitter.com/_couper) for the push to post this!