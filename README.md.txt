# 🔐 Image Encryption & Decryption GUI

A simple and interactive Python GUI to **encrypt and decrypt images** using **XOR** logic or **pixel flipping**, built with **CustomTkinter**.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/GUI-CustomTkinter-lightblue?style=flat-square" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" />
</p>

---

## ✨ Features

- 📂 Load JPG or PNG image
- 🔒 Encrypt using XOR with a numeric key
- 🔄 Flip image horizontally or vertically
- 🔓 Decrypt using the same method
- 🖼️ Preview original and output image side-by-side
- 💾 Save processed image easily

---

## 📸 Demo

| Original | Encrypted |
|----------|-----------|
| ![orig](assets/original_sample.png) | ![enc](assets/encrypted_sample.png) |


---

## 🧪 How It Works

1. Choose to **Encrypt** or **Decrypt**
2. Select the method: `XOR` or `Swap` (flip)
3. Provide a numeric key (for XOR)
4. Run and preview the result
5. Save the output if desired

---

## 🚀 Getting Started

### 🔧 Installation

```bash
git clone https://github.com/yourusername/image-encryption-gui.git
cd image-encryption-gui
pip install -r requirements.txt
