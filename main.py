from flask import Flask, render_template, request
import os
import youtube_dl

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin']='*'
    environ.headers['Access-Control-Allow-Method']='*'
    environ.headers['Access-Control-Allow-Headers']='x-requested-with,content-type'
    return environ
@app.route('/getVideoInfo',methods=['GET'])
def get_video_info():
    message = request.args.get('videoUrl')
    # print(message)
        # 创建 youtube-dl 对象
    ydl = youtube_dl.YoutubeDL()
    
    # 获取视频信息
    info = ydl.extract_info(message, download=False)
    
    # 获取视频的下载链接
    video_url = info['url']
    
    print('视频下载链接：', video_url)
    # 在这里对数据进行处理
    return  video_url

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
