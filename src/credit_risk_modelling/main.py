import numpy as np

from credit_risk_modelling.charts.draw import (
    get_cumulative_distribution_function_chart,
)
from credit_risk_modelling.distributions.binomial import (
    indipendent_binomial_loss_distribution_analytic,
    indipendent_binomial_loss_distribution_simulation,
)
from credit_risk_modelling.metrics.risk_measures import (
    compute_risk_measure_analytic,
    compute_risk_measures_simulation,
)


if __name__ == "__main__":
    alpha = 0.95
    N = 100
    p = 0.01
    c = 10
    pmf, cdf = indipendent_binomial_loss_distribution_analytic(N, p)
    compute_risk_measure_analytic(N, alpha, pmf, cdf, c)
    n = 100
    m = 1000000
    p = np.load("defaultProbabilties.npy")
    # c = np.load('exposures.npy')
    # p = np.ones(100)*0.01
    c = np.ones(100) * 10
    sorted_loss_distribution = indipendent_binomial_loss_distribution_simulation(n, m, p, c)
    (
        expected_loss,
        stdev_loss,
        expected_shortfall,
        value_at_risk,
    ) = compute_risk_measures_simulation(m, sorted_loss_distribution, alpha)
    print("expected_loss:", expected_loss)
    print("stdev_loss:", stdev_loss)
    print("expected_shortfall:", expected_shortfall)
    print("value_at_risk:", value_at_risk)

    get_cumulative_distribution_function_chart(
        distribution_value=sorted_loss_distribution,
        plot_chart_streamlit=False,
        plot_chart=True,
        title="Cumulative Distribution Function",
    )
