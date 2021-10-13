prompt = "Tell me something and I will repeat it back to you"
prompt += "\nEnter 'stop' to stop program: "
message = ""

while message != "stop":
    message = input(prompt)
    print(message)