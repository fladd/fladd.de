#!/usr/bin/env python
"""
eeepower.py is a simple tool for power management on Ubuntu.

This tool can set the CPU governor, Asus Super Hybrid Engine (FSE speed;
eeepc-wmi kernel module needed),and display backlight.

It is also capable to detect automatically whether the machine is running on
AC power or on battery and can apply predefined settings. These settings can
be changed directly in the script file.

This tool needs to be run as root!

"""

import sys
import multiprocessing
import pynotify


# SETTINGS
PERFORMANCE_AC = 'performance'  # 'performance', 'normal', 'powersave'
PERFORMANCE_BATTERY = 'powersave'  # 'performance', 'normal', 'powersave'
BACKLIGHT_AC = 15  # 0-15
BACKLIGHT_BATTERY = 2  # 0-15
POPUP_NOTIFICATIONS = True


# Functions
def set_performance(value, notify):
    """Set performance mode.

    This will set CPU frequency scaling as well as the
    Asus Super Hybrid Engine (FSB speed).

    Keyword arguments:
    value  -- "performance", "ondemand" or "powersave" (str)
    notify -- Show popup notification (bool)

    """

    modes = {"performance": '0', "ondemand": '1', "powersave": '2'}
    try:
        with open("/sys/devices/platform/eeepc-wmi/cpufv", 'w') as f:
            f.write(modes[value])
    except:
        pass
    for cpu in range(0, multiprocessing.cpu_count()):
        with open(
            "/sys/devices/system/cpu/cpu{0}/cpufreq/scaling_governor".format(
                cpu), 'w') as f:
            f.write(value)
    with open(
            "/sys/devices/system/cpu/cpu{0}/cpufreq/scaling_governor".format(
                multiprocessing.cpu_count() - 1)) as f:
        mode = f.read()

    print("Performance: {0}".format(mode.rstrip()))

    if notify:
        show_notification("Performance mode", "{0}".format(mode))


def set_backlight(value, notify):
    """Set the display backlight.

    Keyword arguments:
    value  -- 0-15 (int)
    notify -- Show popup notification (bool)

    """

    with open("/sys/class/backlight/acpi_video0/brightness", 'w') as f:
        f.write(repr(value))
    with open(
            "/sys/class/backlight/acpi_video0/brightness") as f:
        backlight = f.read()
    print("Backlight: {0}".format(backlight.rstrip()))
    if notify:
        show_notification("Backlight", "{0}".format(backlight))


def get_settings():
    """Get current settings.

    Returns state, performance and backlight settings (tuple).

    """

    with open("/sys/class/power_supply/AC0/online") as f:
        ac = int(f.read())
        if ac:
            state = "AC"
        else:
            state = "Battery"
    with open(
        "/sys/devices/system/cpu/cpu{0}/cpufreq/scaling_governor".format(
            multiprocessing.cpu_count() - 1)) as f:
        performance = f.read()
    with open("/sys/class/backlight/acpi_video0/brightness") as f:
        backlight = f.read()
    return (state.rstrip(), performance.rstrip(), backlight.rstrip())


def show_notification(title, message):
    """Show a popup notification.

    The message can be formatted using HTML.

    Keyword arguments:
    title   -- the title of the notification (str)
    message -- the message of the notification (str)

    """

    pynotify.init("Markup")
    n = pynotify.Notification(title, message)
    n.show()


if __name__ == "__main__":

    try:
        if sys.argv[1] == "-a" or sys.argv[1] == "--auto":
            with open("/sys/class/power_supply/AC0/online") as f:
                ac = int(f.read())
                if ac:
                    state = "AC"
                    performance = PERFORMANCE_AC
                    backlight = BACKLIGHT_AC
                else:
                    state = "Battery"
                    performance = PERFORMANCE_BATTERY
                    backlight = BACKLIGHT_BATTERY
                print("State: {0}".format(state))
                set_performance(performance, False)
                set_backlight(backlight, False)
                if POPUP_NOTIFICATIONS:
                    state, performance, backlight = get_settings()
                    show_notification("{0}".format(state),
                           "{0}<br />{1}".format(performance, backlight))
        elif sys.argv[1] == "-b" or sys.argv[1] == "--backlight":
            if 0 <= int(sys.argv[2]) <= 15:
                set_backlight(int(sys.argv[2]), POPUP_NOTIFICATIONS)
        elif sys.argv[1] == "-p" or sys.argv[1] == "--performance":
            if len(sys.argv) < 3:
                state, performance, backlight = get_settings()
                if performance == "performance":
                    set_performance("powersave", True)
                elif performance == "powersave":
                    set_performance("ondemand", True)
                elif performance == "ondemand":
                    set_performance("performance", True)
            elif sys.argv[2] in ("performance", "ondemand", "powersave"):
                set_performance(sys.argv[2], POPUP_NOTIFICATIONS)
            else:
                raise Exception
        elif sys.argv[1] == "-s" or sys.argv[1] == "--show":
            state, performance, backlight = get_settings()
            print("State: {0}".format(state.rstrip()))
            print("Performance: {0}".format(performance.rstrip()))
            print("Backlight: {0}".format(backlight.rstrip()))
            if POPUP_NOTIFICATIONS:
                show_notification("{0}".format(state),
                       "{0}<br />{1}".format(performance, backlight))
        elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
            raise Exception
    except:
        print("")
        print("This tool needs to be run as root!")
        print("")
        print("Usage:")
        print("")
        print("    python eeepower.py [opition] [value]")
        print("")
        print("Options:")
        print("")
        print("    -a, --auto           Automatically detect if on AC or")
        print("                         battery and set correspondingly")
        print("")
        print("    -b, --backlight      Set the backlight of the display:")
        print("                         0-15")
        print("")
        print("    -h, --help           This help")
        print("")
        print("    -p,  --performance   Set performance mode:")
        print("                         performance, ondemand, powersave")
        print("                         If no value, toggle through states")
        print("")
        print("    -s, --show           Show current settings")
        print("")
        print("See the script file for more information")
        print("")
        sys.exit(1)
