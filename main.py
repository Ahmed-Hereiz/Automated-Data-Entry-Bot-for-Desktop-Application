import platform
import sys
import argparse
from pathlib import Path
import os

def clean_output_directory():
    output_dir = Path("output")
    if output_dir.exists() and output_dir.is_dir():
        for file in output_dir.iterdir():
            if file.is_file():
                file.unlink()
            elif file.is_dir():
                import shutil
                shutil.rmtree(file)

def run_automation(num_posts):
    os_name = platform.system()
    print(f"Detected OS: {os_name}")
    try:
        if os_name == "Windows":
            from main_windows import NotepadAutomationBot
            bot = NotepadAutomationBot()
            bot.action(num_posts=num_posts)
        elif os_name == "Linux":
            from main_linux import NanoAutomationBot
            bot = NanoAutomationBot()
            bot.action(num_posts=num_posts)
        else:
            raise Exception(f"Unsupported operating system: {os_name}")
    except Exception as e:
        print(f"Error running automation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated Data Entry Bot")
    parser.add_argument(
        "--num-posts", type=int, default=10,
        help="Number of posts to process (default: 10)"
    )
    args = parser.parse_args()

    clean_output_directory()  # Delete files in output/ before proceeding
    run_automation(num_posts=args.num_posts)
