import tkinter as tk
import cv2
import qrcode
import win32clipboard

# Create a window
window = tk.Tk()

# Set the window title
window.title("Text Input")

# Create a label
label = tk.Label(window, text="Enter some text or copy it to the clipboard:")
label.pack()

# Create a text entry field
text_entry = tk.Entry(window)
text_entry.pack()

# Function to print the text input and display QR code
def print_text():
    # Get text from text entry or clipboard
    if text_entry.get() != "":
        text = text_entry.get()
    else:
        win32clipboard.OpenClipboard()
        text = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

    # Generate QR code image
    img = qrcode.make(text)
    img.save("img.png")

    # Load QR code image using OpenCV
    image = cv2.imread("img.png")

    # Display QR code image using OpenCV
    cv2.imshow("QR Code", image)
    cv2.waitKey(0)

    print("You entered:", text)

# Create a button to print the text input and display QR code
button = tk.Button(window, text="Submit", command=print_text)
button.pack()

# Bind event handler to focus in event
def on_focus_in(event):
    # Get contents of clipboard
    win32clipboard.OpenClipboard()
    clipboard_text = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    
    # Set contents of text box to clipboard contents
    text_entry.delete(0, tk.END)
    text_entry.insert(tk.END, clipboard_text)

window.bind("<FocusIn>", on_focus_in)

# Run the window
window.mainloop()
