from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.db import migrations

from datetime import datetime, timedelta
import time

def new_catalog(apps, schema_editor):

    # Суперпользователь id=1
    user = User.objects.create_superuser(username='root',
    email='shop260222@mail.ru',
    password='SsNn5678+-@')
    print("Суперпользователь создан")
    
    # Группа менеджеров
    managers = Group.objects.get_or_create(name = 'Managers')
    managers = Group.objects.get(name='Managers')
    print("Группа менеджеров создана")
    
    # Пользователь с ролью менеджера id=2
    user = User.objects.create_user(username='manager', password='Ss0066+-')
    managers.user_set.add(user)
    print("Менеджер добавлен в группу менеджеров")

    # Простые пользователи id=3...27 
    user = User.objects.create_user(username='user1', password='Uu0066+-', email='user1@mail.ru', first_name='Дина', last_name='Мусина')
    user = User.objects.create_user(username='user2', password='Uu0066+-', email='user2@mail.ru', first_name='Адия', last_name='Жунусова')
    user = User.objects.create_user(username='user3', password='Uu0066+-', email='user3@mail.ru', first_name='Айнура', last_name='Кенина')
    user = User.objects.create_user(username='user4', password='Uu0066+-', email='user4@mail.ru', first_name='Рустем', last_name='Какимов')
    user = User.objects.create_user(username='user5', password='Uu0066+-', email='user5@mail.ru', first_name='Алишер', last_name='Кабдуалиев')
    user = User.objects.create_user(username='user6', password='Uu0066+-', email='user6@mail.ru', first_name='Бауржан', last_name='Арыкбаев')
    user = User.objects.create_user(username='user7', password='Uu0066+-', email='user7@mail.ru', first_name='Алишер', last_name='Танатаров')
    user = User.objects.create_user(username='user8', password='Uu0066+-', email='user8@mail.ru', first_name='Мерует', last_name='Искакова')
    user = User.objects.create_user(username='user9', password='Uu0066+-', email='user9@mail.ru', first_name='Ольга', last_name='Муравьева')
    user = User.objects.create_user(username='user10', password='Uu0066+-', email='user10@mail.ru', first_name='Ақжарқын', last_name='Сансызбаева')
    user = User.objects.create_user(username='user11', password='Uu0066+-', email='user11@mail.ru', first_name='Арайлым', last_name='Алматова')
    user = User.objects.create_user(username='user12', password='Uu0066+-', email='user12@mail.ru', first_name='Айгерім', last_name='Дүйсенбиева')
    user = User.objects.create_user(username='user13', password='Uu0066+-', email='user13@mail.ru', first_name='Салтанат', last_name='Зиноллаева')
    user = User.objects.create_user(username='user14', password='Uu0066+-', email='user14@mail.ru', first_name='Сейтқасым', last_name='Болат')
    user = User.objects.create_user(username='user15', password='Uu0066+-', email='user15@mail.ru', first_name='Сара', last_name='Фазилова')
    user = User.objects.create_user(username='user16', password='Uu0066+-', email='user16@mail.ru', first_name='Бектас', last_name='Ерсейіт')
    user = User.objects.create_user(username='user17', password='Uu0066+-', email='user17@mail.ru', first_name='Диас', last_name='Мырзаш')
    user = User.objects.create_user(username='user18', password='Uu0066+-', email='user18@mail.ru', first_name='Нұржан', last_name='Жүрсінбек')
    user = User.objects.create_user(username='user19', password='Uu0066+-', email='user19@mail.ru', first_name='Дина', last_name='Жағыпар')
    user = User.objects.create_user(username='user20', password='Uu0066+-', email='user20@mail.ru', first_name='Жастілек', last_name='Жасталап')
    user = User.objects.create_user(username='user21', password='Uu0066+-', email='user21@mail.ru', first_name='Еркебұлан', last_name='Қадыхан')
    user = User.objects.create_user(username='user22', password='Uu0066+-', email='user22@mail.ru', first_name='Молдир', last_name='Бутабекова')
    user = User.objects.create_user(username='user23', password='Uu0066+-', email='user23@mail.ru', first_name='Аружан', last_name='Таурбекова')
    user = User.objects.create_user(username='user24', password='Uu0066+-', email='user24@mail.ru', first_name='Алтынай', last_name='Қожанова')
    user = User.objects.create_user(username='user25', password='Uu0066+-', email='user25@mail.ru', first_name='Эльнара', last_name='Иминова')
    print("Созданы простые пользователи")

    ##### Организации #####

    Organization = apps.get_model("product", "Organization")

    organization = Organization()
    organization.title='LG Electronics Almaty Kazakhstan'
    organization.address='просп. Абая 42, Алматы 050040'
    organization.phone='8 (727) 346 7837'
    organization.save()

    organization = Organization()
    organization.title='ТОО Самсунг Электроникс Центральная Евразия'
    organization.address='Проспект Аль-Фараби здание 36, блок Б, 3 этаж., Алматы 050059'
    organization.phone='+77273211212'
    organization.save()

    organization = Organization()
    organization.title='ТОО «Хуавей Текнолоджиз Казахстан»'
    organization.address='пр. Достык 210Б, блок 1, 11 этаж, БЦ «KOKTEM GRAND» 050051; г. Алматы'
    organization.phone='+7 (727) 344 09 99'
    organization.save()

    organization = Organization()
    organization.title='STN distribution'
    organization.address='Казахстан, 050012, Алматы,  ул.Муратбаева, д.180, оф.201, БЦ "Гермес"'
    organization.phone='+7 (727) 333 0 999'
    organization.save()

    organization = Organization()
    organization.title='Lenovo Shop Kazakhstan'
    organization.address='Республика Казахстан, 050060г. Алматы, ул. Тажибаевой 184, офис 104'
    organization.phone='+7 (705) 674-89-09'
    organization.save()

    organization = Organization()
    organization.title='Canon Ru'
    organization.address='г. Алматы, Казахстан, проспект Аль-Фараби 7, БЦ "Нурлы-тау"'
    organization.phone='+7 727 277 77 95'
    organization.save()

    organization = Organization()
    organization.title='HP inc.'
    organization.address='77/7, Al-Farabi Ave., 6th Floor (West Wing) P.C. 050040 Almaty Kazakhstan'
    organization.phone='+7-727-356-2180'
    organization.save()

    organization = Organization()
    organization.title='ТОО АСБИС Казахстан'
    organization.address='050018, Республика Казахстан, г. Алматы, Жетысуский район, ул. Тюлькубасская, дом 2'
    organization.phone='+7 727 390 46 06'
    organization.save()

    print("Организации добавлены")

    ##### Приходные накладные  #####

    Invoice = apps.get_model("product", "Invoice")
    
    invoice = Invoice()
    invoice.organization_id = 4
    invoice.datei = datetime.now() - timedelta(days=45)
    invoice.numb = 1
    invoice.save()

    invoice = Invoice()
    invoice.organization_id = 2
    invoice.datei = datetime.now() - timedelta(days=44)
    invoice.numb = 2
    invoice.save()

    invoice = Invoice()
    invoice.organization_id = 8
    invoice.datei = datetime.now() - timedelta(days=43)
    invoice.numb = 3
    invoice.save()

    invoice = Invoice()
    invoice.organization_id = 4
    invoice.datei = datetime.now() - timedelta(days=42)
    invoice.numb = 4
    invoice.save()

    invoice = Invoice()
    invoice.organization_id = 8
    invoice.datei = datetime.now() - timedelta(days=41)
    invoice.numb = 5
    invoice.save()

    print("Приходные накладные добавлены")

    ##### Категория товара #####

    Category = apps.get_model("product", "Category")

    category = Category()
    category.title='Смартфон'   
    category.save()

    category = Category()
    category.title='Кнопочный телефон'   
    category.save()

    category = Category()
    category.title='Смарт-часы'   
    category.save()

    category = Category()
    category.title='Наушники'   
    category.save()

    category = Category()
    category.title='Планшет'   
    category.save()

    category = Category()
    category.title='Электронная книга'   
    category.save()

    print("Категория товара добавлена")

    ##### Каталог товаров #####
    
    Catalog = apps.get_model("product", "Catalog")

    catalog = Catalog()
    catalog.invoice_id = 1
    catalog.code='159421'
    catalog.category_id=1
    catalog.title='Смартфон Tecno POP 5, 32Gb, Ice Lake Green (BD2p)'
    catalog.info='Смартфон POP 5 оснащен классическим экраном 6.1" HD+ с выемкой в виде точки для более широкого обзора и удобства просмотра. Экран смартфона POP 5 также обладает сверхвысоким разрешением (720x1560), что обеспечивает более четкое и впечатляющее изображение.'
    catalog.details='Размер экрана, дюйм: 6.1; Разрешение экрана: 1560 x 720; Тип матрицы: IPS; Объем оперативной памяти: 2 Гб; Объем встроенной памяти: 32 Гб; Модель процессора: SC7731e; Частота процессора: 1.3 ГГц; Основная камера, Мп: 5; Фронтальная камера, Мп: 5; Беспроводные интерфейсы: Wi-Fi, Bluetooth; Емкость аккумулятора: 5000 мАч'
    catalog.price=38990
    catalog.quantity=10
    #catalog.photo='images/Tecno_POP_5_32Gb_Ice_Lake_Green_BD2p.jpg'
    catalog.photo='images/product01.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 1
    catalog.code='151551'
    catalog.category_id=1
    catalog.title='Смартфон Tecno POP 4 Pro, 16Gb, Cosmic Shine (BC3)'
    catalog.info='В телефоне POP 4 Pro используется классический экран с каплевидным вырезом диагональю 6.52 дюйма. Большой размер дисплея и идеальное соотношение размеров экрана и корпуса позволяют достичь лучшего качества отображения.'
    catalog.details='Размер экрана, дюйм: 6.52; Разрешение экрана: 1200 x 540; Объем оперативной памяти: 1 Гб; Объем встроенной памяти: 16 Гб; Модель процессора: MT6739WA; Частота процессора: 1.25 ГГц; Основная камера, Мп: 8; Фронтальная камера, Мп: 8; Беспроводные интерфейсы: Wi-Fi, Bluetooth; Емкость аккумулятора: 5000 мАч'
    catalog.price=39990
    catalog.quantity=10
    #catalog.photo='images/Tecno_POP_4_Pro_16Gb_Cosmic_Shine_BC3.jpg'
    catalog.photo='images/product02.jpg'
    catalog.save()
    print(catalog.id)
    
    catalog = Catalog()
    catalog.invoice_id = 1
    catalog.code='151555'
    catalog.category_id=1
    catalog.title='Смартфон Tecno Spark 6, 64Gb, Comet Black (KE7)'
    catalog.info='Вычислительная мощность центрального процессора увеличилась на 60%, производительность графического процессора увеличилась на 26%. Мощный процессор обеспечивает стабильную и плавную работу устройства, о которой вы даже не догадывались, и гарантирует, что игры станут еще одним невероятным удовольствием.'
    catalog.details='Размер экрана, дюйм: 6.8; Разрешение экрана: 1640 x 720 [20.5:9]; Тип матрицы: IPS; Объем оперативной памяти: 4 Гб; Объем встроенной памяти: 64 Гб; Модель процессора: Helio G70; Частота процессора: 2 ГГц + 1.7 ГГц; Основная камера, Мп: 16 + 2 + 2 + 2; Фронтальная камера, Мп: 8; Беспроводные интерфейсы: Wi-Fi, Bluetooth; Емкость аккумулятора: 5000 мАч'
    catalog.price=64990
    catalog.quantity=10
    #catalog.photo='images/Tecno_Spark_6_64Gb_Comet_Black_KE7.jpg'
    catalog.photo='images/product03.jpg'
    catalog.save()
    print(catalog.id)
    
    catalog = Catalog()
    catalog.invoice_id = 1
    catalog.code='149582'
    catalog.category_id=1
    catalog.title='Смартфон Tecno POP 2F, 16Gb, Midnight Black (B1f)'
    catalog.info='Благодаря 16 ГБ памяти у вас будет больше места для хранения ваших любимых и драгоценных воспоминаний. Расширение хранилища - отличный шаг к достижению высочайшей производительности, предлагая потрясающий пользовательский интерфейс'
    catalog.details='Размер экрана, дюйм: 5.5; Разрешение экрана: 960 x 480 [18:9]; Объем оперативной памяти: 1 Гб; Объем встроенной памяти: 16 Гб; Модель процессора: MT6582; Частота процессора: 1.3 ГГц; Основная камера, Мп: 5; Фронтальная камера, Мп: 8; Беспроводные интерфейсы: Wi-Fi, Bluetooth; Емкость аккумулятора: 2400 мАч'
    catalog.price=27990
    catalog.quantity=10
    #catalog.photo='images/Tecno_POP_2F_16Gb_Midnight_Black_B1f.jpg'
    catalog.photo='images/product04.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 1
    catalog.code='151549'
    catalog.category_id=1
    catalog.title='Смартфон Tecno POP 3, 16Gb, Sandstone Black (BB2)'
    catalog.info='Благодаря 16 ГБ ПЗУ у вас будет больше места для хранения ваших любимых воспоминаний и важных файлов. Меньше беспокойства о частой уборке, чтобы освободить место. Практичный и как всегда отличный.'
    catalog.details='Размер экрана, дюйм: 5.7; Разрешение экрана: 960 x 480 [18:9]; Тип матрицы: TN; Объем оперативной памяти: 1 Гб; Объем встроенной памяти: 16 Гб; Модель процессора: MT6580; Частота процессора: 1.3 ГГц; Основная камера, Мп: 5; Фронтальная камера, Мп: 8; Беспроводные интерфейсы: Wi-Fi, Bluetooth; Емкость аккумулятора: 3500 мАч'
    catalog.price=28990
    catalog.quantity=10
    #catalog.photo='images/Tecno_POP_3_16Gb_Sandstone_Black_BB2.jpg'
    catalog.photo='images/product05.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 2
    catalog.code='159457'
    catalog.category_id=1
    catalog.title='Смартфон Samsung Galaxy A03 Core, 32Gb, Black (SM-A032F)'
    catalog.info='Расширьте границы доступного с 6.5-дюймовым экраном с V-образным вырезом. Благодаря технологии HD+ дисплей Galaxy A03 Core демонстрирует яркую, четкую и чистую картинку.'
    catalog.details='Размер экрана, дюйм: 6.5; азрешение экрана: 1600 x 720 [20:9]; Объем оперативной памяти: 2 Гб; Объем встроенной памяти: 32 Гб; Модель процессора: SC9863A; Частота процессора: 1.6 ГГц + 1.2 ГГц; Основная камера, Мп: 8; Фронтальная камера, Мп: 5;Беспроводные интерфейсы: Wi-Fi, Bluetooth; Емкость аккумулятора: 5000 мАч'
    catalog.price=48990
    catalog.quantity=10
    #catalog.photo='images/Samsung_Galaxy_A03_Core_32Gb_Black_SM-A032F.jpg'
    catalog.photo='images/product06.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 2
    catalog.code='156712'
    catalog.category_id=1
    catalog.title='Смартфон Samsung Galaxy A22, 64Gb, White (SM-A225F)'
    catalog.info='Насладитесь детальным изображением на Super AMOLED 6.4'' Infinity-U экране с разрешением HD+ и яркостью до 600 нит. Благодаря увеличенному экрану вы увидите больше, а сверх плавная прокрутка обеспечивает комфортный просмотр во время игрового сеанса или скроллинга изображения на экране'
    catalog.details='Размер экрана, дюйм: 6.4 / Разрешение экрана: 1600 х 720 [20:9] / Тип матрицы: Super AMOLED / Объем оперативной памяти: 4 Гб / Объем встроенной памяти: 64 Гб / Модель процессора: MT6769V/CTZA / Частота процессора: 2.0 ГГц + 1.8 ГГц / Разрешение основной камеры: 48 Мп + 8 Мп + 2 Мп + 2 Мп / Разрешение фронтальной камеры: 13 Мп / Беспроводные интерфейсы: Wi-Fi; Bluetooth; NFC / Емкость аккумулятора: 5000 мАч'
    catalog.price=90100
    catalog.quantity=10    
    #catalog.photo='images/Samsung_Galaxy_A22_64Gb_White_SM-A225F.jpg'
    catalog.photo='images/product07.jpg'
    catalog.save()
    print(catalog.id)
   
    catalog = Catalog()
    catalog.invoice_id = 2
    catalog.code='153241'
    catalog.category_id=1
    catalog.title='Смартфон Samsung Galaxy A02, 32Gb, Black (SM-A022G)'
    catalog.info='Большой 6.5-дюймовый HD+ экран с V-образным вырезом для камеры создан для и полного погружения в контент.'
    catalog.details='Размер экрана, дюйм: 6.5; Разрешение экрана: 1600 x 720 [20:9]; Тип матрицы: TFT; Объем оперативной памяти: 2 Гб; Объем встроенной памяти: 32 Гб; Модель процессора: MT6739; Частота процессора: 1.5; Основная камера, Мп: 13 + 2; Фронтальная камера, Мп: 5; Беспроводные интерфейсы: Wi-Fi, Bluetooth; Емкость аккумулятора: 5000 мАч'
    catalog.price=53990
    catalog.quantity=10
    #catalog.photo='images/Samsung_Galaxy_A02_32Gb_Black_SM-A022G.jpg'
    catalog.photo='images/product08.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 2
    catalog.code='156722'
    catalog.category_id=1
    catalog.title='Смартфон Samsung Galaxy A12, 32Gb, Blue (SM-A127F)'
    catalog.info='Большой 6.5-дюймовый HD+ экран с V-образным вырезом для камеры создан для полного погружения в контент. Благодаря поддержке технологии HD+ картинка на Galaxy A12 яркая и насыщенная.'
    catalog.details='Размер экрана, дюйм: 6.5; Разрешение экрана: 1600 x 720 [20:9]; Тип матрицы: TFT; Объем оперативной памяти: 3 Гб; Объем встроенной памяти: 32 Гб; Модель процессора: 850; Частота процессора: 2 ГГц; Основная камера, Мп: 48 + 5 + 2 + 2; Фронтальная камера, Мп: 8; Беспроводные интерфейсы: Wi-Fi, Bluetooth, NFC; Емкость аккумулятора: 5000 мАч'
    catalog.price=69990
    catalog.quantity=10
    #catalog.photo='images/Samsung_Galaxy_A12_32Gb_Blue_SM-A127F.jpg'
    catalog.photo='images/product09.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 2
    catalog.code='153441'
    catalog.category_id=1
    catalog.title='Смартфон Samsung Galaxy A32, 64Gb, Awesome Black (SM-A325F)'
    catalog.info='Насладитесь детальным изображением на Super AMOLED 6.4'' Infinity-U экране с разрешением FHD+ и яркостью до 800 нит, которое отлично видно даже при ярком дневном свете. Функция защиты глаз "Eye Comfort Shield" снижает уровень синего свечения, а сверх плавная прокрутка обеспечивает комфортный просмотр во время игрового сеанса или скроллинга изображения на экране.'
    catalog.details='Размер экрана, дюйм: 6.4; Разрешение экрана: 2400 x 1080 [20:9]; Тип матрицы: Super AMOLED; Объем оперативной памяти: 4 Гб; Объем встроенной памяти: 64 Гб; Модель процессора: Helio G80; Частота процессора: 2 ГГц + 1.8 ГГц; Основная камера, Мп: 64 + 8 + 5 + 5; Фронтальная камера, Мп: 20; Беспроводные интерфейсы: Wi-Fi, Bluetooth, NFC; Емкость аккумулятора: 5000 мАч'
    catalog.price=199990
    catalog.quantity=10
    #catalog.photo='images/Samsung_Galaxy_A32_64Gb_Awesome_Black_SM-A325F.jpg'
    catalog.photo='images/product10.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 3
    catalog.code='159919'
    catalog.category_id=1
    catalog.title='Смартфон Xiaomi Redmi 9C, 128Gb, Midnight Gray (M2006C3MG)'
    catalog.info='Смартфон'
    catalog.details='Размер экрана, дюйм: 6.52 / Разрешение экрана: 1600 х 720 [20:9] / Тип матрицы: IPS / Объем оперативной памяти: 4 Гб / Объем встроенной памяти: 64 Гб / Модель процессора: Snapdragon 460 / Частота процессора: 1.8 ГГц / Разрешение основной камеры: 13 Мп + 2 Мп + 2 Мп / Разрешение фронтальной камеры: 8 Мп / Беспроводные интерфейсы: Wi-Fi; Bluetooth / Емкость аккумулятора: 5000 мАч'
    catalog.price=69900
    catalog.quantity=10
    #catalog.photo='images/Xiaomi_Redmi_9C_128Gb_Midnight_Gray_M2006C3MG.jpg'
    catalog.photo='images/product11.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 3
    catalog.code='147507'
    catalog.category_id=1
    catalog.title='Смартфон Xiaomi Redmi 9A, 32Gb, Granite Grey (M2006C3LG)'
    catalog.info='Xiaomi Redmi 9A - версия бюджетного смартфона, главными особенностями которого являются большой экран с диагональю 6.53" и емкий аккумулятор на 5000 мАч. Основная и фронтальная AI камеры (13 Мп и 5 Мп соответственно) позволяют без труда делать прекрасные качественные фотографии.'
    catalog.details='Размер экрана, дюйм: 6.53; Разрешение экрана: 1600 x 720 [20:9]; Объем оперативной памяти: 2 Гб; Объем встроенной памяти: 32 Гб; Модель процессора: Helio G25; Частота процессора: 2.0 ГГц; Основная камера, Мп: 13; Фронтальная камера, Мп: 5; Беспроводные интерфейсы: Wi-Fi, Bluetooth; Емкость аккумулятора: 5000 мАч'
    catalog.price=54990
    catalog.quantity=10
    #catalog.photo='images/Xiaomi_Redmi_9A_32Gb_Granite_Grey_M2006C3LG.jpg'
    catalog.photo='images/product12.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 3
    catalog.code='145755'
    catalog.category_id=1
    catalog.title='Смартфон Xiaomi Redmi Note 9S, 64Gb, Interstellar Grey'
    catalog.info='Таких камер у Xiaomi еще не было. Первым бросается в глаза именно квадратный блок камер. 4 камеры занимают небольшую площадь и гармонично смотрятся в общем дизайне устройства.'
    catalog.details='Размер экрана, дюйм: 6.67; Разрешение экрана: 2400 x 1080 [20:9]; Тип матрицы: IPS; Объем оперативной памяти: 4 Гб; Объем встроенной памяти: 64 Гб; Модель процессора: Snapdragon 720G; Частота процессора: 2.3 ГГц; Основная камера, Мп: 48 + 8 + 5 + 2; Фронтальная камера, Мп: 16; Беспроводные интерфейсы: Wi-Fi, Bluetooth, IrDA; Емкость аккумулятора: 5020 мАч'
    catalog.price=88900
    catalog.quantity=10
    #catalog.photo='images/Xiaomi_Redmi_Note_9S_64Gb_Interstellar_Grey.jpg'
    catalog.photo='images/product13.jpg'
    catalog.save()
    print(catalog.id)
    
    catalog = Catalog()
    catalog.invoice_id = 3
    catalog.code='157496'
    catalog.category_id=1
    catalog.title='Смартфон Xiaomi Redmi 10, 4Gb, 64Gb, Sea Blue (21061119AG)'
    catalog.info='Xiaomi Redmi 10 первый обладатель мощного процессора MediaTek Helio G88. Совершенно новый чип обеспечивает более четкие фотографии и улучшенный игровой процесс.'
    catalog.details='Размер экрана, дюйм: 6.5; Разрешение экрана: 2400 x 1080 [20:9]; Объем оперативной памяти: 4 Гб; Объем встроенной памяти: 64 Гб; Модель процессора: Helio G88; Частота процессора: 2.0 ГГц + 1.8 ГГц; Основная камера, Мп: 50 + 8 + 2 + 2; Фронтальная камера, Мп: 8; Беспроводные интерфейсы: Wi-Fi, Bluetooth, IrDA; Емкость аккумулятора: 5000 мАч'
    catalog.price=89990
    catalog.quantity=10
    #catalog.photo='images/Xiaomi_Redmi_10_4Gb_64Gb_Sea_Blue_21061119AG.jpg'
    catalog.photo='images/product14.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 3
    catalog.code='159921'
    catalog.category_id=1
    catalog.title='Смартфон Xiaomi Redmi Note 11, 64Gb, Twilight Blue (2201117TG)'
    catalog.info='Смартфон'
    catalog.details='Размер экрана, дюйм: 6.43; Разрешение экрана: 2400 x 1080 [20:9]; Тип матрицы: AMOLED; Объем оперативной памяти: 4 Гб; Объем встроенной памяти: 64 Гб; Модель процессора: Snapdragon 680; Частота процессора: 2.4 ГГц + 1.9 ГГц; Основная камера, Мп: 50 + 8 + 2 + 2; Фронтальная камера, Мп: 13; Беспроводные интерфейсы: Wi-Fi, Bluetooth, IrDA; Емкость аккумулятора: 5000 мАч'
    catalog.price=109990
    catalog.quantity=10
    #catalog.photo='images/Xiaomi_Redmi_Note_11_64Gb_Twilight_Blue_2201117TG.jpg'
    catalog.photo='images/product15.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 4
    catalog.code='153536'
    catalog.category_id=1
    catalog.title='Смартфон Meizu M10, 2Gb, 32Gb, Phantom Black (M918H)'
    catalog.info='Смартфон'
    catalog.details='Размер экрана, дюйм: 6.5 / Разрешение экрана: 1600 х 720 [20:9] / Объем оперативной памяти: 2 Гб / Объем встроенной памяти: 32 Гб / Модель процессора: Helio P25 / Частота процессора: 2.5 ГГц / Разрешение основной камеры: 13 Мп + 2 Мп + 2 Мп / Разрешение фронтальной камеры: 8 Мп / Беспроводные интерфейсы: Wi-Fi; Bluetooth / Емкость аккумулятора: 4000 мАч'
    catalog.price=45900
    catalog.quantity=10
    #catalog.photo='images/Meizu_M10_2Gb_32Gb_Phantom_Black_M918H.jpg'
    catalog.photo='images/product16.jpg'
    catalog.save()
    print(catalog.id)
    
    catalog = Catalog()
    catalog.invoice_id = 4
    catalog.code='154927'
    catalog.category_id=1
    catalog.title='Смартфон OPPO A54, 64Gb, Black (CPH2239)'
    catalog.info='3D-корпус с уникальным дизайном задней крышки и тонкой рамкой 0.2 мм не только изящно выглядит, но и удобен при долгом использовании.'
    catalog.details='Размер экрана, дюйм: 6.51; Разрешение экрана: 1600 x 720 [20:9]; Тип матрицы: IPS; Объем оперативной памяти: 4 Гб; Объем встроенной памяти: 64 Гб; Модель процессора: Helio P35; Частота процессора: 2.3 ГГц; Основная камера, Мп: 13 + 2 + 2; Фронтальная камера, Мп: 16; Беспроводные интерфейсы: Wi-Fi, Bluetooth, NFC; Емкость аккумулятора: 5000 мАч'
    catalog.price=94900
    catalog.quantity=10
    #catalog.photo='images/OPPO_A54_64Gb_Black_CPH2239.jpg'
    catalog.photo='images/product17.jpg'
    catalog.save()
    print(catalog.id)
    
    catalog = Catalog()
    catalog.invoice_id = 4
    catalog.code='Артикул '
    catalog.category_id=1
    catalog.title='Смартфон OPPO A74, 128Gb, Black (CPH2219)'
    catalog.info='Продвинутый сканер, встроенный в экран устройства, быстро и с высокой точностью считывает отпечатки пальцев и позволяет разблокировать смартфон одним касанием.'
    catalog.details='Размер экрана, дюйм: 6.43; Разрешение экрана: 2400 x 1080 [20:9]; Тип матрицы: AMOLED; Объем оперативной памяти: 4 Гб; Объем встроенной памяти: 128 Гб; Модель процессора: Snapdragon 662; Частота процессора: 1.8 ГГц + 2 ГГц; Основная камера, Мп: 48 + 2 + 2; Фронтальная камера, Мп: 16; Беспроводные интерфейсы: Wi-Fi, Bluetooth, NFC; Емкость аккумулятора: 5000 мАч'
    catalog.price=119990
    catalog.quantity=10
    #catalog.photo='images/OPPO_A74_128Gb_Black_CPH2219.jpg'
    catalog.photo='images/product18.jpg'
    catalog.save()
    print(catalog.id)
    
    catalog = Catalog()
    catalog.invoice_id = 4
    catalog.code='150469'
    catalog.category_id=1
    catalog.title='Смартфон OPPO Reno4 Lite, 8Gb, Black (CPH2125)'
    catalog.info='Смартфоны серии Reno являются самыми тонкими и легкими в модельном ряду OPPO, корпус таких устройств имеет гладко закругленные края, им очень удобно пользоваться.'
    catalog.details='Размер экрана, дюйм: 6.43; Разрешение экрана: 2400 x 1080 [20:9]; Тип матрицы: Super AMOLED; Объем оперативной памяти: 8 Гб; Объем встроенной памяти: 128 Гб; Модель процессора: Helio P95; Частота процессора: 2.2 ГГц; Основная камера, Мп: 48 + 8 + 2 + 2; Фронтальная камера, Мп: 16 + 2; Беспроводные интерфейсы: Wi-Fi, Bluetooth, NFC; Емкость аккумулятора: 4000 мАч'
    catalog.price=125990
    catalog.quantity=10
    #catalog.photo='images/OPPO_Reno4_Lite_8Gb_Black_CPH2125.jpg'
    catalog.photo='images/product19.jpg'
    catalog.save()
    print(catalog.id)
    
    catalog = Catalog()
    catalog.invoice_id = 4
    catalog.code='154925'
    catalog.category_id=1
    catalog.title='Смартфон OPPO Reno5 Lite, 128Gb, Black (CPH2205)'
    catalog.info='Камера Reno5 Lite с четырьмя объективами и искусственным интеллектом идеально подходит для съемки всех моментов жизни. Reno5 Lite отображает жизненный путь в ярких и кристально чистых деталях - от макросъемки до сверхширокоугольных и зум-снимков.'
    catalog.details='Размер экрана, дюйм: 6.43; Разрешение экрана: 2400 x 1080 [20:9]; Тип матрицы: AMOLED; Объем оперативной памяти: 8 Гб; Объем встроенной памяти: 128 Гб; Модель процессора: Helio P95; Частота процессора: 2.2 ГГц; Основная камера, Мп: 48 + 8 + 2 + 2; Фронтальная камера, Мп: 32; Беспроводные интерфейсы: Wi-Fi, Bluetooth, NFC; Емкость аккумулятора: 4310 мАч'
    catalog.price=139990
    catalog.quantity=10
    #catalog.photo='images/OPPO_Reno5_Lite_128Gb_Black_CPH2205.jpg'
    catalog.photo='images/product20.jpg'
    catalog.save()
    print(catalog.id)
    
    catalog = Catalog()
    catalog.invoice_id = 5
    catalog.code='155256'
    catalog.category_id=2
    catalog.title='Мобильный телефон Nokia 125 DS, Black'
    catalog.info='Мобильный телефон'
    catalog.details='Размер экрана, дюйм: 2.4 / Разрешение экрана: 240 x 320 / Объем встроенной памяти: 4 Мб / Емкость аккумулятора: 1020 мАч'
    catalog.price=13390
    catalog.quantity=10
    #catalog.photo='images/Nokia_125_DS_Black.jpg'
    catalog.photo='images/product21.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 5
    catalog.code='151280'
    catalog.category_id=2
    catalog.title='Мобильный телефон Tecno T454, Champagne Gold'
    catalog.info='Мобильный телефон'
    catalog.details='Размер экрана, дюйм: 2.8 / Разрешение экрана: 240 x 320 / Объем оперативной памяти: 4 Мб / Объем встроенной памяти: 4 Мб / Беспроводные интерфейсы: Bluetooth / Емкость аккумулятора: 1500 мАч'
    catalog.price=7990
    catalog.quantity=10
    #catalog.photo='images/Tecno_T454_Champagne_Gold.jpg'
    catalog.photo='images/product22.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 5
    catalog.code='158563'
    catalog.category_id=2
    catalog.title='Мобильный телефон TeXet TM-122, Black'
    catalog.info='TM-122 – не простой телефон, функции которого ограничиваются звонками и SMS. FM-радио, встроенный плеер и многое другое расширяют спектр применения мобильного устройства и позволяют полноценно реализовать его потенциал при максимуме комфорта.'
    catalog.details='Размер экрана, дюйм: 1.77; Разрешение экрана: 128 x 160; Емкость аккумулятора: 600 мАч'
    catalog.price=4590
    catalog.quantity=10
    #catalog.photo='images/TeXet_TM-122_Black.jpg'
    catalog.photo='images/product23.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 5
    catalog.code='139072'
    catalog.category_id=2
    catalog.title='Мобильный телефон Philips Xenium E109, Red'
    catalog.info='Если вам необходим опережающий моду дизайн для демонстрации вашего стиля, то эта плоская, современная конструкция с высококачественной отделкой не имеет себе равных.'
    catalog.details='Размер экрана, дюйм: 1.77; Разрешение экрана: 128 x 160; Тип матрицы: TFT; Объем оперативной памяти: 32 Мб; Объем встроенной памяти: 32 Мб; Модель процессора: MT6261D; Емкость аккумулятора: 1000 мАч'
    catalog.price=8790
    catalog.quantity=10
    #catalog.photo='images/Philips_Xenium_E109_Red.jpg'
    catalog.photo='images/product24.jpg'
    catalog.save()
    print(catalog.id)

    catalog = Catalog()
    catalog.invoice_id = 5
    catalog.code='149529'
    catalog.category_id=2
    catalog.title='Мобильный телефон Prestigio Muze H1, Black'
    catalog.info='Компактный 2.4-дюймовый телефон с закругленными углами довольно приятно держать в руках. А благодаря небольшим габаритам и весу до 85 грамм он без труда поместится в карман джинсов или куртки. '
    catalog.details='Размер экрана, дюйм: 2.4; Разрешение экрана: 240 x 240; Тип матрицы: TFT; Объем оперативной памяти: 32 Мб; Объем встроенной памяти: 32 Мб; Модель процессора: Spreadtrum SC6531E; Беспроводные интерфейсы: Bluetooth; Емкость аккумулятора: 1400 мАч'
    catalog.price=6590
    catalog.quantity=10
    #catalog.photo='images/Prestigio_Muze_H1_Black.jpg'
    catalog.photo='images/product25.jpg'
    catalog.save()
    print(catalog.id)

    print("Каталог товаров добавлен")

    ##### Продажа + Доставка #####
    
    Sale = apps.get_model("product", "Sale")
    Delivery = apps.get_model("product", "Delivery")

    sale = Sale()
    sale.saleday = datetime.now() - timedelta(days=30)
    sale.catalog_id = 1
    sale.price = 38990
    sale.quantity = 1
    sale.user_id = 3
    sale.rating = 5
    sale.details='Прикольный телефон, всё хорошо работает. Очень хорошо работает камера только в режиме зума, фоткает текстуру ткани детально.'
    sale.save()
    sale.saleday = datetime.now() - timedelta(days=30)
    sale.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.movement = 'Заявка принята в обработку'
    delivery.details='Заявка принята в обработку'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.movement = 'Товар в пути'
    delivery.details='Товар в пути'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.movement = 'Товар на складе'
    delivery.details='Товар на складе'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.movement = 'Заявка закрыта, товар доставлен'
    delivery.details='Заявка закрыта, товар доставлен'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.save()

    ###

    sale = Sale()
    sale.saleday = datetime.now() - timedelta(days=29)
    sale.catalog_id = 1
    sale.price = 38990
    sale.quantity = 1
    sale.user_id = 4
    sale.rating = 4
    sale.details='Шустрый,очень хорошо. Камера дёргается и качество не очень.'
    sale.save()
    sale.saleday = datetime.now() - timedelta(days=29)
    sale.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.movement = 'Заявка принята в обработку'
    delivery.details='Заявка принята в обработку'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.movement = 'Товар в пути'
    delivery.details='Товар в пути'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.movement = 'Товар на складе'
    delivery.details='Товар на складе'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.movement = 'Заявка закрыта, товар доставлен'
    delivery.details='Заявка закрыта, товар доставлен'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.save()

    ###

    sale = Sale()
    sale.saleday = datetime.now() - timedelta(days=28)
    sale.catalog_id = 6
    sale.price = 48990
    sale.quantity = 1
    sale.user_id = 5
    sale.rating = 5
    sale.details='Специально не стала сразу писать отзыв-сначала решила посмотреть в деле. Приятно удивлена: в диапазоне цен до 10 000 рублей считаю это лучший телефон. Покупался дочке на день рождения на 11 лет. Выглядит солидно-но не громоздко. Все игры тянет,вотс ап яндекс музыка, Ютуб детям, родительский контроль-все работает. Звук немного как из ведра-но для ребенка отлично. Громкий-память 32 uu,-более, чем достаточно. Камера четкая: подружек кошечек,видео -все сняли все красиво)'
    sale.save()
    sale.saleday = datetime.now() - timedelta(days=28)
    sale.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.movement = 'Заявка принята в обработку'
    delivery.details='Заявка принята в обработку'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.movement = 'Товар в пути'
    delivery.details='Товар в пути'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.movement = 'Товар на складе'
    delivery.details='Товар на складе'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.movement = 'Заявка закрыта, товар доставлен'
    delivery.details='Заявка закрыта, товар доставлен'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.save()

    ###

    sale = Sale()
    sale.saleday = datetime.now() - timedelta(days=27)
    sale.catalog_id = 6
    sale.price = 48990
    sale.quantity = 1
    sale.user_id = 6
    sale.rating = 5
    sale.details='Работает. Привезли вчера. Долго думала и выбирала. Купила только на основании отзывов. Спасибо всем, кто пишет отзывы. Легко и просто. Разобралась. Вообщем нормальный телефон.'
    sale.save()
    sale.saleday = datetime.now() - timedelta(days=27)
    sale.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.movement = 'Заявка принята в обработку'
    delivery.details='Заявка принята в обработку'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.movement = 'Товар в пути'
    delivery.details='Товар в пути'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.movement = 'Товар на складе'
    delivery.details='Товар на складе'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.movement = 'Заявка закрыта, товар доставлен'
    delivery.details='Заявка закрыта, товар доставлен'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.save()
    
    ###

    sale = Sale()
    sale.saleday = datetime.now() - timedelta(days=26)
    sale.catalog_id = 11
    sale.price = 69900
    sale.quantity = 1
    sale.user_id = 7
    sale.rating = 5
    sale.details='Не претендую на профессиональный обзор, для меня как обычного пользователя отличный рабочий аппарат в своем классе и ценовом сегменте'
    sale.save()
    sale.saleday = datetime.now() - timedelta(days=26)
    sale.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.movement = 'Заявка принята в обработку'
    delivery.details='Заявка принята в обработку'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.movement = 'Товар в пути'
    delivery.details='Товар в пути'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.movement = 'Товар на складе'
    delivery.details='Товар на складе'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.movement = 'Заявка закрыта, товар доставлен'
    delivery.details='Заявка закрыта, товар доставлен'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.save()

    ###

    sale = Sale()
    sale.saleday = datetime.now() - timedelta(days=25)
    sale.catalog_id = 11
    sale.price = 69900
    sale.quantity = 1
    sale.user_id = 8
    sale.rating = 5
    sale.details='Отличный телефон в данной ценовой категории.Большая батарейка позволяет не заряжать несколько дней,если вы не играете конечно). Камера посредственная, но телефон и не покупался для красивых фото. Большой экран что является плюсом т.к брался для пожилого человека.'
    sale.save()
    sale.saleday = datetime.now() - timedelta(days=25)
    sale.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.movement = 'Заявка принята в обработку'
    delivery.details='Заявка принята в обработку'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.movement = 'Товар в пути'
    delivery.details='Товар в пути'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.movement = 'Товар на складе'
    delivery.details='Товар на складе'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.movement = 'Заявка закрыта, товар доставлен'
    delivery.details='Заявка закрыта, товар доставлен'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.save()

    ###

    sale = Sale()
    sale.saleday = datetime.now() - timedelta(days=24)
    sale.catalog_id = 16
    sale.price = 45900
    sale.quantity = 1
    sale.user_id = 9
    sale.rating = 5
    sale.details='Все гуд, покупали ребенку 3гб оперативки вполне хватает.'
    sale.save()
    sale.saleday = datetime.now() - timedelta(days=24)
    sale.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.movement = 'Заявка принята в обработку'
    delivery.details='Заявка принята в обработку'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.movement = 'Товар в пути'
    delivery.details='Товар в пути'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.movement = 'Товар на складе'
    delivery.details='Товар на складе'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.movement = 'Заявка закрыта, товар доставлен'
    delivery.details='Заявка закрыта, товар доставлен'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.save()
    
    ###

    sale = Sale()
    sale.saleday = datetime.now() - timedelta(days=23)
    sale.catalog_id = 16
    sale.price = 45900
    sale.quantity = 1
    sale.user_id = 10
    sale.rating = 4
    sale.details='Телефон не тупит, экран яркий и не сильно уступает IPS матрице на моём телефоне и мониторе.'
    sale.save()
    sale.saleday = datetime.now() - timedelta(days=23)
    sale.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.movement = 'Заявка принята в обработку'
    delivery.details='Заявка принята в обработку'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.movement = 'Товар в пути'
    delivery.details='Товар в пути'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.movement = 'Товар на складе'
    delivery.details='Товар на складе'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.movement = 'Заявка закрыта, товар доставлен'
    delivery.details='Заявка закрыта, товар доставлен'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.save()

    ###

    sale = Sale()
    sale.saleday = datetime.now() - timedelta(days=22)
    sale.catalog_id = 21
    sale.price = 13390
    sale.quantity = 1
    sale.user_id = 11
    sale.rating = 3
    sale.details='Сравниваю с LG GS107, который до сих пор работает отлично, гораздо громче, радио отлично ловит без гарнитуры, зарядки хватает на 5-7 дней и это с ещё родным аккумулятором. Взял Nokia в надежде что он будет схоже по параметрам с LG GS107, но он оказался гораздо хуже.'
    sale.save()
    sale.saleday = datetime.now() - timedelta(days=22)
    sale.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.movement = 'Заявка принята в обработку'
    delivery.details='Заявка принята в обработку'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.movement = 'Товар в пути'
    delivery.details='Товар в пути'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.movement = 'Товар на складе'
    delivery.details='Товар на складе'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.movement = 'Заявка закрыта, товар доставлен'
    delivery.details='Заявка закрыта, товар доставлен'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.save()
    
    ###

    sale = Sale()
    sale.saleday = datetime.now() - timedelta(days=21)
    sale.catalog_id = 21
    sale.price = 13390
    sale.quantity = 1
    sale.user_id = 12
    sale.rating = 5
    sale.details='огромные кнопки. тел отлично подошел владелице 83 лет. довольна.'
    sale.save()
    sale.saleday = datetime.now() - timedelta(days=21)
    sale.save()

    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.movement = 'Заявка принята в обработку'
    delivery.details='Заявка принята в обработку'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=1)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.movement = 'Товар в пути'
    delivery.details='Товар в пути'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=2)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.movement = 'Товар на складе'
    delivery.details='Товар на складе'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=3)
    delivery.save()
    
    delivery = Delivery()
    delivery.sale = sale
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.movement = 'Заявка закрыта, товар доставлен'
    delivery.details='Заявка закрыта, товар доставлен'
    delivery.save()
    delivery.deliveryday = sale.saleday + timedelta(days=4)
    delivery.save()

    print("Продажа + Доставка добавлен")

class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(new_catalog),
        migrations.RunSQL("""CREATE VIEW view_catalog AS
                        SELECT catalog.id, catalog.code, catalog.category_id, category.title AS category, catalog.title, catalog.info, catalog.details, catalog.price, catalog.quantity, catalog.photo, 
                        (SELECT AVG(rating) FROM sale WHERE sale.catalog_id = catalog.id) AS avg_rating,
                        (SELECT SUM(quantity) FROM sale WHERE sale.catalog_id = catalog.id) AS sale_quantity,
                        CASE 
                            WHEN (catalog.quantity - (SELECT SUM(quantity) FROM sale WHERE sale.catalog_id = catalog.id)) IS NULL 
                        THEN catalog.quantity 
                            ELSE (catalog.quantity - (SELECT SUM(quantity) FROM sale WHERE sale.catalog_id = catalog.id)) 
                        END
                        AS available
                        FROM catalog LEFT JOIN category ON catalog.category_id = category.id;"""),
        migrations.RunSQL("""CREATE VIEW view_sale AS
                        SELECT sale.id, username, saleday, catalog_id, view_catalog.category, view_catalog.title, info, code, sale.price, sale.quantity, sale.price*sale.quantity AS total, user_id, rating, sale.details,
                        (SELECT strftime('%d.%m.%Y',deliveryday) || ' - ' || movement FROM delivery WHERE sale_id = sale.id AND deliveryday = (SELECT MAX(deliveryday) AS Expr1 FROM delivery AS S WHERE  (sale_id = sale.id) )) AS final
                        FROM sale LEFT JOIN view_catalog ON sale.catalog_id = view_catalog.id
                        LEFT JOIN auth_user ON sale.user_id = auth_user.id"""),
        #migrations.RunSQL("""CREATE VIEW view_catalog AS
        #                SELECT catalog.id, catalog.code, catalog.category_id, category.title AS category, catalog.title, catalog.info, catalog.details, catalog.price, catalog.quantity, catalog.photo, 
        #                (SELECT AVG(rating) FROM sale WHERE sale.catalog_id = catalog.id) AS avg_rating,
        #                (SELECT SUM(quantity) FROM sale WHERE sale.catalog_id = catalog.id) AS sale_quantity,
        #                CASE WHEN (catalog.quantity - (SELECT SUM(quantity) FROM sale WHERE sale.catalog_id = catalog.id)) IS NULL 
        #                THEN catalog.quantity
        #                ELSE (catalog.quantity - (SELECT SUM(quantity) FROM sale WHERE sale.catalog_id = catalog.id))  
        #                END
        #                AS available
        #                FROM catalog LEFT JOIN category ON catalog.category_id = category.id"""),        
        #migrations.RunSQL("""CREATE VIEW view_sale AS
        #                SELECT sale.id, username, saleday, catalog_id, view_catalog.category, view_catalog.title, info, code, sale.price, sale.quantity, sale.price*sale.quantity AS total, user_id, rating, sale.details,
        #                (SELECT to_char( deliveryday, 'DD.MM.YYYY') || ' - ' || movement FROM delivery WHERE sale_id = sale.id AND deliveryday = (SELECT MAX(deliveryday) AS Expr1 FROM delivery AS S WHERE  (sale_id = sale.id) )) AS final
        #                FROM sale LEFT JOIN view_catalog ON sale.catalog_id = view_catalog.id
        #                LEFT JOIN auth_user ON sale.user_id = auth_user.id"""),
    ]
