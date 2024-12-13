import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

sampling_rate = 44100


def generate_sine_wave(frequency, duration, amplitude):
    num_samples = int(sampling_rate * duration)
    time = np.linspace(0, duration, num_samples, endpoint=False)
    audio_signal = amplitude * np.sin(2 * np.pi * frequency * time)
    return audio_signal


def generate_rectangular_wave(frequency, duration, amplitude):
    num_samples = int(sampling_rate * duration)
    time = np.linspace(0, duration, num_samples, endpoint=False)
    audio_signal = amplitude * np.sign(np.sin(2 * np.pi * frequency * time))
    return audio_signal


def generate_asymetric_triangular_wave(frequency, duration, amplitude):
    num_samples = int(sampling_rate * duration)
    time = np.linspace(0, duration, num_samples, endpoint=False)
    period = 1 / frequency
    audio_signal = amplitude * (2 * (time / period - np.floor(0.5 + time / period)))
    return audio_signal


def generate_symetric_triangular_wave(frequency, duration, amplitude):
    num_samples = int(sampling_rate * duration)
    time = np.linspace(0, duration, num_samples, endpoint=False)
    period = 1 / frequency
    audio_signal = amplitude * (2 * np.abs(2 * (time / period - np.floor(time / period + 0.5))) - 1)
    return audio_signal


def visualize_signal(audio_signal, duration, title="Audio signal"):
    plt.figure(figsize=(10, 4))
    time = np.linspace(0, duration, len(audio_signal), endpoint=False)
    plt.plot(time, audio_signal)
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.grid()
    plt.show()


def plot_positive_spectrum(signal, title="Signal Spectrum (Positive Frequencies Only)"):
    signal_fft = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(len(signal), 1 / sampling_rate)
    positive_frequencies = frequencies[:len(frequencies) // 2]
    positive_signal_fft = 2.0 / len(signal) * np.abs(signal_fft[:len(signal) // 2])

    plt.figure(figsize=(10, 6))
    plt.plot(positive_frequencies, positive_signal_fft)
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.grid()
    plt.show()


def save_signal_to_wav(filename, signal):
    max_amplitude = np.max(np.abs(signal))
    normalized_signal = signal / max_amplitude
    wavfile.write(filename, sampling_rate, normalized_signal)


def main():
    frequency = 440  # Example frequency
    duration = 1
    amplitude = 1

    # Generate sine audio signal.
    audio_signal = generate_sine_wave(frequency, duration, amplitude)
    visualize_signal(audio_signal, duration, title="Sine Wave")
    plot_positive_spectrum(audio_signal, title="Sine Wave Spectrum (Positive Frequencies Only)")
    save_signal_to_wav("sine_wave.wav", audio_signal)

    # Generate rectangular audio signal.
    audio_signal = generate_rectangular_wave(frequency, duration, amplitude)
    visualize_signal(audio_signal, duration, title="Rectangular Wave")
    plot_positive_spectrum(audio_signal, title="Rectangular Wave Spectrum (Positive Frequencies Only)")
    save_signal_to_wav("rectangular_wave.wav", audio_signal)

    # Generate asymmetric triangular audio signal.
    audio_signal = generate_asymetric_triangular_wave(frequency, duration, amplitude)
    visualize_signal(audio_signal, duration, title="Asymmetric Triangular Wave")
    plot_positive_spectrum(audio_signal, title="Asymmetric Triangular Wave Spectrum (Positive Frequencies Only)")
    save_signal_to_wav("asymmetric_triangular_wave.wav", audio_signal)

    # Generate symmetric triangular audio signal.
    audio_signal = generate_symetric_triangular_wave(frequency, duration, amplitude)
    visualize_signal(audio_signal, duration, title="Symmetric Triangular Wave")
    plot_positive_spectrum(audio_signal, title="Symmetric Triangular Wave Spectrum (Positive Frequencies Only)")
    save_signal_to_wav("symmetric_triangular_wave.wav", audio_signal)


if __name__ == "__main__":
    main()