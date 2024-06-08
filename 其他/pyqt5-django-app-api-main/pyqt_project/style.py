def login_back_frame():
    return """
    QLabel{
    color: #E0E0E0;
    }

    QPushButton{
    border: none;
    margin-right: 7% auto;
    border-radius: 25%;
    width: 50%;
    height: 50%;
    }

    QPushButton::hover{
        background-color : #80CBC4;
        color: #212121;
    }

    QPushButton::pressed{
    background-color: #26A69A;
    }
    """


def main_frame():
    return """    
    QFrame {
    background-color: #263238;
    border-radius: 20%;
    padding: 6px;
    color: #E0E0E0;
    }
    """


def line_edit():
    return """
    QLineEdit {
    border: none;
    border-bottom: 1px solid #B0BEC5;
    }
    """


def log_button():
    return """
    QPushButton{
    background-color: #FF5252;
    border-radius: 5%;
    border:solid #B0BEC5;
    }
    QPushButton::hover{
    background-color : #FF1744;
    }
    QPushButton::pressed{
    background-color: #D50000;
    }
    """


def top_layout_home():
    return """
    QFrame{
    background-color: #37474F;
    border-radius: 8%;
    }

    QToolBar{
    spacing: 7px;
    }

    QPushButton{
    border: none;
    margin-right: 7% auto;
    border-radius: 20%;
    width: 40%;
    height: 40%;
    }

    QPushButton::hover{
        background-color : #80CBC4;
        color: #212121;
    }

    QPushButton::pressed{
    background-color: #26A69A;
    }
    """


def add_contact_layout():
    return """
    QGroupBox{
    border-radius: 7%;
    background-color: #37474F;
    }

    QLineEdit{
    border: none;
    border-bottom: 1px solid #B0BEC5;
    background-color: #37474F;
    }
    """


def left_layout_student():
    return """
    QFrame{
    background-color: #009688;
    color: #FFFFFF;
    }

    QLabel{
    color: #E0E0E0;
    }

    QPushButton{
    border: none;
    text-align: left;
    padding: 5%;
    color: #FFFFFF;
    border-radius: 7%;
    }

    QPushButton::hover{
        background-color : #80CBC4;
        color: #212121;
    }

    QPushButton::focus{
    background-color: #26A69A;
    }
    """


def right_layout_student():
    return """
    QFrame{
    background-color: #00796B;
    border-radius: 20%;
    }

    QPushButton{
    border: none;
    margin-right: 7% auto;
    border-radius: 15%;
    width: 30%;
    height: 30%;
    }

    QPushButton::hover{
        background-color : #80CBC4;
        color: #212121;
    }

    QPushButton::pressed{
    background-color: #26A69A;
    }

    QLineEdit{
    border: none;
    background-color: #00796B;
    border-bottom: 1px solid #E0E0E0;
    color: #E0E0E0;
    }
    """


def item_bottom_layout():
    return """
    QFrame{
    border-radius: 7%;
    background-color: #37474F;
    }
    """


def group_box_student():
    return """
    QGroupBox{
    background-color: #455A64;
    border-radius: 7%;
    color: #E0E0E0;
    }

    QLineEdit{
    border: none;
    border-bottom: 1px solid #B0BEC5;
    background-color: #455A64;
    }

    QComboBox{
    background-color: #546E7A;
    color: #E0E0E0;
    }

    QLabel{
    color: #E0E0E0;
    }
    """


def group_box_teacher():
    return """
    QGroupBox{
    background-color: #37474F;
    border-radius: 7%;
    color: #E0E0E0;
    }

    QLineEdit{
    border: none;
    border-bottom: 1px solid #B0BEC5;
    background-color: #37474F;
    }

    QComboBox{
    background-color: #455A64;
    color: #E0E0E0;
    }

    QLabel{
    color: #E0E0E0;
    }
    """


def dashboard_frame():
    return """
    QFrame{
    background-color: #37474F;
    border-bottom: 3px solid #FF5252;
    }
    QLabel{
    color: #E0E0E0;
    }
    """
