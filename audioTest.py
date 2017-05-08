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

print sampleRate
fft1[21999:] *= 1
#fft2[20000:] *= 0




ifft1 = np.fft.irfft(fft1)
ifft2 = np.fft.irfft(fft2)
np.savez_compressed('ifft.npy', ifft1)

np.savez_compressed("orig.npy",aud1)
np.savez_compressed('fft.npy', fft1)
np.savez_compressed('ifft.npy', np.int16(ifft1))


print fft1.shape
print freq.shape

plt.plot(aud1)
plt.ylabel("Amplitude")
plt.xlabel("Time [s]")
plt.grid(b=True, which="major", color='gray', linestyle='--')
plt.xticks(range(0,len(aud1),int(sampleRate)), [w/float(sampleRate) for w in range(0,len(aud1),int(sampleRate))])
plt.show()

plt.plot(fft1)
plt.grid(b=True, which="major", color='gray', linestyle='--')
plt.xticks(range(0,len(freq),36666/5), [np.around(w/3.666666666, decimals=-2) for w in range(0,len(freq),36666/5)])

plt.ylabel("Amplitude")
plt.xlabel("Frequency [Hz]")
plt.show()

plt.subplot(221)
plt.plot(aud1)
plt.subplot(222)
plt.plot(aud2)
plt.subplot(223)
plt.plot(ifft1)
plt.subplot(224)
plt.plot(ifft2)
#plt.show()

print ifft1.size
out = np.int16(np.column_stack((ifft1, ifft2)))
wav.write("out.wav",sampleRate, out )
