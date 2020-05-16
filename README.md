# Django файловый навигатор на базе FUSE

# FUSE
FUSE (File System in User Space) on python [fusepy](https://github.com/fusepy/fusepy).

Кастомную файловую систему можно использовать по-разному. Главное её достоинство в том, что она рукописная и
достаточно реализовать не все функции взаимодействия с файлами, чтобы с ней работать.  

**Пример использования**: зашифрованная файловая система, структуру и способ шифрования которой знаешь только ты.

**Тестирование**: ```pytest```

___

Моя файловая система пока только делает как бы ссылку на другую папку, которая передаётся вторым аргументом.
Файловая система не делает копию, а лишь отображает, будто в ней есть именно эти файлы, и умеет открывать их для чтения.

**Запуск**: ```python fuse_main.py <dir to be mounted> --dir <source dir>```

**Линковка**: ```from fuse_main import run_fuse```

# Django file navigator
На данном этапе реализует перемещение по корневой папке, указанной основной, и открытие UTF-8 файлов на чтение.

**Пример использования**: удалённое взаимодействие с примонтированным диском на базе FUSE.

**Способ перемещения**:
1. Открытие папки по url: ```<path>/```.
2. Открытие файла по url: ```<path>```.  
— схоже с обычным перемещением по папкам.

**Запуск**: ```python manage.py runserver```
