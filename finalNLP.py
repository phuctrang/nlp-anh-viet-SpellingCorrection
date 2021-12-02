import re
import sys
import unicodedata as ud
import streamlit as st
from spellcheck_words import is_spelled_correctly
from spellcheck_words_vi import is_spelled_correctly_vi
from textblob import TextBlob
from gingerit.gingerit import GingerIt
warning = '\033[91m'
unwarning = '\033[m'
from load_css import local_css
local_css("style.css")
x = '\n' + "<span class='highlight green'>"
y = "</span>"
x1 = '\n' + "<span class='highlight green1'>"
y1 = "</span>"
h1 = '\n' + "<span class='highlight hd'>"
h2 = "</span>"
                                                                                                           #<marquee direction="up">Vân canh thông tin</marquee>
def header(url):
    st.markdown(f'<p style="background-color:#00004d;text-align:center;color:#ff0066;font-size:40px;text-align=center;border-radius:10%;font-family: "Times New Roman", Times, serif;"><marquee direction="right">{url}</marquee></p>', unsafe_allow_html=True)
header('NLP - SPELLING CORRECTION - HPT')
menu = ["1. Introduction", "2. Check spelling Words", "3. Correct spelling words", "4. Check spelling grammar", "5. Correct spelling grammar"]
choice = st.sidebar.selectbox("OPTIONS", menu)
def so_Luong_Amtiet(text):
    # TODO: Fix bug on datetime, E.g. 2013/10/20 09:20:30
    text = ud.normalize('NFC', text)
    sign = ["==>", "->", "\.\.\.", ">>"]
    digits = "\d+([\.,_]\d+)+"
    email = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    web = "^(http[s]?://)?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$"
    datetime = [
        "\d{1,2}\/\d{1,2}(\/\d+)?",
        "\d{1,2}-\d{1,2}(-\d+)?",
    ]
    word = "\w+"
    non_word = "[^\w\s]"
    abbreviations = [
        "[A-ZĐ]+\.",
        "Tp\.",
        "Mr\.", "Mrs\.", "Ms\.",
        "Dr\.", "ThS\."
    ]
    patterns = []
    patterns.extend(abbreviations)
    patterns.extend(sign)
    patterns.extend([web, email])
    patterns.extend(datetime)
    patterns.extend([digits, non_word, word])
    patterns = "(" + "|".join(patterns) + ")"
    if sys.version_info < (3, 0):
        patterns = patterns.decode('utf-8')
    tokens = re.findall(patterns, text, re.UNICODE)
    return [token[0] for token in tokens]
# EN
def check_words(data_check):
    data_check.replace(".", "")
    data_check.replace("I", "")
    data = so_Luong_Amtiet(data_check)
    # data = data.remove('?')
    dem = 0
    for i in range(len(data)):
        if not is_spelled_correctly(data[i]):
            dem +=1
            str ="".join(data[i])
            a = "<span class='highlight blue'>"
            b = "</span>"
            str1 = a+str+b
            data[i] = str1
    return {"result": data, "false_number": dem}
# VI
def check_words_vi(data_check):
    data = so_Luong_Amtiet(data_check)
    dem = 0
    # data = data.remove('?')
    for i in range(len(data)):
        if not is_spelled_correctly_vi(data[i]):
            dem += 1
            str ="".join(data[i])
            a = "<span class='highlight blue'>"
            b = "</span>"
            str1 = a+str+b
            data[i] = str1
    return {"result": data, "false_number": dem}
#EN
def correct_words(data_input):
    data_input = so_Luong_Amtiet(data_input)
    data_input1 = " ".join(data_input)
    text = TextBlob(data_input1)
    kq = text.correct()
    return kq

#EN
def Check_grammar(data_input):
    dem = 0
    data_input = so_Luong_Amtiet(data_input)
    data_input = " ".join(data_input)
    dip = data_input.split('.')
    parse = GingerIt()
    for i in range(len(dip)):
        correct_i = parse.parse(dip[i])["result"]
        if dip[i] not in correct_i:
            dem +=1
            a = "<span class='highlight blue'>"
            b = "</span>"
            # str1 = a + str + b
            dip[i] = a + dip[i] + b
    rt = "".join(dip)
    return {"result": rt, "false_number": dem}
#EN
def Correct_grammar(data_input):
    data_input = so_Luong_Amtiet(data_input)
    data_input = " ".join(data_input)
    dip = data_input.split('.')
    parse = GingerIt()
    for i in range(len(dip)):
        correct_i = parse.parse(dip[i])["result"]
        if dip[i] not in correct_i:
            dip[i] = parse.parse(dip[i])["result"]
    # rt = "\r\n".join(dip)
    rt = ".".join(dip)
    return rt
if choice == "1. Introduction":
    a = "<span class='highlight blue'>"
    b = "</span>"
    sai = a +'correctio' +b
    t1 = x+'Website' +y
    t = x + 'Welcome to the spelling '+ y
    ok  = t + sai + t1
    st.markdown(ok, unsafe_allow_html=True)
    # st.image("trang.jpg", width=400)
    ##<marquee direction="up">Vân can<marquee direction="up">h thông tin</marquee>
    new_title = '<p style="font-family:sans-serif; color:#baf605; font-size: 42px;">&#10004; A cat</p>'
    new_title1 = '<p style="font-family:sans-serif; color:red; font-size: 42px;text-decoration: line-through;">A doog</p>'
    new_title2 = '<p style="font-family:sans-serif; color:#fff; font-size: 42px;">Author</p>'
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(new_title, unsafe_allow_html=True)
        st.image("https://static.streamlit.io/examples/cat.jpg")
    with col2:
        st.markdown(new_title1, unsafe_allow_html=True)
        st.image("https://static.streamlit.io/examples/dog.jpg")
    with col3:
        st.markdown(new_title2, unsafe_allow_html=True)
        st.image("https://scontent.fdad3-4.fna.fbcdn.net/v/t1.6435-9/58068344_576680626075948_468038172681437184_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=174925&_nc_ohc=zqEl80ipoDAAX8dz9Ze&tn=txMtl062vm3NfXl6&_nc_ht=scontent.fdad3-4.fna&oh=2c3a31c1ddfeefc4c2ee7b05c5f1380a&oe=61C7042E", width=250)
        st.markdown("Hồ Phúc Trang from ITK41C   Computer science")
if choice == "2. Check spelling Words":
    c = h1 + 'Check spelling Words'+ h2
    st.markdown(c, unsafe_allow_html=True)
    st.subheader = "Check spelling Words"
    input_type = st.selectbox(
        "SELECT A LANGUAGE TO CHECK WORDS",
        ("English", "Vietnamses"),
    )
    if input_type == "English":
        input_type1 = st.selectbox(
            "# SELECT YOUR INPUT ? #",
            ("Enter text", "Choose file"),
        )
        if input_type1 == "Enter text":
            Enter_text = st.text_input("\nEnter your text:")
            data = Enter_text
            if st.button("View this text:", key=1, on_click=None):
                st.text_area("CONTENTS: ", value=data, height=None, max_chars=None, key=1)
            if st.button("CHECK", key=2):
                st.markdown(data)
                check = " ".join(check_words(data)["result"])
                fal = check_words(data)["false_number"]
                c = "RESULT CHECKING: "
                c = x+c+y
                st.markdown(c, unsafe_allow_html=True)
                st.markdown(check, unsafe_allow_html=True)
                st.markdown(x1 + "Detected error is: " + y1 + x+ str(fal)+y, unsafe_allow_html=True)
                # st.text_area("\nRESULT CHECKING: ", value=check, height=None, max_chars=None, key=2)
                # st.download_button(label='Download text', data=check, file_name='output_check_words.txt')

        elif input_type1 == "Choose file":
            txt_file = st.file_uploader("Choose file to checking: ", type=["txt"])
            if st.button("View this file:", key=1, on_click=None):
                data = txt_file.read().decode()
                st.text_area("CONTENTS of :" + txt_file.name, value=data, height=None, max_chars=None, key=1)
            if st.button("CHECK", key=2):
                data = txt_file.read().decode()
                st.markdown(data)
                check = " ".join(check_words(data)["result"])
                fal = check_words(data)["false_number"]
                c = "RESULT CHECKING: "
                c = x+c+y
                st.markdown(c, unsafe_allow_html=True)
                st.markdown(check, unsafe_allow_html=True)
                st.markdown(x1 + "Detected error is: " + y1 + x+ str(fal)+y, unsafe_allow_html=True)
                # st.text_area("\nRESULT CHECKING: ", value=check, height=None, max_chars=None, key=2)
                # st.download_button(label='Download text', data=check, file_name='output_check_words.txt')
    elif input_type == "Vietnamses":
        input_type2 = st.selectbox(
            "Chọn hình thức đầu vào của bạn !",
            ("Nhập trực tiếp", "Chọn tệp"),
        )
        if input_type2 == "Nhập trực tiếp":
            Enter_text = st.text_input("\nNhập vào chuỗi cần kiểm tra:")
            data = Enter_text
            if st.button("Xem lại đoạn văn bản này", key=1, on_click=None):
                st.text_area("Nội dung: ", value=data, height=None, max_chars=None, key=1)
            if st.button("BẮT ĐẦU KIỂM TRA", key=2):
                st.markdown(data)
                check = " ".join(check_words_vi(data)["result"])
                fal = check_words_vi(data)["false_number"]
                c = "Kết quả là: "
                c = x + c + y
                st.markdown(c, unsafe_allow_html=True)
                st.markdown(check, unsafe_allow_html=True)
                st.markdown(x1+"Lỗi sai được phát hiện là: "+ y1 + x+ str(fal)+y, unsafe_allow_html=True)
                # st.text_area("\nRESULT CHECKING: ", value=check, height=None, max_chars=None, key=2)
                # st.download_button(label='Download text', data=check, file_name='output_check_words.txt')

        elif input_type2 == "Chọn tệp":
            txt_file = st.file_uploader("Chọn một tệp từ máy của bạn: ", type=["txt"])
            if st.button("Xem tệp", key=1, on_click=None):
                data = txt_file.read().decode()
                st.text_area("Nội dung của :" + txt_file.name, value=data, height=None, max_chars=None, key=1)
            if st.button("BẮT ĐẦU KIỂM TRA", key=2):
                data = txt_file.read().decode()
                st.markdown(data)
                check = " ".join(check_words_vi(data)["result"])
                fal = check_words_vi(data)["false_number"]
                c = "Kết quả là: "
                c = x + c + y
                st.markdown(c, unsafe_allow_html=True)
                st.markdown(check, unsafe_allow_html=True)
                st.markdown(x1 + "Lỗi sai được phát hiện là: " + y1 + x+ str(fal)+y, unsafe_allow_html=True)
if choice == "3. Correct spelling words":
    c = h1 + 'Correct spelling Words' + h2
    st.markdown(c, unsafe_allow_html=True)
    st.subheader = "Correct spelling Words"
    input_type = st.selectbox(
        "SELECT A LANGUAGE TO CORRECT WORDS",
        ("English", "Vietnamses"),
    )
    if input_type == "English":
        input_type1 = st.selectbox(
            "# SELECT YOUR INPUT ? #",
            ("Enter text", "Choose file"),
        )
        if input_type1 == "Enter text":
            Enter_text = st.text_input("Enter your text:")
            data = Enter_text
            if st.button("View this text:", key=1, on_click=None):
                st.text_area("CONTENTS: ", value=data, height=None, max_chars=None, key=1)
            if st.button("CORRECT", key=2):
                st.markdown(data)
                check = "".join(correct_words(data))
                st.text_area("\nRESULT CORRECT: ", value=check, height=None, max_chars=None, key=2)
                new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">&#10004;</p>'
                st.markdown(new_title, unsafe_allow_html=True)
                st.download_button(label='Download this text', data=check, file_name='output_correct.txt')
        elif input_type1 == "Choose file":
            txt_file = st.file_uploader("Choose file to spelling correct: ", type=["txt"])
            if st.button("View this file:", key=1, on_click=None):
                data = txt_file.read().decode()
                st.text_area("CONTENTS of :" + txt_file.name, value=data, height=None, max_chars=None, key=1)
            if st.button("CORRECT", key=2):
                data = txt_file.read().decode()
                st.markdown(data)
                check = "".join(correct_words(data))
                st.text_area("\nRESULT CORRECT: ", value=check, height=None, max_chars=None, key=2)
                new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">&#10004;</p>'
                st.markdown(new_title, unsafe_allow_html=True)
                st.download_button(label='Download text', data=check, file_name='output_correct.txt')
    elif input_type == "Vietnamses":
    	st.markdown("Updating ... hmmm! ")
if choice == "4. Check spelling grammar":
    c = h1 + 'Check spelling grammar' + h2
    st.markdown(c, unsafe_allow_html=True)
    st.subheader = "Check spelling grammar"
    input_type = st.selectbox(
        "# SELECT YOUR INPUT ? #",
        ("Enter text", "Choose file"),
    )
    if input_type == "Enter text":
        Enter_text = st.text_input("Enter your text:")
        data = Enter_text
        if st.button("View this text:", key=1, on_click=None):
            st.text_area("CONTENTS: ", value=data, height=None, max_chars=None, key=1)
        if st.button("CHECK", key=2):
            st.markdown(data)
            check = "".join(Check_grammar(data)["result"])
            fal = Check_grammar(data)["false_number"]
            c = "RESULT CHECKING: "
            c = x + c + y
            st.markdown(c, unsafe_allow_html=True)
            st.markdown(check, unsafe_allow_html=True)
            st.markdown(x1 + "Detected error is: " + y1 + x + str(fal) + y, unsafe_allow_html=True)
            # st.text_area("\nRESULT CHECK: ", value=check, height=None, max_chars=None, key=2)
            # st.download_button(label='Download this text', data=check, file_name='output_CHECK_GR.txt')
    elif input_type == "Choose file":
        txt_file = st.file_uploader("Choose file to check grammar: ", type=["txt"])
        if txt_file:
            data = txt_file.read().decode()
            if st.button("View this file:", key=1, on_click=None):
                # st.markdown(txt_file.read().decode())
                st.text_area("CONTENTS OF : " + txt_file.name, value=data, height=None, max_chars=None,key=1)
            if st.markdown(txt_file.read().decode()):
                if st.button("CHECK", key=2):
                    st.markdown(data)
                    check = Check_grammar(data)
                    check = Check_grammar(data)["result"]
                    fal = Check_grammar(data)["false_number"]
                    c = "RESULT CHECKING: "
                    c = x + c + y
                    # st.markdown(c + check, unsafe_allow_html=True)
                    st.markdown(c, unsafe_allow_html=True)
                    st.markdown(check, unsafe_allow_html=True)
                    st.markdown(x1 + "Detected error is: " + y1 + x + str(fal) + y, unsafe_allow_html=True)
                    # st.text_area("\nRESULT CHECK SPELLING: error syntax is %!%[sentence]%1%", value=check, height=300, max_chars=None, key=2)
                    # st.download_button(label='Download text', data=check, file_name='output_check_grammar.txt')
import streamlit as st
import os
import time
import glob
from gtts import gTTS
from googletrans import Translator
try:
    os.mkdir("temp")
except:
    pass
translator = Translator()
def text_to_speech(input_language, output_language, text, tld):
    # translation = translator.translate(text, src=input_language, dest=output_language)
    # trans_text = translation.text
    # tts = gTTS(trans_text, lang=output_language, tld=tld, slow=False)
    # my_file_name = "audio"
    # tts.save(f"temp/{my_file_name}.mp3")
    # return my_file_name, trans_text
    translation = translator.translate(text, src=input_language, dest=output_language)
    trans_text = translation.text
    tts = gTTS(trans_text, lang=output_language, tld=tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, trans_text
if choice == "5. Correct spelling grammar":
    correctLocal = ''
    outp_Local = ''
    c = h1 + 'Correct spelling grammar' + h2
    st.markdown(c, unsafe_allow_html=True)
    st.subheader = "Correct spelling grammar"
    input_type = st.selectbox(
        "# SELECT YOUR INPUT ? #",
        ("Enter text", "Choose file"),
    )
    if input_type == "Enter text":
        Enter_text = st.text_input("Enter your text:")
        data = Enter_text
        if st.button("View this text:", key=1, on_click=None):
            st.text_area("CONTENTS: ", value=data, height=None, max_chars=None, key=1)
        if st.button("CORRECT-GR", key=2):
            st.markdown(data)
            correct = "".join(Correct_grammar(data))
            st.text_area("\nRESULT CORRECT: ", value=correct, height=None, max_chars=None, key=2)
            st.download_button(label='Download this text', data=correct, file_name='output_CORR_GR.txt')


        out_lang = st.selectbox(
            "EXTRA FEATURE :\n\tSELECT YOUR OUTPUT LANGUAGE TO TRANSLATE ",
            ("Vietnamese", "Japanese", "Hindi", "korean"),
        )
        correctLocal = "".join(Correct_grammar(data))
        if out_lang == "Vietnamese":
            if st.button("Convert to vietnamese"):
                output_language = "vi"
                inp = "en"
                tld = "com"
                # correctLocal = "".join(Correct_grammar(data))
                result, output_text = text_to_speech(inp, output_language, correctLocal, tld)
                audio_file = open(f"temp/{result}.mp3", "rb")
                audio_bytes = audio_file.read()
                st.markdown(f"## Your audio:")
                st.audio(audio_bytes, format="audio/mp3", start_time=0)
                # display_output_text = st.checkbox("Display output text")
            if st.button("Display_output_text"):
                inp = "en"
                tld = "com"
                output_language = "vi"
                result, output_text = text_to_speech(inp, output_language, correctLocal, tld)
                st.write(f" {output_text}")
        elif out_lang == "Japanese":
            if st.button("Convert to Japanese"):
                output_language = "ja"
                inp = "en"
                tld = "com"
                # correctLocal = "".join(Correct_grammar(data))
                result, output_text = text_to_speech(inp, output_language, correctLocal, tld)
                audio_file = open(f"temp/{result}.mp3", "rb")
                audio_bytes = audio_file.read()
                st.markdown(f"## Your audio:")
                st.audio(audio_bytes, format="audio/mp3", start_time=0)
                # outp_Local = f" {output_text}"
                # # display_output_text = st.checkbox("Display output text")
            if st.button("Display_output_text"):
                inp = "en"
                tld = "com"
                output_language = "ja"
                result, output_text = text_to_speech(inp, output_language, correctLocal, tld)
                st.write(f" {output_text}")
        elif out_lang == "Hindi":
            if st.button("Convert to Híndi"):
                output_language = "hi"
                inp = "en"
                tld = "com"
                # correctLocal = "".join(Correct_grammar(data))
                result, output_text = text_to_speech(inp, output_language, correctLocal, tld)
                audio_file = open(f"temp/{result}.mp3", "rb")
                audio_bytes = audio_file.read()
                st.markdown(f"## Your audio:")
                st.audio(audio_bytes, format="audio/mp3", start_time=0)
                # outp_Local = f" {output_text}"
                # # display_output_text = st.checkbox("Display output text")
            if st.button("Display_output_text"):
                inp = "en"
                tld = "com"
                output_language = "hi"
                result, output_text = text_to_speech(inp, output_language, correctLocal, tld)
                st.write(f" {output_text}")
        else:
            if st.button("Convert to korean"):
                output_language = "ko"
                inp = "en"
                tld = "com"
                # correctLocal = "".join(Correct_grammar(data))
                result, output_text = text_to_speech(inp, output_language, correctLocal, tld)
                audio_file = open(f"temp/{result}.mp3", "rb")
                audio_bytes = audio_file.read()
                st.markdown(f"## Your audio:")
                st.audio(audio_bytes, format="audio/mp3", start_time=0)
                # outp_Local = f" {output_text}"
                # # display_output_text = st.checkbox("Display output text")
            if st.button("Display_output_text"):
                inp = "en"
                tld = "com"
                output_language = "ko"
                result, output_text = text_to_speech(inp, output_language, correctLocal, tld)
                st.write(f" {output_text}")
    elif input_type == "Choose file":
        txt_file = st.file_uploader("Choose file to correct grammar: ", type=["txt"])
        #
        if txt_file:
            data = txt_file.read().decode()
            if st.button("View this file:", key=1, on_click=None):
                # st.markdown(txt_file.read().decode())
                st.text_area("CONTENTS OF : " + txt_file.name, value=data, height=None, max_chars=None,key=1)
            if st.markdown(txt_file.read().decode()):
                if st.button("CORRECT", key=2):
                    st.markdown(data)
                    correct = Correct_grammar(data)
                    st.text_area("\nRESULT CORRECT SPELLING: ", value=correct, height=300, max_chars=None, key=2)
                    st.download_button(label='Download this text', data=correct, file_name='output_correct_grammar.txt')

                out_lang = st.selectbox(
                    "EXTRA FEATURE :\n\tSELECT YOUR OUTPUT LANGUAGE TO TRANSLATE ",
                    ("Vietnamese", "Japanese", "Hindi", "korean"),
                )
                correctLocal = "".join(Correct_grammar(data))
                if out_lang == "Vietnamese":
                    if st.button("Convert to vietnamese"):
                        output_language = "vi"
                        inp = "en"
                        tld = "com"
                        # correctLocal = "".join(Correct_grammar(data))
                        result, output_text = text_to_speech(inp, output_language, correctLocal, tld)
                        audio_file = open(f"temp/{result}.mp3", "rb")
                        audio_bytes = audio_file.read()
                        st.markdown(f"## Your audio:")
                        st.audio(audio_bytes, format="audio/mp3", start_time=0)
                        # display_output_text = st.checkbox("Display output text")
                    if st.button("Display_output_text"):
                        inp = "en"
                        tld = "com"
                        output_language = "vi"
                        result, output_text = text_to_speech(inp, output_language, correctLocal, tld)
                        st.write(f" {output_text}")
                elif out_lang == "Japanese":
                    if st.button("Convert to Japanese"):
                        output_language = "ja"
                        inp = "en"
                        tld = "com"
                        # correctLocal = "".join(Correct_grammar(data))
                        result, output_text = text_to_speech(inp, output_language, correctLocal, tld)
                        audio_file = open(f"temp/{result}.mp3", "rb")
                        audio_bytes = audio_file.read()
                        st.markdown(f"## Your audio:")
                        st.audio(audio_bytes, format="audio/mp3", start_time=0)
                        # outp_Local = f" {output_text}"
                        # # display_output_text = st.checkbox("Display output text")
                    if st.button("Display_output_text"):
                        inp = "en"
                        tld = "com"
                        output_language = "ja"
                        result, output_text = text_to_speech(inp, output_language, correctLocal, tld)
                        st.write(f" {output_text}")
                elif out_lang == "Hindi":
                    if st.button("Convert to Híndi"):
                        output_language = "hi"
                        inp = "en"
                        tld = "com"
                        # correctLocal = "".join(Correct_grammar(data))
                        result, output_text = text_to_speech(inp, output_language, correctLocal, tld)
                        audio_file = open(f"temp/{result}.mp3", "rb")
                        audio_bytes = audio_file.read()
                        st.markdown(f"## Your audio:")
                        st.audio(audio_bytes, format="audio/mp3", start_time=0)
                        # outp_Local = f" {output_text}"
                        # # display_output_text = st.checkbox("Display output text")
                    if st.button("Display_output_text"):
                        inp = "en"
                        tld = "com"
                        output_language = "hi"
                        result, output_text = text_to_speech(inp, output_language, correctLocal, tld)
                        st.write(f" {output_text}")
                else:
                    if st.button("Convert to korean"):
                        output_language = "ko"
                        inp = "en"
                        tld = "com"
                        # correctLocal = "".join(Correct_grammar(data))
                        result, output_text = text_to_speech(inp, output_language, correctLocal, tld)
                        audio_file = open(f"temp/{result}.mp3", "rb")
                        audio_bytes = audio_file.read()
                        st.markdown(f"## Your audio:")
                        st.audio(audio_bytes, format="audio/mp3", start_time=0)
                        # outp_Local = f" {output_text}"
                        # # display_output_text = st.checkbox("Display output text")
                    if st.button("Display_output_text"):
                        inp = "en"
                        tld = "com"
                        output_language = "ko"
                        result, output_text = text_to_speech(inp, output_language, correctLocal, tld)
                        st.write(f" {output_text}")




