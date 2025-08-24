import logging

class UnitConverter:
    """A simple unit converter for length measurements."""

    _CONVERSION_FACTORS = {
        # Length
        "meter": 1.0,
        "m": 1.0,
        "kilo meter": 1000.0,
        "kilometer": 1000.0,
        "km": 1000.0,
        "mile": 1609.34,
        "mi": 1609.34,
        "foot": 0.3048,
        "ft": 0.3048,

        # Mass
        "kilogram": 1.0,
        "kg": 1.0,
        "gram": 0.001,
        "g": 0.001,
        
        # Volume
        "liter": 1.0,
        "l": 1.0,
        "mili liter": 0.001,
        "ml": 0.001,
        "mililiter": 0.001,

        #currency
        "usd": 0.85,
        "eur": 1,
    }

    _TEMP_UNITS = {"celsius", "fahrenheit", "kelvin", "c", "f", "k"}

    def _convert_temperature(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in self._TEMP_UNITS or to_unit not in self._TEMP_UNITS:
            raise ValueError(f"Unsupported temperature units: {from_unit} -> {to_unit}")
    
        # Convert source -> Celsius
        celsius=0

        if from_unit == "celsius" or from_unit=='c':
            celsius = value
        elif from_unit == "fahrenheit" or from_unit=='f':
            celsius = (value - 32) * 5 / 9
        elif from_unit == "kelvin" or from_unit=='k':
            celsius = value - 273.15


        # Celsius -> target
        if to_unit == "celsius" or to_unit=='c':
            return celsius
        elif to_unit == "fahrenheit" or to_unit=='f':
            return celsius * 9 / 5 + 32
        elif to_unit == "kelvin" or to_unit=='k':
            return celsius + 273.15

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        # Temperature conversion
        if from_unit in self._TEMP_UNITS or to_unit in self._TEMP_UNITS:
            result = self._convert_temperature(value, from_unit, to_unit)

            return result

        # Linear conversion
        if from_unit not in self._CONVERSION_FACTORS or to_unit not in self._CONVERSION_FACTORS:
            logging.error(f"Unsupported conversion: {from_unit} -> {to_unit}")
            raise ValueError(f"Unsupported conversion: {from_unit} -> {to_unit}")

        value_in_base = value * self._CONVERSION_FACTORS[from_unit]
        result = value_in_base / self._CONVERSION_FACTORS[to_unit]

        logging.info(f"Converted {value} {from_unit} -> {result:.4f} {to_unit}")

        return result
