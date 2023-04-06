# 手順

-前提-
クローン後、src/Python ディレクトリは削除する

1. docker-compose.yml/Dockerfile/requirements.txt の 3 つをもとに Docker を構築
2. docker compose exec python bash で python コンテナの中に入る
3. pipenv install でパッケージをインストール
4. pipenv shell で仮想環境を構築
5. pipenv run python manage.py startapp \*\*\* でアプリを作成
6. /app/config/settings.py に、今作成したアプリを登録する（33 行目付近、INSTALLED_APPS に、アプリ名.apps.アプリ名 config を追記する。kanban というアプリ名であれば、kanban.apps.KanbanConfig）
