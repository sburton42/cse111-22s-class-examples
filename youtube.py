
def add_video(video_list, title, length):
    """
    Adds the provided video to the list.
    Params:
        video_list: The list to add to.
        title: The title of the video you want to add.
    Returns:
        None
    """
    video = [title, length]
    video_list.append(video)

    # Same as:
    # video_list.append([title, length])

    # Similar to this:
    # video_list = [[title, length]]

def display_videos(video_list):
    """
    Displays a listing of all the videos.
    Params:
        video_list: The list of videos
    Returns:
        None
    """

    print()
    print("Upcoming playlist:")
    for i, video in enumerate(video_list):
        # video is now a list of things, a title and a length
        title = video[0]
        print(f" {i + 1}. {title}")

    time = get_total_time(video_list)
    print(f"The total running time is: {time:.2f} minutes")

    # for i in range(len(video_list)):
    #     video = video_list[i]

    #     # video is now a list of things, a title and a length
    #     title = video[0]
    #     print(f" {i + 1}. {title}")


def display_next_video(video_list):
    #video = video_list[0]
    title = video_list[0][0]
    length = video_list[0][1]

    print(f"Up next: {title} ({length} seconds)")


def remove_video(video_list):
    """
    Removes the video from the front of the playlist (it has been watched)
    """
    video_list.pop(0)

def get_total_time(video_list):
    """
    Calculates and returns the total time of the playlist in minutes.
    """
    total_length = 0

    for video in video_list:
        length = video[1]
        total_length += length
        # total_length = total_length + length

    return total_length / 60

def main():
    print("Welcome to console YouTube")

    videos = []
    add_video(videos, "Top Gun Trailer", 120)
    add_video(videos, "Screaming Goat", 7)

    display_videos(videos)
    display_next_video(videos)

    remove_video(videos)

    display_videos(videos)
    display_next_video(videos)

if __name__ == "__main__":
    main()

