import tkinter as tk
from tkinter import messagebox
import random
import webbrowser
import urllib.parse

whatsapp_number = "Your Number"
pesan = "OIOIOI"


def tekan_ya():
    messagebox.showinfo("Jawaban", "YEYEYYEYYYYYYYYYYY")
    buka_whatsapp()

def tekan_tidak():
    messagebox.showinfo("Jawaban", "Oh, okey... aku masih bisa menunggu ko :), cepat membaik yaa")


def buka_whatsapp():
    encoded_message = urllib.parse.quote(pesan)
    webbrowser.open_new(f"https://api.whatsapp.com/send?phone=+62081287939099&text=Halo aku kembali, (tambahin kalo kamu mau ngomong sesuatu)")

window = tk.Tk()
window.title("Miss U :(((")
window.geometry("400x600")
window.configure(bg='#FFC0CB')

frame = tk.Frame(window, bg='#FFC0CB', bd=5)
frame.place(relx=0.5, rely=0.5, anchor='center')

label = tk.Label(frame, text="kamu sudah membaik kah?.\ni miss u :C", font=("Helvetica", 16, "bold"), bg='#FFC0CB', fg='#FF79B4', justify=tk.CENTER)
label.pack(pady=20)

ya_button = tk.Button(frame, text="sudah", font=("Helvetica", 14), command=tekan_ya, bg='#FF79B4', fg='white', width=8)
ya_button.pack(side=tk.LEFT, padx=10,)

tidak_button = tk.Button(frame, text="belum", font=("Helvetica", 14), command=tekan_tidak, bg='#FF69B4', fg='white', width=8)
tidak_button.pack(side=tk.RIGHT, padx=10,)

window.mainloop()