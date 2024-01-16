import requests
import duckduckgo

headers = {"Authorization": "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxx"} #change xxxxxxxxxxxxxxxxx to YOUR user token for huggingface.

def query(payload, API_URL):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

print("DuckBart Started!")
while True:
  q = input("prompt:")
  try:
    try:
      if q.startswith("Answer this:") or q.startswith("Answer mode:") or q.startswith("Ans:") or q.startswith("Answer:"):
        s = duckduckgo.get_zci(q)
        o = query({
        "inputs": s,
        }, "https://api-inference.huggingface.co/models/google/pegasus-xsum")
        print("<USER>: " + q + " <BOT>:" + o[0]['summary_text'])
      else:
        o = query({
        "inputs": "<USER>: " + q + " <BOT>:",
        }, "https://api-inference.huggingface.co/models/EleutherAI/gpt-j-6B")
        ans = o[0]['generated_text'].split("<USER>:")[1]
        if ('don\'t understand' in ans or 'don\'t know' in ans or 'try' in ans or 'not sure' in ans):
          raise Exception("Not understand!")
        print("<USER>:" + ans.replace("<BOT>:<USER>", "").replace("\\r", ""))
    except:
      s = duckduckgo.get_zci(q)
      o = query({
      "inputs": s,
      }, "https://api-inference.huggingface.co/models/google/pegasus-xsum")
      print("<USER>: " + q + " <BOT>:" + o[0]['summary_text'])
  except:
    print("Result not found.")
