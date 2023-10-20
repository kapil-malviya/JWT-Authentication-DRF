# Custom JSON Renderer for User Responses
# This renderer is designed to handel the serialization of response data, ensuring a consistent JSON format
# It specifically addresses cases where the response data includes 'ErrorDetail' objects


from rest_framework import renderers
import json
 

class UserRenderer(renderers.JSONRenderer):
	# Set the charset for the JSON response
	charset='utf-8'
	def render(self, data, accepted_media_type=None, renderer_context=None):
		response = ''
		# Check if the response data contains 'ErrorDetail' objects
		if 'ErrorDetail' in str(data):
			# If errors are detected, format them under the 'errors' key
			response = json.dumps({'errors':data})
		else:
			# If no errors are present, simply format the data as JSON
			response = json.dumps(data)
		
		return response
