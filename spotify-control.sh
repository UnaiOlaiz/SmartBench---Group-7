#!/bin/bash

# Simple script to control Raspotify
# Usage: ./spotify-control.sh start|stop|restart|status

SERVICE="raspotify"

case "$1" in
    start)
        sudo systemctl start $SERVICE
        echo "Raspotify started"
        ;;
    stop)
        sudo systemctl stop $SERVICE
        echo "Raspotify stopped"
        ;;
    restart)
        sudo systemctl restart $SERVICE
        echo "Raspotify restarted"
        ;;
    status)
        sudo systemctl status $SERVICE
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
        exit 1
        ;;
esac

