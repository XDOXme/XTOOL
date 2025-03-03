import flet as ft
global jobs_failed
import requests
import time
import random
from fake_useragent import UserAgent
import platform
from credit_card_info_generator import generate_credit_card

jobs_successful = 0
jobs_skipped = 0
jobs_failed = 0
color_S = "#9FEF00"
color_Shadow = "#456602"

Theme_block = "#1A2332"
Theme_bg = "#141D2B"
Theme_Shadow = "#0F1620"
Theme_Text_color = "BLACK"
Theme_Xtool_Text = "WHITE"

text_attacked = ft.Text("XTOOL ", font_family="PT Mono", size=40, color = Theme_Xtool_Text)
text_Xtool = ft.Text(" XTOOL", font_family="PT Mono", size=40, color = color_S)
# Контейнер с название софта логотипом и текущей жертвой
Title_container = ft.Container(
    bgcolor = Theme_block,
    shadow=ft.BoxShadow(
        spread_radius=2,
        blur_radius=0,
        color=Theme_Shadow,
        offset=ft.Offset(2.2, 2.2),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
    content= ft.Row([text_Xtool, text_attacked],ft.MainAxisAlignment.SPACE_BETWEEN),
    border_radius = 5,
    height = 80,
    width = 1400
    )
# Контейнер с прогресс баром
Progress = ft.ProgressBar(color=color_S, border_radius=90,value=0,bar_height=10,width=1340)
jobs_successful_txt = ft.Text(f"{jobs_successful} jobs successful", font_family="PT Mono", size=16, color = "#9FEF00")
jobs_skipped_txt = ft.Text(f" {jobs_skipped} jobs skipped", font_family="PT Mono", size=16, color = "#E9F000")
jobs_failed_txt = ft.Text(f" {jobs_failed} jobs failed", font_family="PT Mono", size=16, color = "#F80363")
Progress_container = ft.Container(
    bgcolor = Theme_block,
    content= ft.Column([ft.Divider(height=10, color=ft.colors.TRANSPARENT),ft.Row([ft.VerticalDivider(width=1, color=ft.colors.TRANSPARENT),Progress,ft.VerticalDivider(width=1, color=ft.colors.TRANSPARENT)]),ft.Row([ft.VerticalDivider(width=10, color=ft.colors.TRANSPARENT),jobs_successful_txt,jobs_skipped_txt,jobs_failed_txt])]),
    border_radius = 5,
    height = 90,
    width = 1400,
    shadow=ft.BoxShadow(
        spread_radius=2,
        blur_radius=0,
        color=Theme_Shadow,
        offset=ft.Offset(2.2, 2.2),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ))
# Текст кнопки Export Data
Text_ExportData = ft.Text(f" Export data ", font_family="PT Mono", size=16, color = Theme_Xtool_Text)

def on_hover(e):
    Text_ExportData.color = color_S if e.data == "true" else Theme_Xtool_Text
    e.control.update()

def on_hover_But(e):
    e.control.shadow.offset = ft.Offset(3, 3) if e.data == "true" else ft.Offset(2.2, 2.2)
    e.control.update()

# Кнопки
Button_Export_container = ft.Container(
    bgcolor = Theme_block,
    border_radius = 5,
    height = 20,
    margin=5,
    content= Text_ExportData,
    ink = True,
    on_hover = on_hover,
    on_click=lambda e: print(1),
    shadow=ft.BoxShadow(
        spread_radius=2,
        blur_radius=0,
        color=Theme_Shadow,
        offset=ft.Offset(2.2, 2.2),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ))

# Список кнопок
Button_List = ft.Row([Button_Export_container])

# Модули
# Поиск по базам
SearchDatabase = ft.Text("Поиск по базам", font_family="PT Mono", size=26, color = color_S)

Module_DataBase_container = ft.Container(
    bgcolor = Theme_block,
    padding=10,
    shadow=ft.BoxShadow(
        spread_radius=2,
        blur_radius=0,
        color=Theme_Shadow,
        offset=ft.Offset(2.2, 2.2),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
    content= ft.Column([SearchDatabase]),
    border_radius = 5,
    width = 333
    )
Generator_Mode_label = ft.TextStyle(color = color_S)
Generator_Mode = ft.Dropdown(
        border_color = Theme_Xtool_Text,
        label = "Что генерировать?",
        label_style=Generator_Mode_label,
        bgcolor = "#1a1c1e",
        filled = False,
        text_style = ft.TextStyle(color = Theme_Xtool_Text),
        focused_border_color = color_S,
        options=[
            ft.dropdown.Option("Ключи MullVad"),
            ft.dropdown.Option("Ключи Warp+"),
            ft.dropdown.Option("Личность"),
            ft.dropdown.Option("Дискорд токен"),
            ft.dropdown.Option("User-Agent"),
            ft.dropdown.Option("Прокси"),
            ft.dropdown.Option("Банковские карты"),
            ft.dropdown.Option("Почты"),
        ],
    )

Gen_value = ft.Slider(value = 1,min=1, max=100, active_color = color_S, divisions=99, label="Количество: {value}")

def Gen(Gen_Mode, Gen_value):
    if Gen_Mode == "Личность":
        response = requests.get('https://api.randomdatatools.ru', params={'count': int(Gen_value)})
        data = response.json()
        if Gen_value != 1:
            for i in range(int(Gen_value)):
                print(f"""Фио: {data[i]['LastName']} {data[i]['FirstName']} {data[i]['FatherName']}
Дата рождения: {data[i]['DateOfBirth']}
Полных лет: {data[i]['YearsOld']}
Номер телефона: {data[i]['Phone']}
Логин: {data[i]['Login']}
Пароль: {data[i]['Password']}
Почта: {data[i]['Email']}
Гендер: {data[i]['Gender']}
Серия и номер паспорта: {data[i]['PasportNum']}
Код подразделения: {data[i]['PasportCode']}
Кем выдан паспорт: {data[i]['PasportOtd']}
Дата выдача паспорта: {data[i]['PasportDate']}
Идентификационный номер налогоплательщика (ИНН) для физ. лиц и ИП: {data[i]['inn_fiz']}
Идентификационный номер налогоплательщика (ИНН) для юр. лиц: {data[i]['inn_ur']}
Страховой номер индивидуального лицевого счёта (СНИЛС): {data[i]['snils']}
Номер полиса обязательного медицинского страхования (ОМС): {data[i]['oms']}
Основной государственный регистрационный номер(ОГРН): {data[i]['ogrn']}
Код причины постановки на учет (КПП): {data[i]['kpp']}
Адрес: {data[i]['Address']}
БИК банка: {data[i]['bankBIK']}
Корреспондентский счет: {data[i]['bankCorr']}
ИНН банка: {data[i]['bankINN']}
КПП банка: {data[i]['bankKPP']}
Номер счета: {data[i]['bankNum']}
Имя владельца карты: {data[i]['bankClient']}
Номер кредитной карты: {data[i]['bankCard']}
Срок действия карты: {data[i]['bankDate']}
CVC/CVV код: {data[i]['bankCVC']}
Специальность: {data[i]['EduSpecialty']}
Направление: {data[i]['EduProgram']}
Учебное заведение: {data[i]['EduName']}
Серия/Номер диплома: {data[i]['EduDocNum']}
Регистрационный номер: {data[i]['EduRegNumber']}
Дата окончания обучения: {data[i]['EduYear']}
Марка и модель автомобиля: {data[i]['CarBrand']} {data[i]['CarModel']}
Год выпуска: {data[i]['CarYear']}
Цвет автомобиля: {data[i]['CarColor']}
Номерной знак: {data[i]['CarNumber']}
VIN Код: {data[i]['CarVIN']}
Серия/номер СТС: {data[i]['CarSTS']}
Дата выдачи СТС: {data[i]['CarSTSDate']}
Серия/номер ПТС: {data[i]['CarPTS']}
Дата выдачи ПТС: {data[i]['CarPTSDate']}

""")
        else:
            print(f"""Фио: {data['LastName']} {data['FirstName']} {data['FatherName']}
Дата рождения: {data['DateOfBirth']}
Полных лет: {data['YearsOld']}
Номер телефона: {data['Phone']}
Логин: {data['Login']}
Пароль: {data['Password']}
Почта: {data['Email']}
Гендер: {data['Gender']}
Серия и номер паспорта: {data['PasportNum']}
Код подразделения: {data['PasportCode']}
Кем выдан паспорт: {data['PasportOtd']}
Дата выдача паспорта: {data['PasportDate']}
Идентификационный номер налогоплательщика (ИНН) для физ. лиц и ИП: {data['inn_fiz']}
Идентификационный номер налогоплательщика (ИНН) для юр. лиц: {data['inn_ur']}
Страховой номер индивидуального лицевого счёта (СНИЛС): {data['snils']}
Номер полиса обязательного медицинского страхования (ОМС): {data['oms']}
Основной государственный регистрационный номер(ОГРН): {data['ogrn']}
Код причины постановки на учет (КПП): {data['kpp']}
Адрес: {data['Address']}
БИК банка: {data['bankBIK']}
Корреспондентский счет: {data['bankCorr']}
ИНН банка: {data['bankINN']}
КПП банка: {data['bankKPP']}
Номер счета: {data['bankNum']}
Имя владельца карты: {data['bankClient']}
Номер кредитной карты: {data['bankCard']}
Срок действия карты: {data['bankDate']}
CVC/CVV код: {data['bankCVC']}
Специальность: {data['EduSpecialty']}
Направление: {data['EduProgram']}
Учебное заведение: {data['EduName']}
Серия/Номер диплома: {data['EduDocNum']}
Регистрационный номер: {data['EduRegNumber']}
Дата окончания обучения: {data['EduYear']}
Марка и модель автомобиля: {data['CarBrand']} {data['CarModel']}
Год выпуска: {data['CarYear']}
Цвет автомобиля: {data['CarColor']}
Номерной знак: {data['CarNumber']}
VIN Код: {data['CarVIN']}
Серия/номер СТС: {data['CarSTS']}
Дата выдачи СТС: {data['CarSTSDate']}
Серия/номер ПТС: {data['CarPTS']}
Дата выдачи ПТС: {data['CarPTSDate']}

""")
    if Gen_Mode == "User-Agent":
        ua = UserAgent()
        for i in range(int(Gen_value)):
            print(f"{i + 1} Юзер-Агент: {ua.random}\n")
    if Gen_Mode == "Банковские карты":
        for i in range(int(Gen_value)):
            card = generate_credit_card('Mir')
            print(f"Номер карты: {card['card_number']}\nСрок действия: {card['expiry_date']}\nCVC/CVV: {card['cvv']}\n")
        


Button_Gen_container = ft.Container(
    bgcolor = color_S,
    border_radius = 5,
    height = 30,
    margin=5,
    content= ft.Text(f" Запуск ", font_family="PT Mono", size=20, color = Theme_Text_color),
    ink = True,
    on_hover = on_hover_But,
    on_click=lambda e: Gen(Generator_Mode.value, Gen_value.value),
    shadow=ft.BoxShadow(
        spread_radius=1.8,
        blur_radius=0,
        color=color_Shadow,
        offset=ft.Offset(2.2, 2.2),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ))
Generator_Text = ft.Text("Генератор", font_family="PT Mono", size=26, color = color_S)
Module_Generator_container = ft.Container(
    bgcolor = Theme_block,
    padding=10,
    shadow=ft.BoxShadow(
        spread_radius=2,
        blur_radius=0,
        color=Theme_Shadow,
        offset=ft.Offset(2.2, 2.2),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
    content= ft.Column([Generator_Text,Generator_Mode,Gen_value,Button_Gen_container]),
    border_radius = 5,
    width = 333
    )


#Бомбер
#Номер бомбера
Bomber_Number = ft.TextField(label="Номер телефона", hint_text="e. g. 79999999999",hint_style = ft.TextStyle(color = "#9b9fa6"), focused_border_color = color_S,text_style = ft.TextStyle(color = Theme_Xtool_Text), label_style= ft.TextStyle(color = color_S), border_color = Theme_Xtool_Text)
#Повторы бомбера
Bomber_Replay = ft.Slider(value = 1,min=1, max=50, active_color = color_S, divisions=49, label="{value} Повторы")
#Кнопка запуска бомбера
Button_StartBomber_container = ft.Container(
    bgcolor = color_S,
    border_radius = 5,
    height = 30,
    margin=5,
    content= ft.Text(f" Запуск ", font_family="PT Mono", size=20, color = Theme_Text_color),
    ink = True,
    on_hover = on_hover_But,
    on_click=lambda e: StartBomber(Bomber_Number.value, Bomber_Replay.value),
    shadow=ft.BoxShadow(
        spread_radius=1.8,
        blur_radius=0,
        color=color_Shadow,
        offset=ft.Offset(2.2, 2.2),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ))

#Запуск бомбера
def StartBomber(number, replay):

    from Source.Bomber.Run import start_async_attacks
    from Source.Bomber.Attack.Services import urls
    from Source.Bomber.Attack.Feedback_Services import feedback_urls
    
    start_async_attacks(number, replay)
    
Bomber_Text = ft.Text("Бомбер", font_family="PT Mono", size=26, color = color_S)
Module_Bomber_container = ft.Container(
    bgcolor = Theme_block,
    padding=10,
    
    shadow=ft.BoxShadow(
        spread_radius=2,
        blur_radius=0,
        color=Theme_Shadow,
        offset=ft.Offset(2.2, 2.2),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
    content= ft.Column([Bomber_Text,Bomber_Number, Bomber_Replay, Button_StartBomber_container]),
    border_radius = 5,
    width = 333
    )

# Снос
Snos_Tag = ft.TextField(label="Тег", hint_text="e. g. @XTERR0R",hint_style = ft.TextStyle(color = "#9b9fa6"), focused_border_color = color_S, label_style= ft.TextStyle(color = color_S),text_style = ft.TextStyle(color = Theme_Xtool_Text), border_color = Theme_Xtool_Text)

Snos_time = ft.Slider(value = 5,min=5, max=360, active_color = color_S, divisions=71, label="{value} Интервал")

Snos_value = ft.Slider(value = 1,min=1, max=1000, active_color = color_S, divisions=111, label="{value} Жалоб будет отправлено")

Snos_Target = ft.Dropdown(
        border_color = Theme_Xtool_Text,
        label = "Тип цели",
        label_style= ft.TextStyle(color = color_S),
        focused_border_color = color_S,
        text_style = ft.TextStyle(color = Theme_Xtool_Text),
        bgcolor = "#1a1c1e",
        filled = False,
        options=[
            ft.dropdown.Option("Канал"),
            ft.dropdown.Option("Юзер"),
        ],
    )
    
Snos_Option = ft.Dropdown(
        border_color = Theme_Xtool_Text,
        label = "Тип отправки",
        label_style= ft.TextStyle(color = color_S),
        focused_border_color = color_S,
        text_style = ft.TextStyle(color = Theme_Xtool_Text),
        bgcolor = "#1a1c1e",
        filled = False,
        options=[
            ft.dropdown.Option("Письма"),
            ft.dropdown.Option("Сайт Поддержки"),
            ft.dropdown.Option("Письма и Сайт Поддержки"),
        ],
    )

Button_StartSnos_container = ft.Container(
    bgcolor = color_S,
    border_radius = 5,
    height = 30,
    margin=5,
    content= ft.Text(f" Запуск ", font_family="PT Mono", size=20, color = Theme_Text_color),
    ink = True,
    on_hover = on_hover_But,
    on_click=lambda e: Snos(),
    shadow=ft.BoxShadow(
        spread_radius=1.8,
        blur_radius=0,
        color=color_Shadow,
        offset=ft.Offset(2.2, 2.2),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ))
Snos_Text = ft.Text("Снос", font_family="PT Mono", size=26, color = color_S)
Module_Snos_container = ft.Container(
    bgcolor = Theme_block,
    padding=10,
    shadow=ft.BoxShadow(
        spread_radius=2,
        blur_radius=0,
        color=Theme_Shadow,
        offset=ft.Offset(2.2, 2.2),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
    content= ft.Column([Snos_Text, Snos_Tag, Snos_Target,Snos_Option, Snos_time,Snos_value,Button_StartSnos_container]),
    border_radius = 5,
    width = 333
    )
#Ну тут еще какая-то хуйня  
Swat_Text = ft.Text("Сват", font_family="PT Mono", size=26, color = color_S)

Module_Swat_container = ft.Container(
    bgcolor = Theme_block,
    padding=10,
    shadow=ft.BoxShadow(
        spread_radius=2,
        blur_radius=0,
        color=Theme_Shadow,
        offset=ft.Offset(2.2, 2.2),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
    content= ft.Column([Swat_Text]),
    border_radius = 5,
    width = 333
    )

Sender_Text = ft.Text("Сендер", font_family="PT Mono", size=26, color = color_S)

Module_Sender_container = ft.Container(
    bgcolor = Theme_block,
    padding=10,
    shadow=ft.BoxShadow(
        spread_radius=2,
        blur_radius=0,
        color=Theme_Shadow,
        offset=ft.Offset(2.2, 2.2),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
    content= ft.Column([Sender_Text]),
    border_radius = 5,
    width = 333
    )
Button_ChangeColor_container = ft.Container(
    bgcolor = color_S,
    border_radius = 5,
    height = 30,
    width = 308,
    margin=5,
    content= ft.Text(f" Поменять цвет ", font_family="PT Mono", size=20, color = Theme_Text_color,text_align = ft.TextAlign.CENTER),
    ink = True,
    on_hover = on_hover_But,
    on_click=lambda e: change_color(),
    shadow=ft.BoxShadow(
        spread_radius=1.8,
        blur_radius=0,
        color=color_Shadow,
        offset=ft.Offset(2.2, 2.2),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ))
Button_ChangeTheme_container = ft.Container(
    bgcolor = color_S,
    border_radius = 5,
    height = 30,
    width = 308,
    margin=5,
    content= ft.Text(f" Поменять тему ", font_family="PT Mono", size=20, color = Theme_Text_color, text_align = ft.TextAlign.CENTER),
    ink = True,
    on_hover = on_hover_But,
    on_click=lambda e: change_Theme(),
    shadow=ft.BoxShadow(
        spread_radius=1.8,
        blur_radius=0,
        color=color_Shadow,
        offset=ft.Offset(2.2, 2.2),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ))
    
def Check_TG(e):
    if checkbox_tg.value:
        Module_Settings_container.content = ft.Column([checkbox_tg,Button_ChangeColor_container,Button_ChangeTheme_container])
        e.control.update()
    else:
        Module_Settings_container.content = ft.Column([Settings_Text,checkbox_tg,Button_ChangeColor_container,Button_ChangeTheme_container])
        e.control.update()   
    
checkbox_tg = ft.Checkbox(label="Отправлять сообщения в telegram?", value=False)
Settings_Text = ft.Text("Настройки", font_family="PT Mono", size=26, color = color_S)
Module_Settings_container = ft.Container(
    bgcolor = Theme_block,
    padding=10,
    shadow=ft.BoxShadow(
        spread_radius=2,
        blur_radius=0,
        color=Theme_Shadow,
        offset=ft.Offset(2.2, 2.2),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
    content= ft.Column([Settings_Text,checkbox_tg,Button_ChangeColor_container,Button_ChangeTheme_container]),
    border_radius = 5,
    width = 333
    )

    
AutoReg_Text = ft.Text("Авторег", font_family="PT Mono", size=26, color = color_S)
Module_Autoreg_container = ft.Container(
    bgcolor = Theme_block,
    padding=10,
    shadow=ft.BoxShadow(
        spread_radius=2,
        blur_radius=0,
        color=Theme_Shadow,
        offset=ft.Offset(2.2, 2.2),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
    content= ft.Column([AutoReg_Text]),
    border_radius = 5,
    width = 333
    )

Module_List= ft.Row([ft.Column([Module_DataBase_container, Module_Generator_container],alignment = ft.MainAxisAlignment.START),ft.Column([Module_Bomber_container,Module_Sender_container]),ft.Column([Module_Snos_container,Module_Autoreg_container]),ft.Column([Module_Settings_container,Module_Swat_container])],vertical_alignment = ft.CrossAxisAlignment.START)

def change_Theme():
    global Theme_block, Theme_bg, Theme_Shadow
    if Theme_bg == "#141D2B":
        Theme_bg = "#FFFFFF"
        Theme_block = "#F5F5F5"
        Theme_Shadow = "#E0E0E0"
        Theme_Text_color = "WHITE"
        Theme_Xtool_Text = "BLACK"
        Generator_Mode.bgcolor = Theme_Text_color
        Snos_Target.bgcolor = Theme_Text_color
        Snos_Option.bgcolor = Theme_Text_color
        Bomber_Number.hint_style.color = Theme_Xtool_Text
        Snos_Tag.hint_style.color = Theme_Xtool_Text
    elif Theme_bg == "#FFFFFF":
        Theme_block = "#1A2332"
        Theme_bg = "#141D2B"
        Theme_Shadow = "#0F1620"
        Theme_Text_color = "BLACK"
        Theme_Xtool_Text = "WHITE"
        Generator_Mode.bgcolor = "#1a1c1e"
        Snos_Target.bgcolor = "#1a1c1e"
        Snos_Option.bgcolor = "#1a1c1e"
        Bomber_Number.hint_style.color = "#9b9fa6"
        Snos_Tag.hint_style.color = "#9b9fa6"
    
    Title_container.bgcolor = Theme_block
    Title_container.shadow.color = Theme_Shadow
    Progress_container.bgcolor = Theme_block
    Progress_container.shadow.color = Theme_Shadow
    Text_ExportData.color = Theme_Xtool_Text
    Button_Export_container.bgcolor = Theme_block
    Button_Export_container.shadow.color = Theme_Shadow
    Module_DataBase_container.bgcolor = Theme_block
    Module_DataBase_container.shadow.color = Theme_Shadow
    Generator_Mode.border_color = Theme_Xtool_Text
    Generator_Mode.text_style.color = Theme_Xtool_Text
    Snos_Target.border_color = Theme_Xtool_Text
    Snos_Target.text_style.color = Theme_Xtool_Text
    text_attacked.color = Theme_Xtool_Text
    Bomber_Number.border_color = Theme_Xtool_Text
    Bomber_Number.text_style.color = Theme_Xtool_Text
    Snos_Tag.border_color = Theme_Xtool_Text
    Button_Gen_container.content.color = Theme_Text_color
    Button_StartBomber_container.content.color = Theme_Text_color
    Module_Generator_container.bgcolor = Theme_block
    Module_Generator_container.shadow.color = Theme_Shadow
    Module_Bomber_container.bgcolor = Theme_block
    Module_Bomber_container.shadow.color = Theme_Shadow
    Snos_Option.border_color = Theme_Xtool_Text
    Snos_Option.text_style.color = Theme_Xtool_Text
    Button_StartSnos_container.content.color = Theme_Text_color
    Module_Snos_container.bgcolor = Theme_block
    Module_Snos_container.shadow.color = Theme_Shadow
    Snos_Tag.text_style.color = Theme_Xtool_Text
    Module_Swat_container.bgcolor = Theme_block
    Module_Swat_container.shadow.color = Theme_Shadow
    Module_Sender_container.bgcolor = Theme_block
    Module_Sender_container.shadow.color = Theme_Shadow
    Button_ChangeColor_container.content.color = Theme_Text_color
    Button_ChangeTheme_container.content.color = Theme_Text_color
    Module_Settings_container.bgcolor = Theme_block
    Module_Settings_container.shadow.color = Theme_Shadow
    Module_Autoreg_container.bgcolor = Theme_block
    Module_Autoreg_container.shadow.color = Theme_Shadow
    
    
    
    changer_Theme_bg()
    update()

    

def change_color():
    global color_S
    if color_S == "#00efc7":
        color_S = "#5000ef"
        color_Shadow = "#230266"
    elif color_S == "#5000ef":
        color_S = "#ef0028"
        color_Shadow = "#660213"
    elif color_S == "#ef0028":
        color_S = "#9FEF00"
        color_Shadow = "#456602"
    elif color_S == "#9FEF00":
        color_S = "#00efc7"
        color_Shadow = "#026655"
        
    text_Xtool.color = color_S
    Progress.color = color_S
    SearchDatabase.color = color_S
    Generator_Mode_label.color = color_S
    Generator_Mode_label.focused_border_color = color_S
    Generator_Mode.focused_border_color = color_S
    Gen_value.active_color = color_S
    Button_Gen_container.bgcolor = color_S
    Generator_Text.color = color_S
    Bomber_Number.focused_border_color = color_S
    Bomber_Number.label_style.color = color_S
    Bomber_Replay.active_color = color_S
    Button_StartBomber_container.bgcolor = color_S
    Bomber_Text.color = color_S
    Snos_Tag.focused_border_color = color_S
    Snos_Tag.label_style.color = color_S
    Snos_time.active_color = color_S
    Snos_value.active_color = color_S
    Snos_Target.label_style.color = color_S
    Snos_Target.focused_border_color = color_S
    Snos_Option.label_style.color = color_S
    Snos_Option.focused_border_color = color_S
    Button_StartSnos_container.bgcolor = color_S
    Snos_Text.color = color_S
    Swat_Text.color = color_S
    Sender_Text.color = color_S
    Button_ChangeColor_container.bgcolor = color_S
    Settings_Text.color = color_S
    AutoReg_Text.color = color_S
    Button_Gen_container.shadow.color = color_Shadow
    Button_StartBomber_container.shadow.color = color_Shadow
    Button_StartSnos_container.shadow.color = color_Shadow
    Button_ChangeColor_container.shadow.color = color_Shadow
    Button_ChangeTheme_container.bgcolor = color_S
    Button_ChangeTheme_container.shadow.color = color_Shadow

    update()

    Button_ChangeTheme_container


def Snos():
    global jobs_successful,jobs_failed
    Progress.value = 0
    jobs_successful = 0
    jobs_failed = 0
    jobs_successful_txt.value = f"{jobs_successful} jobs successful"
    jobs_successful_txt.value = f"{jobs_successful} jobs successful"
    update()
    if Snos_Option.value == "Сайт Поддержки":

        url = 'https://telegram.org/support'
        ua = UserAgent()
        

        def send_complaint(text, contact):
            global jobs_successful,jobs_failed
            headers = {
                'User-Agent': ua.random
            }
            payload = {
                'text': text,
                'contact': contact
            }
            
            proxies = {
            'http': '51.15.242.202:8888',
            'http': '91.148.127.162:8080',
            'http': '50.221.74.130:80',
            'http': '93.177.67.178:80',
            'http': '173.213.71.6:80',
        }
            
            response = requests.post(url, data=payload, headers=headers, proxies=proxies)
            
            if response.status_code == 200:
                Progress.value = Progress.value + 1 / Snos_value.value
                jobs_successful = jobs_successful + 1
                print(f"Жалоба с текстом:\n<{text}> была успешно отправлена\nВсего успешно отправленных жалоб: {jobs_successful}\n")
                jobs_successful_txt.value = f"{jobs_successful} jobs successful"
                update()
            else:
                jobs_failed = jobs_failed + 1
                print(f"Жалоба с текстом:\n<{text}> не была отправлена\nВсего успешно отправленных жалоб: {jobs_successful}\n")
                jobs_failed_txt.value = f"{jobs_failed} jobs failed"
                update()

        text = [
        f"Здравствуйте, уважаемые сотрудники Telegram. Я обращаюсь с жалобой на пользователя {Snos_Tag.value}, который незаконно распространяет мои личные данные, включая мою домашнюю и электронную почту. Прошу незамедлительно заблокировать его аккаунт.",
        f"Прошу заблокировать пользователя {Snos_Tag.value} за распространение моего номера телефона, домашнего адреса и даты рождения без моего согласия. Это серьезное нарушение конфиденциальности, которое подвергает меня риску.",
        f"Здравствуйте, я обращаюсь с жалобой на {Snos_Tag.value}, который публикует мою личную информацию, включая мои банковские реквизиты и адрес. Это создает серьезную угрозу моей безопасности и финансовому благополучию.",
        f"Прошу заблокировать аккаунт {Snos_Tag.value}, который без моего согласия размещает мои фотографии, личные сообщения и номер телефона. Это представляет серьезную угрозу моей репутации и благополучию.",
        f"Обращаюсь с просьбой заблокировать {Snos_Tag.value} за публикацию моих медицинских карт и результатов анализов. Это грубое нарушение конфиденциальности, которое может нанести вред моему здоровью.",
        f"Прошу принять меры против {Snos_Tag.value}, который раскрывает мои отношения, публикуя мои частные переписки и личные фото. Это неэтично и нарушает мое право на неприкосновенность частной жизни.",
        f"Я столкнулся с киберпреследованием со стороны {Snos_Tag.value}, который распространяет ложную информацию о моей личности и моем месте жительства. Это вызывает у меня тревогу и беспокойство. Прошу срочно заблокировать его аккаунт.",
        f"Уважаемые сотрудники Telegram, я прошу вас заблокировать {Snos_Tag.value}, который угрожает опубликовать конфиденциальную информацию о моей семье, если я не выполню его требования. Это серьезная угроза, которая нарушает мою безопасность.",
        f"Прошу принять меры против {Snos_Tag.value}, который шантажирует меня, угрожая раскрыть мои интимные фотографии. Это незаконно и совершенно неприемлемо. Прошу немедленно вмешаться и заблокировать его аккаунт.",
        f"Я обращаюсь с жалобой на {Snos_Tag.value}, который создал фальшивый профиль, используя мою личную информацию, и распространяет ложную информацию о моей работе и личной жизни. Это клевета и нарушение конфиденциальности. Прошу вас принять меры для защиты моих прав.",
        f"Уважаемые сотрудники Telegram, я обращаюсь с жалобой на пользователя {Snos_Tag.value}, который публикует скриншоты моих личных сообщений и переписок без моего согласия. Это серьезное нарушение конфиденциальности, которое подрывает мои отношения и репутацию.",
        f"Прошу вас заблокировать аккаунт {Snos_Tag.value}, который незаконно распространяет мои личные данные, включая мой адрес и номер социального страхования. Это создает серьезную угрозу моей безопасности и финансовому благополучию.",
        f"Я столкнулся с киберпреследованием со стороны {Snos_Tag.value}, который публикует мои персональные данные, включая информацию о моем месте работы и образовании. Это вторжение в мою частную жизнь и создает для меня значительный дискомфорт.",
        f"Прошу принять меры против {Snos_Tag.value}, который использует мои личные фотографии для создания фальшивых аккаунтов и распространения оскорбительных постов от моего имени. Это наносит ущерб моей репутации и вызывает у меня тревогу и беспокойство.",
        f"Я обращаюсь с жалобой на {Snos_Tag.value}, который угрожает опубликовать компрометирующие видео со мной, если я не выполню его требования. Это шантаж, и я опасаюсь за свою безопасность и благополучие.",
        f"Прошу заблокировать аккаунт {Snos_Tag.value}, который использует мои личные данные для создания фишинговых веб-сайтов в попытке получить мою конфиденциальную информацию. Это незаконно и подвергает меня риску мошенничества и кражи личных данных.",
        f"Я столкнулся с доксингом со стороны {Snos_Tag.value}, который раскрыл мой домашний адрес, номер телефона и личную информацию членов моей семьи. Это серьезное нарушение конфиденциальности, которое подвергает меня и моих близких риску.",
        f"Уважаемые сотрудники Telegram, я прошу вас заблокировать {Snos_Tag.value}, который распространяет мои личные данные, включая мою расовую и религиозную принадлежность. Это разжигание ненависти и дискриминации, которое создает для меня враждебную и небезопасную среду.",
        f"Прошу принять меры против {Snos_Tag.value}, который публикует мои персональные данные вместе с ложными обвинениями и клеветой. Это наносит ущерб моей репутации и подвергает меня общественному порицанию.",
        f"Я обращаюсь с жалобой на {Snos_Tag.value}, который создал фальшивый профиль, используя мои личные данные, и отправляет оскорбительные и угрожающие сообщения другим пользователям от моего имени. Это мошенничество, и я опасаюсь за свою безопасность и репутацию.",
        f"Здравствуйте! Сообщаю о пользователе {Snos_Tag.value}, который неправомерно распространяет мои персональные данные, включая номер телефона, адрес и список контактов, причиняя мне существенный ущерб.",
        f"Прошу заблокировать аккаунт {Snos_Tag.value}, который без моего согласия размещает конфиденциальные банковские реквизиты и информацию о моем имуществе, нарушая мои права и ставя под угрозу мою финансовую безопасность.",
        f"Требую заблокировать пользователя {Snos_Tag.value}, который шантажирует меня публикацией личных фотографий и переписки, полученных незаконно. Это серьезное нарушение моей конфиденциальности и причиняет мне моральный вред.",
        f"Жалоба на аккаунт {Snos_Tag.value}, который неоднократно публикует ложные сведения о моем местонахождении, ставя под угрозу мою безопасность и физическое благополучие.",
        f"Прошу предоставить информацию об аккаунте {Snos_Tag.value}, который распространяет мои личные медицинские данные, включая диагнозы и результаты анализов, нарушая мое право на конфиденциальность и охрану здоровья.",
        f"Здравствуйте! Пользователь {Snos_Tag.value} размещает на своем канале мои паспортные данные, фотографии и информацию о родственных связях, что является грубым нарушением моего права на неприкосновенность частной жизни.",
        f"Прошу заблокировать пользователя {Snos_Tag.value}, который с целью мести публикует мои данные об образовании и обучении, что может нанести ущерб моей репутации и возможностям трудоустройства.",
        f"Требую блокировки аккаунта {Snos_Tag.value}, поскольку пользователь распространяет информацию о моих юридических проблемах и судебных разбирательствах, что нарушает мои права и препятствует моему восстановлению в обществе.",
        f"Жалоба на пользователя {Snos_Tag.value}, который незаконно получил и обнародовал мои банковские выписки и налоговые декларации, что может привести к финансовым потерям и проблемам с налоговыми органами.",
        f"Прошу заблокировать аккаунт {Snos_Tag.value}, который публикует конфиденциальные записи моих телефонных разговоров и электронной переписки, грубо нарушая мои права на неприкосновенность частной жизни и коммуникаций.",
        f"Здравствуйте, меня зовут Иван, и мне угрожает пользователь {Snos_Tag.value}. Он распространяет мою личную информацию, включая мой номер телефона, адрес и данные банковской карты. Я опасаюсь за свою безопасность и прошу вас заблокировать этого пользователя.",
        f"Уважаемые представители Telegram, я подаю жалобу на пользователя {Snos_Tag.value}, который раскрыл мои фотографии и интимные сообщения без моего согласия. Это является серьезным нарушением моего права на неприкосновенность частной жизни, и я требую немедленной блокировки этого аккаунта.",
        f"Здравствуйте, я Юлия, и меня беспокоит пользователь {Snos_Tag.value}, публикующий мои личные данные, включая мой номер паспорта, медицинские записи и записи о трудоустройстве. Такое поведение неприемлемо, и я опасаюсь за свою безопасность и репутацию. Примите меры немедленно.",
        f"Уважаемая команда Telegram, пользователь {Snos_Tag.value} выложил в сеть мой номер телефона и адрес, что привело к потоку нежелательных звонков и сообщений. Я подвергаюсь преследованиям и прошу вас заблокировать этого пользователя и оказать содействие в расследовании.",
        f"Я, Анна, подаю жалобу на пользователя {Snos_Tag.value}, который выдал мою личную информацию в открытом чате. Теперь мои контактные данные доступны для всех, что создает угрозу моей безопасности. Заблокируйте этого пользователя и дайте мне знать о дальнейших действиях.",
        f"Здравствуйте, уважаемые сотрудники Telegram, меня зовут Максим, и меня преследует пользователь {Snos_Tag.value}. Он опубликовал мои фотографии с места работы, личные сообщения с семьей и даже данные о моих банковских счетах. Прошу вас срочно принять меры и защитить мою частную жизнь.",
        f"Уважаемый Telegram, я жалуюсь на пользователя {Snos_Tag.value}, который разгласил мой домашний адрес, номера телефонов и банковские реквизиты. Такое поведение угрожает моей безопасности и финансовому благополучию. Прошу вас заблокировать этого пользователя и оказать помощь в расследовании.",
        f"Уважаемая команда поддержки, пользователь {Snos_Tag.value} распространяет мою личную информацию, включая мое полное имя, дату рождения и адрес электронной почты. Это серьезное нарушение моей конфиденциальности, и я требую немедленных действий. Заблокируйте аккаунт этого пользователя и расследуйте данное происшествие.",
        f"Я обращаюсь с жалобой на пользователя {Snos_Tag.value}, который раскрыл мои данные о трудоустройстве, включая мое резюме, данные о зарплате и сведения о моих бывших работодателях. Это серьезное нарушение конфиденциальности, которое может нанести ущерб моей карьере. Прошу о немедленной блокировке этого пользователя и принятии мер против виновного.",
        f"Уважаемые представители Telegram, пользователь {Snos_Tag.value} публикует мои сообщения из личной переписки с друзьями и членами семьи. Это грубое вторжение в мою частную жизнь, и я чувствую себя униженной и преданной. Прошу вас заблокировать этого пользователя и помочь мне разобраться в этом крайне неприятном инциденте.",
        f"Уважаемая команда Telegram, меня преследует пользователь {Snos_Tag.value}, который распространяет мои личные фотографии и видео без моего согласия. Такое поведение является серьезным нарушением моей конфиденциальности и причиняет мне значительный моральный ущерб. Прошу о немедленной блокировке этого пользователя и принятии мер против него.",
        f"Я обращаюсь с жалобой на пользователя {Snos_Tag.value}, который выложил в сеть мою переписку с врачом, содержащую конфиденциальную медицинскую информацию. Такой поступок является нарушением закона о защите персональных данных и может иметь серьезные последствия для моего здоровья. Прошу вас заблокировать этого пользователя и помочь мне привлечь его к ответственности.",
        f"Уважаемые представители Telegram, пользователь {Snos_Tag.value} опубликовал мои данные о кредитной истории и другую финансовую информацию, что привело к несанкционированным запросам на кредит и попыткам мошенничества. Такое поведение угрожает моей финансовой безопасности и репутации. Прошу вас принять меры против этого пользователя и помочь мне восстановить мою финансовую стабильность.",
        f"Я подаю жалобу на пользователя {Snos_Tag.value}, который раскрыл мои политические убеждения и религиозные взгляды. Это привело к преследованиям и угрозам в мой адрес. Такое поведение является нарушением моих основных прав и свобод и создает угрозу для моей безопасности. Прошу вас заблокировать этого пользователя и принять меры для защиты моих прав.",
        f"Уважаемая служба поддержки, пользователь {Snos_Tag.value} выложил в сеть мою личную переписку, содержащую конфиденциальную информацию о моей семье и друзьях. Это является серьезным нарушением их права на неприкосновенность частной жизни и может нанести им значительный ущерб. Прошу вас заблокировать этого пользователя и помочь мне привлечь его к ответственности за его действия.",
        f"Я обращаюсь с жалобой на пользователя {Snos_Tag.value}, который опубликовал мои юридические документы, включая судебные решения и постановления. Такое поведение является нарушением закона и может нанести ущерб моему делу. Прошу вас заблокировать этого пользователя и оказать содействие в расследовании этого инцидента.",
        f"Уважаемая команда Telegram, пользователь {Snos_Tag.value} раскрыл мои данные об образовании, включая мои оценки, дипломы и резюме. Такое поведение является нарушением моей конфиденциальности и может нанести ущерб моей академической и профессиональной репутации. Прошу вас заблокировать этого пользователя и помочь мне защитить мои права.",
        f"Я подаю жалобу на пользователя {Snos_Tag.value}, который выложил в сеть мою личную переписку с адвокатом, содержащую конфиденциальную информацию о моем текущем судебном деле. Такое поведение является нарушением правил адвокатской этики и может нанести ущерб моему делу. Прошу вас заблокировать этого пользователя и оказать содействие в расследовании этого инцидента.",
        f"Уважаемая служба поддержки, пользователь {Snos_Tag.value} опубликовал мои личные фотографии и видео, которые я отправил своему партнеру. Это является серьезным нарушением моей конфиденциальности и может нанести непоправимый ущерб моим отношениям. Прошу вас немедленно заблокировать этого пользователя и помочь мне удалить эти материалы из интернета.",
        f"Я обращаюсь с жалобой на пользователя {Snos_Tag.value}, который выложил в сеть мою личную переписку с психологом, содержащую конфиденциальную информацию о моем психическом здоровье. Такое поведение является нарушением врачебной тайны и может нанести серьезный ущерб моему благополучию. Прошу вас заблокировать этого пользователя и помочь мне привлечь его к ответственности за его действия.",
        f"Здравствуйте, уважаемые сотрудники Telegram! Пользователь {Snos_Tag.value} разместил на своей странице мою фотографию и личный номер телефона, а также угрожает распространить сведения о моем месте жительства и работе. Такое поведение нарушает мою конфиденциальность и подвергает меня опасности. Прошу вас заблокировать аккаунт {Snos_Tag.value} и удалить все мои личные данные.",
        f"Обращаюсь к вам с жалобой на действия пользователя {Snos_Tag.value}. Этот человек распространяет на своей странице мою финансовую информацию, включая данные о банковских счетах и кредитных картах. Это ставит под угрозу мою финансовую безопасность и может привести к серьезным последствиям. Убедительно прошу вас принять меры против {Snos_Tag.value} и удалить все мои персональные данные с его страницы.",
        f"Добрый день, специалисты Telegram! Несколько дней назад пользователь {Snos_Tag.value} начал размещать на своей странице мои закрытые медицинские данные, включая результаты анализов и диагноз. Я считаю это грубым нарушением моей медицинской конфиденциальности. Данная информация может быть использована против меня злоумышленниками и причинить мне значительный вред. Прошу вас заблокировать учетную запись {Snos_Tag.value} и удалить все мои медицинские сведения с его страницы.",
        f"Уважаемая команда Telegram! Я обнаружила, что пользователь {Snos_Tag.value} публикует на своем канале мою переписку из личного мессенджера. Эта переписка содержит конфиденциальные разговоры с близкими мне людьми. Распространение этих сообщений нарушает мое право на частную жизнь и причиняет мне моральный ущерб. Прошу вас принять меры против {Snos_Tag.value} и удалить все мои личные сообщения с его страницы.",
        f"Обращаюсь к вам с просьбой о помощи. Пользователь {Snos_Tag.value} уже неделю как распространяет в своих постах мои личные дневниковые записи. Эти записи содержат мои самые сокровенные мысли и переживания. Их публикация приносит мне огромные страдания и разрушает мою жизнь. Убедительно прошу вас заблокировать аккаунт {Snos_Tag.value} и удалить все мои дневниковые записи с его страницы.",
        f"Добрый день, поддержка Telegram! Пользователь {Snos_Tag.value} создал фейковый аккаунт с моей фотографией и персональными данными. На этой странице он публикует клеветнические и оскорбительные заявления, наносящие ущерб моей репутации и моральному состоянию. Я считаю эти действия злонамеренными и требую немедленного вмешательства. Прошу вас заблокировать учетную запись {Snos_Tag.value} и удалить все мои личные сведения с фейкового аккаунта.",
        f"Уважаемый Telegram! Я хочу сообщить о пользователе {Snos_Tag.value}, который опубликовал в своем канале мои детские фотографии без моего согласия. Эти снимки являются неприкосновенной частью моей жизни, и их распространение без моего ведома нарушает мое право на неприкосновенность частной жизни. Прошу вас заблокировать аккаунт {Snos_Tag.value} и удалить все мои детские фотографии с его страницы.",
        f"Здравствуйте, команда Telegram! Я столкнулась с ужасной ситуацией, где пользователь {Snos_Tag.value} угрожает распространить мои интимные видеозаписи, если я не заплачу ему выкуп. Это акт шантажа и нарушения моей неприкосновенности частной жизни. Я опасаюсь за свою безопасность и прошу вас незамедлительно вмешаться. Прошу вас заблокировать аккаунт {Snos_Tag.value} и удалить все мои личные видеозаписи с его страницы.",
        f"Обращаюсь к вам с жалобой на пользователя {Snos_Tag.value}, который разгласил в своем канале мои данные о местоположении, включая домашний адрес и места, где я часто бываю. Такое поведение подвергает мою жизнь и жизнь моих близких опасности. Я считаю, что {Snos_Tag.value} действует с умыслом причинить мне вред, и требую его немедленной блокировки. Прошу вас удалить все мои личные данные с его страницы.",
        f"Уважаемые специалисты Telegram! Я пишу, чтобы сообщить о пользователе {Snos_Tag.value}, который получил доступ к моей личной переписке в мессенджере и публикует ее на своей странице без моего согласия. Эта переписка содержит конфиденциальные разговоры с моими коллегами, друзьями и деловыми партнерами. Я считаю, что действия {Snos_Tag.value} являются злонамеренными и нарушают мое право на неприкосновенность частной жизни. Убедительно прошу вас принять меры против {Snos_Tag.value} и удалить все мои личные сообщения с его страницы.",
        f"Здравствуйте, уважаемые сотрудники Telegram! Пользователь {Snos_Tag.value} разместил на своей странице мою интеллектуальную собственность, включая мои авторские статьи и разработки, без моего согласия. Такие действия нарушают мои авторские права и наносят ущерб моему бизнесу. Прошу вас заблокировать аккаунт {Snos_Tag.value} и удалить весь мой контент с его страницы.",
        f"Обращаюсь к вам с жалобой на действия пользователя {Snos_Tag.value}. Этот человек распространяет на своей странице мои коммерческие секреты, включая информацию о нашей ценовой политике, стратегии развития и планах на будущее. Это ставит под угрозу наш бизнес и может привести к серьезным финансовым потерям. Убедительно прошу вас принять меры против {Snos_Tag.value} и удалить все мои коммерческие секреты с его страницы.",
        f"Добрый день, специалисты Telegram! Несколько дней назад пользователь {Snos_Tag.value} начал размещать на своей странице мои конфиденциальные деловые документы, включая договоры с клиентами и финансовые отчеты. Я считаю это грубым нарушением моей деловой репутации и требую немедленного вмешательства. Прошу вас заблокировать учетную запись {Snos_Tag.value} и удалить все мои деловые документы с его страницы.",
        f"Уважаемая команда Telegram! Я обнаружила, что пользователь {Snos_Tag.value} публикует на своем канале мои личные фото и видео, которые я никогда не размещала в открытом доступе. Это грубое нарушение моего права на неприкосновенность частной жизни и причиняет мне моральный ущерб. Прошу вас принять меры против {Snos_Tag.value} и удалить все мои личные фото и видео с его страницы.",
        f"Обращаюсь к вам с просьбой о помощи. Пользователь {Snos_Tag.value} уже неделю как распространяет в своих постах мои сообщения из электронной почты. Эти сообщения содержат конфиденциальную переписку с моими деловыми партнерами и клиентами. Их публикация наносит ущерб моей репутации и может привести к потере доверия со стороны моих партнеров. Убедительно прошу вас заблокировать аккаунт {Snos_Tag.value} и удалить все мои сообщения из электронной почты с его страницы.",
        f"Добрый день, поддержка Telegram! Пользователь {Snos_Tag.value} создал фейковый аккаунт с моими фото и личными данными. На этой странице он публикует ложную информацию обо мне и моих близких, а также распространяет клеветнические заявления. Я считаю эти действия злонамеренными и требую их немедленного прекращения. Прошу вас заблокировать учетную запись {Snos_Tag.value} и удалить все мои личные сведения с фейкового аккаунта.",
        f"Уважаемый Telegram! Я хочу сообщить о пользователе {Snos_Tag.value}, который опубликовал в своем канале мои школьные сочинения и домашние задания без моего согласия. Эти работы являются частью моего учебного процесса и не предназначены для публичного распространения. Их публикация нарушает мое право на неприкосновенность частной жизни и наносит ущерб моей репутации. Прошу вас заблокировать аккаунт {Snos_Tag.value} и удалить все мои школьные работы с его страницы.",
        f"Здравствуйте, команда Telegram! Я столкнулась с ужасной ситуацией, где пользователь {Snos_Tag.value} угрожает опубликовать мои старые фотографии, которые я считала удаленными. Он требует от меня денег в обмен на то, чтобы не обнародовать эти фотографии. Это акт шантажа и нарушения моей неприкосновенности частной жизни. Я опасаюсь за свою безопасность и прошу вас незамедлительно вмешаться. Прошу вас заблокировать аккаунт {Snos_Tag.value} и удалить все мои старые фотографии с его страницы.",
        f"Обращаюсь к вам с жалобой на пользователя {Snos_Tag.value}, который разгласил в своем канале мои номера телефонов, включая личный и рабочий. Такое поведение подвергает мою жизнь и жизнь моих близких опасности преследований и домогательств. Я считаю, что {Snos_Tag.value} действует с умыслом причинить мне вред, и требую его немедленной блокировки. Прошу вас удалить все мои номера телефонов с его страницы.",
        f"Уважаемые специалисты Telegram! Я пишу, чтобы сообщить о пользователе {Snos_Tag.value}, который получил доступ к моему аккаунту в социальной сети и опубликовал мои личные сообщения без моего согласия. Эта переписка содержит конфиденциальные разговоры с моими друзьями и семьей. Я считаю, что действия {Snos_Tag.value} являются злонамеренными и нарушают мое право на неприкосновенность частной жизни. Убедительно прошу вас принять меры против {Snos_Tag.value} и удалить все мои личные сообщения с его страницы.",
        f"Уважаемые сотрудники Telegram! Пользователь {Snos_Tag.value} разместил на своей странице мои конфиденциальные медицинские данные, включая результаты анализов и диагноз, без моего согласия. Распространение такой информации нарушает мои права на неприкосновенность частной жизни и может нанести мне непоправимый вред. Прошу вас заблокировать аккаунт {Snos_Tag.value} и удалить все мои медицинские данные с его страницы.",
        f"Обращаюсь к вам с жалобой на действия пользователя {Snos_Tag.value}. Этот человек распространяет на своей странице мои личные фотографии, которые я никогда не публиковал в открытом доступе. Это грубое нарушение моего права на неприкосновенность частной жизни и причиняет мне моральный ущерб. Убедительно прошу вас принять меры против {Snos_Tag.value} и удалить все мои личные фотографии с его страницы.",
        f"Добрый день, специалисты Telegram! Несколько дней назад пользователь {Snos_Tag.value} начал размещать на своей странице мои закрытые финансовые документы, включая выписки с банковских счетов и налоговые декларации. Я считаю это грубым нарушением моей финансовой конфиденциальности и требую немедленного вмешательства. Прошу вас заблокировать учетную запись {Snos_Tag.value} и удалить все мои финансовые документы с его страницы.",
        f"Уважаемая команда Telegram! Я обнаружила, что пользователь {Snos_Tag.value} публикует на своем канале мои личные дневниковые записи без моего согласия. Эти записи содержат мои самые сокровенные мысли и переживания. Их публикация приносит мне огромные страдания и разрушает мою жизнь. Убедительно прошу вас заблокировать аккаунт {Snos_Tag.value} и удалить все мои дневниковые записи с его страницы.",
        f"Обращаюсь к вам с просьбой о помощи. Пользователь {Snos_Tag.value} уже неделю как распространяет в своих постах мои личные письма и открытки. Эти письма содержат конфиденциальную переписку с моими близкими людьми. Их публикация нарушает мое право на частную жизнь и причиняет мне моральный ущерб. Убедительно прошу вас заблокировать аккаунт {Snos_Tag.value} и удалить все мои личные письма с его страницы.",
        f"Добрый день, поддержка Telegram! Пользователь {Snos_Tag.value} создал фейковый аккаунт с моими фото и личными данными. На этой странице он публикует клеветнические и оскорбительные заявления, наносящие ущерб моей репутации и моральному состоянию. Я считаю эти действия злонамеренными и требую их немедленного прекращения. Прошу вас заблокировать учетную запись {Snos_Tag.value} и удалить все мои личные сведения с фейкового аккаунта.",
        f"Уважаемый Telegram! Я хочу сообщить о пользователе {Snos_Tag.value}, который опубликовал в своем канале мои детские фотографии без моего согласия. Эти снимки являются неприкосновенной частью моей жизни, и их распространение без моего ведома нарушает мое право на неприкосновенность частной жизни. Прошу вас заблокировать аккаунт {Snos_Tag.value} и удалить все мои детские фотографии с его страницы.",
        f"Здравствуйте, команда Telegram! Я столкнулась с ужасной ситуацией, где пользователь {Snos_Tag.value} угрожает опубликовать мои интимные видеозаписи, если я не заплачу ему выкуп. Это акт шантажа и нарушения моей неприкосновенности частной жизни. Я опасаюсь за свою безопасность и прошу вас незамедлительно вмешаться. Прошу вас заблокировать аккаунт {Snos_Tag.value} и удалить все мои интимные видеозаписи с его страницы.",
        f"Обращаюсь к вам с жалобой на пользователя {Snos_Tag.value}, который разгласил в своем канале мои данные о местоположении, включая домашний адрес и места, где я часто бываю. Такое поведение подвергает мою жизнь и жизнь моих близких опасности. Я считаю, что {Snos_Tag.value} действует с умыслом причинить мне вред, и требую его немедленной блокировки. Прошу вас удалить все мои личные данные с его страницы.",
        f"Уважаемые специалисты Telegram! Я пишу, чтобы сообщить о пользователе {Snos_Tag.value}, который получил доступ к моей личной переписке в мессенджере и публикует ее на своей странице без моего согласия. Эта переписка содержит конфиденциальные разговоры с моими коллегами, друзьями и деловыми партнерами. Я считаю, что действия {Snos_Tag.value} являются злонамеренными и нарушают мое право на неприкосновенность частной жизни. Убедительно прошу вас принять меры против {Snos_Tag.value} и удалить все мои личные сообщения с его страницы.",
        f"Здравствуйте, уважаемые сотрудники Telegram! Пользователь {Snos_Tag.value} разместил на своей странице мои авторские статьи и разработки, защищенные авторским правом, без моего согласия. Такие действия нарушают мои авторские права и наносят ущерб моему бизнесу. Прошу вас заблокировать аккаунт {Snos_Tag.value} и удалить весь мой контент с его страницы.",
        f"Обращаюсь к вам с жалобой на действия пользователя {Snos_Tag.value}. Этот человек распространяет на своей странице мои коммерческие секреты, включая информацию о нашей ценовой политике, стратегии развития и планах на будущее. Это ставит под угрозу наш бизнес и может привести к серьезным финансовым потерям. Убедительно прошу вас принять меры против {Snos_Tag.value} и удалить все мои коммерческие секреты с его страницы.",
        f"Добрый день, специалисты Telegram! Несколько дней назад пользователь {Snos_Tag.value} начал размещать на своей странице мои конфиденциальные деловые документы, включая договоры с клиентами и финансовые отчеты. Я считаю это грубым нарушением моей деловой репутации и требую немедленного вмешательства. Прошу вас заблокировать учетную запись {Snos_Tag.value} и удалить все мои деловые документы с его страницы.",
        f"Уважаемая команда Telegram! Я обнаружила, что пользователь {Snos_Tag.value} публикует на своем канале мои личные фото и видео, которые я никогда не размещала в открытом доступе. Это грубое нарушение моего права на неприкосновенность частной жизни и причиняет мне моральный ущерб. Прошу вас принять меры против {Snos_Tag.value} и удалить все мои личные фото и видео с его страницы.",
        f"Обращаюсь к вам с просьбой о помощи. Пользователь {Snos_Tag.value} уже неделю как распространяет в своих постах мои сообщения из электронной почты. Эти сообщения содержат конфиденциальную переписку с моими деловыми партнерами и клиентами. Их публикация наносит ущерб моей репутации и может привести к потере доверия со стороны моих партнеров. Убедительно прошу вас заблокировать аккаунт {Snos_Tag.value} и удалить все мои сообщения из электронной почты с его страницы.",
        f"Уважаемые сотрудники Telegram! Пользователь {Snos_Tag.value} разместил на своей странице мои конфиденциальные данные о здоровье, включая результаты анализов и диагноз, без моего согласия. Такие действия нарушают мои права на неприкосновенность частной жизни и могут нанести мне непоправимый вред. Прошу вас заблокировать аккаунт {Snos_Tag.value} и удалить все мои медицинские данные с его страницы.",
        f"Обращаюсь к вам с жалобой на действия пользователя {Snos_Tag.value}. Этот человек распространяет на своей странице мои личные фотографии, которые я никогда не публиковал в открытом доступе. Это грубое нарушение моего права на неприкосновенность частной жизни и причиняет мне моральный ущерб. Убедительно прошу вас принять меры против {Snos_Tag.value} и удалить все мои личные фотографии с его страницы.",
        f"Добрый день, специалисты Telegram! Несколько дней назад пользователь {Snos_Tag.value} начал размещать на своей странице мои закрытые финансовые документы, включая выписки с банковских счетов и налоговые декларации. Я считаю это грубым нарушением моей финансовой конфиденциальности и требую немедленного вмешательства. Прошу вас заблокировать учетную запись {Snos_Tag.value} и удалить все мои финансовые документы с его страницы.",
        f"Уважаемая команда Telegram! Я обнаружила, что пользователь {Snos_Tag.value} публикует на своем канале мои личные дневниковые записи без моего согласия. Эти записи содержат мои самые сокровенные мысли и переживания. Их публикация приносит мне огромные страдания и разрушает мою жизнь. Убедительно прошу вас заблокировать аккаунт {Snos_Tag.value} и удалить все мои дневниковые записи с его страницы.",
        f"Обращаюсь к вам с просьбой о помощи. Пользователь {Snos_Tag.value} уже неделю как распространяет в своих постах мои личные письма и открытки. Эти письма содержат конфиденциальную переписку с моими близкими людьми. Их публикация нарушает мое право на частную жизнь и причиняет мне моральный ущерб. Убедительно прошу вас заблокировать аккаунт {Snos_Tag.value} и удалить все мои личные письма с его страницы.",
        f"Добрый день, поддержка Telegram! Пользователь {Snos_Tag.value} создал фейковый аккаунт с моими фото и личными данными. На этой странице он публикует клеветнические и оскорбительные заявления, наносящие ущерб моей репутации и моральному состоянию. Я считаю эти действия злонамеренными и требую их немедленного прекращения. Прошу вас заблокировать учетную запись {Snos_Tag.value} и удалить все мои личные сведения с фейкового аккаунта.",
        f"Уважаемый Telegram! Я хочу сообщить о пользователе {Snos_Tag.value}, который опубликовал в своем канале мои детские фотографии без моего согласия. Эти снимки являются неприкосновенной частью моей жизни, и их распространение без моего ведома нарушает мое право на неприкосновенность частной жизни. Прошу вас заблокировать аккаунт {Snos_Tag.value} и удалить все мои детские фотографии с его страницы.",
        f"Здравствуйте, команда Telegram! Я столкнулась с ужасной ситуацией, где пользователь {Snos_Tag.value} угрожает опубликовать мои интимные видеозаписи, если я не заплачу ему выкуп. Это акт шантажа и нарушения моей неприкосновенности частной жизни. Я опасаюсь за свою безопасность и прошу вас незамедлительно вмешаться. Прошу вас заблокировать аккаунт {Snos_Tag.value} и удалить все мои интимные видеозаписи с его страницы.",
        f"Обращаюсь к вам с жалобой на пользователя {Snos_Tag.value}, который разгласил в своем канале мои данные о местоположении, включая домашний адрес и места, где я часто бываю. Такое поведение подвергает мою жизнь и жизнь моих близких опасности. Я считаю, что {Snos_Tag.value} действует с умыслом причинить мне вред, и требую его немедленной блокировки. Прошу вас удалить все мои личные данные с его страницы.",
        f"Уважаемые специалисты Telegram! Я пишу, чтобы сообщить о пользователе {Snos_Tag.value}, который получил доступ к моей личной переписке в мессенджере и публикует ее на своей странице без моего согласия. Эта переписка содержит конфиденциальные разговоры с моими коллегами, друзьями и деловыми партнерами. Я считаю, что действия {Snos_Tag.value} являются злонамеренными и нарушают мое право на неприкосновенность частной жизни. Убедительно прошу вас принять меры против {Snos_Tag.value} и удалить все мои личные сообщения с его страницы.",
        f"Здравствуйте, уважаемые сотрудники Telegram! Пользователь {Snos_Tag.value} разместил на своей странице мои авторские статьи и разработки, защищенные авторским правом, без моего согласия. Такие действия нарушают мои авторские права и наносят ущерб моему бизнесу. Прошу вас заблокировать аккаунт {Snos_Tag.value} и удалить весь мой контент с его страницы.",
        f"Обращаюсь к вам с жалобой на действия пользователя {Snos_Tag.value}. Этот человек распространяет на своей странице мои коммерческие секреты, включая информацию о нашей ценовой политике, стратегии развития и планах на будущее. Это ставит под угрозу наш бизнес и может привести к серьезным финансовым потерям. Убедительно прошу вас принять меры против {Snos_Tag.value} и удалить все мои коммерческие секреты с его страницы.",
        f"Добрый день, специалисты Telegram! Несколько дней назад пользователь {Snos_Tag.value} начал размещать на своей странице мои конфиденциальные деловые документы, включая договоры с клиентами и финансовые отчеты. Я считаю это грубым нарушением моей деловой репутации и требую немедленного вмешательства. Прошу вас заблокировать учетную запись {Snos_Tag.value} и удалить все мои деловые документы с его страницы.",
        f"Уважаемая команда Telegram! Я обнаружила, что пользователь {Snos_Tag.value} публикует на своем канале мои личные фото и видео, которые я никогда не размещала в открытом доступе. Это грубое нарушение моего права на неприкосновенность частной жизни и причиняет мне моральный ущерб. Прошу вас принять меры против {Snos_Tag.value} и удалить все мои личные фото и видео с его страницы.",
        f"Обращаюсь к вам с просьбой о помощи. Пользователь {Snos_Tag.value} уже неделю как распространяет в своих постах мои сообщения из электронной почты. Эти сообщения содержат конфиденциальную переписку с моими деловыми партнерами и клиентами. Их публикация наносит ущерб моей репутации и может привести к потере доверия со стороны моих партнеров. Убедительно прошу вас заблокировать аккаунт {Snos_Tag.value} и удалить все мои сообщения из электронной почты с его страницы.",
        f"Hey there, guys from Telegram! I'm writing to complain about this user {Snos_Tag.value} who's been illegally sharing my personal info, like my home address and email. Could you please block their account right away?",
        f"I'm asking for {Snos_Tag.value}'s account to be blocked for sharing my phone number and home address without my permission. This is seriously invading my privacy and putting me in danger.",
        f"Also, I'd like to report {Snos_Tag.value} again for posting my personal info like my bank details and address, which is really threatening to my safety and finances.",
        f"And one more thing - {Snos_Tag.value} is posting my photos, messages, and phone number without permission, which is a huge threat to my privacy and well-being. Could you do something about it?",
        f"Finally, I want to emphasize that {Snos_Tag.value} should be blocked for posting my medical records and test results, as this is a serious violation of my privacy that could harm my health.I'm asking you guys to do something about {Snos_Tag.value}. He's been leaking my personal info, including my private messages and photos. That's so wrong and it violates my privacy rights.",
        f"Also, I keep getting harassed by {Snos_Tag.value} online. He keeps spreading lies about me and my whereabouts, which is making me really anxious. Can you please ban his account right away?",
        f"Hey there, Telegram team, I need some help. {Snos_Tag.value} is threatening to release confidential info about my family unless I do what he wants. That's a serious security risk, and it's illegal. Could you please take action and ban him?",
        f"Lastly, {Snos_Tag.value} has been blackmailing me with threats to leak my intimate photos. It's totally unacceptable and against the law. Please do something about it right away and ban his account.Hey there, I'm writing to complain about {Snos_Tag.value}. They've created a fake account using my information and are spreading lies about me online. It's defamation and it's really messing with my privacy. Can you please take some action to protect me?",
        f"Also, I want to report {Snos_Tag.value} for sharing my personal info without permission. They're publishing screenshots of my private messages and that's not cool. It's a serious invasion of privacy and it's hurting my reputation. Can you help me out with that too?",
        f"And lastly, {Snos_Tag.value} is sharing my personal details online, like my address and SSN. That's illegal and it could lead to identity theft. It's making me really scared and uncomfortable. Can you do something about that too? Thanks in advance!Hey there, I'm writing to you about a situation I've been facing with {Snos_Tag.value}. They're using my personal photos to create fake accounts and posting offensive stuff in my name. It's really messing up my reputation and making me feel stressed out.",
        f"Also, I've received threats from {Snos_Tag.value} saying they'll post some compromising videos if I don't do what they want. That's blackmail and I'm scared for my safety.",
        f"There's also this account {Snos_Tag.value} which is using my data to set up phishing websites. They're trying to get my personal info and that's illegal. It could lead to identity theft and fraud.",
        f"And then there was this doxing incident by {Snos_Tag.value} where they revealed my home address and phone number, as well as my family's personal info. That's a serious privacy violation that could put me and my loved ones in danger.Hey there, Telegram team! I'm reaching out about this user {Snos_Tag.value}. They're spreading my personal info, like my race and religion, which is creating a hostile environment for me and others.",
        f"They also publish my private info with false accusations, damaging my reputation and putting me at risk of public shaming. I've even noticed they've created a fake account using my details and are sending harassing messages to others. It's a clear case of fraud, and it's making me worry about my safety.",
        f"Can you please take action against this user? They're violating my privacy and I need your help to stop them. Thanks in advance!Hey there! I'm reaching out about this user {Snos_Tag.value} who's been blackmailing me with personal photos and stuff. It's a real invasion of my privacy, and it's causing me a lot of stress. Can you please block this person's account?",
        f"Also, there's this other account {Snos_Tag.value} that keeps posting false info about my whereabouts, which could put me in danger. Could you look into that too?",
        f"And another thing - this {Snos_Tag.value} guy is sharing my medical info, like diagnoses and results, which is totally illegal and violates my right to privacy. Would you mind investigating that too?",
        f"Lastly, this {Snos_Tag.value} person is posting my passport info, photos, and family stuff on their channel, which is so disrespectful. Can we get this guy banned?",
        f"Thanks in advance for your help!I'm asking you to ban the account of {Snos_Tag.value} because they're spreading rumors about my legal issues and court cases, which is violating my rights and preventing me from being reintegrated into society.",
        f"Also, I'm complaining about {Snos_Tag.value}'s actions. They illegally accessed and published my bank records and tax info, which could lead to financial loss and trouble with the IRS.",
        f"Finally, I want to report {Snos_Tag.value} for posting confidential recordings of my conversations and emails, which are seriously violating my privacy and communication rights.",
        f"Hi there, my name's Ivan and I'm being harassed by {Snos_Tag.value}. They're sharing my personal info, including my number, address, and credit card details. It's making me feel unsafe and I need your help to ban this user.Hey there, I'm writing to you as a concerned user of Telegram. I want to report a serious breach of privacy by the user {Snos_Tag.value}. They have been sharing my personal photos and messages without my permission, which is a violation of my privacy rights. Could you please take action and block this account immediately?",
        f"Hey there, my name is Julia and I'm really upset about the way user {Snos_Tag.value} has been posting my private information online. They've shared my passport number, health records, and employment history, which is completely unacceptable. I'm afraid for my safety and my reputation, so could you please help me out?",
        f"Hi there, I wanted to let you know about a situation that has me really worried. User {Snos_Tag.value} shared my phone number and home address online, and now I'm getting a lot of unwanted calls and messages. It's really annoying and scary, and I need your help to deal with this. Can you please block this user and help me figure out what to do?",
        f"Hello there, this is Anna speaking. I have a complaint about user {Snos_Tag.value} who shared my personal information publicly in a chat. Now, anyone can see my contact details, which makes me feel unsafe. Please block this user immediately and let me know how I can proceed.Hey there, Telegram folks, it's Max here. I'm getting harassed by a user named {Snos_Tag.value}. They've posted pictures of me at work, read my private messages with family, and even found details about my bank account. I need you guys to do something about it and protect my privacy ASAP.",
        f"Telegram, I'm writing to complain about {Snos_Tag.value} who's been leaking my personal info. They have my home address, phone numbers, and bank details - this is a serious threat to my safety and finances. Can you please block this user and help me investigate?",
        f"Support team, {Snos_Tag.value} has been sharing my personal info like my full name, birthday, and email. This is so violating my privacy and I want them to stop immediately. Please block their account and start an investigation.Hey there, I'm writing to complain about this guy {Snos_Tag.value}. He's been leaking my private info, like my work history and salary, and it's really messed up. It could ruin my career, so I need you guys to take him down ASAP.",
        f"Also, another user, {Snos_Tag.value}, is posting my personal messages with friends and family. That's so wrong and disrespectful, and I'm feeling really hurt by it. Can you please block them and help me sort this out?",
        f"Finally, there's this other person, {Snos_Tag.value} who's sharing my private photos and videos. That's totally inappropriate and wrong, and it's causing me a lot of distress. Can you help me stop them? Thanks in advance for your help!I'm filing a complaint about this guy {Snos_Tag.value} who posted some personal stuff I shared with my doctor online. That's a big no-no, man. It's illegal to share private medical info without permission. It could seriously hurt my health if people find out. Can you guys please block this guy and make sure he gets in trouble?"
        ]

        contact = [
            "+79967285422",
            "+79269736273",
            "+79963668355",
            "+79661214909",
            "+79254106650",
            "+79269069196",
            "+79315894431",
            "+79621570718",
            "+79867238675",
            "+79033711373",
            "+79533953258",
            "+79064584010",
            "+79038092452",
            "+79521188823",
            "+79838644127",
            "+79835359331",
            "+79505439173",
            "+79016118684",
            "+79047696829",
            "+79526758975",
            "+79868892975",
            "+79528755667",
            "+79524094589",
            "+79838075754",
            "+79533539187",
            "+79016244929",
            "+79019113582",
            "+79508953716",
            "+79519911023",
            "+79865765940",
            "+79866794388",
            "+79524606513",
            "+79021034453",
            "+79832055591",
            "+79065276189",
            "+79085238579",
            "+79053555112",
            "+79514185646",
            "+79524648058",
            "+79802057486",
            "+79537057668",
            "+79809294592",
            "+79065328918",
            "+79516054166",
            "+79838569719",
            "+79058655468",
            "+79056843341",
            "+79835348173",
            "+79013637173",
            "+79083688238",
            "+79837871337",
            "+79863631697",
            "+79024406958",
            "+79837482542",
            "+79839795796",
            "+79025097886",
            "+79831781122",
            "+79024179155",
            "+79525801970",
            "+79019916162",
            "+79864355726",
            "+79068195131",
            "+79521577989",
            "+79531345614",
            "+79061106981",
            "+79024309449",
            "+79534464624",
            "+79515491847",
            "+79801981414",
            "+79803897072",
            "+79504673069",
            "+79507972723",
            "+79043151270",
            "+79058205698",
            "+79861304316",
            "+79014038949",
            "+79041211288",
            "+79806225329",
            "+79501216565",
            "+79809898545",
            "+79062464037",
            "+79063527713",
            "+79062137218",
            "+79862824613",
            "+79021223176",
            "+79521245370",
            "+79037313374",
            "+79039668710",
            "+79015396857",
            "+79018068194",
            "+79043984229",
            "+79017931058",
            "+79804605493",
            "+79503279310",
            "+79091791410",
            "+79833836114",
            "+79512531957",
            "+79011237140",
            "+79049744481",
            "+79839422161",
            "+79531751199",
            "+79804031176",
            "+79807867434",
            "+79033144225",
            "+79837701759",
            "+79832407224",
            "+79505116666",
            "+79099127394"
        ]

        def Snos_Send():
            chosen_text = random.choice(text)
            chosen_contact = random.choice(contact)
            send_complaint(chosen_text, chosen_contact)
            time.sleep(Snos_time.value)
        for _ in range(int(Snos_value.value)):
            Snos_Send()
            

def main(page: ft.Page):
    page.fonts = {
        "PT Mono": "/Fonts/PTM55F.ttf"
    }
    page.theme = ft.Theme(font_family="PT Mono")
    page.bgcolor = Theme_bg
    page.window.width = 1400
    page.title = "XTOOL"
    page.scroll = ft.ScrollMode.HIDDEN
    page.window.height = 800
    page.window.resizable = False
    page.add(Title_container, Progress_container, Button_List, Module_List)
    global update
    global changer_Theme_bg
    def changer_Theme_bg():
        page.bgcolor = Theme_bg
    def update():
        jobs_successful_txt.update()
        page.update()
        


ft.app(main, assets_dir="Source")