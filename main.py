def calculate_lift(density, velocity, wing_area, lift_coefficient):
    """
    Calculates the lift force using the lift equation.
    :param density: Air density (kg/m³)
    :param velocity: Airspeed (m/s)
    :param wing_area: Wing area (m²)
    :param lift_coefficient: Coefficient of lift (dimensionless)
    :return: Lift force in Newtons (N)
    """
    lift = 0.5 * density * velocity**2 * wing_area * lift_coefficient
    return lift
