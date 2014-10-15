#!/usr/bin/env python

import os
import sys
from pprint import pprint
import wit

def readYaml(self,fname):
		f = open( fname )
		dict = yaml.safe_load(f)
		f.close()
		
		return dict
		
if __name__ == '__main__':
	self.info = self.readYaml('/Users/kevin/Dropbox/accounts.yaml')
    wit_token = self.info['WIT_TOKEN']
    
    w = wit.Wit(wit_token)
    input_text = "what's the weather this week"
    pprint(w.get_message(input_text)) 
