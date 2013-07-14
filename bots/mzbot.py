# A simple bot framework

import requests
import json

class MZBot(object):
	def __init__(self, endpoint):
		self.endpoint = endpoint

	def doCommands(self, cmd_list):
		json_data = json.dumps(cmd_list)
		headers = {"Content-type": "text/json"}
		resp = requests.post(self.endpoint, data=json_data, headers=headers)
		return resp.json()

	def assert_success(self,result):
		if isinstance(result,dict):
			if result['success']:
				return
			raise Exception(result['error'])
		
		if isinstance(result,list):
			for r in result:
				if not r['success']:
					raise Exception(r['error'])
				return
		raise Exception('Bad response type from server')

if __name__=='__main__':
	import sys
	endpoint = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:9000/"
	b = MZBot(endpoint)
	print b.doCommands([{'cmd':'static_capabilities'}])
