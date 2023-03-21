An example on how to parse ports given log files using a python regex module

The example logs can be found in the `test_port_parser.py` file as well as in a mock log file in logs/logfile.log

## Virtual Env
I created a virtual env for this project. Use the `requirements.txt` to build your own.
```
$ python -m venv venv

$ ./venv/bin/python --version
Python 3.9.14
```

## Unittest
I wrote a simple unittest that tests the parse_port function against the sample logs. These test cases can be extended with other log examples and pytest ran to ensure the appropriate ports are parsed as expected.

```
$ ./venv/bin/python -m pytest -vvv
========================================================================== test session starts ==========================================================================
platform linux -- Python 3.9.14, pytest-7.2.2, pluggy-1.0.0 
cachedir: .pytest_cache
collected 1 item                                                                                                                                                        

test_port_parser.py::test_parse_port PASSED                                                                                                                       [100%]

=========================================================================== 1 passed in 0.05s ===========================================================================

```

## Port Parser
The main function simply loops through a user input log directory and prints results to screen. User can include a `-d` switch to print debug info
```
$ ./venv/bin/python port_parser.py logs -h
usage: port_parser.py [-h] [-d] dir

Parses log files in a log directory for ports associated with each log entry

positional arguments:
  dir          Input logs directory

optional arguments:
  -h, --help   show this help message and exit
  -d, --debug  output debug information
```

### Output
```
$ ./venv/bin/python port_parser.py logs
INFO:port_parser:Log entry '<86>May 28 08:21:45 ...' includes these ports: 11332
INFO:port_parser:Log entry '<14>Aug 18 09:00:04 ...' includes these ports: 19778
INFO:port_parser:Log entry '<134>1 2020-08-14T18...' includes these ports: 60641,80

$ ./venv/bin/python port_parser.py logs -d
DEBUG:port_parser:parsing /home/e0183912/Python/DEV/ideas/port_parser/logs/logfile.log
DEBUG:port_parser:ports found for logfile.log, line 1: 11332
INFO:port_parser:Log entry '<86>May 28 08:21:45 ...' includes these ports: 11332
DEBUG:port_parser:ports found for logfile.log, line 2: 19778
INFO:port_parser:Log entry '<14>Aug 18 09:00:04 ...' includes these ports: 19778
DEBUG:port_parser:ports found for logfile.log, line 3: 60641,80
INFO:port_parser:Log entry '<134>1 2020-08-14T18...' includes these ports: 60641,80
```

The port_parser.py can be easilty redesigned to compile logs from other sources. i.e., results from an API call to a system storing logs; accepting stdin; pulling from a database; etc.

Depending on the input source using concurrent.futures.ThreadPoolExecutor for I/O-bound inputs would speed up log collection by multithreading those calls.

May also consider concurrent.futures.ProcessPoolExecutor to multiprocess thru the logs depending on the number/size.