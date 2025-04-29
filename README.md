# monte-carlo-portfolio-simulator

🏦 Interactive Monte Carlo Portfolio Simulator
A Streamlit proof-of-concept that lets you model thousands of potential portfolio outcomes under customizable return and volatility assumptions. Visualize percentile bands over time and explore the distribution of terminal values.

🔍 What it does
Set your assumptions

Initial investment

Expected annual return (µ)

Annual volatility (σ)

Time horizon (years)

Number of simulations

Random seed for reproducibility

Run Geometric Brownian Motion (GBM)
Simulates each path step-by-step over trading days (default 252) using GBM:

𝑆
𝑡
+
Δ
𝑡
=
𝑆
𝑡
exp
⁡
(
(
𝜇
−
1
2
𝜎
2
)
Δ
𝑡
+
𝜎
Δ
𝑡
 
𝜖
)
S 
t+Δt
​
 =S 
t
​
 exp((μ− 
2
1
​
 σ 
2
 )Δt+σ 
Δt
​
 ϵ)
Visualize results

Fan chart of the 5th–95th and 25th–75th percentile bands plus the median trajectory

Histogram of terminal portfolio values

Download the full simulation dataset as CSV for deeper analysis.

Demo only—no production risk controls, back-testing, or persistence.
For enterprise risk-analytics pipelines or interactive dashboards, contact me.

✨ Key Features
Customizable inputs: return, volatility, horizon, simulation count

Interactive fan chart: percentile bands rendered with Plotly

Terminal distribution: histogram of end-of-horizon values

Data export: download simulation table (Years × simulation runs)

Single-file app: zero frontend code—just Python + Streamlit

🚀 Quick Start (Local)
bash
Copy
Edit
git clone https://github.com/THartyMBA/monte-carlo-portfolio-simulator.git
cd monte-carlo-portfolio-simulator
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run monte_carlo_portfolio_simulator.py
Open your browser to http://localhost:8501.

Adjust the sliders and inputs in the sidebar.

Click Run Simulations to see your fan chart and histogram.

☁️ Deploy on Streamlit Community Cloud
Push this repo (public or private) to GitHub under THartyMBA.

Go to streamlit.io/cloud → New app → select your repo and branch → Deploy.

Share the live URL with stakeholders—no secrets or API keys required.

🛠️ Requirements
shell
Copy
Edit
streamlit>=1.32
numpy
pandas
plotly
(All CPU-friendly; runs smoothly on the free tier.)

🗂️ Repo Structure
vbnet
Copy
Edit
monte-carlo-portfolio-simulator/
├─ monte_carlo_portfolio_simulator.py   ← single-file Streamlit app  
├─ requirements.txt  
└─ README.md                            ← you’re reading it  
📜 License
CC0 1.0 – public-domain dedication. Attribution appreciated but not required.

🙏 Acknowledgements
Streamlit – rapid interactive Python apps

NumPy & Pandas – data processing

Plotly – interactive visualizations

Simulate, visualize, and download your portfolio scenarios in seconds! 🚀
