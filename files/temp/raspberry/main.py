import pyaudio
import wave
import audioop
from collections import deque
import os
import io
import time
import math

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

CHUNK = 1024  # CHUNKS of bytes to read each time from mic
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
THRESHOLD = 1500  # The threshold intensity that defines silence
SILENCE_LIMIT = 3  # Silence limit in seconds to stop the recording
PREV_AUDIO = 0.5  #seconds of audo to prepend to the sending data


# [START speech_transcribe_streaming]
def transcribe_streaming(stream_file):
    """Streams transcription of the given audio file."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    # [START speech_python_migration_streaming_request]
    with io.open(stream_file, 'rb') as audio_file:
        content = audio_file.read()

    # In practice, stream should be a generator yielding chunks of audio data.
    stream = [content]
    requests = (types.StreamingRecognizeRequest(audio_content=chunk)
                for chunk in stream)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='cs-CZ')
    streaming_config = types.StreamingRecognitionConfig(config=config)

    # streaming_recognize returns a generator.
    # [START speech_python_migration_streaming_response]
    responses = client.streaming_recognize(streaming_config, requests)
    # [END speech_python_migration_streaming_request]

    for response in responses:
        # Once the transcription has settled, the first result will contain the
        # is_final result. The other results will be for subsequent portions of
        # the audio.
        for result in response.results:
            print('Finished: {}'.format(result.is_final))
            print('Stability: {}'.format(result.stability))
            alternatives = result.alternatives
            # The alternatives are ordered from most likely to least.
            for alternative in alternatives:
                print('Confidence: {}'.format(alternative.confidence))
                print(u'Transcript: {}'.format(alternative.transcript))

    return responses
    # [END speech_python_migration_streaming_response]
# [END speech_transcribe_streaming]


def listen_for_speech(threshold=THRESHOLD):
    #Open stream
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print ("* Listening mic. ")
    audio2send = []
    cur_data = ''  # current chunk  of audio data
    rel = RATE/CHUNK
    slid_win = deque(maxlen=math.floor(SILENCE_LIMIT * rel))
    #Prepend audio from 0.5 seconds before noise was detected
    prev_audio = deque(maxlen=math.floor(PREV_AUDIO * rel))
    started = False
    response = []

    while (True):
        cur_data = stream.read(CHUNK)
        slid_win.append(math.sqrt(abs(audioop.avg(cur_data, 4))))
        #print slid_win[-1]
        if(sum([x > THRESHOLD for x in slid_win]) > 0):
            if(not started):
                print ("Starting record of phrase")
                started = True
            audio2send.append(cur_data)
        elif (started is True):
            stream.stop_stream()
            print ("Finished")
            filename = save_speech(list(prev_audio) + audio2send, p)
            stt_google_wav(filename)
            # Remove temp file. Comment line to review.
            os.remove(filename)
            # Reset all
            started = False
            slid_win = deque(maxlen=math.floor(SILENCE_LIMIT * rel))
            prev_audio = deque(maxlen=math.floor(0.5 * rel))
            audio2send = []
            stream.start_stream()
            print ("Listening ...")
        else:
            prev_audio.append(cur_data)

    print ("exiting")
    p.terminate()
    return


def save_speech(data, p):
    filename = 'output_'+str(int(time.time()))
    # writes data to WAV file
    data = b''.join(data)
    wf = wave.open(filename + '.wav', 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(16000)  # TODO make this value a function parameter?
    wf.writeframes(data)
    wf.close()
    return filename + '.wav'


def stt_google_wav(audio_fname):
    """ Sends audio file (audio_fname) to Google's text to speech
        service and returns service's response. We need a FLAC
        converter if audio is not FLAC (check FLAC_CONV). """

    print ("Sending ", audio_fname)
    #Convert to flac first
    responses = transcribe_streaming(audio_fname)
    
    for response in responses:
        for result in response.results:
            for alternative in result.alternatives:
                print('=' * 20)
                print('transcript: ' + alternative.transcript)
                print('confidence: ' + str(alternative.confidence))
                if alternative.transcript == "exit":
                    print("exit")
                if alternative.transcript.lower() == "zapni světlo":
                    print("světlo zapnuto")
                if alternative.transcript.lower() == "zapni světla":
                    print("světlo zapnuto")
                if alternative.transcript.lower() == "vypni světlo":
                    print("světlo vypnuto")
                if alternative.transcript.lower() == "vypni světla":
                    print("světlo vypnuto")


if(__name__ == '__main__'):

    listen_for_speech()
