def send_message():
    message = entry.get()
    if message:
        chat_display.insert(tk.END, f"You: {message}\n")
        entry.delete(0, tk.END) 