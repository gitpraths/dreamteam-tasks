import time
import pyperclip

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl+C to quit.')
input()                    
print('Started.')
startTime = time.time()    
lastTime = startTime
lapNum = 1
output = ''

try:
    while True:
        input()
        lapTime = time.time() - lastTime
        totalTime = time.time() - startTime
        lapNumStr = str(lapNum).rjust(2)
        lapTimeStr = str(round(lapTime, 2)).rjust(5)
        totalTimeStr = str(round(totalTime, 2)).rjust(6)
        output += f'Lap #{lapNumStr}: {lapTimeStr} ({totalTimeStr})\n'
        print(f'Lap #{lapNumStr}: {lapTimeStr} ({totalTimeStr})', end='')
        lapNum += 1
        lastTime = time.time() 
except KeyboardInterrupt:
  
    print('\nDone.')
    
pyperclip.copy(output)
print('The output has been copied to your clipboard.')