from moviepy.video.io.VideoFileClip import VideoFileClip



# Function to separate minutes and seconds
def separate_time(input_time):
    # Split the input time using ":" as the delimiter
    parts = input_time.split(":")
    
    # Check if the input format is correct (contains exactly two parts)
    if len(parts) == 2:
        minutes = int(parts[0])
        seconds = int(parts[1])
        
        return minutes, seconds
    else:
        print("Invalid input format. Please enter time in the format mm:ss.")
        return None, None



# Call the function to separate minutes and seconds




def trim_video(input_file, output_file, start_time, end_time):
    video_clip = VideoFileClip(input_file).subclip(start_time, end_time)
    video_clip.write_videofile(output_file, codec="libx264", audio_codec="aac", preset="ultrafast", ffmpeg_params=["-crf", "18"])



# Example usage
inpu =input("enter input file name: ")
outpu = "trimmed_" + inpu
trstart=input("enter start time mm:ss : ")
minutes, seconds = separate_time(trstart)
ss=((minutes*60) + seconds)

trend=input("enter end time mm:ss : ")
minutes, seconds = separate_time(trend)
es=((minutes*60) + seconds)
trim_video(inpu,outpu, ss,es)



