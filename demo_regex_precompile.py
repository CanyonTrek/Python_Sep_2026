#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO match text using str testing and
# pattern matching using Regex and re.py module.
"""
    DocString
"""
import sys
import re

def search_pattern(pattern=r"^.{19}$", file=r"f:\labs\words"):
    try:
        fh_in = open(file, mode="rt")
    except FileNotFoundError as err:
        print(f"Error: {err.args[0]}, {err.args[1]}, {err.filename}", file=sys.stderr)
        sys.exit(1)
    except PermissionError as err:
        print(f"Error: {err.args[0]}, {err.args[1]}, {err.filename}", file=sys.stderr)
        sys.exit(2)
    except Exception as err:
        print(f"Some other occurred - Investigate", file=sys.stderr)
        sys.exit(3)
    else:
        # Executes if try block succeeds
        reobj = re.compile(pattern) # Compiles pattern ONLY ONCE
        for line in fh_in:
            m = reobj.search(line)  # Match using PRECOMPILED Pattern
            if m:
                print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")
        fh_in.close() # Close file handle.
    finally:
        # ALWAYS executes!
        print("And now for something completely different..")

    return None

def main():
    search_pattern()
    return None

# Namespace Trick
if __name__ == "__main__":
    main()
    sys.exit(0)