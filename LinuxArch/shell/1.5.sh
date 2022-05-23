#!/bin/bash


case "$1" in
    start)
      echo "starting"
      ;;
    stop)
      echo "stopping"
      ;;
    status)
      echo "display status"
      ;;
    restart)
      echo "stopping"
      sleep 2
      echo "starting"
      ;;
    condrestart)
      if test "x$2" != x; then
        echo "stopping"
        sleep 4
        echo "starting"
      fi
      ;;
    *)
      echo $"Usage: $0 {start|stop|restart|condrestart|status}"
      exit 1
esac

