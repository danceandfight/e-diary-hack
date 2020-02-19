# Модуль для улучшения качества жизни школьников

В данном модуле реализованы три функции позволяющие исправлять в электронном дневнике двойки и тройки на пятерки, удалять замечания и делать самому себе похвалы.

## Как использовать

Скачайте репозиторий и поместите файлы из него в папку с `manage.py`. В файле scripts.py находятся функции, которые нужно будет использовать, а в файле commendation_examples.txt - список фраз для похвалы.

Для использования программы сайт должен быть уже запущен и вы должны находиться в командной строке в каталоге с файлом `manage.py`, затем запустить shell (интерактивную консоль Django) и импортировать функции:

`python3 manage.py shell`
`from scripts import fix_marks, remove_chastisements, create_commendation`

Для того чтобы исправить сразу все плохие оценки на пятерки введите следующую команду, подставив нужные фамилию и имя:
`fix_marks('Фамилия Имя')`

Для того что бы удалить сразу все замечания от учителей введите:
`remove_chastisements('Фамилия Имя')`

Для того, что бы оставить в дневнике похвалу за последний урок по выбранному предмету, используйте:
`create_commendation('Фамилия Имя', 'Название предмета')`

Эта функция выбирает из файла `commendation_examples.txt` случайную фразу и использует ее как текст похвалы. Можете добавить в файл свои фразы, открыв в его блокноте.

Фамилия, имя и название предмета пишутся в кавычках с большой буквы.


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
