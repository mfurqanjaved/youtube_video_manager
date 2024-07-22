import sqlite3

conn = sqlite3.connect('youtube_manager_db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL
)

''')

def list_videos():
    print("\n")
    print("*"*50)
    cursor.execute('SELECT * FROM videos')
    for row in cursor.fetchall():
        print(row)
        print("\n")
        print("*"*50)
        

def add_video(name, time):
    cursor.execute('''
    INSERT INTO videos(name, time)
    VALUES(?, ?)
    ''', (name, time))
    conn.commit()
    print("video added succesfuly")

def update_video(video_id, name, time):
    cursor.execute('''
    UPDATE videos
    SET name = ?, time = ?
    WHERE id = ?
    ''', (name, time, video_id))
    conn.commit()
    print("video updated succesfuly")

def delete_video(video_id):
    cursor.execute('''
    DELETE FROM videos
    WHERE id = ?
    ''', (video_id,))
    conn.commit()
    print("video deleted succesfuly")


def main():
    while True:

        print("\n")
        print("youtube manager app with DB")
        print("\n")
        print("1. List all youtube videos")
        print("2. Add a new youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        print("\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()

        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video duration: ")
            add_video(name, time) 

        elif choice == "3":
            video_id = input("Enter the video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video duration: ")
            add_video(name, time) 

        elif choice == "4":
            video_id = input("Enter the video ID to delete: ")  # Prompt for video_id here
            cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again")
            

    conn.close()

if __name__ == '__main__':
    main()
