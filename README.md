"# Project_Planner" 

1) Хранение ссылок на файлы (скачивание тхт, exel, csv)

2) генерация кода, для восстановления пароля

3) Косяк в шаблоне. Ввод пассворда_1 при регистрации ругается на кортеж.



<!-- 
Plan:
 -->



Запуск сервера:
set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run

Миграции:
set FLASK_APP=webapp && flask db migrate -m "*" - создаем саму миграци, * - описание

flask db upgrade - производим саму миграцию. синхронизируем код и бд