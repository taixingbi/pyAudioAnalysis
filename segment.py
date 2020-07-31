
# from pyAudioAnalysis import audioSegmentation

# filename= '300_AUDIO.wav'

# audioSegmentation.readSegmentGT(filename)

# python pyAudioAnalysis/audioAnalysis.py fileSpectrogram -i 300_AUDIO.wav



from pyAudioAnalysis import audioBasicIO as aIO
from pyAudioAnalysis import audioSegmentation as aS

filename= '300_AUDIO.wav' 
#filename= 'pyAudioAnalysis/data/3WORDS.wav' 

Fs, x= aIO.read_audio_file(filename)

segments = aS.silence_removal(x, Fs, 0.020, 0.020, smooth_window = 1.0, weight = 0.3, plot = False)
print(segments)

print("done")
