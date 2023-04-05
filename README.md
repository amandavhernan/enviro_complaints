# EnviroComplaints 🌿

EnviroComplaints is a Slack bot that collects and sends messages about [new complaints](https://opendata.maryland.gov/Energy-and-Environment/Maryland-Department-of-the-Environment-MDE-Water-a/cnkn-n3pr) submitted to the Maryland Department of the Environment.

## Final Submission

A memo of at least 300 words summarizing your process and progress in making this bot. Include any goals you weren't able to accomplish and why. I want you to pay special attention to what the output looks like, refining the text and other elements you surface. Some other questions to consider:

* Do I need to store this data somehow? What would that look like?
* If this bot were able to accept input from users, what would that look like and how might it respond?
* What's the best schedule for updates?

## Update | 3/19/23

I currently have a partially finished bot. After break, I want to experiment with the formatting of the bot's messages. I specifically want to make the messages more engaging and easier to read. I would also like to incorporate some kind of visual element into the bot's message. 
The main blocker I'm experiencing is that I'm not entirely confident that what I have will work properly and if it's the most efficient way to build my bot. My bot is currently set to run once a day. In addition to sending messages on Slack, my ideal bot would also update data on an accompanying site that displays analysis and graphics such as maps or charts. 

Some of my stretch goals include:
* Improve bot's message format 
* Learn how to incorporate images or graphics into bot's message
* Use GitHub Actions to build an updatable site 

## Update | 4/1/23

This week, I focused on debugging the errors I found in my code last week. The main issue I'm dealing with is that my bot repeatedly sends the most recent complaint on Slack. Looking at my to-do list, I plan to focus on debugging the message formatting errors next week. And during the final week, I plan to add code to bot.py to build an updatable datasette database, and automate my bot using GitHub Actions.

What I accomplished this week:
- [x] Fixed Slack message error
- [x] Fixed last update error
- [x] Successfully sent messages on Slack
- [x] Built a datasette database

What I have left to do:
- [ ] Format Slack notifications so every new complaint is contained in a single message
- [ ] Figure out why only the most recently added complaint was sent as a message on Slack
- [ ] Adjust message format, figure out why the first line doesn't appear
- [ ] Add GitHub Actions workflow
- [ ] Build updatable datasette database
