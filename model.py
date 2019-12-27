from textgenrnn import textgenrnn
import random 
def train():
    textgen = textgenrnn()

    textgen.train_from_largetext_file('test.txt', num_epochs=20,word_level=True)
    print('success')
    #textgen.generate()


def model_():
    x=1
    while(x):
        x=0
        r = random.randint(3, 15)
        r2=random.randint(0, 1)
        temp=[0.8,1.0]
        textgen_2 = textgenrnn('textgenrnn_weights.hdf5',vocab_path='textgenrnn_vocab.json',config_path='textgenrnn_config.json')
        test = textgen_2.generate(1, temperature=temp[r2],max_gen_length=r,return_as_list=True)
        test=test[0]
        if 'เย็ด' in test or 'ดวง' in test or 'เงี่ยน' in test or 'บอ ท' in test or 'ชักว่าว' in test or 'แคป' in test or 'คำคม' in test or 'มัธยม' in test or 'ตูด' in test or 'หี' in test or 'ควย' in test or 'คำ คม' in test:
            x=1
        #print(test)
    return test