import pyaudio
import wave
# from pydub import AudioSegment

def record_audio():
    # Parameters for the audio recording
    FORMAT = pyaudio.paInt16  # Format for audio recording (16-bit resolution)
    CHANNELS = 1              # Mono audio
    RATE = 44100              # Sampling rate (44.1 kHz)
    CHUNK = 1024              # Number of frames per buffer
    RECORD_SECONDS = 10       # Duration of recording (in seconds)
    OUTPUT_WAV_FILE = "output.wav"  # Temporary output .wav file
    OUTPUT_MP3_FILE = "output.mp3"  # Final output .mp3 file

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("Recording started...")

    frames = []

    # Record data in chunks
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording finished.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded data as a .wav file
    wave_file = wave.open(OUTPUT_WAV_FILE, 'wb')
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(audio.get_sample_size(FORMAT))
    wave_file.setframerate(RATE)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()

    print(f"Audio saved as {OUTPUT_WAV_FILE}")

import os
from dotenv import load_dotenv
import logging
from deepgram.utils import verboselogs
from datetime import datetime
import httpx

from deepgram import (
    DeepgramClient,
    DeepgramClientOptions,
    PrerecordedOptions,
    FileSource,
)

load_dotenv()

AUDIO_FILE = "output.wav"
print()
print()


def get_transcription():
    try:
        # STEP 1 Create a Deepgram client using the API key in the environment variables
        deepgram_api = os.getenv("DG_API_KEY")
        # config: DeepgramClientOptions = DeepgramClientOptions(
        #     verbose=verboselogs.SPAM,
        # )
        deepgram = DeepgramClient(deepgram_api) #, config)
        # OR use defaults
        # deepgram: DeepgramClient = DeepgramClient()

        # STEP 2 Call the transcribe_file method on the rest class
        with open(AUDIO_FILE, 'rb') as audio_file:
            buffer_data = audio_file.read()

        # Prepare the payload for transcription
        payload: FileSource = {
            "buffer": buffer_data,
        }

        # Configure transcription options
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
        )

        # Transcribe the audio file
        response = deepgram.listen.rest.v("1").transcribe_file(payload, options)

        # Extract the transcription from the response
        transcription = response.results.channels[0].alternatives[0].transcript
        print(transcription)
        return transcription

    except Exception as e:
        print(f"Exception: {e}")

