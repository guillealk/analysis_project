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
    value = "'404 NOT FOUND'"
    query = ('select date(time) as date, '
             'round(count(status)*100.0/(select count(*) from log)*100, 2) '
             'as error from log '
             'where status=%s group by date '
             'having count(status)*100.0/(select count(*) from log)*100 > 1 '
             'order by error desc;' % value)
    return get_entries(query)


def get_entries(query):
    co = psycopg2.connect("dbname=news")
    cursor = co.cursor()
    cursor.execute(query)
    POSTS = cursor.fetchall()
    co.close()
    return POSTS
