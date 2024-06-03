import os
import pyaudio
import wave

def record_audio_and_save(save_path, n_times=3):
    input("To start audio recording press Enter: ")
    for i in range(n_times):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        RECORD_SECONDS = 6
        WAVE_OUTPUT_FILENAME = os.path.join(save_path, f"{i}.wav")

        audio = pyaudio.PyAudio()

        stream = audio.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)

        print("Recording...")

        frames = []

        for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("Finished recording...")

        stream.stop_stream()
        stream.close()
        audio.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        input(f"Enter to record next or CTRL+C to Exit. ({i + 1}/{n_times})")


def record_background_save(save_path, n_times=3):
    input("To start recording background noise press Enter: ")
    for i in range(n_times):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        RECORD_SECONDS = 6
        WAVE_OUTPUT_FILENAME = os.path.join(save_path, f"{i}.wav")

        audio = pyaudio.PyAudio()

        stream = audio.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)

        print("Recording...")

        frames = []

        for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("Finished recording...")

        stream.stop_stream()
        stream.close()
        audio.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        input(f"Enter to record next or CTRL+C to Exit. ({i + 1}/{n_times})")
        print(f"Currently on {i + 1}/{n_times}")

print("Recording audio positive for the wake word: \n")
record_audio_and_save("audio_data")

print("Recording background noise: \n")
record_background_save("background_audio_data")
