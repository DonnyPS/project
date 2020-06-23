def hangman(word):
    wrong = 0       #tracking berapa kali salah tebak
    stages = ["",   #daftar karakter yang akan ditampilkan bila salah tebak
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word) #tracking tinggal berapa kali lagi peserta bisa menjawab
    board = ["__"] * len(word) #menampilkan character __ sebanyak huruf dalam word
    win = False #tracking apakah peserta menang atau tidak
    print("Welcome to Hangman")
    while wrong < len(stages) - 1: #selama jumlah kesalahan menebak masih dibawah 8, maka
        print("\n") #cetak baris kosong
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters: #jika huruf tebakan peserta ada dalam list
            cind = rletters.index(char) #huruf tebakan peserta ada di indeks keberapa dlm list
            board[cind] = char #maka tampikan hurufnya untuk menganti karakter _
            rletters[cind] = '$' #memberi nilai $
        else:
            wrong += 1 #jika salah menebak maka variable wrong ditambahkan nilai 1
            print((" ".join(board))) #cetak kondisi board,  _ _ _
            e = wrong + 1
            print("\n".join(stages[0: e]))#cetak brs karakter di list stages sesuai nilai e
        if "__" not in board: #jika semua huruf berhasil ditebak
            print("You win!") #cetak anda menang
            print(" ".join(board)) #cetak kondisi board,  _ _ _
            win = True         #memberi nilai True pada variable win
            break              #aplikasi berhenti
    if not win:
        print("\n"
              .join(stages[0: wrong])) #cetak brs karakter di list stages sesuai nilai wrong
        print("You lose! It was {}.".format(word))

hangman("cat")