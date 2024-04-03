#Task 1
import random
moods = ['happy', 'sad', 'energetic', 'calm', 'mad']

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

times = ['morning', 'afternoon', 'evening']

for x in days:
    for y in times:
        mood_time = random.choice(moods)
        print(f"On {x} {y} you were feeling {mood_time}")