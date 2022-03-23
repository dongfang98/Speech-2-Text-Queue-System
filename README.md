# Speech-2-Text-Queue-System
How many API calls you can handle simultaneously and why?
After test with stub functions, I found my computer can run 16 API calls simultaneously, with 8 Intel Core i9.  
API: https://towardsdatascience.com/easy-speech-to-text-with-python-3df0d973b426

## Phase 1: Build Queue System
### Multiprocess
In 'multiprocess.py', I develop a queue system to exercise my requirements with stub functions return after 3 seconds. Test it with different parameters.  
The computer takes 3.2430672645568848 seconds to deal with 16 processes, but take 6.203618049621582 seconds to run 17 processes, which means 16 API calls can be run simultaneously.  
Run 16 stub functions of 3 seconds⬇️  
<img width="530" alt="image" src="https://user-images.githubusercontent.com/78338843/159695027-4054d241-91a9-4194-a1d5-5f80364d948c.png">  
Run 17 stub functions of 3 seconds⬇️  
<img width="530" alt="image" src="https://user-images.githubusercontent.com/78338843/159695087-647762ac-dd04-4856-9071-8b8fc2e4122b.png">  
I also write two functions to put and get numbers from a queue, with tracking interface to show how many processes are going on and success of each.  
<img width="530" alt="image" src="https://user-images.githubusercontent.com/78338843/159697064-802d365b-eadf-4f4a-8bed-c222609dfe99.png">
### Mutithread
In 'mutithread.py', I implement one process with two threads calculating '8 ** 20'.   
<img width="530" alt="image" src="https://user-images.githubusercontent.com/78338843/159696921-5121b4d1-2665-48a6-aa36-43a00bc19def.png">
