An example on how to parse ports given log files using a python regex module

The example logs can be found in the `test_port_parser.py` file

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
$ ./venv/bin/python port_parser.py logs
INFO:port_parser:Log entry '<86>May 28 08:21:45 ...' includes 11332 ports
INFO:port_parser:Log entry '<14>Aug 18 09:00:04 ...' includes 19778 ports
INFO:port_parser:Log entry '<134>1 2020-08-14T18...' includes 60641,80 ports

$ ./venv/bin/python port_parser.py logs -d
DEBUG:port_parser:parsing /home/e0183912/Python/DEV/ideas/port_parser/logs/logfile.log
DEBUG:port_parser:ports found for /home/e0183912/Python/DEV/ideas/port_parser/logs/logfile.log: 11332
INFO:port_parser:Log entry '<86>May 28 08:21:45 ...' includes 11332 ports
DEBUG:port_parser:ports found for /home/e0183912/Python/DEV/ideas/port_parser/logs/logfile.log: 19778
INFO:port_parser:Log entry '<14>Aug 18 09:00:04 ...' includes 19778 ports
DEBUG:port_parser:ports found for /home/e0183912/Python/DEV/ideas/port_parser/logs/logfile.log: 60641,80
INFO:port_parser:Log entry '<134>1 2020-08-14T18...' includes 60641,80 ports
```