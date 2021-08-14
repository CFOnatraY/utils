def read_and_analyze_data():
    lines_to_return = []
    with open('2019.csv') as file:
        for line in file:
            line_content = line.split(';')
            date = line_content[0]
            start_time = line_content[1]
            end_time = line_content[2]
            building = line_content[3]
            space = line_content[4]
            activity_type = line_content[5]
            observation_detail = line_content[6]
            formatted_lines =\
                analyze_entry(date, start_time, end_time, building, space, activity_type, observation_detail)
            lines_to_return.extend(formatted_lines)
    return lines_to_return


def analyze_entry(date, start_time, end_time, building, space, activity_type, observation_detail):
    start_h = int(start_time.split(':')[0])
    end_h = int(end_time.split(':')[0])

    if start_h < 13 and end_h < 13:
        start_h = start_h if start_h >= 7 else 7
        start_time = '{}:00'.format(start_h)

        return ['{};{};{};{};{};{};{}'.format(
            date, start_time, end_time, building, space, activity_type, observation_detail)]

    elif start_h >= 13 and end_h < 18:
        return ['{};{};{};{};{};{};{}'.format(
            date, start_time, end_time, building, space, activity_type, observation_detail)]

    elif start_h >= 18 and end_h <= 23:
        return ['{};{};{};{};{};{};{}'.format(
            date, start_time, end_time, building, space, activity_type, observation_detail)]

    else:
        start_h = start_h if start_h >= 7 else 7
        start_time = '{}:00'.format(start_h)

        if 23 >= end_h >= 18:
            morning = '{0};{1};13:00;{2};{3};{4}:{5}'.format(date, start_time, building, space, activity_type,
                                                             observation_detail)
            after_noon = '{0};13:00;18:00;{1};{2};{3}:{4}'.format(date, building, space, activity_type,
                                                                  observation_detail)
            night = '{0};18:00;{1};{2};{3};{4}:{5}'.format(date, end_time, building, space, activity_type,
                                                           observation_detail)
            return [morning, after_noon, night]
        elif end_h < 18:
            morning = '{0};{1};13:00;{2};{3};{4}:{5}'.format(date, start_time, building, space, activity_type,
                                                             observation_detail)

            after_noon = '{0};13:00;{1};{2};{3};{4}:{5}'.format(date, end_time, building, space, activity_type,
                                                                observation_detail)
            return [morning, after_noon]


def create_new_file(list_to_write):
    file_formated = open('2019_formatted.csv', 'w+')

    for line in list_to_write:
        file_formated.write(line)
    file_formated.close()


formatted_data = read_and_analyze_data()
create_new_file(formatted_data)
