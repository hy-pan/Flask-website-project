import json
import os

from flask import Flask, request
from flask import render_template

from settings import PIC_DIR, HOST,CSS_DIR


app = Flask(__name__)
count_num = 0

@app.route('/')
def index():
    return render_template('welcome.html', default_pic=os.path.join(
        HOST, 'static', 'default'),num1=os.path.join(
        HOST, 'static','image','1.jpg'),num2=os.path.join(
        HOST, 'static','image','2.jpg'),num3=os.path.join(
        HOST, 'static','image','3.jpg'),num4=os.path.join(
        HOST, 'static','image','4.jpg'),num5=os.path.join(
        HOST, 'static','image','5.jpg'),carousel_css=os.path.join(HOST, 'static','css','carousel.css'),jquery_carousel_js=os.path.join(HOST, 'static','js','jquery.carousel.js'))

@app.route('/upload', methods=['POST'])
def upload_pic():
    if request.method == 'POST':
        # get the picture
        pic = request.files['pic']
        # picname = request.form.get('picname')
        # picname = str(int(datetime.datetime.now().timestamp()))

        # save the picture
        picname = "picture.jpg"
        pic.save(os.path.join(PIC_DIR, 'upload', picname))


        # deep_learning algorithm
        """
        处理static/upload/picture
        保存为static/processed/picture_processed
        """
        global count_num
        # replace demo_RESNET.py with your own model
        os.system('cd /root/mx-rcnn && python demo_RESNET.py')
        os.system("python3 /root/web_project_phy/transform.py %s" % count_num )
        count_num = count_num + 1

        return json.dumps({
            "url": os.path.join(HOST, 'static','storage', '0000' + format(str(count_num-1), '0>3s') + '.jpg')
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2333)
