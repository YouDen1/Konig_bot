from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType, Message
import markup as nav

bot = Bot("6274077012:AAEZmuLbHyjRamWhS-gEf1tsSw9wzbTsNUc")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    #await message.answer(f"{message.from_user.first_name}, добро пожаловать в Калининградскую область!", reply_markup= nav.mainMenu)
    await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://kgd.ru/media/k2/galleries/72424/hrabrovo01.JPG", caption="Добро пожаловать в Калининградскую область!\nСегодня мы проведём экскурсию по эксклаву России.\nСначала направимся в центр региона из Храброво, единственного аэропорта области.\nНажмите на кнопку ниже.", reply_markup= nav.mainMenu)  

@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: Message):
    await message.reply(message.photo[-1].file_id)

@dp.message_handler()
async def answer(message: types.Message):
    if message.text == "Калининград" or message.text == "В центр города":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Kaliningrad_Panorama_%285664122123%29.jpg/1920px-Kaliningrad_Panorama_%285664122123%29.jpg", caption="Это центр Калининграда, в нём располагается площадь Победы, две церкви, мэрия города, КГТУ, северный вокзал и множество ТЦ.\nОтсюда мы сможем отправиться дальше.", reply_markup= nav.kaliningradMenu)
    elif message.text == "Пройтись по городу" or message.text == "Дом Советов":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Kaliningrad_05-2017_img68_House_of_Soviets.jpg/1024px-Kaliningrad_05-2017_img68_House_of_Soviets.jpg", caption="Это Дом Советов - одна из главных достопримечательностей Калининграда. Является символом долгостроя города. Изначально оно создавалось для размещения всего правительства города в одном месте, но вскоре проект забросили. На данный момент здание сносят.\nКуда идём дальше?", reply_markup= nav.houseSovetovMenu)
    elif message.text == "Рыбная деревня":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Kaliningrad_05-2017_img07_Fishery_Village.jpg/1920px-Kaliningrad_05-2017_img07_Fishery_Village.jpg", caption="Это рыбная деревня. Она является туристическим районом в городе, но это лишь имитация довоенной застройки. В этом районе расположены гостиницы, офисные здания и строящийся жилой комплекс..\nКуда дальше?", reply_markup= nav.fishDerevnyaMenu)
    elif message.text == "Остров Канта":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://cdnn21.img.ria.ru/images/07e5/08/03/1744195165_0:208:2000:1333_1920x0_80_0_0_acd700bd500b094a10fc37e94df9cd88.jpg", caption="Мы наблюдаем остров Канта, или как раньше его называли Кнайпхоф. Изначально он не входил в состав Кёнигсберга и был самостоятельным, но в 1724 году стал его частью. На острове сохранился Кёнигсбергский собор, который является визитной карточкой края, а также могилой Иманнуила Канта.\nКуда дальше?", reply_markup= nav.islandOfKantMenu)
    elif message.text == "Памятник сому":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://cdnn21.img.ria.ru/images/152635/59/1526355951_0:0:1555:1037_1440x900_80_0_1_4e5c8d113572e42582c1c86476558f44.jpg.webp?source-sid=not_rian_photo", caption="Это памятник посвященный сому. Однажды, в июле 2016 года при реконструкции старинного моста Высоцкого водолазы обнаружили сома весом в 200-220 киллограм, и после этой находки они решили посвятить этой рыбе памятник.\nКуда следуем дальше?", reply_markup= nav.buildSomMenu)   
    elif message.text == "Стадион Калининград":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://upload.wikimedia.org/wikipedia/commons/a/a4/Kaliningrad_stadium_-_2018-04-07.jpg", caption="Это Стадион Калининград, построен в 2018 году специально для ЧМ 2018 года, он находится на Октябрьском острове, является самым большим стадионом в Янтарном крае и вмещает 35016 человек.\nКуда дальше?", reply_markup= nav.StadiumMenu)   
    elif message.text == "Музей мирового океана":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Kaliningrad_-_World_Ocean_Muzeum_-_Vityaz_-_View_of_World_Ocean_Museum_main_building.jpg/1920px-Kaliningrad_-_World_Ocean_Muzeum_-_Vityaz_-_View_of_World_Ocean_Museum_main_building.jpg", caption="Сейчас мы наблюдаем Музей Мирового Океана - первый в России комплексный маринистический музей. В нём находятся экспозиции, посвящённые судоходству, морской флоре и фауне и много чему еще.\nКуда идём дальше?", reply_markup= nav.museumOfSeaMenu)   
    elif message.text == "Музей янтаря":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://m.ambermuseum.ru/i/image/home/face.jpg", caption="Это музей янтаря, он был основан в 1979 году. В нём можно увидеть различные экспонаты, связанные с янтарём и знаменитой Янтарной комнатой.\nКуда дальше?", reply_markup= nav.museumAmberMenu)
    elif message.text == "Пятый форт":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://upload.wikimedia.org/wikipedia/commons/b/bf/Fort_5_entrance.jpg", caption="Сейчас мы наблюдаем Форт № 5 — Король Фридрих Вильгельм III. Форт когда-то служил военным фортификационным сооружением в Кёнигсберге, прикрывавшим шоссейную дорогу на Пиллау. Сейчас он  имеет статус музея истории Великой Отечественной войны.\nКуда дальше?", reply_markup= nav.fiveFortMenu)   

    elif message.text == "Зеленоградск":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://russo-travel.ru/upload/medialibrary/964/9642d5dd4bda478363d805deecf85579.jpg", caption="Это центр Зеленоградска- курортный проспект, именно здесь и находится большая часть достопримечательностей. Давай-те их рассмотрим!", reply_markup= nav.InZelenogradskMenu)
    elif message.text == "Посмотреть на котов":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://live.staticflickr.com/65535/50180089767_193c1ba382_c.jpg", caption="Это знак на въезде в город, на ней изображены прикольные коты))", reply_markup= nav.walkToCatsMenu)
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://live.staticflickr.com/65535/50179832856_69fcd34ce2_b.jpg", caption="Здесь можно заметить стрит-арт, на котором изображен спящий кот.")
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://cs12.pikabu.ru/post_img/big/2022/03/20/6/164776639818355520.png", caption="Это светофор на котором изображены коты, когда-то такие светофоры хотели сделать на территории всего города, но идею не одобрили(((")
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://cs14.pikabu.ru/post_img/big/2022/03/20/6/1647766328114655845.png", caption="Это мини-город котов, расположен рядом со светофором на курортном проспекте. Здесь обитает основная масса шерстяных жителей города.")
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://kaliningradinfo.ru/upload/iblock/737/7377dc9c3ab9476e189f0ce3cbaf7040.jpg", caption="Закончим на этом памятнике, посвящённый всем котам Зеленоградска, на нём можно покататься.\nКуда дальше?")
    elif message.text == "Памятник курортнице":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://guruturizma.ru/wp-content/uploads/2022/09/kurortnica.jpeg", caption="Сейчас мы наблюдаем памятник курортнице, который посвящен всем туристам города. На чемодане можно заметить сидящего кота.\nКуда следуем дальше?", reply_markup= nav.womanTouristenu)
    elif message.text == "Посмотреть на променад":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://www.semiestrel.ru/wp-content/uploads/2021/07/promenad.jpg", caption="Это местный променад, на нём есть велодорожка, много скамеек и различные тренажёры. По нему можно пройтись, любуясь красотой Балтийского берега.\nКуда идём дальше?", reply_markup= nav.walkToZelenogradskSeaMenu)
    elif message.text == "Колесо обозрения":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://img.tourister.ru/files/2/8/2/1/6/9/2/4/original.jpg", caption="Это колесо обозрения под названием «Глаз Балтики». Его высота составляет 50 метров! Оно расположено у площади «Роза ветров».\nКуда дальше?", reply_markup= nav.ferrisWheelMenu)

    elif message.text == "Светлогорск":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://planetofhotels.com/guide/sites/default/files/styles/big_gallery_image/public/text_gallery/Svetlogorsk-4.jpg", caption="Мы находимся в центре Светлогорска! Здесь мы наблюдаем местный рынок, на котором например можно приобрести сувениры, такие как: магниты, изделия из янтаря и так далее.\nКуда пойдём дальше?", reply_markup= nav.SvetlogorskMenu)
    elif message.text == "Башня водолечебницы":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://cdn2.tu-tu.ru/image/pagetree_node_data/1/af6989840642f5ad3399555913bfff0d/", caption="Сейчас мы наблюдаем башню водолечебницы.\nОна является самым известным архитектурным сооружением города. Башня была построена в 1907-1908 г, а её высота достигает 25 метров! Она служила для снабжения Светлогорска (тогда Раушена) водой, а в  настоящее время башня и здание лечебницы относятся к Светлогорскому центральному военному санаторию.\nКуда следуем дальше?", reply_markup= nav.towerWaterMenu)
    elif message.text == "Променад":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://vipavto39.ru/wp-content/uploads/2019/09/svetlogorsk.jpg", caption="Это вид снизу на местный и красивый променад. Отсюда можно наблюдать Балтийское море. Также по нему любят прогуляться, ведь по пути встречается много интересных достопримечательностей.\nКуда дальше?", reply_markup= nav.svetlogorskPromenadMenu)
    elif message.text == "Солнечные часы":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/07/fe/ee/00/caption.jpg?w=1200&h=-1&s=1", caption="Это ещё одна достопримечательность Светлогорска - солнечные часы, она была построена в июне 1975 года. Диаметр часов составляет 10,1 метра, благодаря ним можно узнать, сколько сейчас время.\nКуда идём дальше?", reply_markup= nav.sunClocksMenu)

    elif message.text == "Советск":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://tripplanet.ru/wp-content/uploads/europe/russia/sovetsk/dostoprimechatelnosti-sovetska.jpg", caption="Сейчас мы в Советске, но когда-то он назывался Тильзитом, а в 1946 году его переименовали. Является вторым по численности городом в области.\nПредлагаю направиться дальше!", reply_markup= nav.SovetskMenu)
    elif message.text == "Мост Королевы Луизы":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://amberkenig.ru/wp-content/uploads/2021/08/1560895347_0_0_2880_1620_600x0_80_0_0_5d3047a2f93ee5af401c0ed76153da43.jpg", caption="Мы наблюдаем мост Королевы Луизы. Он был построен в 1907 году в честь 100 летия Тильзитского мира. Это сооружение является главной визитной карточкой города, а также является пограничным пунктом РФ и Литвы.\nКуда следуем дальше?", reply_markup= nav.towerLuisaMenu)
    elif message.text == "Памятник трамваю":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://upload.wikimedia.org/wikipedia/commons/2/24/MS-IV-12_tram_in_Sovetsk.jpg", caption="Сейчас мы у памятника, посвященный трамваям, которые когда-то ходили по городу. Расположен в центре города.\nКуда дальше?", reply_markup= nav.tramMenu)
    elif message.text == "Памятник первым переселенцам":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/11/cc/3b/3b/caption.jpg?w=1200&h=1200&s=1", caption="Сейчас мы у памятника, посвящённому первым переселенцам из СССР в новый регион. Рядом с ним расположен поезд, символизирующий долгий путь.\nКуда дальше?", reply_markup= nav.newCitizensMenu)

    elif message.text == "Куршская коса":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://russo-travel.ru/upload/medialibrary/7ef/7efcde1dad56f63987fcf6b383361ced.jpg", caption="Это Куршская коса, она является национальным парком РФ, а также включена в список Всемирного наследия ЮНЕСКО. Её длина составляет 98 километров! Также коса является пограничным пунктом, соединяющий Россию и Литву.\nКуда следуем дальше?", reply_markup= nav.KosaMenu)
    elif message.text == "Высота Мюллера":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://park-kosa.ru/images/cache_images/iblock/e2f/e2f0c6abc3b769fe42287481bf213804.506b07a7.jpg", caption="Мы находимся на Высоте Мюллера - это самая высокая точка дюны Болотной(44,4 м). Она названа в честь лесничего кёнигсбергского Управления лесами Людвига Мюллера\nКуда дальше?", reply_markup= nav.highMullerMenu)
    elif message.text == "Танцующий лес":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://upload.wikimedia.org/wikipedia/commons/b/ba/Wald_der_tanzenden_B%C3%A4ume01.jpg", caption="Сейчас мы наблюдаем Танцующий лес. Это место отличается от остальных лесов тем, что стволы деревьев изогнуты и получается, что они танцуют))\nКуда идём дальше?", reply_markup= nav.dancingForestMenu)
    elif message.text == "Высота Эфа":
        await dp.bot.send_photo(chat_id=message.from_user.id, photo="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0b/d2/0b/19/caption.jpg?w=1200&h=-1&s=1", caption="Перед нами Высота Эфа - это маршрут протяжённостью 2,8 км. Её самая высокая точка - 62 метров. Была обрела название в честь дюнного инспектора Франца Эфа\nКуда дальше?", reply_markup= nav.highEfaMenu)

    else:
        await message.answer("Я вас не понимаю((")

if __name__ == "__main__":
    executor.start_polling(dp)