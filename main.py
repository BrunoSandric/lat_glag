#!.env/bin/python
import cups
import json


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
