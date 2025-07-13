import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import os

# Global variables
original_image = None
processed_image = None
original_path = ""

# Logic Functions
def xor_process(img_array, key=123):
    return np.bitwise_xor(img_array, key)

def flip_process(img_array, mode='horizontal'):
    if mode == 'horizontal':
        return np.flip(img_array, axis=1)
    elif mode == 'vertical':
        return np.flip(img_array, axis=0)
    else:
        raise ValueError("Invalid flip mode")

def load_image():
    global original_image, original_path

    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if file_path:
        original_path = file_path
        original_image = Image.open(file_path).convert("RGB")
        preview_img = original_image.resize((200, 200))
        preview_tk = ImageTk.PhotoImage(preview_img)
        original_label.configure(image=preview_tk, text="")
        original_label.image = preview_tk
        status_label.configure(text=f"Loaded: {os.path.basename(file_path)}", text_color="green")

def process_image():
    global original_image, processed_image

    if original_image is None:
        status_label.configure(text="⚠️ Please load an image first!", text_color="red")
        return

    action = action_option.get()  # Encrypt or Decrypt
    method = method_option.get()  # XOR or Swap
    flip_mode = flip_option.get().lower()

    try:
        key = int(key_entry.get())
    except ValueError:
        status_label.configure(text="⚠️ Key must be a number", text_color="red")
        return

    img_array = np.array(original_image)

    try:
        if method == "XOR":
            processed_array = xor_process(img_array, key)
        elif method == "Swap":
            processed_array = flip_process(img_array, flip_mode)
        else:
            raise ValueError("Invalid method")

        processed_image = Image.fromarray(processed_array)
        preview_img = processed_image.resize((200, 200))
        preview_tk = ImageTk.PhotoImage(preview_img)
        result_label.configure(image=preview_tk, text="")
        result_label.image = preview_tk

        action_symbol = "🔒" if action == "Encrypt" else "🔓"
        status_label.configure(text=f"{action_symbol} {action}ion successful!", text_color="blue")
    except Exception as e:
        status_label.configure(text=f"⚠️ Error: {e}", text_color="red")

def save_image():
    global processed_image
    if processed_image is None:
        status_label.configure(text="⚠️ No processed image to save!", text_color="red")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")],
                                             initialfile="output_image.png")
    if save_path:
        processed_image.save(save_path)
        status_label.configure(text=f"💾 Saved to: {save_path}", text_color="green")

# GUI Setup
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🔐 Image Encryptor / Decryptor")
app.geometry("650x650")
app.resizable(False, False)

# Title
title_label = ctk.CTkLabel(app, text="Image Encryption & Decryption", font=ctk.CTkFont(size=24, weight="bold"))
title_label.pack(pady=10)

# Load Button
load_button = ctk.CTkButton(app, text="📂 Load Image", command=load_image)
load_button.pack(pady=8)

# Action Option
action_option = ctk.CTkOptionMenu(app, values=["Encrypt", "Decrypt"])
action_option.set("Encrypt")
action_option.pack(pady=4)

# Method Option
method_option = ctk.CTkOptionMenu(app, values=["XOR", "Swap"])
method_option.set("XOR")
method_option.pack(pady=4)

# Key
key_entry = ctk.CTkEntry(app, placeholder_text="Key (for XOR)", width=200)
key_entry.insert(0, "123")
key_entry.pack(pady=4)

# Flip Option
flip_option = ctk.CTkOptionMenu(app, values=["Horizontal", "Vertical"])
flip_option.set("Horizontal")
flip_option.pack(pady=4)

# Encrypt/Decrypt Button
process_button = ctk.CTkButton(app, text="▶️ Run", command=process_image)
process_button.pack(pady=12)

# Save Button
save_button = ctk.CTkButton(app, text="💾 Download Output Image", command=save_image)
save_button.pack(pady=4)

# Preview Frame
preview_frame = ctk.CTkFrame(app)
preview_frame.pack(pady=20)

original_label = ctk.CTkLabel(preview_frame, text="Original", width=200, height=200, corner_radius=8)
original_label.grid(row=0, column=0, padx=15)

result_label = ctk.CTkLabel(preview_frame, text="Result", width=200, height=200, corner_radius=8)
result_label.grid(row=0, column=1, padx=15)

# Status Label
status_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=14))
status_label.pack(pady=10)

app.mainloop()
