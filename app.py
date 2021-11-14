def MatrixCreator(key):
    alphabets = []
    for k in key:
        if k == 'j':
            k = 'i'
        if k not in alphabets:
            alphabets.append(k)
    for char in range(ord('a'), ord('z') + 1):
        k = chr(char)
        if (k not in alphabets) and (k != 'j'):
            alphabets.append(k)

    matrix = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(alphabets[(5 * i) + j])
        matrix.append(row)
    return matrix

def main():
    planeText = input('Plane text: ').lower().replace(' ', '')
    key = input('Key: ').lower().replace(' ', '')
    matrix = MatrixCreator(key)
    print(matrix)

if __name__ == "__main__":
    main()