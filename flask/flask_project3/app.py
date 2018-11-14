from flask import Flask
from flask import render_template,redirect,url_for,abort
import os
from json import loads


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

def get_articleList():
    article_list = []
    file_name = os.listdir('.')
    for i in file_name:
        if i.split(".")[-1] == 'json':
            with open(i, 'rb') as f:
                pdf_json = loads(f.read())
                article_list.append(pdf_json)
    return article_list

@app.route('/')
def index():
    # 显示文章名称的列表
    # 也就是 /home/shiyanlou/files/ 目录下所有 json 文件中的 `title` 信息列表
    article_list = get_articleList()
    # file_name = os.listdir('.')
    # for i in file_name:
    #     if i.split(".")[-1] == 'json':
    #         with open(i,'rb') as f:
    #             pdf_json = loads(f.read())
    #             article_list.append(pdf_json)
    return render_template('index.html', article_list=article_list)



# 读取并显示 filename.json 中的文章内容
# 例如 filename='helloshiyanlou' 的时候显示 helloshiyanlou.json 中的内容
# 如果 filename 不存在，则显示包含字符串 `shiyanlou 404` 404 错误页面

@app.route('/files/<filename>')
def file(filename):
    article_title = []
    article_list = get_articleList()
    for i in article_list:
        article_title.append(i['title'])
    if filename not in article_title :
        abort(404)
    else:
        for i in article_list:
            if filename == i["title"]:
                return render_template('file.html', article_list=i)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run(debug=True)
    # # #index()
    # print(get_articleList())