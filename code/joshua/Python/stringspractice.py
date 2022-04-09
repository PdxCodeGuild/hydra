from re import X
import re
import string
from xml.etree import cElementTree


def loud_text(text):
    word = ("-").join(list(text)).upper()
    return word


def test_loud_text():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text(
        'this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'



def double_letters(word):
    double = ''
    for letter in word:
        double += letter*2
    return double


def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'





def count_letter(letter, word):
    x = 0

    for item in word:
        if item == letter:
            x += 1
    return x


def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter(
        'p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2







def latest_letter(word):
    word = sorted(word)
    return word[-1]
    


def test_latest_letter():
    return latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'





def count_hi(text):
    x = text.count('hi')
    return x

def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi llama hill') == 2







def snake_case(text):
    word = str(text).lower().replace(' ', '_')
    ting = ['`','~','!','@','#','$','%','^','&','*','(',')','-','+','=','{','[','}','}','|',':',';','<','>','?','.']
    for item in word:
        if item in ting:
            word = word.replace(item,'')
    return word
        


def test_snake_case():
    assert snake_case('Hello World!') == 'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'




def camel_case(text):
        for i in text:
            if i in string.punctuation:
                text = text.replace(i,'')
        camel_list = list(text.title())
        
        
        camel_list[0] = camel_list[0].lower()
        
        camel_list = "".join(camel_list)
        
        return camel_list.replace(' ','')
       


def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'


def alternating_case(text):
    sting = ''
    x = 1
    for i in text:
        if x % 2 == 0:
            sting += i.lower()
            x +=1

        else:
            sting += i.upper()
            x +=1

    return sting





def test_alternating_case():
    assert alternating_case('Hello World!') == 'HeLlO WoRlD!'
    assert alternating_case(
        'This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'