zodb_config_sqlite = """
%import relstorage
<zodb main>
<relstorage>
    keep-history false
    cache-local-mb 0
    <sqlite3>
       data-dir Data/sqlite
    </sqlite3>
</relstorage>
</zodb>"""

zodb_config_psql="""
%import relstorage
<zodb main>
<relstorage>
  <postgresql>
    # The dsn is optional, as are each of the parameters in the dsn.
    dsn dbname='zodb' user='zodbuser' host='localhost' password='test'
  </postgresql>
</relstorage>
</zodb>
"""