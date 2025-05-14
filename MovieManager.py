import speech_recognition as sr 
from moviepy.editor import VideoFileClip, AudioFileClip, ComposeAudioClip

class MovieManager:
    def get_war_audio(Self, mp4_file,war_file):
        vc=VideoFileClip(mp4_file)
        ac=vc.audio
        ac.write_audiofile(war_file, codec='pcm_s16le')
        ac.close()
        vc.close()
    def audio_to_text(Self, audio_file):
        r=sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
             audio= r.record(source)
        try:
            text=r.recognize_google(audio)
            return text
        except
             return 'unknow'
        

mm=MovieManager()
#mm.get_wav_audio('video.mp4', 'audio.wav')
speech=mm.audio_to_text('audio.wav')
print(speech)