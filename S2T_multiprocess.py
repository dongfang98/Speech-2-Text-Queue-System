#import library
import speech_recognition as sr
from multiprocessing import Process, Queue, Pool
import os, time
from time import sleep

#test how many process can be handled simultaneously
#16 processes can be handled simultaneously
def speech_to_text(name):
    print ('Run API Call %s (%s), converting audio transcripts into text ...' % (name, os.getpid()))
    start = time.time()
    r = sr.Recognizer()
    with sr.AudioFile('test.wav') as source:
        audio_text = r.listen(source)
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            # using google speech recognition
            text = r.recognize_google(audio_text)
        except:
            print('Sorry.. run again...')
    time.sleep(0)
    end = time.time()
    print ('API Call %s runs %0.2f seconds. Result %s' % (name, (end - start), text))


#n is the number of processes
def main(n):

    print ('Parent process %s.' % os.getpid())
    start = time.time()
    p = Pool()
    for i in range(n):
        p.apply_async(speech_to_text, args=(i,))
    print ('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print ('All subprocesses done.')
    end = time.time()
    print("Totally used {} seconds".format((end - start)))

    
if __name__ == '__main__':
	main(16)