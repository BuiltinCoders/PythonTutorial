from pygame import mixer
import time
import datetime

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    # mixer.music.set_volume(0.7)
    
    while True:
        mixer.music.play()
        user_input = input("Enter The Stopper:\n")
        if user_input==stopper:
            mixer.music.stop()
            break

def log(msg):
    with open("records.txt", "a") as f:
        f.write(f"{msg} is done at {datetime.datetime.now()}\n")

watersces = 5
eyessces = 15
physces = 25

if __name__ == "__main__":

    init_water = time.time()
    init_eyes = time.time()
    init_physical = time.time()
    
    # for water
    while True:
        if (time.time()-init_water)>watersces:
            # time.sleep(5)
            print("Water Reminder, Type 'drank' to stop the sound")
            musiconloop(r"E:\NITESH\Study\Python\Part 2\Asserts\Sound Effects\water.mp3", "drank")
            init_water = time.time()
            log("Water drink task")
    
    # for eyes exercise
        if (time.time()-init_eyes)>eyessces:
            # time.sleep(5)
            print("Eyes Reminder, Type 'Eydone' to stop the sound")
            musiconloop(r"E:\NITESH\Study\Python\Part 2\Asserts\Sound Effects\eyes.mp3", "Eydone")
            init_eyes = time.time()
            log("Eyes exercise task")
   
    # for physical exercise
        if (time.time()-init_physical)>physces:
            # time.sleep(5)
            print("Phical Exercise Reminder, Type 'Eydone' to stop the sound")
            musiconloop(r"E:\NITESH\Study\Python\Part 2\Asserts\Sound Effects\physical.mp3", "Phydone")
            init_physical = time.time()
            log("Physical exercise task")




# # Modules
# import pygame
# from datetime import datetime
# import time


# # sound player
# def water():
#     pygame.mixer.init()
#     pygame.mixer.music.load(r"E:\NITESH\Study\Python\Part 2\Asserts\Sound Effects\water.mp3")
#     pygame.mixer.music.set_volume(0.7)
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)

# # Time
# # now = datetime.now()
# # current_time = now.strftime("%H:%M:%S")
# # hour, minute, seconds = current_time.split(":")

# # # Main Program

# # print(f"Current Time: {current_time}")
# # game = True
# # while int(hour)>9 and int(hour)<23:
# #     time.sleep(3)
# #     while game:
# #         water()
# #         query = input("Did you drank water:\n")
        
# #         if "drank" in query:
# #             print("We will notify you after 10s")
# #             time.sleep(10)


