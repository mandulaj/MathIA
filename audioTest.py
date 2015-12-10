import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav




data = wav.read("data/test.wav")

print data

sampleRate = float(data[0])

audio = np.array(data[1], dtype=float)


aud1 = audio.T[0].T
aud2 = audio.T[1].T
print aud1.shape
freq = np.fft.rfftfreq(aud1.size, d=1./sampleRate)
fft1 = np.fft.rfft(aud1)
fft2 = np.fft.rfft(aud2)

fft1[1000:] *= 0.5
fft2[1000:] *= 0.5

ifft1 = np.fft.irfft(fft1)
ifft2 = np.fft.irfft(fft2)


print fft1.shape
print freq.shape

plt.subplot(221)
plt.plot(aud1)
plt.subplot(222)
plt.plot(aud2)
plt.subplot(223)
plt.plot(ifft1)
plt.subplot(224)
plt.plot(ifft2)
plt.show()

print ifft1.size
out = np.int16(np.column_stack((ifft1, ifft2)))
wav.write("out.wav",sampleRate, out )
