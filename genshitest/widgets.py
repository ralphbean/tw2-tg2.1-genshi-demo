import genshitest.model as model
from tw2.jqplugins.jqgrid import SQLAjqGridWidget

class LogGrid(SQLAjqGridWidget):
    id = 'awesome-loggrid'
    entity = model.User
    excluded_columns = ['id']
    datetime_format = "%x %X"

    prmFilter = {'stringResult': True, 'searchOnEnter': False}

    options = {
        'pager': 'awesome-loggrid_pager',
        'url': '/jqgrid/',
        'rowNum':15,
        'rowList':[15,150, 1500],
        'viewrecords':True,
        'imgpath': 'scripts/jqGrid/themes/green/images',
        'shrinkToFit': True,
        'height': 'auto',
    }

