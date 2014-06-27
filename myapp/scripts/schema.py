import argparse
import sys
from sqlalchemy.schema import CreateIndex
from sqlalchemy.schema import CreateTable

from .. import get_app
from .. import database
from .. models import Base

def createdatabase(app):
    metadata = Base.metadata
    db = database.get_database(app)
    metadata.bind = db
    metadata.create_all(db)

def createsql(app, out):
    metadata = Base.metadata
    db = database.get_database(app)
    metadata.bind = db
    tables = metadata.sorted_tables

    for table in tables:
        sql = CreateTable(table).compile(db.engine).string
        sql = sql.strip() + ';\n'
        indexes = table.indexes
        for index in sorted(indexes, key=lambda i: i.name):
            sql += CreateIndex(index).compile(db.engine).string + ';\n'

        sql += '\n'
        out.write(sql)

def main():
    parser = argparse.ArgumentParser(description='create database')
    subparsers = parser.add_subparsers(help='subcommand help')

    s_parser = subparsers.add_parser('sql')
    s_parser.add_argument('-t', '--table', nargs='*', default=None)
    s_parser.add_argument('-o', '--out', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    s_parser.set_defaults(command='sql')

    s_parser = subparsers.add_parser('database')
    s_parser.set_defaults(command='database')

    app = get_app()
    args = parser.parse_args()
    if args.command == 'sql':
        createsql(app, args.out)
    elif args.command == 'database':
        createdatabase(app)

if __name__ == '__main__':
    main()
