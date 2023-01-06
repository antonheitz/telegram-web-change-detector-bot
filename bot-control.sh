#!/bin/bash

# check if the 

case "$1" in
    # setup
    "setup")
        echo "running setup..."
        echo "Please enter your bots token:"
        read token
        echo "What interval would you like to clock the checks in minutes?"
        read check_interval
        echo "creating .env file"
        echo "BOT_TOKEN=$token
BOT_CHECK_INTERVAL=$check_interval" > .env
        echo "done."
        ;;
    # dev
    "dev")
        echo "Running in dev mode..."
        set -a
        source .env
        set +a
        python3 main.py
        ;;
    # build
    "build")
        echo "build"
        ;;
    # start
    "start")
        echo "start"
        ;;
    # stop
    "stop")
        echo "stop"
        ;;
    *)
        echo "Please provide a valid command: build | start | stop "
        ;;
esac