import subprocess
import threading
import re
import os


class ClipboardWatcher:
    def __init__(self):
        self.clip = self.get_clipboard_data()

    def get_clipboard_data(self):
        p = subprocess.Popen(["pbpaste"], stdout=subprocess.PIPE)
        p.wait()
        data = p.stdout.read()
        return data.decode("utf-8")

    def check_for_clipboard_change(self):
        threading.Timer(0.5, self.check_for_clipboard_change).start()
        new_clip = self.get_clipboard_data()

        if self.clip != new_clip:
            self.clip = new_clip
            print("Clipboard changed")

            match = re.findall(r"\d+\.\n(?:.*\n){3}(.*)", self.clip)
            out = "\n".join(match)

            try:
                with open("../data/list_of_company_names_raw.csv", "a") as file:
                    file.write("\n" + out)
            except Exception as e:
                print(f"Error writing to file: {e}")


if __name__ == "__main__":
    watcher = ClipboardWatcher()
    watcher.check_for_clipboard_change()
