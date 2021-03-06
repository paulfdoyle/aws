# This script created a queue
#
# Author - Paul Doyle Aug 2013
#
#
import boto.sqs
import boto.sqs.queue
import argparse
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
sys.path.append('/data')
from keys import access_key_id, secret_access_key

parser = argparse.ArgumentParser()
parser.add_argument("qname")
parser.add_argument("qmsg")
args = parser.parse_args()

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
q = conn.get_queue(args.qname)

try:
	msg = args.qmsg
	m = Message()
	m.set_body(msg)
	status = q.write(m)
	print "Message: " + args.qmsg + " -  written to " + args.qname
except:
	print "Could not write message"

