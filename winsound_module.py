import winsound

def make_noise():
    duration = 1000
    freq = 540
    winsound.Beep(freq, duration)

make_noise()