
import numpy as np


def compute_risk_measures_simulation(
    m: int, loss_distribution: np.array, alpha: float
) -> tuple[float]:
    """ """
    expected_loss = np.mean(loss_distribution)
    stdev_loss = np.std(loss_distribution)
    expected_shortfall = np.mean(loss_distribution[int(m * alpha) : m])
    value_at_risk = loss_distribution[int(m * alpha)]

    return expected_loss, stdev_loss, expected_shortfall, value_at_risk


def compute_risk_measure_analytic(
    N: int, alpha: float, pmf: np.array, cdf: np.array, c: np.array | float
):
    """ """
    var = c * np.interp(alpha, cdf, np.linspace(0, N, N + 1))
    number_defaults = np.linspace(0, N, N + 1)
    myAlphas = np.linspace(alpha, 1, 1000)
    number_defaults_interpolated = np.interp(myAlphas, cdf, number_defaults)
    tail_losses = c * number_defaults_interpolated
    tail_pmf = np.interp(tail_losses, number_defaults, pmf)
    expected_shortfall = np.dot(tail_losses, tail_pmf) / sum(tail_pmf)

    return var, expected_shortfall
