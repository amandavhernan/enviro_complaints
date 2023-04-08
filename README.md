# EnviroComplaints 🌿

EnviroComplaints is a Slack bot that collects and sends messages about [new complaints](https://opendata.maryland.gov/Energy-and-Environment/Maryland-Department-of-the-Environment-MDE-Water-a/cnkn-n3pr) submitted to the Maryland Department of the Environment.

## Final Submission

Throughout my time building this bot, there were a lot of ups and downs to say the least. Despite the challenges, I genuinely enjoyed building my bot and I learned a lot along the way. One of the first challenges I faced was converting the values in the dataset's "recieved_date" field into datetime objects. This conversion allowed me to compare dates to determine which complaints were new. Another challenge I encountered was formatting the bot's messages. At first, I was using a while loop, but this made my bot's messages inaccurate and redundant. I realized I should instead use a function, so my script wouldn't run indefinitely. I also experienced some trial and error with formatting the actual messages so the values would appear where I wanted them to. I decided to use emojis and bold text to add some character and make the messages easier to read. Another major challenge I encountered was setting up GitHub Actions. The first workflow file I wrote was missing a few elements, such as my Slack API token, my GitHub token, and dependencies. Toward the end, I was also missing code that would allow GitHub Actions to commit changes. I struggled a bit with cron expressions, so I used ChatGPT to generate one for me. I asked it to give me a cron statement for 9:30 a.m. EST. ChatGPT happily obliged and returned a codeblock with the expression, and explained what each number/character meant. Something I haven’t figured out how to implement yet is sending images or graphics over Slack. I would like to use Plotly to create a choropleth map of Maryland counties. This map, which would update as new complaints are added, would assign a color/shade to each county based on how many complaints have been reported there. The bot would send this map in addition to its list of new complaints. I plan to dedicate time next week to explore this potential feature further.

* Do I need to store this data somehow? What would that look like?

My script is set up to save the data retrieved from the API as a CSV. This CSV is updated when the script runs if new complaints are found.

* If this bot were able to accept input from users, what would that look like and how might it respond?

If I redesigned this bot to accept input from users, I would design it so users can search the list of new complaints by county. For example, I might want to know if any of the new complaints found were reported in Prince George's County. The bot would take a search term, such as "Prince George's" or "Prince George's County," and return any complaints where the "county" field matched. This search feature could also be implemented before the list of new complaints is generated, so the list only contains complaints that match the user's input. Another idea I have is to redesign this bot to allow users to ask questions about the data. Someone might want to know which county has had the most reported complaints or what type of complaint is the most common. The bot would answer these questions by summarizing the data and returning the output to the user.

* What's the best schedule for updates?

Since the dataset is updated once a day, it makes the most sense to check for complaints everyday rather than on a weekly basis. I also noticed that the dataset is updated early in the day, which is why I set my bot to run at 9:30 a.m. everyday. I also made the decision to run it earlier in the day rather than later because if this bot was used in a newsroom setting, getting this update early would allow more time for additional reporting. 

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
