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
        Column used for the x-axis values.
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


def create_donut_chart(
    df: pd.DataFrame,
    category_column: str,
    value_column: str,
    title: str,
):
    """
    Create a reusable Plotly donut chart.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the categories and their values.
    category_column : str
        Column containing the category labels.
    value_column : str
        Column containing the values used to calculate proportions.
    title : str
        Chart title.

    Returns
    -------
    plotly.graph_objects.Figure
        Configured Plotly donut chart with category labels
        and percentage annotations.
    """

    fig = px.pie(
        df,
        names=category_column,
        values=value_column,
        title=title,
        hole=0.45,
    )

    fig.update_traces(
        textposition="inside",
        textinfo="label+percent",
    )

    fig.update_layout(
        template="plotly_white",
        margin=dict(l=30, r=20, t=70, b=30),
        legend_title_text=None,
    )

    return fig


def create_treemap_chart(
    df: pd.DataFrame,
    category_column: str,
    value_column: str,
    title: str,
):
    """
    Create a reusable Plotly treemap chart.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the categories and their values.
    category_column : str
        Column containing the category labels used to define
        the treemap areas.
    value_column : str
        Column containing the values that determine the area
        of each rectangle.
    title : str
        Chart title.

    Returns
    -------
    plotly.graph_objects.Figure
        Configured Plotly treemap with category labels,
        percentage annotations, and hover information.
    """

    fig = px.treemap(
        df,
        path=[category_column],
        values=value_column,
        title=title,
    )

    fig.update_traces(
        textinfo="label+percent entry",
        hovertemplate=(
            "<b>%{label}</b><br>"
            "Datasets: %{value}<br>"
            "Share: %{percentEntry:.1%}"
            "<extra></extra>"
        ),
    )

    fig.update_layout(
        margin=dict(l=20, r=20, t=70, b=20),
    )

    return fig
