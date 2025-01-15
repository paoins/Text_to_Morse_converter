import numpy as np
import sounddevice as sd
import time



def create_beep(frequency=1000, duration=0.2, sample_rate=22050, element='dot'):
    """
    Generate a beep sound.
    :param frequency: Frequency of the beep in Hz (default: 1000)
    :param duration: Duration of the beep in seconds (default: 0.2)
    :param sample_rate: Sampling rate in Hz (default: 22050)
    :param element: 'dot' for short beep, 'dash' for long beep (default: 'dot')
    """
    if element == 'dash':
        duration = duration * 3  # Longer beep for 'dash'

    # Generate time values
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    # Create a sine wave
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    # Play the sound
    sd.play(wave, samplerate=sample_rate)
    sd.wait()



def create_morse_audio(morse):
    '''
    Convert a Morse code string into audio.
    :param morse: A string containing Morse code element
    '''
    for x in morse:
        if x == '.':
            create_beep(element='dot')
        elif x == '-':
            create_beep(element='dash')
        elif x == ' ':
            time.sleep(0.6)
        elif x == '/' :
            time.sleep(1.4)


