from flask import Flask, request, redirect

app = Flask(__name__)

# 192.168.1
ALLOWED_SUBNET = "192.168.1"  # Allow all devices in 192.168.1.x
FORM_URL = "https://forms.microsoft.com/Pages/ResponsePage.aspx?id=MyLm9SCzHU2nNzgHYTLo22_12ZhQ5p1AucR_V7HurK5UN0NXWDcxSzdXOE5PU1NQSU9ER1JLTkI2MS4u"

# 192.168.1.1 → Default Gateway (Router)
# 192.168.1.2 to 192.168.1.254 → Assigned to devices on the network (like your laptop at 192.168.1.5)
# Another example of wrong ip of 192.168.10.15
@app.route("/")
def check_ip():
    user_ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    print(f"User IP Detected: {user_ip}")  # Debugging

    if user_ip.startswith(ALLOWED_SUBNET):  # Check if IP is in the 192.168.1.x range
        return redirect(FORM_URL)
    else:
        return f"Access Denied! Your IP: {user_ip}", 403  # Display IP for debugging

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1000, debug=True)
