Sure, here's a README file in English for the provided code:

```markdown
# Custom Tkinter Client Search Layout

This code implements a graphical user interface (GUI) layout using Custom Tkinter to facilitate client search functionality.

## About

The layout is designed to perform searches for clients using Custom Tkinter, a customized version of the Tkinter library in Python.

```python
import customtkinter
from tkinter import *
import json
import os

# Setting appearance mode and color theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Creating a window
window = customtkinter.CTk()
window.geometry("800x600")
window.title("Search Data")
window.resizable(False, False)  # Restrict window resize

# Defining fonts using Custom Tkinter
# ...

# Creating StringVar to store entries
cpf_var = customtkinter.StringVar()

# Creating frames, labels, entries, buttons, and canvas elements
# ...

# Configuring a canvas for data layout
# ...

# Displaying information labels
# ...

# Loading images (commented out)
# ...

window.mainloop()
```

## How to Use

The code creates a GUI layout for searching client data. It sets up a window and various widgets like labels, entry fields, buttons, and a canvas for displaying information.

## Licensing

This code is provided under the "All Rights reserved ©" policy for Mugiwara's Corp.

## Credits

- This layout was developed using the Custom Tkinter library.
- Mugiwara's Corp. owns all rights to the code and associated elements.

For implementation details, feel free to refer to the code provided.
```

This README briefly explains the purpose of the code, describes its functionalities, highlights the usage, licensing information, and credits to Mugiwara's Corp.
