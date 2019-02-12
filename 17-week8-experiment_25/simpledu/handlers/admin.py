from flask import Blueprint

admin = Blueprint('admin', __name__, url_prefix='/admin')

#主义路由和函数名的变化
@admin.route('/')
def index():
    return 'admin'
