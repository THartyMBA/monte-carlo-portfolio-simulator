# monte_carlo_portfolio_simulator.py
"""
Interactive Monte Carlo Portfolio Simulator  🏦📈
────────────────────────────────────────────────────────────────────────────
Simulate thousands of portfolio paths under user-defined return & volatility,
visualize outcome distributions, and download the raw simulation data.

1. Set initial investment, expected annual return, annual volatility, horizon, and number of simulations.
2. Generates Geometric Brownian Motion paths.
3. Plots percentile “fan chart” of portfolio value over time.
4. Shows distribution of terminal values.
5. Download full simulation table as CSV.

*Proof-of-concept demo—no production risk controls or persistence.*
"""

import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# ─────────────────────────────────────────────────────── Streamlit UI ───────────────────────────────────────────────────────
st.set_page_config(page_title="Monte Carlo Portfolio Simulator", layout="wide")
st.title("🏦 Interactive Monte Carlo Portfolio Simulator")

st.info(
    "🔔 **Demo Notice**  \n"
    "This is a lightweight proof-of-concept—perfect for portfolios or demos.  \n"
    "For production-grade risk analytics or web-based dashboards, [contact me](https://drtomharty.com/bio).",
    icon="💡"
)

# User inputs
initial_investment = st.number_input("Initial Investment ($)", min_value=0.0, value=10000.0, step=100.0)
expected_return = st.slider("Expected Annual Return (%)", min_value=-10.0, max_value=30.0, value=7.0, step=0.1)
annual_volatility = st.slider("Annual Volatility (%)", min_value=0.0, max_value=100.0, value=15.0, step=0.1)
years = st.slider("Time Horizon (years)", min_value=1, max_value=50, value=20, step=1)
n_simulations = st.slider("Number of Simulations", min_value=100, max_value=5000, value=1000, step=100)
random_seed = st.number_input("Random Seed", value=42, step=1)

if st.button("🚀 Run Simulations"):
    # Set up
    np.random.seed(random_seed)
    trading_days = 252
    total_steps = years * trading_days
    dt = 1 / trading_days
    mu = expected_return / 100
    sigma = annual_volatility / 100

    # Initialize array: rows=time steps+1, cols=simulations
    paths = np.zeros((total_steps + 1, n_simulations))
    paths[0] = initial_investment

    # Simulate paths
    for t in range(1, total_steps + 1):
        rand = np.random.standard_normal(n_simulations)
        paths[t] = paths[t - 1] * np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * rand)

    # Time axis in years
    time_axis = np.linspace(0, years, total_steps + 1)

    # Compute percentiles
    pct5, pct25, pct50, pct75, pct95 = np.percentile(paths, [5, 25, 50, 75, 95], axis=1)

    # Fan chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time_axis, y=pct95, line=dict(color="lightgrey"), showlegend=False))
    fig.add_trace(go.Scatter(x=time_axis, y=pct5, line=dict(color="lightgrey"), fill="tonexty", fillcolor="rgba(200,200,200,0.5)", name="5–95%"))
    fig.add_trace(go.Scatter(x=time_axis, y=pct75, line=dict(color="lightblue"), showlegend=False))
    fig.add_trace(go.Scatter(x=time_axis, y=pct25, line=dict(color="lightblue"), fill="tonexty", fillcolor="rgba(173,216,230,0.5)", name="25–75%"))
    fig.add_trace(go.Scatter(x=time_axis, y=pct50, line=dict(color="black"), name="Median (50%)"))
    fig.update_layout(
        title="Monte Carlo Simulated Portfolio Value",
        xaxis_title="Years",
        yaxis_title="Portfolio Value ($)",
        legend_title="Percentile Bands",
        hovermode="x unified",
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)

    # Terminal value distribution
    terminal_values = paths[-1]
    st.subheader("Distribution of Terminal Portfolio Values")
    hist_fig = px.histogram(
        pd.DataFrame({"Terminal Value": terminal_values}),
        x="Terminal Value",
        nbins=50,
        title="Histogram of Terminal Values"
    )
    st.plotly_chart(hist_fig, use_container_width=True)

    # Download full simulation table
    sim_df = pd.DataFrame(paths, index=time_axis).reset_index().rename(columns={"index": "Years"})
    csv = sim_df.to_csv(index=False).encode()
    st.download_button(
        label="⬇️ Download simulation data (CSV)",
        data=csv,
        file_name="monte_carlo_simulations.csv",
        mime="text/csv"
    )
