from tkinter import *
import cv2
import PIL.Image, PIL.ImageTk
import pyttsx3,datetime
import speech_recognition as sr
import os,random,smtplib,roman,playsound,time,sys
from PIL import Image
import ctypes,wikipedia,datetime,json,re
import webbrowser,requests,urllib,selenium
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch

from decte import *

wikipedia.set_lang('vi')
language = 'vi'

#numbers = {'hundred': 100, 'thousand': 1000, 'lakh': 100000}
#a = {'name': 'your email'}

window = Tk()
window.resizable(height=True,width=True)

global var
global var1
global text


var = StringVar()
var1 = StringVar()


def speak(text):
    print("Trợ lý ảo: ", text)
    engine = pyttsx3.init()  # hàm khỏi tạo
    voices = engine.getProperty('voices')  # lấy all giong tròn máy
    rate = engine.getProperty('rate')  # tốc đọ nói
    volume = engine.getProperty('volume')  # âm
    engine.setProperty('volume', volume - 0.0)  # thay đổi âm
    engine.setProperty('rate', rate - 50)  # giọng nói bình thương
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


def hello(name):
    day_time = int(strftime('%H'))
   # day_time = 9
    if 0 <= day_time < 11:
        var1.set(f"Chào bạn {name}.\nChúc bạn buổi sáng tốt lành")
        window.update()
        speak(f"Chào bạn {name}.Chúc bạn buổi sáng tốt lành")
    elif 11 <= day_time < 13:
        var1.set(f"Chào bạn {name}.\nChúc bạn có một trưa vui vẽ")
        window.update()
        speak(f"Chào bạn {name}.Chúc bạn có một trưa vui vẽ")
    elif 13 <= day_time < 18:
        var1.set(f"Chào bạn {name}.\nBuổi  vui vẽ bạn nhé ")
        window.update()
        speak(f"Chào bạn {name}.Buổi  vui vẽ bạn nhé ")
    elif 18 <= day_time < 22:
        var1.set(f"Chào bạn {name}.\nBạn ăn cơm chưa  ")
        window.update()
        speak(f"Chào bạn {name}.Bạn ăn cơm chưa  ")
    elif 22 <= day_time <= 23:
        var1.set(f"Chào bạn {name} Muội rồi. Bạn nên đi ngủ nhé ")
        window.update()
        speak(f"Chào bạn {name} Muội rồi. Bạn nên đi ngủ nhé ")
    else:
        var1.set("Thời gian bên tôi đàn lỗi.\nBạn vui lòng kiểm tra lại ")
        window.update()
        speak(f"Thời gian bên tôi đang lỗi.\nBạn vui lòng kiểm tra lại ")


def get_audio():
    ear_robot = sr.Recognizer()
    with sr.Microphone() as source:
        print("Trợ lý ảo: Đang nghe !--__--!")
        var1.set("Trợ lý ảo: Đang nghe !--__--!")
        window.update()
        audio  = ear_robot.listen(source, phrase_time_limit= 4) # che trong s
        try:
            text = ear_robot.recognize_google(audio, language = "vi-VN")
            print("Người dùng: ",text)
            var.set(text)
            window.update()
            return text
        except:
            print("Trợ lý ảo: Lồi  ")

def get_audio_2():
    ear_robot = sr.Recognizer()
    with sr.Microphone() as source:
        print("Đang nghe ===========")
        audio = ear_robot.listen(source, phrase_time_limit= 4)
    try:
        text = ear_robot.recognize_google(audio, language="vi-VN")
    except:
        print("Nhận dạng giọng nói thất bại. Vui long nhập lệnh ở dưới")
        text = get_audio_2()
    return text.lower()

def vonglap():
    while True:
        text = get_audio_2().lower()
        if "ok bạn".lower() in text:
            print(f"Trợ lý ảo: {text}")
            break
        if text != "":
            print(f"Trợ lý ảo: {text}")
            continue
        else:
            print(f"Trợ lý ảo: {text}")
            break


def stop():
    var.set("Hẹn gặp lại\n chúc bạn một ngày tốt lành")
    window.update()
    speak("Hẹn gặp lại.Chúc bạn một ngày tốt lành ")

def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower() # chuyển sang chữ thường
        elif i < 2:
            var1.set("Tôi không nghe rõ bạn nói\nHãy nói lại bạn nhé")
            window.update()
            speak("Tôi không nghe rõ bạn nói, \n Hãy nói lại bạn nhé")
    time.sleep(3) # tạm dừng 3s
    stop()
    return 0

def get_time(text):
    now = datetime.datetime.now()
    if 'giờ' in text:
        var.set(f"{now.hour}:{now.minute}:{now.second}")
        window.update()
        speak(f"Bây giời là {now.hour} giời {now.minute} phút {now.second} giây ")
    elif 'ngày' in text:
        var.set(f"{now.day}/{now.month}/{now.year}")
        window.update()
        speak(f"Hôm nay là ngày {now.day} tháng {now.month} năm {now.year}")
    else:
        var.set("Xin lỗi tôi chưa hiểu bạn nói gì ")
        window.update()
        speak("Xin lỗi tôi chưa hiểu bạn nói gì ")

def open_application(text):
    if "google" in text:
        var.set("Mở Google Chrome ")
        window.update()
        speak("Mở Google Chrome")
        # shilt trải - tắt mới thoát chương trình
        os.startfile(r"C:\\Program Files\\Google\Chrome\\Application\\chrome.exe")
    elif "team view" in text:
        var.set("Đang mở TeamView ")
        window.update()
        speak("Đang mở TeamView ")
        os.startfile("C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe")
    elif "firefox" in text:
        var.set("Đang mở FireFox")
        window.update()
        speak("Đang mở FireFox ")
        os.startfile(r"C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    elif "word" in text:
        var1.set("Đang mở word")
        window.update()
        speak("Đang mở word")
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word 2016.lnk")
    elif "excel" in  text:
        var1.set("Đang mở Excel")
        window.update()
        speak("Đang mở excel")
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel 2016.lnk")
    else:
        var.set("Đã xảy lỗi")
        window.update()
        speak("Ứng dụng chưa được cài đặt")
    vonglap()
#open_application("team view ")
def open_website(text):
    reg_ex = re.search('mở (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = "https://www." + domain
        webbrowser.open(url)
        var1.set("Trang web đã được mở  ")
        window.update()
        speak("Trang web bạn đã được mở ")
        if input("Nhấn q để tiếp tục ") == "q":
            pass
        return True
    else:
        return False
    vonglap()
# open_website("mở youtube.com")

def open_google_and_search(text):
    search_for = str(text).split("kiếm", 1)[1]  # lấy phần tử số 1
    url = f"https://www.google.com/search?q={search_for}"
    webbrowser.get().open(url)
    var1.set("Đây là thông tin bạn cần tìm ")
    window.update()
    speak("Đây là thông tin bạn cần tìm ")
    vonglap()
# open_google_and_search("tim kiếm hoa ")

def open_google_and_search2():
    var1.set("Thông tin bạn cần tìm là gì")
    window.update()
    speak("Thông tin bạn cần tìm là gì ")
    search_for = str(get_text()).lower()  # chuyển chữ thường
    url = f"https://www.google.com/search?q={search_for}"
    webbrowser.get().open(url)
    var1.set("Đây là thông tin bạn cần tìm ")
    window.update()
    speak("Đây là thông tin bạn cần tìm ")
    vonglap()
# open_google_and_search2()

def send_email(text):
    var1.set("Bạn gửi email cho ai vậy ?")
    window.update()
    speak("Bạn gửi email cho ai vậy ?")
    recipient = get_text()
    if "minh" in recipient or "mình" in recipient or "Hùng" in recipient:
        var1.set("Nội dung email bạn muốn gửi là gì")
        window.update()
        speak("Nội dung email bạn muốn gửi là gì ! ... >")
        content = get_text()
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login("nttam.18it5@sict.udn.vn", "nguyentrongtam2468.")
        mail.sendmail("nttam.18it5@sict.udn.",
                      "nttam.18it5@vku.udn.vn", str(content).encode("utf-8"))
        mail.close()
        var1.set("Email của bạn đã được gửi.\nBạn vui lòng kiểm tra ")
        window.update()
        speak("Email của bạn đã được gửi.Bạn vui lòng kiểm tra ")
    else:
        var1.set("Tôi không hiểu bạn muốn gửi email cho ai\nVui lòng thử hiện lại chức năng nhé ! ")
        window.update()
        speak("Tôi không hiểu bạn muốn gửi email cho ai.Vui lòng thử hiện lại chức năng nhé ! ")
    vonglap()
def nhac():
    var1.set("Bạn muốn nghe bài hát nào ?")
    window.update()
    speak("Bạn muốn nghe bài hát nào ?")
    search = get_text()
    while True:
        result = YoutubeSearch(search, max_results=18).to_dict()  # lưu toàn bộ dữ liệu
        if result:
            break
    url = f"https://www.youtube.com" + result[0]['url_suffix']
    webbrowser.get().open(url)
    speak("Bài hát bạn yêu cầu đã được mở.")
    print(result)
    vonglap()

def tell_me_about():
    try:
        var1.set("Bạn muốn biết về gì ")
        window.update()
        speak("Bạn muốn biết về gì ! ")
        text = get_text()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0])
        time.sleep(10)
        for content in contents[1:]:
            var1.set("Bạn muốn nghe thêm không ?")
            window.update()
            speak("Bạn muốn nghe thêm không")
            ans = get_text()
            if "có" not in ans:
                break
            speak(content)
            time.sleep(10)
        var1.set("Cảm ơn bạn đã lắng nghe!!!")
        window.update()
        speak('Cảm ơn bạn đã lắng nghe!!!')
    except:
        speak("Tôi không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại")
    vonglap()


def current_weather():
    var1.set("Bạn muốn xem thời tiết ở đâu ")
    window.update()
    speak("Bạn muốn xem thời tiết ở đâu ")
    # Đường dẫn trang web để lấy dữ liệu về thời tiết
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    # lưu tên thành phố vào biến city
    city = get_text()
    # nếu biến city != 0 và = False thì để đấy ko xử lí gì cả
    if not city:
        pass
    # api_key lấy trên open weather map
    api_key = "a7605b5f44931f71299dac0981de1372"
    # tìm kiếm thông tin thời thời tiết của thành phố
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    # truy cập đường dẫn  lấy dữ liệu thời tiết
    response = requests.get(call_url)
    # lưu dữ liệu thời tiết dưới dạng json và cho vào biến data
    data = response.json()

    # print(data) # json
    # kiểm tra nếu ko gặp lỗi 404 thì xem xét và lấy dữ liệu
    if data["cod"] != "404":

        # lấy value của key main
        city_res = data["main"]
        # nhiệt độ hiện tại
        current_temperature = city_res["temp"]
        # áp suất hiện tại
        current_pressure = city_res["pressure"]
        # độ ẩm hiện tại
        current_humidity = city_res["humidity"]

        # thời gian mặt trời
        suntime = data["sys"]
        # 	lúc mặt trời mọc, mặt trời mọc
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        # lúc mặt trời lặn
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])

        # thông tin thêm
        wthr = data["weather"]
        # mô tả thời tiết
        weather_description = wthr[0]["description"]
        # Lấy thời gian hệ thống cho vào biến now
        now = datetime.datetime.now()
        # hiển thị thông tin với người dùng

        content = f"""
        Hôm nay là ngày {now.day} tháng {now.month} năm {now.year}\n
        Mặt trời mọc vào {sunrise.hour} giờ {sunrise.minute} phút\n
        Mặt trời lặn vào {sunset.hour} giờ {sunset.minute} phút\n
        Nhiệt độ trung bình là {current_temperature} độ C\n
        Áp suất không khí là {current_pressure} héc tơ\n
        Độ ẩm là {current_humidity}%
        """
        var1.set(f"""Ngày {now.day}/{now.month}/{now.year}\n
        {current_temperature} độ C, P = {current_pressure},{current_humidity}%                
        """)
        window.update()
        speak(content)
    else:
        # nếu tên thành phố không đúng thì nó nói dòng dưới 227
        var1.set("Không tìm thấy địa chỉ của bạn")
        window.update()
        speak("Không tìm thấy địa chỉ của bạn")
    vonglap()
def play_youtube():
    var1.set("Nội dụng bạn cần tìm trên youtube là gì ")
    window.update()
    speak("Nội dụng bạn cần tìm trên youtube là gì ?")
    search = get_text()
    url = f"https://www.youtube.com/search?q={search}"
    webbrowser.get().open(url)
    var1.set("Đây là thông tin tôi tìn được bạn xem nhé  ")
    window.update()
    speak("Đây là thông tin tôi tìn được bạn xem nhé !")
    vonglap()
def play_youtube2():
    var1.set("Nội dung bạn cần tìm trên youtube là gì ?")
    window.update()
    speak("Nội dung bạn cần tìm trên youtube là gì ?")
    search = get_text()
    while True:
        result = YoutubeSearch(search, max_results=18).to_dict()  # lưu toàn bộ dữ liệu
        if result:
            break
    url = f"https://www.youtube.com" + result[0]['url_suffix']
    webbrowser.get().open(url)
    var1.set("Đây là thông tin tôi tìm\n được bạn xem qua nhé !")
    window.update()
    speak("Đây là thông tin tôi tìm được bạn xem qua nhé ! ")
    print(result)
    vonglap()
def change_wallpaper():
    api_key = "ls2eD5_RW2EnF-_2NUn_dilR2pUPahLCCJ2mTZ_OQI4"
    url = 'https://api.unsplash.com/photos/random?client_id=' + \
          api_key  # pic from unspalsh.com
    f = urllib2.urlopen(url)  # duyệt web ẩn không hiện
    json_string = f.read()
    f.close()
    parsed_json = json.loads(json_string)
    photo = parsed_json['urls']['full']  # đường dẫn của ảnh tải , chất lượng
    urllib2.urlretrieve(photo, r"F:\PycharmProjects\Do_An\TroLyAo_code\imagechange.png")
    image = os.path.join(r"F:\PycharmProjects\Do_An\TroLyAo_code\imagechange.png")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 3)
    var1.set("Hình nền máy tính bạn đã được thay đổi\nBạn vui lòng kiểm tra nhé ?")
    window.update()
    speak("Hình nền máy tính bạn đã được thay đổi. Bạn vui lòng kiểm tra nhé ?")
    vonglap()
def read_news():
    # b2ea790845b149e2a1e2c91a505ffdb9
    var1.set("Bạn muốn đọc báo về gì")
    window.update()
    speak("Bạn muốn đọc báo về gì")
    queue = get_text()
    params = {
        'apiKey': 'b2ea790845b149e2a1e2c91a505ffdb9',
        "q": queue,
    }
    api_result = requests.get('http://newsapi.org/v2/top-headlines?', params)
    api_response = api_result.json()
    print("Tin tức")

    for number, result in enumerate(api_response['articles'], start=1):
        print(
            f"""Tin {number}:\nTiêu đề: {result['title']}\nTrích dẫn: {result['description']}\nLink: {result['url']}
        """)
        if number <= 3:
            webbrowser.open(result['url'])
    vonglap()
def photo():
    stream = cv2.VideoCapture(0)
    grabbed, frame = stream.read()
    if grabbed:
        cv2.imshow('pic', frame)
        cv2.imwrite('pic.jpg', frame)
    stream.release()
    var1.set("Đã xong vui lòng kiểm trả ")
    window.update()
    vonglap()
def recordVideo():
    cap = cv2.VideoCapture(0)
    out = cv2.VideoWriter('output.mp4', -1, 20.0, (640, 480))
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    vonglap()

def help_me():
    var1.set("")
    window.update()
    speak("""
        Tôi có thể giúp bạn thực hiện các câu lệnh sau đây:
        1. Chào hỏi
        2. Hiển thị giờ
        3. Mở website và ứng dụng
        4. Tìm kiếm trên Google
        5. Gửi email
        6. Dự báo thời tiết
        7. Mở video nhạc
        8. Thay đổi hình nền máy tính
        9. Đọc báo hôm nay
        10. Cho bạn biết các định nghĩa
        Xin cảm ơn bạn
        """)

def play():
    btn2['state'] = 'disabled'
   # btn0['state'] = 'disabled'
    btn1.configure(bg='orange')
    # wishme()
    var1.set("Xin chào! Bạn tên là gì ?")
    window.update()
    speak("Xin chào. bạn tên là gì ? ")
    name = get_text()
    if name:
        var.set(name)
        window.update()
        var1.set(f"Xin chào bạn {name}")
        window.update()
        speak(f"Xin chào bạn {name}.")
        var1.set("Bạn cần tôi giúp gì cho bạn")
        window.update()
        speak(f'Bạn cần tôi giúp gì cho bạn ')
        var1.set("Bạn cần tôi giúp gì cho bạn ")
        window.update()
        while True:
            text = get_text()
            if not text:
                break
            elif "giúp gì ?" in text or "làm gì" in text:
                var.set(text)
                window.update()
                help_me()
            elif 'tạm biệt' in text or 'bye' in text or "hẹn gặp lại" in text:
                var.set(text)
                window.update()
                stop()
                break
            elif "chào" in text or "chào bạn" in text or "xin chào" in text:
                var.set(text)
                window.update()
                hello(name)
            elif "giờ" in text or "ngày" in text:
                var.set(text)
                window.update()
                get_time(text)
            elif "mở" in text:
                var.set(text)
                window.update()
                if '.' in text:
                    open_website(text)
                else:
                    open_application(text)
            elif "tìm kiếm " in text:
                var.set(text)
                window.update()
                if str(text).split("kiếm", 1)[1] == "":
                    open_google_and_search2()  # tìm kiếm với nôi dung chưa có . gọi chức năng tìm kiếm và nói nd
                else:
                    open_google_and_search(text)
            elif "email" in text or "mail" in text or "gmail" in text:
                var.set(text)
                window.update()
                send_email(text)
            elif "thời tiết" in text:
                var.set(text)
                window.update()
                current_weather()

            elif "youtube" in text:
                var.set(text)
                window.update()
                var1.set("Bạn muốn tìm kiếm danh sách hay mở video")
                window.update()
                speak("Bạn muốn tìm kiếm danh sách hay hay mở video ")
                yeu_cau = get_text()
                if "danh sách " in yeu_cau:
                    var.set(text)
                    window.update()
                    play_youtube()
                    if input():
                        pass
                elif "mở video" in yeu_cau:
                    var.set(text)
                    window.update()
                    play_youtube2()
                    if input("Tiếp tục y/n") == "y":
                        pass
            elif "laptop" in text or "hình nền" in text:
                var.set(text)
                window.update()
                change_wallpaper()
            elif "đọc báo" in text:
                var.set(text)
                window.update()
                read_news()
            elif "định nghĩa" in text or "khái niệm" in text:
                var.set(text)
                window.update()
                tell_me_about()
            elif "bài hát" in text or "bật nhạc" in text or "nghe nhạc" in text:
                var.set(text)
                window.update()
                nhac()
            elif "vật thể" in text or "đối tượng" in text or "nhận diện" in text:
                var.set(text)
                window.update()
                identified()
            elif "chụp ảnh" in text:
                var.set(text)
                window.update()
                photo()

            elif 'xem ảnh' in text:
                try:
                    im = Image.open('pic.jpg')
                    query = pytesseract.image_to_string(im)
                    speak(query)
                except Exception as e:
                    var.set("Không dữ liệu ")
                    window.update()
                    print(e)
            else:
                var1.set("Chức năng chưa có.\nBạn vui lòng chọn lại chức năng nhé")
                window.update()
                speak(f'Chức năng chưa có. Bạn vui lòng chọn lại chức năng nhé !')


def update(ind):
    frame = frames[(ind) % 100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

frame = Frame(window)
frame.pack(side="left")

label2 = Label(window, textvariable=var1, bg='#FAB60C')
label2.config(font=("Courier", 20))
var1.set('Trợ lý ')
label2.pack()

label1 = Label(window, textvariable=var, bg='#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Người dùng')
label1.pack()

frames = [PhotoImage(file='Assistant.gif', format='gif -index %i' % (i)) for i in range(100)]

window.title('')
label = Label(window, width=500, height=500)
label.pack()
window.after(0, update, 0)

btn1 = Button(text='Bắt đầu', width=20, command=play, bg='#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text='Thoát', width=20, command=window.destroy, bg='#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()

window.mainloop()


