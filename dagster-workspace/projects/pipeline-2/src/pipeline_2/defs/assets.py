import dagster as dg


@dg.asset
def asset_2(context: dg.AssetExecutionContext) -> dg.MaterializeResult:
    return dg.MaterializeResult()
