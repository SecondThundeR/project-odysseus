# secondthunder-js-bot

[![CodeFactor](https://www.codefactor.io/repository/github/secondthunder/secondthunder-js-bot/badge)](https://www.codefactor.io/repository/github/secondthunder/secondthunder-js-bot) [![DeepScan grade](https://deepscan.io/api/teams/11565/projects/14865/branches/286263/badge/grade.svg)](https://deepscan.io/dashboard#view=project&tid=11565&pid=14865&bid=286263)

This is repository of some random bot for Discord which was created just for fun and for some educational purposes *(Made with Discord.js library)*

## Just a moment of attention

This bot can add and remove words from a JSON array, however this implementation is missing from the main branch due to problems with these operations on Heroku. These additional functionality can be found [on this branch](https://github.com/SecondThundeR/secondthunder-js-bot/tree/add-delete-from-json), so you can choose what you need more from bot

## How to use this bot

### Local use

0. Install neccesary tools *(Node.js, Any IDE or Code Editor, etc.)*
1. Download or clone this repository
2. Create a Discord Bot on [Discord Developers](https://discord.com/developers/applications) page
3. Grab a token of your bot in 'Bot' section and place it in 'config.json'
4. Run `npm install` to install all libraries for bot
5. Run `npm start` to start a bot
6. After getting a log that bot was logged in, you are good to go

### Heroku use

0. Install neccesary tools *(Node.js, Heroku CLI, Any IDE or Code Editor, etc.)*
1. Download or clone this repository
2. Create a Discord Bot on [Discord Developers](https://discord.com/developers/applications) page
3. Grab a token of your bot in 'Bot' section and place it in 'config.json'
4. Create a dyno for your bot on [Heroku](https://dashboard.heroku.com/)
5. Get link of your app and edit a 'DYNO_URL' variable in main.js
6. Pull bot to Heroku and wait for build
7. After getting a log that bot was logged in, you are good to go

## Discussions

This project has a [Github Discussions](https://github.com/SecondThundeR/secondthunder-js-bot/discussions) turned on. Feel free to ask about this project or give new ideas and etc.

## Changelog

This project has a changelog, which you can find [here](https://github.com/SecondThundeR/secondthunder-js-bot/blob/master/Changelog.md)

Also you can track changes of new versions [here](https://github.com/SecondThundeR/secondthunder-js-bot/projects)

## License

This project is licensed under **MIT License**.

For the complete licensing terms, please read [LICENSE](https://github.com/SecondThundeR/secondthunder-js-bot/blob/master/LICENSE) file