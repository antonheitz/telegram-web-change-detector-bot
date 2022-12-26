# Telegram Bot for detecting webstite changes

This bot lets you check for updates on static websites. Just message him the webpage to watch and he will notify you when a change gets detected!

## Content

1. [Setup](#setup)
2. [Bot interactions](#interaction-with-the-bot)

## Setup

You need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), [docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/) set up on your system.

1. Clone & enter this repository:

```bash
git clone git@github.com:antonheitz/telegram-web-change-detector-bot.git
cd telegram-web-change-detector-bot
```

2. Run the Setup

```bash 
./bot-control.sh setup
```

This will ask you for a bot token (you can register your bot with the [BotFather](https://t.me/botfather)). Also you have to enter the base update interval for the website checks (in minutes).

3. Build the docker images

```bash
./bot-control.sh build
```

4. Start/Stop the container

```bash
# start
./bot-control.sh start
# stop
./bot-control.sh stop
```

The database is located in the ./data folder , therefore you can safely start and stop/delete the container without risking to delete websites to be checked.

## Interaction with the bot

Send `help` to the bot to see the commands!