from cjwmodule import i18n


def render(table, params):
    outcolname = params["outcolname"] or "ID"

    result = {"dataframe": table, "column_formats": {outcolname: "{:d}"}}

    if outcolname in table.columns:
        result["error"] = i18n.trans(
            "warning.columnAlreadyExisted.message",
            'This overwrote the "{column_name}" column, which already existed.',
            {"column_name": outcolname},
        )
        del table[outcolname]

    table.insert(0, outcolname, range(1, len(table) + 1))

    return result
