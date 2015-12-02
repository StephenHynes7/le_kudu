le_kudu
=========

Baisc forwarding integration for [Kudu Log Streamer](https://github.com/projectkudu/kudu/wiki/Diagnostic-Log-Stream).

Usage
-----
```
usage: le_kudu.py [-h] -l LOG_TOKEN -e ENDPOINT_URL -u USERNAME -p PASSWORD

optional arguments:
  -h, --help            show this help message and exit
  -l LOG_TOKEN, --log_token LOG_TOKEN
                        Specify your Log Token to set the log which your logs
                        will forward to.
  -e ENDPOINT_URL, --endpoint_url ENDPOINT_URL
                        Your Azure scm endpoint URL that we will query to
                        retrieve your log data from.
  -u USERNAME, --username USERNAME
                        Your username for your endpoint access
  -p PASSWORD, --password PASSWORD
                        Your password your endpoint access
```                        