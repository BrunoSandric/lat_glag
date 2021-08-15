#!.env/bin/python
import cups
import json

import logging as log

# "macros" for logging, ease of use"
d = log.debug
i = log.info
w = log.warning
e = log.error

log.basicConfig(
    filename="log.log",
    encoding="utf-8",
    level=log.DEBUG,
    format="%(asctime)s: %(levelname)s - %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S",
)
i("............... STARTED .................")


def main():
    return 0


def open_cups():
    return 0


def printer_init():
    conn = cups.Connection()
    if conn.getDefault() is None:
        log.warning(
            """
        No default printer is set.
        Please set defaulty server printer.
        Opening CUPS@localhost"""
        )
        open_cups()
    return 0


if __name__ == "__main__":
    printer_init()
    main()
