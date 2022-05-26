import sys


# <================================== Start Actual Algorithm =============================================>
def get_max_number_of_pizza_deliveries(N, queue):
    matrix = [[0 for x in range(N)] for y in range(N)]
    matrix_identifiers = [[set() for x in range(N)] for y in range(N)]
    max_pizza_deliveries = 0
    while len(queue) != 0:
        current_pizza_delivery = queue.pop(0)
        current_x, current_y, current_maximum_distance, identifier = current_pizza_delivery[0], \
                                                                     current_pizza_delivery[1], \
                                                                     current_pizza_delivery[2], \
                                                                     current_pizza_delivery[3]
        matrix_identifier = matrix_identifiers[current_x][current_y]

        if identifier not in matrix_identifier:
            matrix[current_y][current_x] += 1
            max_pizza_deliveries = max(max_pizza_deliveries, matrix[current_x][current_y])
            matrix_identifier.add(identifier)
            if current_maximum_distance > 0:
                matrix_border_checker(queue, current_x + 1, current_y, N, current_maximum_distance, identifier)
                matrix_border_checker(queue, current_x - 1, current_y, N, current_maximum_distance, identifier)
                matrix_border_checker(queue, current_x, current_y + 1, N, current_maximum_distance, identifier)
                matrix_border_checker(queue, current_x, current_y - 1, N, current_maximum_distance, identifier)
    # matrix_printer(matrix)
    return max_pizza_deliveries


def matrix_border_checker(queue, new_x, new_y, N, current_maximum_distance, identifier):
    if 0 <= new_x < N and 0 <= new_y < N and current_maximum_distance >= 0:
        queue.append([new_x, new_y, current_maximum_distance - 1, identifier])


# <================================== End  Actual Algorithm =============================================>


# <================================== Start  Arguments Parser =============================================>
def arguments_parser():
    print("Enter/Paste your content(Numbers only). Press A  to calculate. Press CTRL-Z to quit.")
    contents = []
    while True:
        try:
            line = input()
            if line.strip() != '': contents.append(line.replace('a', ''))
            if 'a' in line.lower(): break
        except:
            e = sys.exc_info()[0]
            print(e)
            break
    arguments_processor(contents)


def arguments_processor(contents):
    try:
        queue = []
        N = 0
        identifier_counter = 1
        for i in range(len(contents)):
            if contents[i] == '': continue
            content = contents[i].split(' ')

            if i == 0:
                N = int(content[0])

            else:
                queue_element = [int(content[0]) - 1, int(content[1]) - 1, int(content[2]), identifier_counter]
                identifier_counter += 1
                queue.append(queue_element)
        print('\n')
        print('Output:', get_max_number_of_pizza_deliveries(N, queue))
        arguments_parser()
    except:
        print('content', content)
        e = sys.exc_info()[0]
        print(e)
        arguments_parser()


# <================================== End Arguments Parser =============================================>


def matrix_printer(matrix):
    for row in matrix:
        print(row)
    print('\n')


if __name__ == '__main__':
    arguments_parser()
