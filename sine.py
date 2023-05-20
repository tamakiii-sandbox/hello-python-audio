import numpy
import sys
from scipy.io.wavfile import write
from termcolor import colored

if len(sys.argv) < 2:
    print(colored('Error: No output file path provided.', 'red'))
    sys.exit(1)

output_file_path = sys.argv[1]

# Choose your desired properties
samplerate = 44100 # Sample rate
freq = 440 # Frequency (Hz)
duration = 5.0 # Duration (seconds)

# Generate the time values
t = numpy.linspace(0, duration, int(samplerate * duration), False)

# Generate the audio signal
note = numpy.sin(freq * t * 2 * numpy.pi)

# Ensure that highest value is in 16-bit range
audio = note * (2**15 - 1) / numpy.max(numpy.abs(note))
audio = audio.astype(numpy.int16)

# Write the audio file
write(output_file_path, samplerate, audio)
