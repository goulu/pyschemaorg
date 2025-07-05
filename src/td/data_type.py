# types from https://schema.org/DataType
# do NOT use python specific types like datetime here !


# https://schema.org/Text A text value.
Text = str

Number = float
# https://schema.org/URL A URL value.
URL = str

# https://schema.org/Date A date value in ISO 8601 date format.
Date = str
# https://schema.org/Time A point in time recurring on multiple days in the form hh:mm:ss[Z|(+|-)hh:mm] (see XML schema for details).
Time = str
# https://schema.org/DateTime A combination of date and time of day in the form[-]CCYY-MM-DDThh: mm: ss[Z | (+ | -)hh:mm](see Chapter 5.4 of ISO 8601).
DateTime = str
# https://schema.org/Duration Quantity: Duration (use ISO 8601 duration format).
Duration = str
