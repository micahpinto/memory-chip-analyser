import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from collections import Counter


def count_bit_blocks(file_path, block_size):
    """
    Counts bit patterns of 'block_size' bits without overlapping.
    Optimized reading with bit register.
    """

    counter = Counter()

    register = 0
    bit_count = 0

    with open(file_path, "rb") as f:

        while True:

            chunk = f.read(4096)

            if not chunk:
                break

            for byte in chunk:

                # Add the 8 bits of the byte to the register
                register = (register << 8) | byte
                bit_count += 8

                # Extract complete blocks
                while bit_count >= block_size:

                    shift = bit_count - block_size

                    pattern = register >> shift

                    counter[pattern] += 1

                    bit_count -= block_size

                    mask = (1 << bit_count) - 1
                    register &= mask

    return counter


def choose_file():
    file_name = filedialog.askopenfilename(
        title="Choose a file",
        filetypes=[("All files", "*.*")]
    )

    if file_name:
        file_var.set(file_name)


def analyse():

    file_path = file_var.get()

    if not file_path:
        messagebox.showerror("Error", "Please choose a file.")
        return

    block_size = int(block_size_var.get())

    counter = count_bit_blocks(file_path, block_size)

    total = sum(counter.values())

    text_widget.delete("1.0", tk.END)

    text_widget.insert(tk.END, f"File: {file_path}\n")
    text_widget.insert(tk.END, f"Blocks of {block_size} bits\n\n")

    text_widget.insert(
        tk.END,
        f"{'Pattern':<8}{'Occurrences':>12}{'Frequency':>15}\n"
    )

    text_widget.insert(
        tk.END,
        "-" * 38 + "\n"
    )

    for i in range(2 ** block_size):

        pattern = format(i, f"0{block_size}b")

        count = counter[i]

        freq = count / total if total else 0

        text_widget.insert(
            tk.END,
            f"{pattern:<8}{count:>12}{freq:>15.6f}\n"
        )

    text_widget.insert(tk.END, "\n")
    text_widget.insert(tk.END, f"Total number of blocks: {total}\n")


# ============== Graphical User Interface ==============

window = tk.Tk()
window.title("Binary Pattern Analyser")
window.geometry("700x600")

file_var = tk.StringVar()

ttk.Label(window, text="File:").pack(anchor="w", padx=10, pady=(10, 0))

frame = ttk.Frame(window)
frame.pack(fill="x", padx=10)

ttk.Entry(frame, textvariable=file_var).pack(
    side="left",
    fill="x",
    expand=True
)

ttk.Button(
    frame,
    text="Browse...",
    command=choose_file
).pack(side="left", padx=5)

ttk.Label(window, text="Block Size").pack(anchor="w", padx=10, pady=(10, 0))

block_size_var = tk.StringVar(value="2")

ttk.Combobox(
    window,
    textvariable=block_size_var,
    values=("2", "3", "4"),
    state="readonly",
    width=5
).pack(anchor="w", padx=10)

ttk.Button(
    window,
    text="Analyse",
    command=analyse
).pack(pady=10)

text_widget = tk.Text(
    window,
    font=("Courier New", 11)
)

text_widget.pack(fill="both", expand=True, padx=10, pady=10)

window.mainloop()
