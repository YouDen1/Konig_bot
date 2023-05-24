from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#Начало
toKaliningrad = KeyboardButton("Калининград")
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(toKaliningrad)

#Калининград
toZelenogradsk = KeyboardButton("Зеленоградск")
toSvetlogorsk = KeyboardButton("Светлогорск")
toSovetsk = KeyboardButton("Советск")
toCuronianSplit = KeyboardButton("Куршская коса")
walkInKaliningrad = KeyboardButton("Пройтись по городу")
kaliningradMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(toZelenogradsk, toSvetlogorsk, toSovetsk, toCuronianSplit, walkInKaliningrad)

#В Калининграде
toCenter = KeyboardButton("В центр города")
houseSovetov = KeyboardButton("Дом Советов")
fishDerevnya = KeyboardButton("Рыбная деревня")
islandOfKant = KeyboardButton("Остров Канта")
buildSom = KeyboardButton("Памятник сому")
Stadium = KeyboardButton("Стадион Калининград")
museumOfSea = KeyboardButton("Музей мирового океана")
museumAmber = KeyboardButton("Музей янтаря")
fiveFort = KeyboardButton("Пятый форт")

houseSovetovMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(fishDerevnya, islandOfKant, buildSom, Stadium, museumOfSea, museumAmber, fiveFort, toCenter)
fishDerevnyaMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(islandOfKant, buildSom, Stadium, museumOfSea, museumAmber, fiveFort, houseSovetov, toCenter)
islandOfKantMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(buildSom, Stadium, museumOfSea, museumAmber, fiveFort, houseSovetov, fishDerevnya, toCenter)
buildSomMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(Stadium, museumOfSea, museumAmber, fiveFort, houseSovetov, fishDerevnya, islandOfKant, toCenter)
StadiumMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(museumOfSea, museumAmber, fiveFort, houseSovetov, fishDerevnya, islandOfKant, buildSom, toCenter)
museumOfSeaMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(museumAmber, fiveFort, houseSovetov, fishDerevnya, islandOfKant, buildSom, Stadium, toCenter)
museumAmberMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(fiveFort, houseSovetov, fishDerevnya, islandOfKant, buildSom, Stadium, museumOfSea, toCenter)
fiveFortMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(houseSovetov, fishDerevnya, islandOfKant, buildSom, Stadium, museumOfSea, museumAmber, toCenter)


inkaliningradMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(toZelenogradsk, toSvetlogorsk, toSovetsk, toCuronianSplit, walkInKaliningrad)

#Зеленоградск
walkToCats = KeyboardButton("Посмотреть на котов")
walkToZelenogradskSea = KeyboardButton("Посмотреть на променад")
ferrisWheel = KeyboardButton("Колесо обозрения")
womanTourist = KeyboardButton("Памятник курортнице")

InZelenogradskMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(walkToCats, walkToZelenogradskSea, ferrisWheel, womanTourist)
walkToCatsMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(walkToZelenogradskSea, ferrisWheel, womanTourist, toKaliningrad)
walkToZelenogradskSeaMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(ferrisWheel, walkToCats, womanTourist, toKaliningrad)
ferrisWheelMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(womanTourist, walkToZelenogradskSea, walkToCats, toKaliningrad)
womanTouristenu = ReplyKeyboardMarkup(resize_keyboard = True).add(walkToCats, ferrisWheel, walkToZelenogradskSea, toKaliningrad)

#Светлогорск
towerWater = KeyboardButton("Башня водолечебницы")
svetlogorskPromenad = KeyboardButton("Променад")
sunClocks = KeyboardButton("Солнечные часы")

SvetlogorskMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(towerWater, svetlogorskPromenad, sunClocks)
sunClocksMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(towerWater, svetlogorskPromenad, toKaliningrad)
svetlogorskPromenadMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(towerWater, sunClocks, toKaliningrad)
towerWaterMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(sunClocks, svetlogorskPromenad, toKaliningrad)

#Советск
towerLuisa = KeyboardButton("Мост Королевы Луизы")
tram = KeyboardButton("Памятник трамваю")
newCitizens = KeyboardButton("Памятник первым переселенцам")

newCitizensMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(tram, towerLuisa, toKaliningrad)
towerLuisaMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(newCitizens, tram, toKaliningrad)
tramMenu = SovetskMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(towerLuisa, newCitizens, toKaliningrad)
SovetskMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(towerLuisa, newCitizens,tram)

#Куршская коса
highMuller = KeyboardButton("Высота Мюллера")
dancingForest = KeyboardButton("Танцующий лес")
highEfa = KeyboardButton("Высота Эфа")

KosaMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(highMuller, dancingForest, highEfa)
highMullerMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(dancingForest, highEfa, toKaliningrad)
dancingForestMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(highEfa, highMuller, toKaliningrad)
highEfaMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(dancingForest, highMuller, toKaliningrad)