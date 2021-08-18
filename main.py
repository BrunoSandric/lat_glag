#!.env/bin/python

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

def Kekok():
    print("Kekok")

def main():
    Kekok()

    return 0


if __name__ == "__main__":
    main()
