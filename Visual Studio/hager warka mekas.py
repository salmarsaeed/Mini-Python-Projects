import tkinter as tk
import random

# الاختيارات الممكنة
choices = ["حجرة", "ورقة", "مقص"]

# تحديد الفائز
def determine_winner(user, computer):
    if user == computer:
        return "تعادل!"
    elif (user == "حجرة" and computer == "مقص") or \
         (user == "ورقة" and computer == "حجرة") or \
         (user == "مقص" and computer == "ورقة"):
        return "أنت فزت!"
    else:
        return "الكمبيوتر فاز!"

# لما اللاعب يختار زر
def play(user_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)

    user_label.config(text=f"أنت اخترت: {user_choice}")
    computer_label.config(text=f"الكمبيوتر اختار: {computer_choice}")
    result_label.config(text=f"النتيجة: {result}")

# إنشاء نافذة
window = tk.Tk()
window.title("لعبة حجرة ورقة مقص")
window.geometry("400x300")
window.config(bg="white")

# العنوان
title_label = tk.Label(window, text="اختر واحد:", font=("Arial", 18, "bold"), bg="white")
title_label.pack(pady=10)

# أزرار الاختيارات
button_frame = tk.Frame(window, bg="white")
button_frame.pack()

rock_button = tk.Button(button_frame, text="حجرة", width=10, font=("Arial", 14), command=lambda: play("حجرة"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="ورقة", width=10, font=("Arial", 14), command=lambda: play("ورقة"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="مقص", width=10, font=("Arial", 14), command=lambda: play("مقص"))
scissors_button.grid(row=0, column=2, padx=10)

# عرض النتائج
user_label = tk.Label(window, text="", font=("Arial", 12), bg="white")
user_label.pack(pady=5)

computer_label = tk.Label(window, text="", font=("Arial", 12), bg="white")
computer_label.pack(pady=5)

result_label = tk.Label(window, text="", font=("Arial", 14, "bold"), bg="white", fg="blue")
result_label.pack(pady=10)

# تشغيل الواجهة
window.mainloop()
