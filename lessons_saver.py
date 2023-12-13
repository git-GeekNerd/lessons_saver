import pyautogui
import os
import time
import fade

from PIL import Image, ImageGrab, ImageDraw, ImageFont
from datetime import datetime
from colorama import Fore, Style

class ScreenshotsCreator:
    def __init__(self):
        # Initialize variables and constants
        self.num_screenshots = 0
        self.scroll_amount = 249
        self.region = (217, 218, 1703, 869)  # Coordinates of the region to capture

    def info_msg(self, message):
        # Display informational messages in the console
        print(Fore.WHITE + '[' + Fore.YELLOW + Style.BRIGHT + 'INFO' + Fore.WHITE + '] ' +
              Fore.GREEN + f'{message}' + Style.RESET_ALL)

    def path_msg(self, message):
        # Display path-related messages in the console
        print(Fore.WHITE + '[' + Fore.CYAN + Style.BRIGHT + 'PATH' + Fore.WHITE + '] ' +
              Fore.BLUE + f'{message}' + Style.RESET_ALL)

    def header_msg(self, message):
        # Display header messages in the console
        print(Fore.YELLOW + Style.BRIGHT + f'\n[{message}]' + Style.RESET_ALL)

    def create_screenshots_folder(self):
        # Create a folder to store screenshots and an instruction file
        documents_folder = os.path.expanduser('~\Documents')
        folder_name = os.path.join(documents_folder, "lessons_saver")

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            self.path_msg(f"Folder successfully created at: '{folder_name}'")

        instruction_file_path = os.path.join(folder_name, "instruction.txt")

        with open(instruction_file_path, 'w', encoding='utf-8') as file:
            file.write("\t\t\tUsage Instructions:\n\n This program takes screenshots and stitches them together." 
                " It is capable of creating long screenshots, for instance, in future code." 
                " If you need to send someone a screenshot from top to bottom but don't know how to do it," 
                " this program will come to your aid!\n\n\n\n\t\t\t#User Guide\n\n\n\n1) Open the program\n2)" 
                " Enter the number of screenshots\n3) After 3 seconds, the program will start scrolling down." 
                " After entering the number of pages, switch to the tab in your browser where you want to take a long screenshot!" 
                " For example, https://www.wikipedia.org | The program will scroll down and take screenshots; the process takes less than five seconds.")

        self.info_msg(f"File with instruction was created in: {Fore.CYAN + instruction_file_path + Fore.GREEN}")
        return folder_name

    def take_screenshots_with_scroll(self):
        # Capture screenshots, annotate them, and save to the specified folder
        folder_name = self.create_screenshots_folder()
        screenshot_width, screenshot_height = self.region[2] - self.region[0], self.region[3] - self.region[1]

        self.header_msg("Start of the screenshot creation process")

        msg_up = '╔════════════╦════════════╦════════════╦════════════╦════════════╦════════════╦════════════╦════════════╗\n'
        print(Fore.RED + Style.BRIGHT + msg_up + Style.RESET_ALL)

        for i in range(self.num_screenshots):
            # Capture, annotate, and save each screenshot
            self.info_msg(f"Creating screenshot {Fore.MAGENTA + str(i + 1) + Fore.GREEN}")

            screenshot = ImageGrab.grab(bbox=self.region)
            draw = ImageDraw.Draw(screenshot)
            font = ImageFont.truetype("arial.ttf", 30)

            if i == 0:
                # Add date only to the first screenshot
                date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                draw.text((screenshot_width - 300, screenshot_height - 40), date_time, fill="purple", font=font)

            draw.text((10, 10), f"# {i + 1}", fill="green", font=font)


            screenshot_path = os.path.join(folder_name, f"screenshot_{i + 1}.png")
            screenshot.save(screenshot_path)

            self.path_msg(f"\t\tScreenshot {Fore.MAGENTA + str(i + 1) + Fore.GREEN} was saved in: {Fore.CYAN + screenshot_path + Fore.GREEN}")

            if i == self.num_screenshots - 1:
                # Add date only to the last screenshot
                date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                draw.text((screenshot_width - 300, (i + 1) * screenshot_height - 40), date_time, fill="purple", font=font)

            pyautogui.scroll(-self.scroll_amount)
            time.sleep(0.01)

        combined_image = Image.new("RGB", (screenshot_width, self.num_screenshots * screenshot_height))
        y_offset = 0

        for i in range(self.num_screenshots):
            # Combine saved screenshots into a single image
            img_path = os.path.join(folder_name, f"screenshot_{i + 1}.png")
            img = Image.open(img_path)
            combined_image.paste(img, (0, y_offset))
            y_offset += img.height

        combined_screenshot_path = os.path.join(folder_name, "combined_screenshot.png")
        combined_image.save(combined_screenshot_path)

        self.info_msg(f"Complete screenshot saved: {Fore.CYAN + combined_screenshot_path + Fore.GREEN}")

        msg_down = '╚════════════╩════════════╩════════════╩════════════╩════════════╩════════════╩════════════╩════════════╝\n'
        print(Fore.RED + Style.BRIGHT + msg_down + Style.RESET_ALL)

        combined_image = Image.new("RGB", (screenshot_width, self.num_screenshots * screenshot_height))
        y_offset = 0

        for i in range(self.num_screenshots):
            # Combine saved screenshots into a single image
            img_path = os.path.join(folder_name, f"screenshot_{i + 1}.png")
            img = Image.open(img_path)
            combined_image.paste(img, (0, y_offset))
            y_offset += img.height

        combined_screenshot_path = os.path.join(folder_name, "combined_screenshot.png")
        combined_image.save(combined_screenshot_path)

        self.info_msg(f"Complete screenshot saved: {Fore.CYAN + combined_screenshot_path + Fore.GREEN}")

        msg_down = '╚════════════╩════════════╩════════════╩════════════╩════════════╩════════════╩════════════╩════════════╝\n'
        print(Fore.RED + Style.BRIGHT + msg_down + Style.RESET_ALL)

    def run_program(self):
        # Main program execution
        start_text = (
            '██╗░░░░░███████╗░██████╗░██████╗░█████╗░███╗░░██╗░██████╗░░░░░░░██████╗░█████╗░██╗░░░██╗███████╗██████╗░\n'
            '██║░░░░░██╔════╝██╔════╝██╔════╝██╔══██╗████╗░██║██╔════╝░░░░░░██╔════╝██╔══██╗██║░░░██║██╔════╝██╔══██╗\n'
            '██║░░░░░█████╗░░╚█████╗░╚█████╗░██║░░██║██╔██╗██║╚█████╗░█████╗╚█████╗░███████║╚██╗░██╔╝█████╗░░██████╔╝\n'
            '██║░░░░░██╔══╝░░░╚═══██╗░╚═══██╗██║░░██║██║╚████║░╚═══██╗╚════╝░╚═══██╗██╔══██║░╚████╔╝░██╔══╝░░██╔══██╗\n'
            '███████╗███████╗██████╔╝██████╔╝╚█████╔╝██║░╚███║██████╔╝░░░░░░██████╔╝██║░░██║░░╚██╔╝░░███████╗██║░░██║\n'
            '╚══════╝╚══════╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░░░░░░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝\n'
        )

        print(fade.greenblue(start_text))


        self.header_msg("Program start")
        try:
            # User input for the number of screenshots
            self.num_screenshots = int(input("Enter the number of screenshots: "))

            start_time = time.time()
            time.sleep(3)
            self.take_screenshots_with_scroll()
            end_time = time.time()

            total_time = end_time - start_time
            avg_time_per_screenshot = total_time / self.num_screenshots

            self.info_msg(f"\t\tTotal {Fore.MAGENTA + str(self.num_screenshots) + Fore.GREEN} screenshots created in the region {Fore.CYAN + str(self.region) + Fore.GREEN}")
            self.info_msg(f"\t\tTotal execution time: {Fore.MAGENTA + f'{total_time:.2f}' + Fore.GREEN} seconds")
            self.info_msg(f"\t\tAverage time per screenshot: {Fore.MAGENTA + f'{avg_time_per_screenshot:.2f}' + Fore.GREEN} seconds\n")

            # Add author information and GitHub link
            print(Fore.YELLOW + Style.BRIGHT + "=" * 60)
            author_info = f"{Fore.BLUE}Author: {Fore.CYAN}git-GeekNerd{Fore.GREEN}"
            github_info = f"{Fore.BLUE}GitHub: {Fore.CYAN}https://github.com/git-GeekNerd/lessons_saver{Fore.GREEN}"

            self.info_msg(author_info)
            self.info_msg(github_info)

            print('\n')

            # Ask if the user wants to run the program again
            run_again = input("Press Enter to exit or [Y] for again... ").strip().lower()
            if run_again == 'y':
                self.run_program()
            else:
                print("Program exited.")


        except ValueError:
            self.info_msg("Input error. Please enter valid numbers.")


if __name__ == "__main__":
    # Instantiate and run the ScreenshotsCreator class
    creator = ScreenshotsCreator()
    creator.run_program()
