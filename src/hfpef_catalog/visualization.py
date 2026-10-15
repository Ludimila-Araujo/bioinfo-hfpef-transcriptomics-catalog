import pandas as pd
import plotly.express as px


def create_bar_chart(
    df: pd.DataFrame,
    x_column: str,
    y_column: str,
    title: str,
    y_axis_title: str,
):
    """
    Create a reusable Plotly bar chart.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the data to visualize.
    x_column : str
        Column used for the categories on the x-axis.
    y_column : str
        Column used for the values on the y-axis.
    title : str
        Chart title.
    y_axis_title : str
        Label displayed on the y-axis.

    Returns
    -------
    plotly.graph_objects.Figure
        Configured Plotly bar chart.
    """
    fig = px.bar(
        df,
        x=x_column,
        y=y_column,
        title=title,
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title=None,
        yaxis_title=y_axis_title,
        margin=dict(l=30, r=20, t=70, b=50),
    )

    return fig


def create_horizontal_bar_chart(
    df: pd.DataFrame,
    x_column: str,
    y_column: str,
    title: str,
    x_axis_title: str,
):
    """
    Create a reusable Plotly horizontal bar chart.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the data to visualize.
    x_column : str
        Column containing the categories.
    y_column : str
        Column containing the values.
    title : str
        Chart title.
    x_axis_title : str
        Label displayed on the x-axis.

    Returns
    -------
    plotly.graph_objects.Figure
        Configured Plotly horizontal bar chart.
    """
    fig = px.bar(
        df,
        x=y_column,
        y=x_column,
        orientation="h",
        title=title,
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title=x_axis_title,
        yaxis_title=None,
        margin=dict(l=30, r=20, t=70, b=50),
    )

    return fig
