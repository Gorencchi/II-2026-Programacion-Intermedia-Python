import ollama as ol
respuesta = ol.chat(
    model="llama3.2",
    messages=[
        {
            "role": "system",
            "content": "System Prompt"
        },
        {
            "role": "user",
            "content": "User Prompt"
        }
    ]
)
print(respuesta["message"]["content"])