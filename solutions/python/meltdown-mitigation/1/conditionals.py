def is_criticality_balanced(temperature, neutrons_emitted):
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted <500000


def reactor_efficiency(voltage, current, theoretical_max_power):
    percentage = ((voltage * current) / theoretical_max_power)*100
    if percentage >= 80:
        return "green"
    elif 60 <= percentage < 80:
        return "orange"
    elif 30 <= percentage < 60:
        return "red"
    else:
        return "black"

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    if (temperature * neutrons_produced_per_second) < 0.9 * threshold:
        return "LOW"
    elif (0.9 * threshold) < (temperature * neutrons_produced_per_second) < (1.1 * threshold):
        return "NORMAL"
    else:
        return "DANGER"
