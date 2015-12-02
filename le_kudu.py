import requests
from logentries import LogentriesHandler
import logging
import argparse
import sys

def setup(args):
	print 'Setting up Logentries Forwarder'
	log = logging.getLogger('logentries')
	log.setLevel(logging.INFO)
	log.addHandler(LogentriesHandler(args.log_token))
	forward_logs(log, args)
	

def forward_logs(log, args):
	print 'Making Kudu log streaming request'
	results = requests.get(args.endpoint_url,
		auth=(args.username, args.password), stream=True)
	print 'Status is %s', results.status_code
	if results.status_code == 200:
		print 'Successful request, streaming log data to Logentries Account'
		for line in results.iter_lines():
			log.info(line)
	else:
		print 'Unable to get successful request'

if __name__ == '__main__':
	ap = argparse.ArgumentParser()
	ap.add_argument('-l', '--log_token',
		help='Specify your Log Token to set the log which your logs will forward to.', required=True)
	ap.add_argument('-e', '--endpoint_url',
		help='Your Azure scm endpoint URL that we will query to retrieve your log data from.', required=True)
	ap.add_argument('-u', '--username', help='Your username for your endpoint access', required=True)
	ap.add_argument('-p', '--password', help='Your password your endpoint access', required=True)
	args = ap.parse_args(sys.argv[1:])
	setup(args)