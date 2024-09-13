def aggregate_weather_data(records):
    city_data = {}

    for record in records:
        city = record.get('city')

        if city not in city_data:
            city_data[city] = {
                'total_temperature': 0,
                'temperature_count': 0,
                'total_humidity': 0,
                'humidity_count': 0
            }
        if 'temperature' in record:
            city_data[city]['total_temperature'] += record['temperature']
            city_data[city]['temperature_count'] += 1
        if 'humidity' in record:
            city_data[city]['total_humidity'] += record['humidity']
            city_data[city]['humidity_count'] += 1
    results = {}
    for city, data in city_data.items():
        avg_temp = (data['total_temperature'] / data['temperature_count']) if data['temperature_count'] > 0 else None
        avg_humidity = (data['total_humidity'] / data['humidity_count']) if data['humidity_count'] > 0 else None

        results[city] = {
            'average_temperature': avg_temp,
            'average_humidity': avg_humidity
        }
    return results    
