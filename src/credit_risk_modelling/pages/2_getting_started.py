import numpy as np
import streamlit as st

from credit_risk_modelling.charts.draw import (
    get_cumulative_distribution_function_chart,
    get_probability_density_function_chart,
)
from credit_risk_modelling.front_end.utils import change_language, get_language


st.set_page_config(page_title="Getting started")
change_language()
language = get_language()

if language == "en":
    st.header("Basic concepts")
    st.markdown(
        """Credit risk is a topic that been interested in: <br><ul><li><b>Default risk</b>: The defaulting of a counterparty (or obligor) obligation.</li>
    <li><b>Migration risk</b>: The deterioration of an obligor's ability to pay, which makes default more probable.</li></ul><br>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        "There are two applications of credit-risk models: <br><ul><li><b>Pricing credit risk</b></li><li><b>Measuring the riskiness of credit exposures</b></li></ul><br>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "The distribution of default losses is the object of central interest for credit-risk modellers. <br> Pricing is interested on the central part of distribution, instead risk management is more interested on its tails.<br>",
        unsafe_allow_html=True,
    )
    st.subheader("Probability distribution")
else:
    st.header("Concetti base")
    st.markdown(
        """Nel credit risk si è interessati al: <br><ul><li><b>Rischio di default</b>: Il mancato pagamento delle obbligazioni da parte della controparte (o debitore).</li>
    <li><b>Rischio di deterioramento</b>: Il peggioramento della capacità di rimborsare i propri debiti da parte della controparte, rendendo più probabile il default.</li></ul><br>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        "Ci sono due principali applicazioni dei modelli di credit-risk: <br><ul><li><b>Il pricing</b></li><li><b>La valutazione del rischio di credito delle esposizioni</b></li></ul><br>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "Nel credit risk si osserva la distribuzione delle perdite: <br> Chi fa pricing è interessato alla parte centrale della distribuzione, mentre il risk manager è più interessato alla coda della distribuzione.<br>",
        unsafe_allow_html=True,
    )
    st.subheader("Distribuzione di probabilità")

mu = 0
sigma = 1
s = np.random.normal(mu, sigma, 1000)
vertical_line_dict = {
    "Tail": {"x": -2.75, "ymin": 0, "ymax": 1, "color": "r", "linestyle": "dashed"},
    "Mean": {"x": 0, "ymin": 0, "ymax": 1, "color": "b", "linestyle": "dashed"},
}
get_probability_density_function_chart(
    distribution_value=s,
    plot_chart_streamlit=True,
    plot_chart=False,
    title="Probability Density Function",
    vertical_line_dict=vertical_line_dict,
)

st.markdown("And now see this chart:")
get_cumulative_distribution_function_chart(
    distribution_value=s,
    plot_chart_streamlit=True,
    plot_chart=False,
    title="Cumulative Distribution Function",
    vertical_line_dict=vertical_line_dict,
)


st.markdown("", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)
