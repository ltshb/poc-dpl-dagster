import dagster as dg


@dg.asset
def asset_1(context: dg.AssetExecutionContext) -> dg.MaterializeResult:
    return dg.MaterializeResult()
