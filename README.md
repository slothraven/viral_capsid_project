# Сервис для сбора и обновления данных для проекта "Генерация меметиков вирусов"

## Цель проекта: изучение капсидов вирусов:
 - Влияние геометрии капсида на функции вируса
 - Поиск зависимостей между геометрией капсида и клетками тканей хоста
 - Разработка алгоритма для моделирования искусственного капсида

## Данные:
  У нас есть 13 дескрипторов и около 1000 образцов в собранной базе данных. Данные были собраны из открытых источников: ViperDB и PDB.
  Также сейчас идет сбор статей по дескрипторам с физико-химическими условиями среды.
  Данные на github представлены в csv таблице, также есть папка с изображениями капсидов вирусов.

### Что мы сделали:
Из-за того, что биологические данные периодически обновляются и добавляются новые была поставлена задача разработать скрипт,
который будет автоматически в какой-то определенный период обновлять и добавлять новую информацию о вирусах.

Был реализован скрипт, который при запуске начинает собирать данные с ViperDB и PDB и сохранять в базу данных

## Как запустить:

```
git clone https://github.com/slothraven/viral_capsid_project.git
cd viral_capsid_project
pip install -r requirements.txt
```
Также для запуска проекта необходим браузер Google Chrome последней версии(Для запуска selenium)
