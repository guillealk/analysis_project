import psycopg2


def get_articles():
    query = ('select a.title, count(*) as views '
             'from log,(select slug, title from articles) as a '
             'where substring(path from 10 for character_length(path)) = slug '
             'group by a.title '
             'order by views desc limit 3;')
    return get_entries(query)


def get_authors():
    query = ('select a.name, count(*) as views from log, '
             '(select slug, title, au.name from articles as ar '
             'left join authors as au on  ar.author=au.id ) as a '
             'where substring(path from 10 for character_length(path)) = slug '
             'group by a.name '
             'order by views desc;')
    return get_entries(query)


def get_errors():
    query = ('select date(time) as date, '
             'round(sum(case when status !=\'200 OK\' then 1 else 0 end) '
             '* 100.0 / count(*), 2) as error from log '
             'group by date '
             'having sum(case when status !=\'200 OK\' then 1 else 0 end) '
             '* 100.0 / count(*) > 1 '
             'order by error;')
    return get_entries(query)


def get_entries(query):
    co = psycopg2.connect("dbname=news")
    cursor = co.cursor()
    cursor.execute(query)
    POSTS = cursor.fetchall()
    co.close()
    return POSTS
