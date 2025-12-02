songs=[
    {'title': 'Phía sau một cô gái', 'artist': 'Soobin Sầm Sơn', 'duration': 240},
    {'title': 'Vài lần đóng đua', 'artist': 'Soobin Sầm Sơn', 'duration': 240}

]

def main():
    while True:
        print("\n--- MUSIC PLAYLIST MANAGER ---")
        print("1. Thêm bài hát")
        print("2. Xem danh sách phát")
        print("3. Tìm bài hát theo ca sĩ")
        print("4. Thoát")
        choice = input("Chọn chức năng: ")
        if choice == '1':
          add_song()
        elif choice == '2':
           view_playlist()
        elif choice == '3':
           search_by_artist()
        elif choice == '4':
           print("Kết thúc chương trình.")
           break
        else:
          print("Lựa chọn không hợp lệ.")

def add_song():
    print("Vui lòng nhập tên bài hát: ")
    title = input()
    print("Vui lòng nhập tên ca sĩ: ")
    artist = input()
    print("nhập thời lượng: ")
    duration = input()
    songs.append({
        "title": title,
        "artist": artist,
        "duration": duration
    })
    print("Đã thêm bài hát vào playlist")
def view_playlist():
    for i in range (len(songs)):
         print ("1.",songs[i]["Title"],"- Nghệ sĩ -",songs[i]["artist"],"(",songs[i]["duration"],"s)")
def search_by_artist():
    print("Nhập tên ca sĩ:")
    artist=input()
    for i in range (len(songs)):
        if songs[i]["artist"]==artist:
            print (songs[i])

if __name__ == "__main__":
    main()
