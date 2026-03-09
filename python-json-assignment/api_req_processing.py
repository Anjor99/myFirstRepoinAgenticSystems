import json

# 1. Store the JSON-formatted API response as a string
api_response = '''
{
  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}
'''

# 2. Parse the JSON string into Python objects
data = json.loads(api_response)

# 3. Extract required values
request_id = data["id"]
status = data["status"]
text_result = data["result"]["text"]
confidence_score = data["result"]["confidence"]

# 4. Print extracted values
print("Request ID:", request_id)
print("Status:", status)
print("Text:", text_result)
print("Confidence:", confidence_score)

# 5. Check confidence score
if confidence_score < 0.9:
    print("Warning: Confidence score is below acceptable threshold!")

# 6. Create a follow-up result dictionary
follow_up_result = {
    "request_id": request_id,
    "processed": True,
    "message": "Response processed successfully"
}

# 7. Convert dictionary to JSON
json_output = json.dumps(follow_up_result, indent=4)

# 8. Write JSON to a file
with open("response.json", "w") as file:
    file.write(json_output)