# 手順

-前提-
クローン後、src/Python ディレクトリは削除する

1. docker-compose.yml/Dockerfile/requirements.txt の 3 つをもとに Docker を構築(docker compose build→docker compose up -d)
2. python コンテナの中に入り、 django-admin startproject config . でプロジェクトの作成
3. container/python/Dockerfile の 7 行目のコメントアウトを外し、再度 Docker の落とし上げ（stop,build,up。これで localhost:8000 がつながったままになる）
4. 再度 python コンテナの中に入り、pipenv install でパッケージをインストール
5. pipenv shell で仮想環境を構築
6. pipenv run python manage.py startapp \*\*\* でアプリを作成
7. /app/config/settings.py に、今作成したアプリを登録する（33 行目付近、INSTALLED_APPS に、アプリ名.apps.アプリ名 config を追記する。kanban というアプリ名であれば、kanban.apps.KanbanConfig）
