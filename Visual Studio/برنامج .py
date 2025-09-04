# -*- coding: utf-8 -*-
import datetime

# قاعدة بيانات المنتجات (اسم: [السعر, الكمية])
products = {
    "مروحة": [150.0, 10],
    "ثلاجة": [2000.0, 5],
    "غسالة": [1800.0, 3],
    "مصباح": [20.0, 50],
    "كنكة كهربائية": [120.0, 7],
    "سخان ماء": [850.0, 4],
}

# عرض المنتجات
def show_products():
    print("\n📦 المنتجات المتاحة:")
    print("-" * 40)
    print("{:<20} {:<10} {:<10}".format("المنتج", "السعر", "الكمية"))
    for name, (price, quantity) in products.items():
        print("{:<20} {:<10} {:<10}".format(name, price, quantity))
    print("-" * 40)

# إضافة منتج جديد
def add_product():
    name = input("🔹 اسم المنتج الجديد: ")
    if name in products:
        print("⚠️ المنتج موجود بالفعل.")
        return
    try:
        price = float(input("🔸 السعر: "))
        quantity = int(input("🔸 الكمية: "))
        products[name] = [price, quantity]
        print(f"✅ تم إضافة المنتج {name} بنجاح.")
    except ValueError:
        print("❌ بيانات غير صحيحة.")

# تحديث كمية منتج
def update_stock():
    name = input("🔄 اسم المنتج لتحديثه: ")
    if name not in products:
        print("❌ المنتج غير موجود.")
        return
    try:
        quantity = int(input("🔼 الكمية الجديدة (تُضاف إلى الموجودة): "))
        products[name][1] += quantity
        print(f"✅ تم تحديث كمية المنتج {name}.")
    except ValueError:
        print("❌ بيانات غير صحيحة.")

# بيع منتج
def sell_product():
    name = input("🛒 اسم المنتج المراد بيعه: ")
    if name not in products:
        print("❌ المنتج غير موجود.")
        return
    try:
        quantity = int(input("🔢 الكمية المطلوبة: "))
        if quantity > products[name][1]:
            print("❌ الكمية غير متوفرة.")
            return
        total = products[name][0] * quantity
        products[name][1] -= quantity
        print(f"💰 السعر الإجمالي: {total} ريال")
        print_invoice(name, quantity, total)
    except ValueError:
        print("❌ بيانات غير صحيحة.")

# طباعة فاتورة
def print_invoice(name, quantity, total):
    print("\n🧾 فاتورة الشراء:")
    print("=" * 40)
    print(f"التاريخ: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"المنتج: {name}")
    print(f"الكمية: {quantity}")
    print(f"الإجمالي: {total} ريال")
    print("=" * 40)

# القائمة الرئيسية
def main():
    while True:
        print("\n📋 قائمة الخيارات:")
        print("1. عرض المنتجات")
        print("2. إضافة منتج جديد")
        print("3. تحديث المخزون")
        print("4. بيع منتج")
        print("5. خروج")

        choice = input("➡️ اختر خياراً (1-5): ")
        if choice == "1":
            show_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            update_stock()
        elif choice == "4":
            sell_product()
        elif choice == "5":
            print("👋 تم الخروج من البرنامج.")
            break
        else:
            print("❌ خيار غير صحيح. حاول مرة أخرى.")

# تشغيل البرنامج
main()
