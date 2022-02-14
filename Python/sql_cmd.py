
from typing import Type


class SQL(object):

    def __init__(self) -> None:
        # super().__init__()
        pass

    #  inspired from:
    #  https://stackoverflow.com/questions/1563967/generate-sql-statements-with-python

    def select(table: str, **kwargs):
        """ Generates SQL for a SELECT statement matching the kwargs passed. """
        sql = list()
        sql.append("SELECT * FROM %s " % table)
        if kwargs:
            sql.append("WHERE " + " AND ".join("%s = '%s'" % (k, v) for k, v in kwargs.iteritems()))
        sql.append(";")
        return "".join(sql)


    def insert(table: str, **kwargs):
        keys = ["%s" % k for k in kwargs]
        values = ["'%s'" % v for v in kwargs.values()]
        sql = list()
        sql.append("INSERT INTO %s (" % table)
        sql.append(", ".join(keys))
        sql.append(") VALUES (")
        sql.append(", ".join(values))
        sql.append(");")
        return "".join(sql)


    def upsert(table: str, **kwargs):
        """ update/insert rows into objects table (update if the row already exists)
            given the key-value pairs in kwargs """
        keys = ["%s" % k for k in kwargs]
        values = ["'%s'" % v for v in kwargs.values()]
        sql = list()
        sql.append("INSERT INTO %s (" % table)
        sql.append(", ".join(keys))
        sql.append(") VALUES (")
        sql.append(", ".join(values))
        sql.append(") ON DUPLICATE KEY UPDATE ")
        sql.append(", ".join("%s = '%s'" % (k, v) for k, v in kwargs.iteritems()))
        sql.append(";")
        return "".join(sql)


    def delete(table: str, **kwargs):
        """ deletes rows from table where **kwargs match """
        sql = list()
        sql.append("DELETE FROM %s " % table)
        sql.append("WHERE " + " AND ".join("%s = '%s'" % (k, v) for k, v in kwargs.iteritems()))
        sql.append(";")
        return "".join(sql)

    def generate_multiple_cmds(func, table: str, rows: list[dict]):
        result = []
        for row in rows:
            result.append(func(table,row))
        return result
