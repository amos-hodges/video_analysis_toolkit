import cv2


def get_video_path():
    # add feature to validate using pathlib?
    # video_path = input("Enter video path:").strip().strip('"')
    video_path = 'C:/Users/AHodges/Desktop/Angel Gil Accident.mkv'
    return video_path


def open_video(video_path):
    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        print("Error: could not open video.")
        return None

    return video


def get_video_info(video):
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    if fps:
        print(f"video duration: {format_duration(frame_count/fps)}")
    else:
        print("video duraiton unavailable")
    print(f"frame rate: {fps:.3f} fps")
    print(f"resolution: {frame_width}px X {frame_height}px")
    print(f"frame count: {frame_count}")


def format_duration(seconds):
    hours = int(seconds // 3600)
    remaining_seconds = seconds % 3600

    minutes = int(remaining_seconds // 60)
    remaining_seconds = seconds % 60

    duration = f"{hours:02d}:{minutes:02d}:{remaining_seconds:06.3f}"
    return duration


def main():

    path = get_video_path()
    video = open_video(path)

    if video is None:
        return

    get_video_info(video)

    video.release()


if __name__ == "__main__":
    main()
