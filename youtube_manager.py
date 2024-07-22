import json

def load_data():
    try:
        with open("youtube.txt","r") as file:
            test = json.load(file)
            return test

    except FileNotFoundError:
        return []


def save_data(videos):
    with open("youtube.txt","w") as file:
        json.dump(videos,file)


def list_all_videos(videos):
    print("\n")
    print("*"*70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}.{video['name']}, Duration: {video['time']}")
        print("*"*70)

def add_video(videos):
    name = input("Enter the title of the video: ")
    time = input("Enter the duration of the video: ")
    videos.append({"name": name, "time": time})
    print("video succesfully added")
    save_data(videos)



def update_video(videos):
    list_all_videos(videos)
    index = input("Enter the index of the video you want to update: ")  
    index = int(index)  
    
    if 1 <= index <= len(videos):
        name = input("enter the new video name: ")
        time = input("enter the new video duration: ")
        videos[index-1] = {"name": name, "time": time}
        print("video succesfully updated")
        save_data(videos)
    else:
        print("Invalid index. Please try again")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video you want to delete: "))

    if 1 <= index <= len(videos):
        del videos[index-1]
        print("video succesfully deleted")
        save_data(videos)
    else:
        print("Invalid index. Please try again")




def main():

    videos = load_data()

    while True:
        print("\n")
        print("Youtube Manager")
        print("1. List all youtube videos")
        print("2. Add a new youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")


        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice. Please try again")



if __name__ == "__main__":
    main()