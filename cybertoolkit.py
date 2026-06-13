import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import string
import hashlib
import socket

# ---------------- Password Generator ----------------
def generate_password():
    length = simpledialog.askinteger("Password Length", "Enter password length:")
    
    if length:
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        result_var.set(f"Generated Password:\n{password}")

# ---------------- Password Strength Checker ----------------
def check_strength():
    password = simpledialog.askstring("Password Strength", "Enter password:")

    if password:
        score = 0

        if len(password) >= 8:
            score += 1
        if any(c.isupper() for c in password):
            score += 1
        if any(c.islower() for c in password):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(c in string.punctuation for c in password):
            score += 1

        if score <= 2:
            strength = "Weak"
        elif score <= 4:
            strength = "Medium"
        else:
            strength = "Strong"

        result_var.set(f"Password Strength: {strength}")

# ---------------- SHA-256 Hash Generator ----------------
def generate_hash():
    text = simpledialog.askstring("SHA-256 Hash", "Enter text:")

    if text:
        hash_value = hashlib.sha256(text.encode()).hexdigest()
        result_var.set(f"SHA-256 Hash:\n{hash_value}")

# ---------------- Port Scanner ----------------
def port_scanner():
    host = simpledialog.askstring("Port Scanner", "Enter Host/IP:")
    port = simpledialog.askinteger("Port Scanner", "Enter Port:")

    if host and port:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((host, port))

            if result == 0:
                result_var.set(f"Port {port} is OPEN")
            else:
                result_var.set(f"Port {port} is CLOSED")

            sock.close()

        except Exception as e:
            messagebox.showerror("Error", str(e))

# ---------------- GUI Window ----------------
root = tk.Tk()
root.title("Cybersecurity Toolkit")
root.geometry("600x400")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Cybersecurity Toolkit",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

btn1 = tk.Button(
    root,
    text="Password Generator",
    width=25,
    command=generate_password
)
btn1.pack(pady=5)

btn2 = tk.Button(
    root,
    text="Password Strength Checker",
    width=25,
    command=check_strength
)
btn2.pack(pady=5)

btn3 = tk.Button(
    root,
    text="SHA-256 Hash Generator",
    width=25,
    command=generate_hash
)
btn3.pack(pady=5)

btn4 = tk.Button(
    root,
    text="Port Scanner",
    width=25,
    command=port_scanner
)
btn4.pack(pady=5)

btn5 = tk.Button(
    root,
    text="Exit",
    width=25,
    command=root.quit
)
btn5.pack(pady=5)

result_var = tk.StringVar()
result_var.set("Results will appear here")

result_label = tk.Label(
    root,
    textvariable=result_var,
    wraplength=550,
    font=("Arial", 10)
)
result_label.pack(pady=20)

root.mainloop()