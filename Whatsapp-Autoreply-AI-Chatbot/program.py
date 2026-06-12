import pyautogui
import time
import pyperclip

from openai import OpenAI



client = OpenAI(
    api_key="your_api_key_here"
)


def is_last_message_from_sender(chat_log, sender_name="jagruthi"):
    # Split the chat into individual messages
    message = chat_log.strip().split("/2026]")[-1]

    if sender_name in message:    
        return True
    return False


def run():
    

    # Step 1: Click on the chrome icon at coordinates (1639, 1412)
    pyautogui.click(1639, 1412)
    time.sleep(1)    

    while True:

        # Step 2: Drag the mouse from (1003,237) to select the text
        pyautogui.moveTo(1003, 237)
        pyautogui.dragTo(1499, 1268, duration=1.0, button="left")

        # Step 3: Copy the selected text to the clipboard
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)

        # Step 4: Retrieve the text from the clipboard
        chat_history = pyperclip.paste()
        print(chat_history)

        if is_last_message_from_sender(chat_history):

            
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a person name naruto who speaks in hindi as well english. You are from india and You are coder. You analyze chat history and respond like naruto. Output should be the next chat response as naruto."
                    },
                    {"role": "user", "content": chat_history}
                ]
            )

            response = completion.choices[0].message.content  
            pyperclip.copy(response)

            # Step 5: Click at coordinates (1808, 1328)
            pyautogui.click(1808, 1328)
            time.sleep(1)

            # Step 6: Paste the text
            pyautogui.hotkey('ctrl', 'v')  
            time.sleep(1)

            # Step 7: Press enter
            pyautogui.press('enter')


if __name__ == "__main__":
    run()

