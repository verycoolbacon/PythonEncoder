import base64

MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', ' ': '/',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

def b64en(msg):
    msg_bytes = msg.encode("utf-8")
    base64_bytes = base64.b64encode(msg_bytes)
    return base64_bytes.decode("utf-8")

def asciien(msg):
    return " ".join([str(ord(char)) for char in msg])

def morseen(msg):
    result = []
    for char in msg:
        result.append(MORSE_DICT[char.upper()])
    return " ".join(result)

def binen(msg):
    result = []
    for char in msg:
        result.append(bin(ord(char))[2:])
    return result

def morse_to_bin(morse_input):
    if "-" not in morse_input and "." not in morse_input:
        return None 
        
    result = []
    for char in morse_input:
        if char == "-":
            result.append("1")
        elif char == ".":
            result.append("0")
        elif char == " ":
            result.append(" ")
        elif char == "/":
            result.append("/")
    return "".join(result)

# ✨ 新增：Byte (Hex) 編碼功能
def byteen(msg):
    msg_bytes = msg.encode("utf-8")
    # 轉成大寫的十六進位字串，並用空格隔開（如 AE A4 F3）
    return " ".join([f"{b:02X}" for b in msg_bytes])

# 主程式開始
user_input = input("input: ")
result = ""
history = [] 

while True:
    print(f"\n[processing text: {user_input}]") 
    # 更新選單，加入 6=byte 
    way_input = input("1=b64 | 2=ascii | 3=morse | 4=binary | 5=morse->bin | 6=byte | 8=revert (Ctrl+Z) | 9=quit \nenter: ")
    
    try:
        way = int(way_input)
        
        if way == 9: # quit
            print("final result = " + str(result))
            break
            
        elif way == 8: # revert 還原上一步
            if len(history) == 0:
                print("no previous text to revert to")
            else:
                user_input = history.pop()  
                print("reverted to previous text")
            continue
            
        elif way > 6 or way < 1: # 修改範圍限制，現在上限是 6
            print("number too large or invalid")
            continue
            
        # 開始執行功能
        if way == 1:
            temp_result = b64en(user_input)
        elif way == 2:
            temp_result = asciien(user_input)
        elif way == 3:
            try:
                temp_result = morseen(user_input)
            except KeyError:
                print("morse code can only use english char/numbers (invalid character found)")
                continue 
        elif way == 4:
            temp_result = " ".join(binen(user_input))
        elif way == 5:
            check_result = morse_to_bin(user_input)
            if check_result is None:
                print("invalid input for morse->bin translator (no '.' or '-' found)")
                continue 
            else:
                temp_result = check_result
        elif way == 6: # ✨ 串接 Byte 編碼
            temp_result = byteen(user_input)
                
        # 轉換成功才更新
        result = temp_result
        print("result = " + str(result))
        
        history.append(user_input) 
        user_input = str(result)  
        
    except ValueError:
        print("number only")