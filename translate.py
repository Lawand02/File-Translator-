from googletrans import Translator
import PyPDF2
import sys
import docx

translator = Translator()

type = input('Enter type file to be translate : txt - pdf - docx - direct : direct translation: ')


lan = input('please Enter language to translate: ')

if str.lower(type) == "direct":
    in_txt=input('text you want translate: ')
    translation = translator.translate(in_txt,dest=lan)
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
    sys.exit()
output = input('Enter name target file please: ')
input = input('Enter name source file please: ')

if str.lower(type) == 'pdf':
    with open(input+'.pdf', 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    translated_text = translator.translate(text, dest=lan).text
    with open(output+'.txt', 'w', encoding='utf-8') as f:
        f.write(translated_text)
    print('successfully...')

    
elif str.lower(type) == "docx":
    doc = docx.Document(input+".docx")
    all_paras = doc.paragraphs
    len(all_paras)
    allText = []
    for para in all_paras:
        read=para.text
        allText.append(read)
        data = '\n'.join(allText)
        translated_text = translator.translate(data, dest=lan).text
        # print(translated_text)
    with open(output+'.txt', 'w', encoding='utf-8') as f:
        f.write(translated_text)
    print('Translation completed successfully.')


elif str.lower(type) == "txt":
    # Read the contents of the input file
    #The code reads the contents of the input file using open and read functions, and assigns the content to the text variable.
    with open(input+'.txt', 'r', encoding='utf-8') as f:
        source_text = f.read()

    # detect the language of the source text
    detected = translator.detect(source_text)

    #The translator.translate() method is used to translate the text to the desired language. It takes the text as input and specifies the target language using the dest parameter.
    translated = translator.translate(source_text, dest=lan)
    if detected  == 'ar':
        direction_code = '\u200F' # Right-to-Left Mark (RLM)
    else:
        direction_code = '\u200E' # Left-to-Right Mark (LRM)

    
    # Write the translated text to the output file
    with open(output+'.txt', 'w', encoding='utf-8') as f:
          #The translated text is obtained from the translation.text attribute.
        #The code then writes the translated text to the output file using open and write functions.
        f.write(translated.text)
    print('Translation completed successfully.')
# if str.lower(type) != "txt" or "pdf" or "docx" or "direct":
#     # If the file type is not 'txt ,pdf ,docx', an error message is displayed
#     print('Invalid file type.')
#     sys.exit()

