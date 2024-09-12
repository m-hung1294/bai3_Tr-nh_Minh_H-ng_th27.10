a = input("Nhập xâu: ").lower() 
char_count = {} 
for char in a:
    if char.isalnum():  
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
for char, count in char_count.items():
    print(f"Chữ '{char}' xuất hiện {count} lần")
for char in a:
    if char.isalnum():  
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
for char, count in char_count.items():
    print(f"Chữ '{char}' xuất hiện {count} lần")