import json
import tkinter as tk
import time
import pyperclip
import http.client

def get_token_from_api():
    conn = http.client.HTTPSConnection("api.discord.gx.games")
    payload = '{"partnerUserId": "aefae130a8653d420cba4c2e1c85571912f85a4d9bb5a09ae48c8f009a0720b1"}'
    headers = {
        'authority': "discord.gx.games",
        'accept': "*/*",
        'accept-language': "en-US,en;q=0.9",
        'content-type': "application/json",
        'origin': "https://www.google.com",
        'referer': "https://www.opera.com/",
        'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': "empty",
        'sec-fetch-mode': "cors",
        'sec-fetch-site': "cross-site",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0"
    }

    try:
        conn.request("POST", "/v1/direct-fulfillment", payload, headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        conn.close()

        # Check if the response contains valid JSON data
        if not data.strip():
            raise ValueError("Empty response from the server")

        # Try to load JSON data
        json_data = json.loads(data)

        # Extract the token from the response
        token = json_data.get('token')

        if token:
            return token
        else:
            raise ValueError("Token not found in the response")

    except json.decoder.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def generate_token():
    # Simulate token generation delay
    time.sleep(0)

    # Get the token from the second script
    token = get_token_from_api()

    if token is not None:
        # Update the label text with the generated token and URL
        label.config(text=f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}")

def copy_to_clipboard():
    # Get the token text from the label
    token_text = label.cget("text")

    # Copy the entire token URL to the clipboard
    pyperclip.copy(token_text)

# Create the main window
window = tk.Tk()
window.title("Nitro Token Generator")
window.geometry("300x150")

# Create and place the label for displaying the token with a smaller font size
label = tk.Label(window, text="Click For Nitro Token", font=("Helvetica", 8))
label.pack(pady=10)

# Create and place the Generate Token button
generate_button = tk.Button(window, text="Generate Token", command=generate_token)
generate_button.pack(pady=5)

# Create and place the Copy button
copy_button = tk.Button(window, text="Copy", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
