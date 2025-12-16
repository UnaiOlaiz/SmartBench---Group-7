import pygame
import threading
import queue
import time
import os


class AudioManager:
    """
    simple pygame audio wrapper with async playback, queue management,
    error protection and basic state control
    """

    def __init__(self,
                 frequency=44100,
                 size=-16,
                 channels=2,
                 buffer=2048,
                 volume=0.8):

        self._init_mixer(frequency, size, channels, buffer)

        self.queue = queue.Queue()
        self.current_file = None
        self.running = True
        self.playing = False

        self.set_volume(volume)

        #start playback thread
        self.thread = threading.Thread(target=self._playback_loop, daemon=True)
        self.thread.start()

    def _init_mixer(self, frequency, size, channels, buffer):
        #initialize pygame mixer safely
        try:
            pygame.mixer.pre_init(frequency, size, channels, buffer)
            pygame.mixer.init()
        except Exception as e:
            print(f"[audiomanager] mixer init error: {e}")
            raise SystemExit("pygame.mixer could not be initialized")

    def _playback_loop(self):
        #background loop that plays queued audio
        while self.running:
            try:
                filepath = self.queue.get(timeout=0.1)
            except queue.Empty:
                continue

            if not os.path.isfile(filepath):
                print(f"[audiomanager] file not found: {filepath}")
                continue

            try:
                self.current_file = filepath
                pygame.mixer.music.load(filepath)
                pygame.mixer.music.play()
                self.playing = True
            except Exception as e:
                print(f"[audiomanager] playback error for {filepath}: {e}")
                self.playing = False
                continue

            while pygame.mixer.music.get_busy() and self.running:
                time.sleep(0.1)

            self.playing = False

    #public api
    def play(self, filepath):
        #add file to queue
        self.queue.put(filepath)

    def stop(self):
        #stop current playback
        pygame.mixer.music.stop()
        self.playing = False

    def pause(self):
        #pause playback
        pygame.mixer.music.pause()

    def resume(self):
        #resume playback
        pygame.mixer.music.unpause()

    def set_volume(self, value):
        #set volume between 0.0 and 1.0
        value = max(0.0, min(1.0, value))
        pygame.mixer.music.set_volume(value)

    def get_volume(self):
        #get current volume
        return pygame.mixer.music.get_volume()

    def is_playing(self):
        #check if audio is currently playing
        return pygame.mixer.music.get_busy()

    def shutdown(self):
        #shutdown mixer and thread
        self.running = False
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        print("[audiomanager] mixer shut down")

