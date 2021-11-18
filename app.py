class Location:
    i = -1
    j = -1

def MatrixCreator(key):
    alphabets = []
    for k in key:
        if k == 'J':
            k = 'I'
        if k not in alphabets:
            alphabets.append(k)
    for char in range(ord('A'), ord('Z') + 1):
        k = chr(char)
        if (k not in alphabets) and (k != 'J'):
            alphabets.append(k)

    matrix = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(alphabets[(5 * i) + j])
        matrix.append(row)
    return matrix

def CharsSplitter(planeText):
    text = []
    i = 0
    while i < len(planeText):
        if i == (len(planeText) - 1):
            text.append(planeText[-1] + 'X')
        else:
            char1 = planeText[i]
            char2 = planeText[i + 1]
            if char1 == char2:
                text.append(char1 + 'X')
            else:
                text.append(char1 + char2)
                i += 1
        i += 1
        
    return text

def FindInMatrix(char, matrix):
    location = Location()
    for i in range(5):
        for j in range(5):
            if char == matrix[i][j]:
                location.i = i
                location.j = j
    return location

def Encrypt(planeText, matrix):
    planeText = CharsSplitter(planeText)
    cipher = ''
    for chars in planeText:
        char1 = chars[0]
        char2 = chars[1]
        char1_loc = FindInMatrix(char1, matrix)
        char2_loc = FindInMatrix(char2, matrix)
        if char1_loc.i == char2_loc.i:
            char1 = matrix[char1_loc.i][(char1_loc.j + 1) % 5]
            char2 = matrix[char2_loc.i][(char2_loc.j + 1) % 5]
        elif char1_loc.j == char2_loc.j:
            char1 = matrix[(char1_loc.i + 1) % 5][char1_loc.j]
            char2 = matrix[(char2_loc.i + 1) % 5][char2_loc.j]
        else:
            char1 = matrix[char1_loc.i][char2_loc.j]
            char2 = matrix[char2_loc.i][char1_loc.j]
        
        cipher += char1
        cipher += char2
        
    return cipher

def main():
    planeText = input('Plane text: ').upper().replace(' ', '')
    key = input('Key: ').upper().replace(' ', '')
    matrix = MatrixCreator(key)
    cipher = Encrypt(planeText, matrix)
    print(cipher)

if __name__ == "__main__":
    main()