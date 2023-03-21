"""This is a port_parser that processes log files to find port numbers"""

import re
from typing import List
import os
import logging
import argparse

logger = logging.getLogger("port_parser")
logging.basicConfig()
debug = logger.debug
info = logger.info

# These are the character groups found before a port is defined from the samples given
# writing them in list form so it's easier to read and add/subtract if other log
# formats are being processed. Tried making the match criteria as geneneal as possible so
# it can be applied to many cases other than the sample ones.
MATCHING_PREFIXES = [
    r"[pP]ort.*?",
    r"service:\""
]

# Create the non-matching group
# `(?:[pP]ort.*?|service:\")`
NON_MATCHING_GROUP = f"(?:{'|'.join(MATCHING_PREFIXES)})"

# "accurate" regex to catch ports 0-65535
PORT_NUM_MATCH = r"(6553[0-5]|655[0-2]\d|65[0-4]\d\d|6[0-4]\d{3}|[1-5]\d{4}|[1-9]\d{0,3}|0)"

# create compile object in global namespace so we're not creating it each time
# the function is called. Should save some time/resources especially if we're
# churning thru many/large log files.
PORT_REGEX = re.compile(NON_MATCHING_GROUP+PORT_NUM_MATCH+r"\b", re.MULTILINE)
def parse_port(input_str: str) -> List[str]:
    """Parses input_str and output a list of strings of parsed ports"""
    results = PORT_REGEX.findall(input_str)
    return results

def arguments() -> argparse.Namespace: 
    parser = argparse.ArgumentParser(description="Parses log files in a log directory for ports associated with each log entry")
    parser.add_argument("dir", help="Input logs directory")
    parser.add_argument("-d", "--debug", action="store_true", help="output debug information")
    return parser.parse_args()

def main() -> None:
    """Main function to run port_parser:
    This is a quick and dirty implementation that simply loops over the files in a log directory
    and analyzes each line for ports. Some re-design is needed if the input source is different.
    i.e., results from an API call to a system storing logs; accepting stdin; pulling from a database; etc.

    Depending on the input source using concurrent.futures.ThreadPoolExecutor for I/O-bound inputs would
    speed up log collection.

    May also consider concurrent.futures.ProcessPoolExecutor to churn thru the logs depending on the number/size.
    """
    
    log_dir = ARGS.dir
    for root, _, files in os.walk(os.path.abspath(log_dir)):
        for file in files:
            abs_path = os.path.join(root, file)
            debug("parsing %s", abs_path)
            with open(abs_path) as f:
                logs = f.read()
            for idx, log in enumerate(logs.splitlines()):
                ports = parse_port(log)
                ports = ','.join(ports)
                debug("ports found for %s, line %s: %s", file, idx+1, ports)
                info("Log entry '%s...' includes these ports: %s", log[:20], ports)
    

if __name__ == "__main__":
    ARGS = arguments()
    if ARGS.debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    try:
        main()
    except Exception as e:
        logger.exception("Exception occured...")
        raise e

