import os
import requests
import pyautogui
from botcity.core import DesktopBot
from time import sleep
from datetime import datetime
from pathlib import Path 

class NotepadAutomationBot(DesktopBot):
    def __init__(self):
        super().__init__()
        self.project_dir = Path.cwd() / "output"
        self.api_url = "https://jsonplaceholder.typicode.com/posts"
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.5

    def setup_environment(self):
        try:
            self.project_dir.mkdir(parents=True, exist_ok=True)
        except OSError as e:
            raise Exception(f"Failed to create project directory: {e}")

    def fetch_posts(self):
        try:
            response = requests.get(self.api_url, timeout=10)
            response.raise_for_status()
            return response.json()[:10]
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch posts from API: {e}")

    def launch_notepad(self):
        try:
            os.startfile("notepad.exe")
            sleep(2)
        except (OSError, FileNotFoundError) as e:
            raise Exception(f"Failed to launch Notepad: {e}")

    def type_post(self, post):
        try:
            title = post.get("title", "Untitled")
            body = post.get("body", "No content")
            post_id = post.get("id", 1)
            
            pyautogui.write(title + "\n\n", interval=0.02)
            pyautogui.write(body + "\n", interval=0.02)
            
            return post_id
        except Exception as e:
            raise Exception(f"Failed to type post: {e}")

    def save_file(self, post_id):
        try:
            filename = f"post_{post_id}.txt"
            file_path = os.path.join(self.project_dir, filename)
            
            pyautogui.hotkey("ctrl", "s")
            sleep(1)
            pyautogui.write(file_path)
            pyautogui.press("enter")
            sleep(1)
            pyautogui.hotkey("alt", "f4")
            sleep(1)
        except Exception as e:
            raise Exception(f"Failed to save file: {e}")


    def action(self, num_posts=None):
        self.setup_environment()
        posts = self.fetch_posts()

        if num_posts is not None:
            posts = posts[:num_posts]

        for post in posts:
            try:
                self.launch_notepad()
                post_id = self.type_post(post)
                self.save_file(post_id)
            except Exception as e:
                print(f"Error processing post {post.get('id', 'unknown')}: {e}")
                pyautogui.hotkey("alt", "f4")
                sleep(1)
                continue


if __name__ == "__main__":
    bot = NotepadAutomationBot()
    try:
        bot.action(2)
    except Exception as e:
        print(f"Error: {e}")