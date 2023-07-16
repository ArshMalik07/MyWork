import sounddevice
from scipy.io.wavfile import write
fs=44100
second = int(input("Enter the time duration in seconds:" ))
print("Recording...\n")
record_voice=sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
sounddevice.wait()
write("out.wav", fs, record_voice)
print("Finished...\n please Check It...")