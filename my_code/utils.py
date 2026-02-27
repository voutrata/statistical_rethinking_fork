import polars as pl, xarray as xr
import matplotlib.pyplot as plt
import arviz as az


def standardize_columns(df: pl.DataFrame,
                        columns:list[str]):
    return df.with_columns(
        (pl.col(*columns) - pl.col(*columns).mean()) / pl.col(*columns).std()
    )

def extract_quantile_columns(df: pl.DataFrame,
                      posterior_predictive: xr.DataArray,
                      outcome_name: str,
                      quantiles: list[float] = [0.11, 0.89],
                     prefix: str="") -> pl.DataFrame:
    quants = getattr(posterior_predictive, outcome_name).quantile(quantiles, dim=["chain", "draw"])
    return  df.with_columns(**{f"{prefix}_{outcome_name}_{str(quant*100)}": quants[i].to_numpy() for i,quant in enumerate(quantiles)})


def plot_trace(trace: az.InferenceData) -> None:
    az.plot_trace(trace)
    plt.tight_layout()