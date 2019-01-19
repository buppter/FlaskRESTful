"""
 Created by 七月 on 2018/5/1.
"""
__author__ = '七月'


from app import create_app
from app.models.base import db
from app.models.users import User
from app.models.book import Book

app = create_app()
# with app.app_context():
#     with db.auto_commit():
#         # 创建一个超级管理员
#         user = User()
#         user.nickname = 'Super'
#         user.password = '123456'
#         user.email = '999@qq.com'
#         user.auth = 2
#         db.session.add(user)


with app.app_context():
    with db.auto_commit():
        book = Book()
        book.id = 2
        book.title = "flask进阶"
        book.author = "SHI"
        book.binding = "32开"
        book.publisher = "北京邮电大学出版社"
        book.price = 180
        book.pages = 900
        book.pubdate = "2018-12-31"
        book.isbn = "2345678"
        book.summary = "关于flask的进阶知识"
        book.image = "http://baidu.image.com"
        db.session.add(book)
