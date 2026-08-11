import customtkinter as ctk
from assistant import process
from translations import TEXTS
import threading


class Interface :


    def __init__(self):

        self.window = ctk.CTk()

        self.window.title("AI Smart Assistant")

        self.window.geometry("1200x750")

        self.window.grid_rowconfigure(0, weight=1)
        
        self.window.grid_columnconfigure(0, weight=1)
        
        self.main_frame = ctk.CTkScrollableFrame(self.window, fg_color="transparent")
        
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        
        self.main_frame.grid_columnconfigure((0, 1), weight=0)

        self.last_answer = ""

        self.placeholder = True

        self.is_answering = False

        self.request_id = 0

        self.language = "EN"

        self.is_copied = False

        self.title = ctk.CTkLabel(

            self.main_frame,

            text=TEXTS[self.language]["title"],

            font=("Arial", 28, "bold")

        )

        self.subtitle = ctk.CTkLabel(

            self.main_frame,

            text=TEXTS[self.language]["sub"],

            font=("Arial", 20)

        )

        self.messages_box = ctk.CTkTextbox(
        
            self.main_frame,

            width=600,

            height=500,

            wrap="word",

            state="disabled"
        
        )

        self.textbox = ctk.CTkTextbox(

            self.main_frame,

            width=400,

            height=25,

            wrap="word",

        )

        self.send_button = ctk.CTkButton(

            self.main_frame,

            command=self.send,

            text=TEXTS[self.language]["send"]

        )

        self.reset_button = ctk.CTkButton(

            self.main_frame,

            command=self.reset,

            text=TEXTS[self.language]["reset"]

        )

        self.language_button = ctk.CTkButton(

            self.main_frame,

            command=self.change_language,

            text=TEXTS[self.language]["lang"]

        )

        self.copy_button = ctk.CTkButton(
        
            self.main_frame,
        
            command=self.copy_answer,
        
            text=TEXTS[self.language]["copy"],

            state="disabled"
        
        )

        self.messages_box.tag_config(
                
            "user",
                
            justify="left"
                
        )
        
        self.messages_box.tag_config(
                
            "assistant",
                
            justify="left"
                
        )

        self.textbox.tag_config(
        
            "placeholder",
        
            justify="left"
        
        )
        
        self.textbox.insert("1.0", TEXTS[self.language]["box"], "placeholder")
        
        self.textbox.bind("<FocusIn>", self.remove_placeholder)
        
        self.textbox.bind("<FocusOut>", self.restore_placeholder)

        self.textbox.bind("<Return>", self.send_with_enter)
                
        self.textbox.bind("<Shift-Return>", self.return_back)


        self.title.grid(row=0, column=0, columnspan=3, padx=20, pady=(20,5))

        self.subtitle.grid(row=1, column=0, columnspan=3, padx=20, pady=(0,20))

        self.messages_box.grid(row=2, column=0, columnspan=3, padx=20, pady=20)

        self.textbox.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

        self.send_button.grid(row=3, column=2, padx=20, pady=20)

        self.reset_button.grid(row=4, column=0, padx=20, pady=20)

        self.language_button.grid(row=4, column=1, padx=20, pady=20)

        self.copy_button.grid(row=4, column=2, padx=20, pady=20)


    def run(self):

        self.window.mainloop()


    def send(self):

        self.is_answering = True

        text = self.textbox.get("1.0", "end").strip()

        self.send_button.configure(
                
            text=TEXTS[self.language]["answering"],
        
            state="disabled"
                
        )

        self.copy_button.configure(state="disabled")

        self.display_user_message(text)


    def display_user_message(self, text):

        if not text :

            self.last_answer = ""

            self.is_answering = False

            self.messages_box.configure(state="normal")

            self.messages_box.insert("end", f'🤖 {TEXTS[self.language]["assistant"]}\n{TEXTS[self.language]["no_text"]}\n', "assistant")

            self.messages_box.see("end")

            self.messages_box.configure(state="disabled")

            self.textbox.delete("1.0", "end")

            self.send_button.configure(

                command=self.send,
                
                text=TEXTS[self.language]["send"],

                state="normal"
    
            )

            return
        
        else:

            self.messages_box.configure(state="normal")

            self.messages_box.insert("end", f"👤 {TEXTS[self.language]["user"]}\n{text}\n\n", "user")

            self.messages_box.insert("end", f"🤖 {TEXTS[self.language]["assistant"]}\n", "assistant")

            self.messages_box.see("end")

            self.messages_box.configure(state="disabled")

            self.request_id += 1

            request_id = self.request_id

            threading.Thread(

                target=self.assistant,

                args=(text, request_id),

                daemon=True

            ).start()


    def assistant(self, text, request_id):

        try:

            result = process(text)

        except Exception as error:

            self.windw.after(

                0,

                self.display_error,

                error,

                request_id

            )

            return
        
        self.window.after(

            0,

            self.display_answer,

            result,

            request_id

        )


    def display_error(self, error, request_id):

        if request_id != self.request_id:
        
            return

        self.last_answer = ""
        
        self.is_answering = False

        self.messages_box.configure(state="normal")

        self.messages_box.insert("end", f'🤖 {TEXTS[self.language]["assistant"]}\n{TEXTS[self.language]["error"]} : {error}\n', "assistant")
        
        self.messages_box.see("end")
        
        self.messages_box.configure(state="disabled")
                    
        self.send_button.configure(
                                        
            text=TEXTS[self.language]["send"],

            state="normal"
                                        
        )


    def display_answer(self, result, request_id):

        if request_id != self.request_id:
        
            return

        self.last_answer = result

        self.is_answering = False

        self.messages_box.configure(state="normal")

        self.messages_box.insert("end", f"{result}\n\n", "assistant")

        self.messages_box.see("end")

        self.messages_box.configure(state="disabled")

        self.send_button.configure(

            text=TEXTS[self.language]["send"],

            state="normal"
            
        )

        self.copy_button.configure(state="normal")


    def copy_answer(self):

        self.is_copied = True
        
        self.window.clipboard_clear()

        self.window.clipboard_append(self.last_answer)

        self.copy_button.configure(text=TEXTS[self.language]["copied"])

        self.send_button.configure(state="disabled")

        self.window.after(1000, self.reset_copy)


    def reset_copy(self):

        self.is_copied = False

        self.copy_button.configure(text=TEXTS[self.language]["copy"])

        self.send_button.configure(state="normal")


    def send_with_enter(self, event):

        self.send()

        return "break"


    def return_back(self, event):

        self.textbox.insert("end", f"\n")

        return "break"


    def remove_placeholder(self, event):

        if self.placeholder:

            self.textbox.delete("1.0", "end")

            self.placeholder = False


    def restore_placeholder(self, event):

        text = self.textbox.get("1.0", "end").strip()

        if not text:

            self.textbox.insert("1.0", TEXTS[self.language]["box"], "placeholder")

            self.placeholder = True


    def reset(self):

        self.request_id += 1

        self.placeholder = True

        self.messages_box.configure(state="normal")
        
        self.messages_box.delete("1.0", "end")
        
        self.messages_box.configure(state="disabled")
    
        self.textbox.delete("1.0", "end")

        self.textbox.insert("1.0", TEXTS[self.language]["box"], "placeholder")

        self.send_button.configure(

            command=self.send,
 
            text=TEXTS[self.language]["send"],

            state="normal"
    
        )
        
        self.copy_button.configure(

            command=self.copy_answer,

            text=TEXTS[self.language]["copy"],

            state="disabled"

        )


    def change_language(self):

        if self.language == "EN":

            self.language = "FR"

        else:

            self.language = "EN"

        self.title.configure(
        
            text=TEXTS[self.language]["title"],

            font=("Arial", 28, "bold")
        
        )
        
        self.subtitle.configure(
        
            text=TEXTS[self.language]["sub"],

            font=("Arial", 20)
        
        )

        if self.placeholder:

            self.textbox.delete("1.0", "end")

            self.textbox.insert("1.0", TEXTS[self.language]["box"], "placeholder")
        
        if self.is_answering:

            self.send_button.configure(
        
                text=TEXTS[self.language]["answering"]
        
            )

        else:

            self.send_button.configure(

                command=self.send,

                text=TEXTS[self.language]["send"]

            )
        
        self.reset_button.configure(
        
            command=self.reset,
        
            text=TEXTS[self.language]["reset"]
        
        )
        
        self.language_button.configure(
        
            command=self.change_language,
        
            text=TEXTS[self.language]["lang"]
        
        )

        if self.is_copied:

            self.copy_button.configure(
        
                text=TEXTS[self.language]["copied"]
        
            )

        else:

            self.copy_button.configure(

                command=self.copy_answer,

                text=TEXTS[self.language]["copy"]

            )