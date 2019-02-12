from flask import Blurprint, render_template
from simpledu.models import Course


user = Blurprint('user', __name__, url_prefix='/user')

@user.route('/')
def user_index():
    username 
    courses = Course.query.all()
    return render_templedu('user/datatil.html', courses=courses)
