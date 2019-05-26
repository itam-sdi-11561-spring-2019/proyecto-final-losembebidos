#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/robotica/PaulyFabs/PM_proyecto_final-master/src/rosserial/rosserial_arduino"

# snsure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/robotica/PaulyFabs/PM_proyecto_final-master/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/robotica/PaulyFabs/PM_proyecto_final-master/install/lib/python2.7/dist-packages:/home/robotica/PaulyFabs/PM_proyecto_final-master/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/robotica/PaulyFabs/PM_proyecto_final-master/build" \
    "/usr/bin/python" \
    "/home/robotica/PaulyFabs/PM_proyecto_final-master/src/rosserial/rosserial_arduino/setup.py" \
    build --build-base "/home/robotica/PaulyFabs/PM_proyecto_final-master/build/rosserial/rosserial_arduino" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/robotica/PaulyFabs/PM_proyecto_final-master/install" --install-scripts="/home/robotica/PaulyFabs/PM_proyecto_final-master/install/bin"
