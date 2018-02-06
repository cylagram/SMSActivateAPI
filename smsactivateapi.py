#!/usr/bin/env python
import requests, json


class APIError(Exception):
	pass

class VOIPGenerator:
	
	def __init__(self, token):
		self.token = token
		if (not token):
			raise APIError(json.dumps({"ok":False, "error_code":402, "error":"The api_key is missing!"}))
		else:
			if "BAD_KEY" in requests.get("http://sms-activate.ru/stubs/handler_api.php?api_key="+token+"&action=getBalance").text:
				raise APIError(json.dumps({"ok":False, "error_code":400, "error":"The api_key is invalid. Try with another!"}))
			else:
				self.api_url = "http://sms-activate.ru/stubs/handler_api.php?api_key="+token+"&"
		
	def getNumbersStatus(self, country):
		if (not country):
			raise APIError(json.dumps({"ok":False, "error_code":401, "error":"Country invalid, use another!"}))
		else:
			value = requests.get(self.api_url+"action=getNumbersStatus&country="+country).text
			if ("ERROR_SQL1" in value):
				raise APIError(json.dumps({"ok":False, "error_code":401, "error":"Country invalid, use another!"}))
			else:
				return value
		
	def getBalance(self):
	    value = requests.get(self.api_url+"action=getBalance").text
		if ("ACCESS_BALANCE" in value):
			return json.dumps({"ok":True, "balance":value.split(":")[1]})
		else:
			return json.dumps({"ok":False, "balance":None})
	
	def getNumber(self, service, country):
		value = requests.get(self.api_url+"action=getNumber&service="+str(service)+"&ref=1222&country="+str(country)).text
		if (not service):
			raise APIError(json.dumps({"ok":False, "error_code": 306, "error":"Service not inserted, put one!"}))
		elif (not country):
			raise APIError(json.dumps({"ok":False, "error_code":401, "error":"Country invalid, use another!"}))
		else:
			if ("NO_NUMBERS" in value):
				return json.dumps({"ok":False, "error":"There are no numbers for this country!"})
			if ("NO_BALANCE" in value):
				return json.dumps({"ok":False, "error":"Balance is insufficent, charge your account!"})
			if ("ACCESS_NUMBER" in value):
				return json.dumps({"ok":True, "id_number": str(value.split(":")[1]), "number": str(value.split(":")[2])})
	
	def getStatus(self, id_number):
		value = requests.get(self.api_url+"action=getStatus&id="+str(id_number)).text
		if ("NO_ACTIVATION" in value):
			raise APIError(json.dumps({"ok":False, "error_code": 403, "error":"The activation ID does not exist!"}))
		else:
			if ("BAD_STATUS" in value):
				return json.dumps({"ok":False, "status":value})
			if ("STATUS_WAIT_CODE" in value):
				return json.dumps({"ok":True, "status":value})
			if ("STATUS_WAIT_RESEND" in value):
				return json.dumps({"ok":True, "status":value})
			if ("STATUS_WAIT_RETRY" in value):
				return json.dumps({"ok":True, "status":value})
			if ("STATUS_CANCEL" in value):
				return json.dumps({"ok":False, "status":value})
			if ("STATUS_OK" in value):
				return json.dumps({"ok":True, "status":value.replace(value.split("K")[1],""), "code": value.split(":")[1]})
		
		