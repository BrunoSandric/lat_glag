# Simple letter translator from Latinica to Glagoljica

Takes a sentence written in Latinica, and transleates it to Glagoljica. Sends both versions to print. 

#Quick start

- Setup/Init environment `activate <PATH_TO_ENV_ACTIVATE>
- install dependencies if needed `pip3 -r requirements.txt`
# Project description 
Simple project descripion.

- Self contained app. 
- All functions should be in one file. 
- Non dependant of running environment (browser, iframe, native).

Data flow is linear, and goes from top to bottom, in order presented in folowing subchapters. 

## GUI

Simple web page with sentence display and onscreenkeyboard. 

## Translator funct.
Input(sentence, sentence_alphabet_type)
Output(original, translated)

Translate letters from one set to other. 

## Prepare to print
Input(original, translated)
Output(pdf_for_print)

## Send to print
Only function to have knowlage of outside world. 
