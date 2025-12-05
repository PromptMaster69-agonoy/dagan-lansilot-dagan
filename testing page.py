from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivymd.theming import ThemeManager
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.list import OneLineListItem
from kivymd.uix.pickers import MDDatePicker, MDTimePicker
from kivy_garden.mapview import MapView, MapMarker, MapLayer
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
from kivy.metrics import dp
import datetime

Window.size = (375, 750)

LabelBase.register(
    name="OpenSans-VariableFont_wdth,wght",
    fn_regular="OpenSans-VariableFont_wdth,wght.ttf",
    fn_bold="OpenSans-Bold.ttf",
)

KV = """
MainWindow:
    LoginScreen:
    SignupScreen:
    HomeScreen:
    ProfileScreen:
    ScheduleScreen:
    MapScreen:
    InboxScreen:
    PersonalInfoScreen:

<LoginScreen>
    name: "login"
    mobile_num: m_number
    password: password

    FloatLayout:
        FitImage:
            source: "login_bg.jpg"
        Image:
            source: "logo.png"
            size_hint: None, None
            size: "180dp", "180dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.86}

        MDLabel:
            text: "Log in"
            bold: True
            font_name: "OpenSans-VariableFont_wdth,wght"
            halign: "left"
            font_size: "22sp"
            valign: "center"
            size_hint: None, None
            pos_hint: {"x": 0.1, "top": 0.73}

        BoxLayout:
            orientation: "vertical"
            size_hint: 0.9, None
            height: self.minimum_height
            pos_hint: {"center_x": 0.5, "center_y": 0.43}
            padding: "20dp"
            spacing: "15dp"

            MDTextField:
                id: m_number
                hint_text: "Enter mobile number"
                font_name: "OpenSans-VariableFont_wdth,wght"
                font_size: "12sp"
                height: "50dp"
                mode: "rectangle"
                multiline: False
                pos_hint: {"center_x": 0.5}
                text_color_focus: 0, 0, 0, 1
                line_color_focus: 0, 0, 0, 1

            MDTextField:
                id: password
                hint_text: "Enter password"
                password: True
                font_name: "OpenSans-VariableFont_wdth,wght"
                font_size: "12sp"
                mode: "rectangle"
                pos_hint: {"center_x": 0.5}
                text_color_focus: 0, 0, 0, 1
                line_color_focus: 0, 0, 0, 1

            MDRectangleFlatButton:
                text: "Login"
                size_hint_x: 1
                height: "55dp"
                text_color: "black"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                on_release: root.login_inter()

            MDRectangleFlatButton:
                text: "Signup"
                size_hint_x: 1
                height: "55dp"
                text_color: "black"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = "signup"

<SignupScreen>
    name: "signup"
    create_num: c_number
    c_pass: c_pass
    v_pass: v_pass

    FloatLayout:
        FitImage:
            source: "signup_bg.jpg"
        MDLabel:
            text: "Sign in"
            bold: True
            font_name: "OpenSans-VariableFont_wdth,wght"
            halign: "left"
            font_size: "22sp"
            valign: "center"
            size_hint: None, None
            pos_hint: {"x": 0.1, "top": 0.73}
        Image:
            source: "logo.png"
            size_hint: None, None
            size: "180dp", "180dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.86}
        BoxLayout:
            orientation: "vertical"
            size_hint: 0.9, None
            height: self.minimum_height
            pos_hint: {"center_x": 0.5, "center_y": 0.38}
            padding: "20dp"
            spacing: "15dp"
            MDTextField:
                id: c_number
                hint_text: "Create mobile number"
                size_hint_x: None
                mode: "rectangle"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                width: "280dp"
                font_size: "12sp"
                text_color_focus: 0, 0, 0, 1
                line_color_focus: 0, 0, 0, 1
            MDTextField:
                id: c_pass
                hint_text: "Create password"
                password: True
                mode: "rectangle"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                size_hint_x: None
                width: "280dp"
                font_size: "12sp"
                text_color_focus: 0, 0, 0, 1
                line_color_focus: 0, 0, 0, 1
            MDTextField:
                id: v_pass
                hint_text: "Verify your password"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                password: True
                mode: "rectangle"
                size_hint_x: None
                width: "280dp"
                font_size: "12sp"
                text_color_focus: 0, 0, 0, 1
                line_color_focus: 0, 0, 0, 1
            MDRectangleFlatButton:
                text: "Signup"
                size_hint_x: 1
                height: "55dp"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                text_color: "black"
                on_release: root.signup_inter()
            MDRectangleFlatButton:
                text: "Back"
                size_hint_x: 1
                height: "55dp"
                text_color: "black"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                on_release: root.go_back()

<HomeScreen>:
    name: "homepage"

    canvas.before:
        Color:
            rgba: 0.05, 0.06, 0.1, 1  # Dark background
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Agonoy Intelligence"
            pos_hint: {"top": 1}
            md_bg_color: get_color_from_hex("#0A0D14")
            specific_text_color: 1, 1, 1, 1
            elevation: 6

        ScrollView:
            do_scroll_x: False

            BoxLayout:
                orientation: "vertical"
                padding: "20dp"
                spacing: "20dp"
                size_hint_y: None
                height: self.minimum_height
                width: root.width

                MDCard:
                    size_hint: None, None
                    size: root.width - dp(40), dp(220)
                    elevation: 6
                    padding: "20dp"
                    radius: [15,]
                    md_bg_color: get_color_from_hex("#1F2937")

                    BoxLayout:
                        orientation: "vertical"
                        spacing: "2dp"

                        MDLabel:
                            text: "Welcome to ISU Pathfinding System!"
                            halign: "center"
                            font_style: "H6"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            bold: True

                        Widget:
                            size_hint_y: None
                            height: dp(2) 

                        MDLabel:
                            text: "Helping students, teachers, and visitors navigate the campus with ease."
                            halign: "center"
                            font_style: "Subtitle1"
                            theme_text_color: "Custom"
                            text_color: 0.7, 0.7, 0.7, 1
                            size_hint_y: None
                            height: self.texture_size[1]

                        Widget:
                            size_hint_y: None
                            height: dp(10)

                        FitImage:
                            source: "your_icon_or_welcome_image.png"
                            size_hint: None, None
                            size: dp(60), dp(60)
                            pos_hint: {"center_x": 0.5}

                # Objectives Card
                MDCard:
                    size_hint: None, None
                    size: root.width - dp(40), dp(240)
                    elevation: 6
                    padding: "20dp"
                    radius: [15,]
                    md_bg_color: get_color_from_hex("#1F2937")

                    BoxLayout:
                        orientation: "vertical"
                        spacing: "15dp"

                        MDLabel:
                            text: "Objectives"
                            halign: "center"
                            font_style: "H5"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            bold: True

                        Widget:
                            size_hint_y: None
                            height: dp(10)  # Spacer to push text lower

                        MDLabel:
                            text: "Reduce the time spent searching for locations and minimize delays or confusion, especially for new students and visitors."
                            halign: "center"
                            font_style: "Body1"
                            theme_text_color: "Custom"
                            text_color: 0.8, 0.8, 0.8, 1
                            size_hint_y: None
                            text_size: self.width, None
                            height: self.texture_size[1]

                        MDLabel:
                            text: "Provide reliable, step-by-step directions using efficient pathfinding algorithms, enhancing the overall user experience."
                            halign: "center"
                            font_style: "Body1"
                            theme_text_color: "Custom"
                            text_color: 0.8, 0.8, 0.8, 1
                            size_hint_y: None
                            text_size: self.width, None
                            height: self.texture_size[1]

        # Bottom Navigation Bar
        BoxLayout:
            size_hint_y: None
            height: "56dp"
            pos_hint: {"y": 0}
            md_bg_color: get_color_from_hex("#0A0D14")

            MDIconButton:
                icon: "home"
                on_release: app.on_home()
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                size_hint_x: 1

            MDIconButton:
                icon: "account"
                on_release: app.on_profile()
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                size_hint_x: 1

            MDIconButton:
                icon: "calendar"
                on_release: app.on_schedule()
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                size_hint_x: 1

            MDIconButton:
                icon: "map"
                on_release: app.on_map()
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                size_hint_x: 1

            MDIconButton:
                icon: "email"
                on_release: app.on_inbox()
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                size_hint_x: 1




<ProfileScreen>:
    name: "profile"

    canvas.before:
        Color: 
            rgba: 10/255, 13/255, 20/255, 1
        Rectangle:
            pos: self.pos
            size: self.size    

    BoxLayout:
        orientation: "vertical"
        size_hint_y: None
        height: self.minimum_height        
        padding: "10dp"
        spacing: "10dp"
        pos_hint: {"top": 0.88}
        width: self.parent.width
        size_hint_x: 1

        OneLineListItem:
            text: "Personal Info"
            on_release: app.root.current = "information"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1

        OneLineListItem:
            text: "Logout"
            on_release: app.root.current = "login"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1


    MDTopAppBar:
        title: "Profile"
        pos_hint: {"top": 1}
        md_bg_color: get_color_from_hex("#0A0D14")
        specific_text_color: 1, 1, 1, 1
        elevation: 0

    BoxLayout:
        size_hint_y: None
        height: "56dp"
        pos_hint: {"y": 0}
        md_bg_color: 0.10, 0.13, 0.20, 1
        padding: "10dp"
        MDIconButton:
            icon: "home"
            on_release: app.on_home()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "account"
            on_release: app.on_profile()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "calendar"
            on_release: app.on_schedule()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "map"
            on_release: app.on_map()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "email"
            on_release: app.on_inbox()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1

<PersonalInfoScreen>
    name: "information"

    canvas.before:
        Color: 
            rgba: 10/255, 13/255, 20/255, 1
        Rectangle:
            pos: self.pos
            size: self.size       

    MDTopAppBar:
        title: "Personal Information"
        pos_hint: {"top": 1}
        md_bg_color: get_color_from_hex("#0A0D14")
        specific_text_color: 1, 1, 1, 1
        elevation: 0

    BoxLayout:
        orientation: "vertical"
        size_hint_y: None
        height: self.minimum_height        
        padding: "10dp"
        spacing: "10dp"
        pos_hint: {"top": 0.88}
        width: self.parent.width
        size_hint_x: 1

        MDLabel:
            text: "Name"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            halign: "left"
            font_style: "H6"
            size_hint_y: None
            height: dp(20)   
            size_hint_x: 1   

        MDTextField:
            hint_text: "Full Name"
            text_color_normal: 1, 1, 1, 1
            text_color_focus: 1, 1, 1, 1
            line_color_normal: 1, 1, 1, 1
            line_color_focus: 1, 1, 1, 1
            hint_text_color_normal: 0.7, 0.7, 0.7, 1
            hint_text_color_focus: 1, 1, 1, 1


        MDLabel:
            text: "Address"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            halign: "left"
            font_style: "H6"
            size_hint_y: None
            height: dp(24)   
            size_hint_x: 1  

        MDTextField:
            hint_text: "Address"
            text_color_normal: 1, 1, 1, 1
            text_color_focus: 1, 1, 1, 1
            line_color_normal: 1, 1, 1, 1
            line_color_focus: 1, 1, 1, 1
            hint_text_color_normal: 0.7, 0.7, 0.7, 1
            hint_text_color_focus: 1, 1, 1, 1


    BoxLayout:
        size_hint_y: None
        height: "56dp"
        pos_hint: {"y": 0}
        md_bg_color: 0.10, 0.13, 0.20, 1
        padding: "10dp"
        MDIconButton:
            icon: "home"
            on_release: app.on_home()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "account"
            on_release: app.on_profile()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "calendar"
            on_release: app.on_schedule()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "map"
            on_release: app.on_map()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "email"
            on_release: app.on_inbox()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1                

<ScheduleScreen>:
    name: "schedule"
    subject: subject
    room: room
    day: day
    time_start: time_s
    time_end: time_e
    table_box: table_box

    canvas.before:
        Color: 
            rgba: 10/255, 13/255, 20/255, 1
        Rectangle:
            pos: self.pos
            size: self.size

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Class Schedule"
            md_bg_color: get_color_from_hex("#0A0D14")
            specific_text_color: 1, 1, 1, 1
            elevation: 0

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: "20dp"
                spacing: "15dp"
                size_hint_y: None
                height: self.minimum_height

                MDLabel:
                    text: "Schedule Details"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "H6"
                    halign: "center"
                    size_hint_y: None
                    height: dp(30)

                MDLabel:
                    text: "Subject"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "Body1"
                    halign: "left"
                    size_hint_y: None
                    height: dp(20)

                MDTextField:
                    id: subject
                    hint_text: "Enter Subject"
                    mode: "rectangle"
                    text_color_normal: 1, 1, 1, 1
                    text_color_focus: 1, 1, 1, 1
                    line_color_normal: 1, 1, 1, 1
                    line_color_focus: 1, 1, 1, 1
                    hint_text_color_normal: 0.7, 0.7, 0.7, 1
                    hint_text_color_focus: 1, 1, 1, 1

                MDLabel:
                    text: "Room"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "Body1"
                    halign: "left"
                    size_hint_y: None
                    height: dp(20)

                MDTextField:
                    id: room
                    hint_text: "Enter Room"
                    mode: "rectangle"
                    text_color_normal: 1, 1, 1, 1
                    text_color_focus: 1, 1, 1, 1
                    line_color_normal: 1, 1, 1, 1
                    line_color_focus: 1, 1, 1, 1
                    hint_text_color_normal: 0.7, 0.7, 0.7, 1
                    hint_text_color_focus: 1, 1, 1, 1

                MDLabel:
                    text: "Day"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "Body1"
                    halign: "left"
                    size_hint_y: None
                    height: dp(20)

                MDTextField:
                    id: day
                    hint_text: "Select Day"
                    readonly: True
                    mode: "rectangle"
                    on_focus: if self.focus: root.day_picker()
                    text_color_normal: 1, 1, 1, 1
                    text_color_focus: 1, 1, 1, 1
                    line_color_normal: 1, 1, 1, 1
                    line_color_focus: 1, 1, 1, 1
                    hint_text_color_normal: 0.7, 0.7, 0.7, 1
                    hint_text_color_focus: 1, 1, 1, 1

                MDBoxLayout:
                    spacing: "10dp"
                    size_hint_y: None
                    height: dp(60)

                    MDTextField:
                        id: time_s
                        hint_text: "Start Time"
                        readonly: True
                        mode: "rectangle"
                        on_focus: if self.focus: root.show_start_time()
                        text_color_normal: 1, 1, 1, 1
                        text_color_focus: 1, 1, 1, 1
                        line_color_normal: 1, 1, 1, 1
                        line_color_focus: 1, 1, 1, 1
                        hint_text_color_normal: 0.7, 0.7, 0.7, 1
                        hint_text_color_focus: 1, 1, 1, 1

                    MDTextField:
                        id: time_e
                        hint_text: "End Time"
                        readonly: True
                        mode: "rectangle"
                        on_focus: if self.focus: root.show_end_time()
                        text_color_normal: 1, 1, 1, 1
                        text_color_focus: 1, 1, 1, 1
                        line_color_normal: 1, 1, 1, 1
                        line_color_focus: 1, 1, 1, 1
                        hint_text_color_normal: 0.7, 0.7, 0.7, 1
                        hint_text_color_focus: 1, 1, 1, 1

                MDRaisedButton:
                    text: "Add Schedule"
                    md_bg_color: get_color_from_hex("#81C784")
                    pos_hint: {"center_x": 0.5}
                    on_release: root.add_schedule()

                MDLabel:
                    text: "Your Schedule"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    halign: "center"
                    font_style: "Subtitle1"
                    padding_y: "10dp"

                MDBoxLayout:
                    id: table_box
                    orientation: "vertical"
                    size_hint_y: None
                    height: dp(300)

    MDBoxLayout:
        size_hint_y: None
        height: "56dp"
        pos_hint: {"y": 0}
        md_bg_color: get_color_from_hex("#0A0D14")
        padding: "10dp"
        MDIconButton:
            icon: "home"
            on_release: app.on_home()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "account"
            on_release: app.on_profile()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "calendar"
            on_release: app.on_schedule()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "map"
            on_release: app.on_map()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "email"
            on_release: app.on_inbox()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1     


<MapScreen>:
    name: "map"

    canvas.before:
        Color: 
            rgba: 10/255, 13/255, 20/255, 1
        Rectangle:
            pos: self.pos
            size: self.size     

    MapView:
        id: mapview
        lat: 16.93804
        lon: 121.76454
        zoom: 18
        on_zoom: 
            if self.zoom > 18: self.zoom = 18
            if self.zoom < 18: self.zoom = 18

    MDTopAppBar:
        id: toolbar  # <-- add this
        title: "Map"
        pos_hint: {"top": 1}
        md_bg_color: get_color_from_hex("#0A0D14")
        specific_text_color: 1, 1, 1, 1
        elevation: 0
        left_action_items: [["menu", lambda x: root.open_menu()]]

    MDBoxLayout:
        size_hint_y: None
        height: "56dp"
        pos_hint: {"y": 0}
        md_bg_color: get_color_from_hex("#0A0D14")
        padding: "10dp"
        MDIconButton:
            icon: "home"
            on_release: app.on_home()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "account"
            on_release: app.on_profile()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "calendar"
            on_release: app.on_schedule()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "map"
            on_release: app.on_map()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "email"
            on_release: app.on_inbox()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1 


<InboxScreen>:
    name: "inbox"

    canvas.before:
        Color: 
            rgba: 10/255, 13/255, 20/255, 1
        Rectangle:
            pos: self.pos
            size: self.size    

    MDTopAppBar:
        title: "Inbox"
        pos_hint: {"top": 1}
        md_bg_color: get_color_from_hex("#0A0D14")
        specific_text_color: 1, 1, 1, 1
        elevation: 0


    BoxLayout:
        size_hint_y: None
        height: "56dp"
        pos_hint: {"y": 0}
        md_bg_color: 0.10, 0.13, 0.20, 1
        padding: "10dp"
        MDIconButton:
            icon: "home"
            on_release: app.on_home()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "account"
            on_release: app.on_profile()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "calendar"
            on_release: app.on_schedule()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "map"
            on_release: app.on_map()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "email"
            on_release: app.on_inbox()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
"""

VALID_ROOMS = {
    "Ramon Magsaysay Building": {

        "rooms": { "1st Floor": ["RM101", "RM102", "RM103"],
                   "2nd Floor": ["Abbreviation Room"]
            },
        "coords": (16.937715315657673, 121.76392437370077)
    },
    "CCSICT Building": {
        "rooms": { "1st Floor" : ["IT101", "IT102", "IT103","IT104"],
                   "2nd Floor": ["IT201", "IT202", "IT203", "IT204"],
                   "3rd Floor": ["IT301", "IT302", "IT303", "IT304"]
            },
        "coords": (16.938197528772875, 121.764063538908)
    },
    "CBM Building": {
        "rooms": {"2nd Floor":["NB101"],
                  "3rd Floor": ["NB201"],
                  "4th Floor": ["NB301"]
            },
        "coords": (16.936043364524572, 121.76446658242533)
    },
    "CED Building": {
        "rooms": { "1st Floor":["UBA","UBB","OB101","OB201"]
                  },
        "coords": (16.937139129220466, 121.76490974482596)
    },
    "SAS Building": {
        "rooms": { "1st Floor":["SAS101","SAS201"]
                  },
        "coords": (16.93736905890547, 121.76374652183607)
    },
}

Building_Paths = {
    "College of Law": {"Ramon Magsaysay": 49, "CCSICT Building": 110},
    "Ramon Magsaysay": {"College of Law": 49, "CCSICT Building": 59},
    "CCSICT Building": {"Ramon Magsaysay": 59, "College of Law": 110}
}


class LoginScreen(Screen):
    mobile_num = ObjectProperty(None)
    password = ObjectProperty(None)

    def login_inter(self):
        mobile_n = self.mobile_num.text
        passw = self.password.text
        if not mobile_n or not passw:
            self.manager.show_message("Please enter both fields.")
        else:
            mobile_n = int(mobile_n)
            if mobile_n in self.manager.students:
                if passw == self.manager.students[mobile_n]:
                    self.manager.show_message("Welcome to Homepage!")
                    self.manager.current = "homepage"
                    self.mobile_num.text = ""
                    self.password.text = ""
                else:
                    self.manager.show_message("Invalid password, please try again.")
                    self.password.text = ""
            else:
                self.manager.show_message("Student not found, please sign up.")
                self.mobile_num.text = ""
                self.password.text = ""


class SignupScreen(Screen):
    create_num = ObjectProperty(None)
    c_pass = ObjectProperty(None)
    v_pass = ObjectProperty(None)

    def signup_inter(self):
        if not self.create_num.text or not self.c_pass.text:
            self.manager.show_message("Please enter given fields.")
            return
        if self.create_num.text.isdigit():
            if int(self.create_num.text) in self.manager.students:
                self.manager.show_message("Account already exists with this number.")
                self.create_num.text = ""
                self.c_pass.text = ""
                self.v_pass.text = ""
                return
            if self.c_pass.text == self.v_pass.text:
                self.manager.students[int(self.create_num.text)] = self.c_pass.text
                self.manager.show_message("Successfully created an account")
                self.c_pass.text = ""
                self.v_pass.text = ""
                self.create_num.text = ""
            else:
                self.manager.show_message("verify password not similar to new password")
                self.v_pass.text = ""
        else:
            self.manager.show_message("Mobile number must be digits only.")
            return

    def go_back(self):
        self.manager.current = "login"


class HomeScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class PersonalInfoScreen(Screen):
    pass


class ScheduleScreen(Screen):
    subject = ObjectProperty(None)
    room = ObjectProperty(None)
    day = ObjectProperty(None)
    time_start = ObjectProperty(None)
    time_end = ObjectProperty(None)
    table_box = ObjectProperty(None)

    def on_pre_enter(self):

        if not hasattr(self, "table_created"):
            self.table_created = True
            self.create_table()

    def create_table(self):
        self.table = MDDataTable(
            use_pagination=True,
            column_data=[
                ("Subject", dp(18)),
                ("Room", dp(18)),
                ("Date", dp(18)),
                ("Time start", dp(18)),
                ("Time end", dp(18)),
            ],
            row_data=[],
            size_hint=(0.95, 0.35),
            pos_hint={"center_x": 0.5},
        )
        self.table_box.add_widget(self.table)

    def day_picker(self):
        menu_items = [
            {
                "text": day,
                "viewclass": "OneLineListItem",
                "height": dp(48),
                "on_release": lambda x=day: self.set_day_value(x)
            }
            for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        ]
        self.day_menu = MDDropdownMenu(
            caller=self.ids.day,
            items=menu_items,
            width_mult=4
        )
        self.day_menu.open()

    def set_day_value(self, value):
        self.ids.day.text = value
        if self.day_menu:
            self.day_menu.dismiss()

    def show_date(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.set_day)
        date_dialog.open()

    def set_day(self, instance, value, date_range):
        if isinstance(value, datetime.date):
            self.day.text = value.strftime("%A")

    def show_start_time(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.set_time)
        time_dialog.open()

    def set_time(self, instance, time_obj):
        self.time_start.text = time_obj.strftime("%I:%M %p")

    def show_end_time(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.end_set_time)
        time_dialog.open()

    def end_set_time(self, instance, time_obj):
        self.time_end.text = time_obj.strftime("%I:%M %p")

    def add_schedule(self):
        subject = self.subject.text.strip()
        room = self.room.text.strip().upper()
        day = self.day.text.strip()
        time_start = self.time_start.text.strip()
        time_end = self.time_end.text.strip()

        if all([subject, room, day, time_start, time_end]):
            self.table.row_data.append((subject, room, day, time_start, time_end))
            self.table.row_data = self.table.row_data.copy()

            self.subject.text = ""
            self.room.text = ""
            self.day.text = ""
            self.time_start.text = ""
            self.time_end.text = ""


class BuildingMarker(MapMarker):
    building_name = ""

class MapScreen(Screen):
    mapview = ObjectProperty(None)
    menu = ObjectProperty(None)
    markers = []

    def dijkstra(self):
        pass

    def on_pre_enter(self):
        if not hasattr(self, "menu_created"):
            self.menu_created = True
            self.create_menu()
        self.mapview = self.ids.mapview
        self.markers = []

    def create_menu(self):
        menu_items = [
            {
                "text": day,
                "viewclass": "OneLineListItem",
                "height": dp(40),
                "on_release": lambda x=day: self.menu_callback(x),
            }
            for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        ]

        # Use a toolbar button as the menu caller
        self.menu = MDDropdownMenu(
            caller=self.ids.toolbar,  # safer than left_actions.children[0]
            items=menu_items,
            width_mult=4,
        )

    def open_menu(self):
        if self.menu:
            self.menu.open()


    def menu_callback(self, day):
        self.menu.dismiss()
        self.show_markers_for_day(day)
        Snackbar(text=f"Showing schedule for {day}", duration=1.5).open()

    def show_building_dialog(self, building_name):
        building = VALID_ROOMS[building_name]

        room_text = "[b]Available Rooms[/b]\n\n"
        for floor, rooms in building["rooms"].items():
            room_text += f"[b]{floor}[/b]\n"
            for r in rooms:
                room_text += f" • {r}\n"
            room_text += "\n"

        schedule_screen = self.manager.get_screen("schedule")

        user_schedule = "[b]Your Schedule Here[/b]\n\n"
        has_schedule = False

        for entry in schedule_screen.table.row_data:
            subject, room, day, start, end = entry

            for _, rooms in building["rooms"].items():
                if room in rooms:
                    user_schedule += f"[b]{subject}[/b]\n"
                    user_schedule += f"Room: {room}\n"
                    user_schedule += f"Day: {day}\n"
                    user_schedule += f"Time: {start} - {end}\n\n"
                    has_schedule = True

        if not has_schedule:
            user_schedule += "No schedule found in this building.\n"

        dialog = MDDialog(
            title=building_name,
            text=room_text + "\n" + user_schedule,
            radius=[18, 18, 18, 18]
        )
        dialog.open()


    def show_markers_for_day(self, day):

        for marker in self.markers[:]:
            if marker.parent:
                self.mapview.remove_widget(marker)
        self.markers.clear()

        schedule_screen = self.manager.get_screen("schedule")

        if not hasattr(schedule_screen, "table") or schedule_screen.table is None:
            self.manager.show_message("No schedule table found — skipping marker creation.")
            return

        for entry in schedule_screen.table.row_data:
            subject, room, sched_day, time_start, time_end = entry

            if sched_day != day:
                self.manager.show_message(f"No available Subject in {day}")
                continue

            building_coords = None
            for building, data in VALID_ROOMS.items():
                for floor, rooms in data["rooms"].items():
                    if room in rooms:
                        building_coords = data["coords"]
                        break
                if building_coords:
                    break

            if not building_coords:
                self.manager.show_toast(f"Room {room} not in VALID_ROOMS")
                continue

            lat, lon = building_coords
            marker = BuildingMarker(lat=lat, lon=lon)
            marker.building_name = building
            marker.on_release = lambda m=marker: self.show_building_dialog(m.building_name)

            # marker = MapMarker(lat=lat, lon=lon)
            self.mapview.add_widget(marker)
            self.markers.append(marker)


class InboxScreen(Screen):
    pass


class MainWindow(ScreenManager):
    students = {}
    schedule = []

    def show_message(self, ms):
        Snackbar(text=ms, duration=1.5).open()

    def show_toast(self,ms):
        toast(text=ms, duration=1.5)


class TestingApp(MDApp):
    def build(self):
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "Gray"
        return Builder.load_string(KV)

    def on_home(self):
        self.root.current = "homepage"

    def on_profile(self):
        self.root.current = "profile"

    def on_information(self):
        self.root.current = "information"

    def on_schedule(self):
        self.root.current = "schedule"

    def on_map(self):
        self.root.current = "map"

    def on_inbox(self):
        self.root.current = "inbox"


if __name__ == "__main__":
    TestingApp().run()
