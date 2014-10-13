#!/usr/bin/env python

import twilio
from twilio.rest import TwilioRestClient
from twilio.rest.exceptions import TwilioRestException
import yaml

def readYaml(fname):
	f = open( fname )
	dict = yaml.safe_load(f)
	f.close()
	return dict

if __name__ == '__main__':
	msg = 'this is a  test'
	info = readYaml('/Users/kevin/Dropbox/accounts.yaml')
	
	account_sid = info['Twilio']['sid'] 
	auth_token  = info['Twilio']['token'] 
	from_phone = info['Twilio']['phone']['Twilio']
	to_phone = info['Twilio']['phone']['nina']
	
	print 'sid', account_sid
	print 'token', auth_token
	print 'from', from_phone, 'to', to_phone
	
	client = TwilioRestClient(account_sid, auth_token)
	m = client.messages.create(body=msg,
				to=to_phone,
				from_=from_phone ) 
	print m
