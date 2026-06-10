import tkinter as tk
from tkinter import messagebox

from pdu import pdu_encode, pdu_decode


def encrypt_message():
    message = input_text.get('1.0', tk.END).rstrip('\n')

    if not message:
        messagebox.showwarning('Input Required', 'Please enter plaintext to encrypt.')
        return

    encrypted = pdu_encode(message)
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, encrypted)

    original_bytes = len(message.encode('ascii', errors='replace'))
    encoded_bytes = len(encrypted) // 2
    saved = original_bytes - encoded_bytes
    bytes_saved_var.set(f'{saved} byte{"s" if saved != 1 else ""} saved  '
                        f'({original_bytes} → {encoded_bytes} bytes)')


def decrypt_message():
    encrypted = input_text.get('1.0', tk.END).strip()

    if not encrypted:
        messagebox.showwarning('Input Required', 'Please enter hex text to decrypt.')
        return

    try:
        plaintext = pdu_decode(encrypted)
    except ValueError as err:
        messagebox.showerror('Invalid Hex', str(err))
        return

    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, plaintext)


def clear_fields():
    input_text.delete('1.0', tk.END)
    output_text.delete('1.0', tk.END)
    bytes_saved_var.set('')


root = tk.Tk()
bytes_saved_var = tk.StringVar()
root.title('PDU Encrypt / Decrypt')
root.geometry('600x480')
root.minsize(500, 350)

input_label = tk.Label(root, text='Input (plaintext or hex):')
input_label.pack(anchor='w', padx=12, pady=(12, 2))

hint_label = tk.Label(root, text='Decrypt hint: paste hex e.g. e8329bfd06dddf723619...', fg='grey', font=('TkDefaultFont', 8))
hint_label.pack(anchor='w', padx=12, pady=(0, 4))

input_text = tk.Text(root, height=8, wrap='word')
input_text.pack(fill='both', expand=True, padx=12)

button_frame = tk.Frame(root)
button_frame.pack(fill='x', padx=12, pady=10)

encrypt_button = tk.Button(button_frame, text='Encrypt', width=12, command=encrypt_message)
encrypt_button.pack(side='left')

decrypt_button = tk.Button(button_frame, text='Decrypt', width=12, command=decrypt_message)
decrypt_button.pack(side='left', padx=8)

clear_button = tk.Button(button_frame, text='Clear', width=12, command=clear_fields)
clear_button.pack(side='left')

output_label = tk.Label(root, text='Output:')
output_label.pack(anchor='w', padx=12, pady=(2, 4))

output_text = tk.Text(root, height=8, wrap='word')
output_text.pack(fill='both', expand=True, padx=12, pady=(0, 4))

status_frame = tk.Frame(root)
status_frame.pack(fill='x', padx=12, pady=(0, 10))

tk.Label(status_frame, text='Bytes saved:').pack(side='left')
bytes_saved_entry = tk.Entry(status_frame, textvariable=bytes_saved_var, state='readonly',
                             relief='flat', fg='green', width=40)
bytes_saved_entry.pack(side='left', padx=(6, 0))

root.mainloop()
