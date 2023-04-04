# enviro_complaints 🌿
A bot that collects and notifies reporters about [new complaints](https://opendata.maryland.gov/Energy-and-Environment/Maryland-Department-of-the-Environment-MDE-Water-a/cnkn-n3pr) submitted to the Maryland Department of the Environment
## Progress
3/14/23 → created repository, added bot to Slack, added the chat:write and im:write scopes, and added slack api token as a codespaces secret
<br/>
3/19/23 → pushed bot code
<br/>
3/27/23 → updated bot code to fix errors, found another error in slack message code
<br/>
3/29/23 → discovered bot is very broken
<br/>
4/3/23 → pushed working bot code, working on implementing Github Actions
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
- [ ] Debug message format to find out why the first line doesn't appear and why it repeats nonstop
- [ ] Merge datasette.py with bot.py to update database with new complaints
- [ ] Add GitHub Actions workflow

Ideal Slack notification format ↓

New complaints:
<br/>
A complaint for Industrial was submitted on (2023-03-27)
<br/>
ID: 140699
<br/>
Incident date: 2023-03-27
<br/>
County: Frederick
<br/>
Status: Under Investigation
<br/>

A complaint for Possible Permit Violation was received on (2023-03-27)
<br/>
ID: 140697
<br/>
Incident date: 2023-03-20
<br/>
County: Baltimore
<br/>
Status: Referred to Outside Agency
