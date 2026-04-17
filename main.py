# 7. Personalizatsiyalangan salomlashuv
def personalized_greeting(name, lang="uz"):
    greetings = {
        "uz": f"Salom, {name}!",
        "en": f"Hello, {name}!",
        "ru": f"Привет, {name}!"
    }
    print(greetings.get(lang.lower(), f"Salom, {name}!"))

# 8. Raqamlarning kvadrati
def square_numbers(numbers):
    for num in numbers:
        print(num ** 2, end=" ")
    print()

# 9. Matnni formatlash
def format_text(text, style="katta"):
    if style == "katta":
        print(text.upper())
    elif style == "kichik":
        print(text.lower())
    elif style == "teskari":
        print(text[::-1])
    else:
        print(text)

# 10. Intervaldagi juft raqamlar
def even_numbers(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i, end=" ")
    print()

# 11. Foydalanuvchi ma’lumotlari
def user_info(name, age, city):
    print(f"Hurmatli {name}, siz {age} yoshdasiz va {city}da yashaysiz.")

# 12. Ro‘yxat statistikasi
def list_statistics(numbers):
    print(f"Yig‘indi: {sum(numbers)}")
    print(f"O‘rtacha: {sum(numbers)/len(numbers):.2f}")
    print(f"Eng katta: {max(numbers)}")

# Testlar
personalized_greeting("Aziz", "en")
square_numbers([2, 4, 6, 8])
format_text("Python dasturlash", "teskari")
even_numbers(1, 20)
user_info("Laylo", 22, "Toshkent")
list_statistics([10, 20, 30, 40, 50])
