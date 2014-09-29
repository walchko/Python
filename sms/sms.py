#!/usr/bin/env python
#
# Kevin J. Walchko
# 22 Sept 2014
#

import twilio
from twilio.rest import TwilioRestClient
from twilio.rest.exceptions import TwilioRestException
import sys
import yaml
#import pprint

# https://www.twilio.com/user/account

"""
Sends a message via SMS using your Twilio account
in: dict(sid, token, phone_to, phone_from), txt message, and who's phone number
out: returns either a message ID or an error statement
"""
def sendMsg(info, msg = 'hello!', who='kevin'):
	try:
		# Your Account Sid and Auth Token from twilio.com/user/account
		account_sid = info['Twilio']['sid'] 
		auth_token  = info['Twilio']['token'] 
		client = TwilioRestClient(account_sid, auth_token)
 
		message = client.messages.create(body=msg,
			to=info['Twilio']['phone'][who] ,    
			from_=info['Twilio']['phone']['Twilio'] ) 
		return message.sid
	
	except TwilioRestException as e:
		return e

if __name__ == '__main__':
	f = open('/Users/kevin/Dropbox/accounts.yaml')
	info = yaml.safe_load(f)
	#pprint.pprint( info )
	#exit()
	
	if len(sys.argv) == 2:
		ret = sendMsg(info,sys.argv[1])
	else:
		ret = sendMsg(info)
	
	print ret

