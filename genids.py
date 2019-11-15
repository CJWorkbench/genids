def render(table, params):
    outcolname = params["outcolname"] or "ID"

    result = {"dataframe": table, "column_formats": {outcolname: "{:d}"}}

    if outcolname in table.columns:
        result["error"] = (
            "This overwrote the '%s' column, which already existed." % outcolname
        )
        del table[outcolname]

    table.insert(0, outcolname, range(1, len(table) + 1))

    return result
