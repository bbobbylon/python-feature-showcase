"""
todo_app.py
============

A small desktop GUI (Graphical User Interface) to-do list app, built with
`tkinter` -- a GUI toolkit that ships with Python itself (no installation
needed). This demonstrates how Python can build actual clickable windowed
applications, not just terminal programs.

Analogy: If the CLI ("Command Line Interface") apps in this project are
like giving instructions to a program by typing them on a walkie-talkie,
a GUI app is like a control panel with buttons and screens you can point
at and click. Tkinter is Python's built-in "control panel builder."

Key GUI concepts demonstrated here:
    - The EVENT LOOP: GUI apps don't run top-to-bottom once like a script;
      they start a loop that waits for events (a click, a key press) and
      reacts to them. `root.mainloop()` at the bottom is what starts this.
    - WIDGETS: buttons, text boxes, and lists are all "widgets" -- visual
      building blocks you compose to build a window.
    - CALLBACKS: functions you attach to a widget (like a button) that run
      automatically WHEN a user interacts with it (a click "calls back"
      into your code).
"""

from __future__ import annotations

import tkinter as tk
from dataclasses import dataclass
from tkinter import messagebox


@dataclass
class ToDoItem:
    """A single to-do list entry. See oop_showcase.py for more on @dataclass."""

    text: str
    done: bool = False


class ToDoApp:
    """
    The whole app is wrapped in a class so its pieces (the window, the
    widgets, the data) can all be reached via `self` instead of scattered
    global variables -- the same organizing idea as the classes in
    oop_showcase.py, just applied to a GUI instead of a data model.
    """

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Python To-Do List (tkinter demo)")
        self.root.geometry("420x480")

        self.items: list[ToDoItem] = []

        # --- Widgets: an entry box + "Add" button on top ---
        entry_frame = tk.Frame(root, padx=10, pady=10)
        entry_frame.pack(fill=tk.X)

        self.entry = tk.Entry(entry_frame, font=("Helvetica", 12))
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        # Pressing Enter in the text box also adds the item -- an event binding.
        self.entry.bind("<Return>", lambda event: self.add_item())

        add_button = tk.Button(entry_frame, text="Add", command=self.add_item)
        add_button.pack(side=tk.LEFT, padx=(8, 0))

        # --- Widgets: the scrollable list of to-do items ---
        list_frame = tk.Frame(root, padx=10)
        list_frame.pack(fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(list_frame, font=("Helvetica", 12), selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # Double-clicking an item toggles it done/not-done.
        self.listbox.bind("<Double-Button-1>", lambda event: self.toggle_selected())

        scrollbar = tk.Scrollbar(list_frame, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        # --- Widgets: action buttons on the bottom ---
        button_frame = tk.Frame(root, padx=10, pady=10)
        button_frame.pack(fill=tk.X)

        tk.Button(button_frame, text="Toggle Done", command=self.toggle_selected).pack(
            side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 4)
        )
        tk.Button(button_frame, text="Delete", command=self.delete_selected).pack(
            side=tk.LEFT, expand=True, fill=tk.X, padx=(4, 0)
        )

        # Seed with a couple of example items so the window isn't empty on launch.
        for sample_text in ["Learn Python basics", "Build a GUI app", "Try the mini games"]:
            self.items.append(ToDoItem(text=sample_text))
        self._refresh_listbox()

    def add_item(self) -> None:
        """Callback for the 'Add' button and pressing Enter in the text box."""
        text = self.entry.get().strip()
        if not text:
            return  # ignore empty submissions
        self.items.append(ToDoItem(text=text))
        self.entry.delete(0, tk.END)  # clear the text box
        self._refresh_listbox()

    def toggle_selected(self) -> None:
        """Callback for 'Toggle Done' and double-clicking a list entry."""
        index = self._get_selected_index()
        if index is None:
            return
        self.items[index].done = not self.items[index].done
        self._refresh_listbox()

    def delete_selected(self) -> None:
        """Callback for the 'Delete' button."""
        index = self._get_selected_index()
        if index is None:
            return
        removed = self.items.pop(index)
        self._refresh_listbox()
        messagebox.showinfo("Deleted", f"Removed: {removed.text}")

    def _get_selected_index(self) -> int | None:
        selection = self.listbox.curselection()
        return selection[0] if selection else None

    def _refresh_listbox(self) -> None:
        """
        Re-draws the listbox from self.items. Simplest possible way to keep
        the UI in sync with the data -- clear it and rebuild it every time
        something changes. (Larger apps use more efficient patterns, but
        this keeps the concept crystal clear.)
        """
        self.listbox.delete(0, tk.END)
        for item in self.items:
            prefix = "[x]" if item.done else "[ ]"
            self.listbox.insert(tk.END, f"{prefix} {item.text}")


def launch() -> None:
    """
    Entry point called from main.py. Creates the root tkinter window and
    starts the event loop.

    IMPORTANT: `root.mainloop()` BLOCKS -- your program pauses here and
    waits for GUI events until the window is closed. That's normal and
    expected for GUI apps (compare to the games in games/, which loop on
    text input instead of window events).
    """
    root = tk.Tk()
    ToDoApp(root)
    root.mainloop()


if __name__ == "__main__":
    launch()
