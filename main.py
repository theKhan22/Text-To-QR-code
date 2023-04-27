import tkinter as tk
import cv2
import qrcode
import win32clipboard


window = tk.Tk()


window.title("Text Input")


label = tk.Label(window, text="Enter some text or copy it to the clipboard:")
label.pack()


text_entry = tk.Entry(window)
text_entry.pack()


def print_text():
    # Get text from text entry or clipboard
    if text_entry.get() != "":
        text = text_entry.get()
    else:
        win32clipboard.OpenClipboard()
        text = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

    
    img = qrcode.make(text)
    img.save("img.png")

   
    image = cv2.imread("img.png")

 
    cv2.imshow("QR Code", image)
    cv2.waitKey(0)

    print("You entered:", text)


button = tk.Button(window, text="Submit", command=print_text)
button.pack()


def on_focus_in(event):
    
    win32clipboard.OpenClipboard()
    clipboard_text = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    
    
    text_entry.delete(0, tk.END)
    text_entry.insert(tk.END, clipboard_text)

window.bind("<FocusIn>", on_focus_in)

# Run the window
window.mainloop()
