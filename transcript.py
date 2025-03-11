from openai import OpenAI
import os
import speech_recognition
from pytubefix import YouTube
from moviepy import *


CWD = os.getcwd()
# Convert the video to a transcript using whisper api
class Transcript:
    def __init__(self, video_path):
        self.link_path = video_path
        self.video_path = ""
        self.audio_path = ""

    # download the youtube video and move the path to the same path as the project. give ability to rewrite it on each run
    def download_youtube_video(self):
        try:
            yt = YouTube(self.link_path)
            ys = yt.streams.get_highest_resolution()
            print(CWD)
            self.video_path = CWD
            print("Starting download....")
            ys.download(output_path=self.video_path)
            print("Download complete!")
            self.video_path = f"{CWD}/{yt.title}.mp4"
            self.audio_path = f"{CWD}/{yt.title}.wav"
        except Exception as e:
            print(f"An error occured: {e}")

    # convert the video to audio, and then extract the text
    def video_to_text(self):
        try:
            print(self.video_path)
            # extract audio from video
            video_clip = VideoFileClip(self.video_path)
            video_clip.audio.write_audiofile(self.audio_path)
            # initialize recognizer
            recognizer =  speech_recognition.Recognizer()
            # load audio file
            with speech_recognition.AudioFile(self.audio_path) as source:
                data = recognizer.record(source)
            #     convert speech to text
            # continue from here the recognizer is not working or is not being instantiated
            print(data)
            print(recognizer)
            text = recognizer.recognize_google(data, key)
            # recognize speech using Google Speech Recognition
            try:
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
                text = recognizer.recognize_google(data, key=)
            except speech_recognition.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except speech_recognition.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

            print("male")
            # video_clip.close()
            print(f"Successfully converted '{self.video_path}' to '{self.audio_path}'")

        except Exception as e:
            print(f"An error occurred: {e}")

    # # convert video to transcript
    # def audio_to_transcript(self):
    #     client = OpenAI()
    #     audio_file = yt.streams[0].default_name
    #     # convert file to audio file depending on the file type (we will take only video and audio for now)
    #     audio_file = self.path
    #     transcription = client.audio.transcriptions.create(
    #         model="whisper-1",
    #         file=audio_file
    #     )
    #
    #     print(transcription.text)



